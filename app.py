"""Vercel/Flask adapter for the Duyên Dịch v3.1 runtime."""
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


@app.get("/")
def index():
    return send_from_directory(ROOT / "ui_test", "index.html")


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
        result = canonical_response(run_v31(payload, strict_number=True))
    except (TypeError, ValueError, OverflowError) as exc:
        return _error(str(exc))
    return app.response_class(
        json.dumps(result, ensure_ascii=False, sort_keys=True),
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
