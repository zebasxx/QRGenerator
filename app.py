import base64
import io
import os
from typing import Optional

from flask import Flask, render_template, request
import qrcode


app = Flask(__name__)


def generate_qr_data_uri(text: str) -> str:
    qr_image = qrcode.make(text)
    buffer = io.BytesIO()
    qr_image.save(buffer, format="PNG")
    buffer.seek(0)
    encoded = base64.b64encode(buffer.read()).decode("utf-8")
    return f"data:image/png;base64,{encoded}"


def read_default_text() -> str:
    # Use INPUT_FILE if provided; default to input/input.txt
    input_file_path = os.environ.get("INPUT_FILE", "input/input.txt")
    if os.path.isfile(input_file_path):
        try:
            with open(input_file_path, "r", encoding="utf-8") as f:
                return f.read()
        except Exception:
            return ""
    return ""


@app.route("/", methods=["GET", "POST"])
def index():
    qr_text: str = ""
    notes: str = ""
    qr_data_uri: Optional[str] = None

    if request.method == "POST":
        qr_text = request.form.get("qr_text", "").strip()
        notes = request.form.get("notes", "")
        if qr_text:
            qr_data_uri = generate_qr_data_uri(qr_text)
    else:
        # Pre-fill with default text from file if present
        qr_text = read_default_text()

    return render_template(
        "index.html",
        qr_text=qr_text,
        notes=notes,
        qr_data_uri=qr_data_uri,
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)