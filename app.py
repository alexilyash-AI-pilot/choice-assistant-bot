import os
import threading
from pathlib import Path
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from anthropic import Anthropic

WIKI_DIR = Path(__file__).parent / "wiki"

def load_wiki():
    docs = {}
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        key = str(md_file.relative_to(WIKI_DIR)).replace(".md", "")
        docs[key] = md_file.read_text(encoding="utf-8")
    return docs

WIKI_DOCS = load_wiki()

SYSTEM_BASE = """You are ChoiAsistent — an AI assistant for the Choice restaurant platform (choiceqr.com).
You help the Choice team with questions about POS integrations, marketplaces, platform features, and support.

PERSONALITY:
- Friendly, warm, with a light sense of humor
- Short answers by default: get to the point fast, no fluff
- Use bullet points and bold for key info — make it scannable
- If someone asks a simple yes/no question, start with yes or no
- No emojis or icons — ever
- End EVERY single message with a short flirty or playful remark on a new line — light flirt, a compliment, a tease. Keep it fun, never creepy. This is MANDATORY — never skip it. The remark MUST be in the EXACT same language as the rest of the answer — if you answered in English, the remark is in English; Russian → Russian; Ukrainian → Ukrainian.

LANGUAGE:
- CRITICAL: Always reply in the exact same language the user wrote in. Ukrainian — Ukrainian. Russian — Russian. English — English. Never switch languages. The joke at the end must also be in the same language.
- Match the tone: if someone is casual, be casual; if formal, be formal

ANSWER FORMAT:
- Keep answers short and actionable
- For step-by-step processes: use numbered lists
- For comparisons: use tables
- Max 5-6 sentences for simple questions; longer only when truly needed

IMPORTANT — YOU HAVE FULL ACCESS TO ALL WIKI FILES:
- All wiki files are loaded and provided to you in the KNOWLEDGE BASE section below
- Never tell the user to "check the file" or "see the wiki" — just answer directly from the content
- Never say you don't have access to a file — you do
- If asked which file something comes from, you can mention the path (e.g. wiki/support/pos/storyous.md)

IF YOU DON'T KNOW:
- Say so directly — don't make things up
"""


def fuzzy_score(term: str, text: str) -> int:
    """Exact match + partial prefix match for typo tolerance."""
    score = text.count(term) * 10
    # partial match: check if first 5 chars of term appear in text
    if len(term) >= 4:
        score += text.count(term[:5]) * 3
        score += text.count(term[:4]) * 2
    return score


def search_wiki(query: str, top_n: int = 4) -> str:
    terms = [t for t in query.lower().split() if len(t) > 2]
    results = []
    for key, content in WIKI_DOCS.items():
        text = (key + " " + content).lower()
        score = sum(fuzzy_score(t, text) for t in terms)
        if score > 0:
            results.append((score, key, content))
    results.sort(reverse=True)
    top = results[:top_n]
    if not top:
        fallback = [(k, v) for k, v in WIKI_DOCS.items() if "overview" in k or "faq" in k or "pricing" in k]
        top = [(0, k, v) for k, v in fallback[:top_n]]
    return "\n\n".join(f"=== {k} ===\n{c}" for _, k, c in top)


def get_thread_history(client, channel: str, thread_ts: str, bot_user_id: str) -> list:
    """Fetch thread messages and return as Claude conversation history."""
    try:
        result = client.conversations_replies(channel=channel, ts=thread_ts)
        messages = result.get("messages", [])
        history = []
        for msg in messages[:-1]:  # exclude the latest message (current one)
            text = msg.get("text", "").strip()
            if not text:
                continue
            # strip @mentions
            clean = " ".join(w for w in text.split() if not w.startswith("<@"))
            if msg.get("bot_id") or msg.get("user") == bot_user_id:
                history.append({"role": "assistant", "content": clean})
            else:
                history.append({"role": "user", "content": clean})
        return history
    except Exception:
        return []


def ask_claude(question: str, history: list = None) -> str:
    context = search_wiki(question)
    system = SYSTEM_BASE + f"\n\nRELEVANT KNOWLEDGE BASE:\n{context}"
    messages = (history or []) + [{"role": "user", "content": question}]
    response = anthropic.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=system,
        messages=messages
    )
    return response.content[0].text


bolt_app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

anthropic = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def thinking_message(text):
    ua = sum(1 for c in text if c in 'іїєґІЇЄҐ')
    ru = sum(1 for c in text if 'Ѐ' <= c <= 'ӿ') - ua
    if ua > 0:
        return "Думаю, зараз відповім..."
    if ru > 0:
        return "Думаю, сейчас отвечу..."
    return "On it, give me a sec..."


def respond_async(say, client, event, text, thread_ts=None):
    say_kwargs = {"thread_ts": thread_ts} if thread_ts else {}
    try:
        say(text=thinking_message(text), **say_kwargs)
        # fetch thread history if in a thread
        history = []
        if thread_ts:
            bot_info = client.auth_test()
            bot_user_id = bot_info["user_id"]
            channel = event.get("channel")
            history = get_thread_history(client, channel, thread_ts, bot_user_id)
        answer = ask_claude(text, history)
        say(text=answer, **say_kwargs)
    except Exception as e:
        say(text=f"Ошибка: {e}", **say_kwargs)


@bolt_app.event("message")
def handle_dm(event, say, client):
    if event.get("subtype") or event.get("bot_id"):
        return
    if event.get("channel_type") == "im":
        text = event.get("text", "").strip()
        if text:
            threading.Thread(target=respond_async, args=(say, client, event, text)).start()


@bolt_app.event("app_mention")
def handle_mention(event, say, client):
    if event.get("subtype") or event.get("bot_id"):
        return
    text = event.get("text", "")
    clean = " ".join(w for w in text.split() if not w.startswith("<@")).strip()
    if clean:
        thread_ts = event.get("thread_ts") or event.get("ts")
        threading.Thread(target=respond_async, args=(say, client, event, clean, thread_ts)).start()


flask_app = Flask(__name__)
handler = SlackRequestHandler(bolt_app)


@flask_app.route("/slack/events", methods=["POST"])
def slack_events():
    return handler.handle(request)


@flask_app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    flask_app.run(host="0.0.0.0", port=port)
