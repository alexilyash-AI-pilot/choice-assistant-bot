import os
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

SYSTEM_PROMPT = f"""You are ChoiAssistant, a helpful AI assistant for the Choice restaurant platform (choiceqr.com).
You help the Choice team answer questions about POS integrations, marketplace integrations, platform features, and support topics.
Answer in the same language the user writes in — Ukrainian, Russian, or English.
Be concise and practical. If you don't know something, say so.

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


@bolt_app.event("message")
def handle_dm(event, say):
    if event.get("channel_type") == "im" and not event.get("bot_id"):
        text = event.get("text", "").strip()
        if text:
            say(ask_claude(text))


@bolt_app.event("app_mention")
def handle_mention(event, say):
    text = event.get("text", "")
    clean = " ".join(w for w in text.split() if not w.startswith("<@")).strip()
    if clean:
        say(ask_claude(clean))


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
