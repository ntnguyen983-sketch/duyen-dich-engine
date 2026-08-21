from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, request, send_from_directory

from runtime.v31.engine import canonical_response, run_v31

ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)


def _error(message: str, status: int = 400):
    return jsonify({"error": message, "code": "INVALID_INPUT"}), status


def _is_hexagram_payload(payload: dict[str, Any]) -> bool:
    return isinstance(payload.get("data_1"), dict) and isinstance(payload.get("data_2"), dict)


def normalize_run_payload(payload: dict[str, Any]) -> tuple[dict[str, Any], str]:
    """Map the supplied hexagram envelope to the unchanged core runtime payload."""
    if not _is_hexagram_payload(payload):
        return payload, "flat"

    data_1 = payload["data_1"]
    data_2 = payload["data_2"]
    time = data_1.get("time")
    number = data_1.get("number")
    question = data_2.get("question")
    gps = data_1.get("gps_show")

    if not isinstance(question, str) or not question.strip():
        raise ValueError("data_2.question is required")
    if not isinstance(time, str) or not time.strip():
        raise ValueError("data_1.time is required")
    if number is None or not str(number).strip().isdigit():
        raise ValueError("data_1.number phải là số nguyên không âm.")
    if not isinstance(gps, dict) or "lat" not in gps or "lng" not in gps:
        raise ValueError("data_1.gps_show phải có lat và lng.")

    number_text = str(number).strip()
    core_payload = {
        "question": question.strip(),
        "number": int(number_text),
        "time": time.strip(),
        "gps": {"lat": gps["lat"], "lng": gps["lng"]},
        "address": payload.get("address"),
        "image": payload.get("image"),
    }
    return core_payload, "hexagram"


@app.get("/")
def index():
    # Keep the canonical HTML unchanged and load the runtime UI hotfix separately.
    # This avoids duplicating the presentation layer while replacing only the broken
    # form-submit behavior after the original inline script has initialized.
    response = send_from_directory(ROOT / "ui_test", "index.html")
    html = response.get_data(as_text=True)
    html = html.replace(
        "</body>",
        '<script src="/ui_test/v31_runtime_fix.js?v=f0754c72"></script></body>',
        1,
    )
    response.set_data(html)
    return response


@app.get("/ui_test/<path:filename>")
def ui_asset(filename: str):
    return send_from_directory(ROOT / "ui_test", filename)


@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "contract_version": "3.1.0", "runtime": "v31"})


@app.route("/api/v31", methods=["GET", "POST"])
def v31_endpoint():
    if request.method == "GET":
        return jsonify({"status": "ready", "method": "POST", "contract_version": "3.1.0"})
    if not request.is_json:
        return _error("Content-Type phải là application/json.")
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return _error("Request body phải là một JSON object.")
    try:
        core_payload, source = normalize_run_payload(payload)
        result = canonical_response(run_v31(core_payload, strict_number=(source == "flat")))
    except (TypeError, ValueError, OverflowError) as exc:
        return _error(str(exc))
    return app.response_class(
        json.dumps(result, ensure_ascii=False, sort_keys=True),
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
