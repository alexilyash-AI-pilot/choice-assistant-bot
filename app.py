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
- Friendly, warm, occasionally funny — but never at the expense of clarity
- Short answers by default: get to the point fast, no fluff
- Use bullet points and bold for key info — make it scannable
- If someone asks a simple yes/no question, start with yes or no
- Light humor is welcome, but keep it professional
- No emojis or icons — ever

LANGUAGE:
- CRITICAL: Always reply in the exact same language the user wrote in. Ukrainian — Ukrainian. Russian — Russian. English — English. Never switch languages.
- Match the tone: if someone is casual, be casual; if formal, be formal

ANSWER FORMAT:
- Keep answers short and actionable
- For step-by-step processes: use numbered lists
- For comparisons: use tables
- Max 5-6 sentences for simple questions; longer only when truly needed

IF ASKED FOR SOURCE FILES:
- Tell the user the relevant file path, e.g. wiki/support/pos/poster.md
- GitHub repo: https://github.com/alexilyash-AI-pilot/choice-assistant-bot

IF YOU DON'T KNOW:
- Say so directly — don't make things up
"""


def search_wiki(query: str, top_n: int = 4) -> str:
    terms = query.lower().split()
    results = []
    for key, content in WIKI_DOCS.items():
        text = (key + " " + content).lower()
        score = sum(text.count(t) for t in terms)
        if score > 0:
            results.append((score, key, content))
    results.sort(reverse=True)
    top = results[:top_n]
    if not top:
        # fallback: return overview files
        fallback = [(k, v) for k, v in WIKI_DOCS.items() if "overview" in k or "faq" in k or "pricing" in k]
        top = [(0, k, v) for k, v in fallback[:top_n]]
    return "\n\n".join(f"=== {k} ===\n{c}" for _, k, c in top)


def ask_claude(question: str) -> str:
    context = search_wiki(question)
    system = SYSTEM_BASE + f"\n\nRELEVANT KNOWLEDGE BASE:\n{context}"
    response = anthropic.messages.create(
        model="claude-haiku-4-5",
        max_tokens=1024,
        system=system,
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text

bolt_app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

anthropic = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])




def thinking_message(text):
    # detect language by unicode ranges
    ua = sum(1 for c in text if 'Ѐ' <= c <= 'ӿ' and c in 'іїєґІЇЄҐ')
    ru = sum(1 for c in text if 'Ѐ' <= c <= 'ӿ') - ua
    if ua > 0:
        return "Думаю, зараз відповім..."
    if ru > 0:
        return "Думаю, сейчас отвечу..."
    return "On it, give me a sec..."


def respond_async(say, text, thread_ts=None):
    say_kwargs = {"thread_ts": thread_ts} if thread_ts else {}
    try:
        say(text=thinking_message(text), **say_kwargs)
        answer = ask_claude(text)
        say(text=answer, **say_kwargs)
    except Exception as e:
        say(text=f"Ошибка: {e}", **say_kwargs)


@bolt_app.event("message")
def handle_dm(event, say):
    if event.get("subtype") or event.get("bot_id"):
        return
    if event.get("channel_type") == "im":
        text = event.get("text", "").strip()
        if text:
            threading.Thread(target=respond_async, args=(say, text)).start()


@bolt_app.event("app_mention")
def handle_mention(event, say):
    if event.get("subtype") or event.get("bot_id"):
        return
    text = event.get("text", "")
    clean = " ".join(w for w in text.split() if not w.startswith("<@")).strip()
    if clean:
        thread_ts = event.get("thread_ts") or event.get("ts")
        threading.Thread(target=respond_async, args=(say, clean, thread_ts)).start()


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
