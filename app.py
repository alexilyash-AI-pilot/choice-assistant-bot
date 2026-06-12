import os
import threading
from pathlib import Path
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from flask import Flask, request
from anthropic import Anthropic

WIKI_DIR = Path(__file__).parent / "wiki"

def load_wiki():
    parts = []
    for md_file in sorted(WIKI_DIR.rglob("*.md")):
        key = str(md_file.relative_to(WIKI_DIR)).replace(".md", "")
        text = md_file.read_text(encoding="utf-8")
        parts.append(f"=== {key} ===\n{text}")
    return "\n\n".join(parts)

WIKI_CONTENT = load_wiki()

SYSTEM_PROMPT = f"""You are ChoiAsistent — an AI assistant for the Choice restaurant platform (choiceqr.com).
You help the Choice team with questions about POS integrations, marketplaces, platform features, and support.

PERSONALITY:
- Friendly, warm, occasionally funny — but never at the expense of clarity
- Short answers by default: get to the point fast, no fluff
- Use bullet points and bold for key info — make it scannable
- If someone asks a simple yes/no question, start with yes or no
- Light humor is welcome, but keep it professional
- No emojis or icons — ever

LANGUAGE:
- CRITICAL: Always reply in the exact same language the user wrote in. If they write in Ukrainian — answer in Ukrainian. Russian — Russian. English — English. Never switch languages.
- Match the tone: if someone is casual, be casual; if formal, be formal

ANSWER FORMAT:
- Keep answers short and actionable
- For step-by-step processes: use numbered lists
- For comparisons: use tables
- Max 5-6 sentences for simple questions; longer only when truly needed

IF ASKED FOR SOURCE FILES:
- Tell the user the relevant file path from the wiki, e.g. wiki/support/pos/poster.md
- Explain they can find the full file in the GitHub repo: https://github.com/alexilyash-AI-pilot/choice-assistant-bot

IF YOU DON'T KNOW:
- Say so directly — don't make things up
- Suggest who to ask (e.g. "check with the integrations team")

KNOWLEDGE BASE:
{WIKI_CONTENT}
"""

bolt_app = App(
    token=os.environ["SLACK_BOT_TOKEN"],
    signing_secret=os.environ["SLACK_SIGNING_SECRET"]
)

anthropic = Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])


def ask_claude(question: str) -> str:
    response = anthropic.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": question}]
    )
    return response.content[0].text


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
    say(text=thinking_message(text), **say_kwargs)
    answer = ask_claude(text)
    say(text=answer, **say_kwargs)


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
