#!/usr/bin/env python3
"""
A bare-bones web UI for Provenance Guard.

    python app.py     # terminal 1: the service
    python ui.py      # terminal 2: this, at http://127.0.0.1:7860

It only talks to the service over HTTP, same as curl, so 400s, 429s and the
audit log behave exactly as they do from the command line. No detection logic
lives here.
"""

import os

import gradio as gr
import requests

BASE_URL = os.environ.get("SERVICE_URL", "http://127.0.0.1:5000")
TIMEOUT = 120  # first submission loads the model


def _post(path, body):
    """Return (status, json) or (None, message) if the service is unreachable."""
    try:
        r = requests.post(f"{BASE_URL}{path}", json=body, timeout=TIMEOUT)
    except requests.RequestException as exc:
        return None, f"Could not reach {BASE_URL}{path}: {exc}. Is `python app.py` running?"
    try:
        return r.status_code, r.json()
    except ValueError:
        return r.status_code, r.text


def submit(text, creator_id):
    status, data = _post("/submit", {"text": text, "creator_id": creator_id})
    if status is None:
        return data, "", {}
    if status != 200:
        msg = data.get("message") if isinstance(data, dict) else str(data)
        return f"Error {status}: {msg}", "", data if isinstance(data, dict) else {}
    summary = (
        f"**{data['label']}**\n\n"
        f"Guess: {data['guess']}  |  Confidence: {data['confidence']}"
    )
    return summary, data["content_id"], data


def appeal(content_id, creator_id, reasoning):
    status, data = _post("/appeal", {"content_id": content_id,
                                     "creator_id": creator_id,
                                     "reasoning": reasoning})
    if status is None:
        return data
    if isinstance(data, dict):
        return data.get("message", str(data)) if status == 200 else f"Error {status}: {data.get('message', data)}"
    return f"Error {status}: {data}"


with gr.Blocks(title="Provenance Guard") as demo:
    gr.Markdown("# Provenance Guard\nPaste text to see how it would be labelled.")

    with gr.Tab("Submit"):
        creator = gr.Textbox(label="Creator ID", value="demo_user")
        text = gr.Textbox(label="Text", lines=10, placeholder="Paste writing here...")
        go = gr.Button("Check text", variant="primary")
        result = gr.Markdown()
        content_id = gr.Textbox(label="content_id (copy into the Appeal tab)", interactive=False)
        raw = gr.JSON(label="Full response")
        go.click(submit, [text, creator], [result, content_id, raw])

    with gr.Tab("Appeal"):
        a_id = gr.Textbox(label="content_id")
        a_creator = gr.Textbox(label="Creator ID", value="demo_user")
        a_reason = gr.Textbox(label="Why is this label wrong?", lines=4)
        a_go = gr.Button("Submit appeal")
        a_out = gr.Markdown()
        a_go.click(appeal, [a_id, a_creator, a_reason], a_out)


if __name__ == "__main__":
    demo.launch()
