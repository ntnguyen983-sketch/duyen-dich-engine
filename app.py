from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from flask import Flask, jsonify, request, send_from_directory

from runtime.v31.engine import canonical_response, run_v31
from services.ai_inference import GeminiConfigurationError, GeminiProviderError, generate_ai_interpretation

ROOT = Path(__file__).resolve().parent
app = Flask(__name__, static_folder=None)


def _error(message: str, status: int = 400):
    return jsonify({"error": message, "code": "INVALID_INPUT"}), status


def _attach_engine_trace(ai_result: dict[str, Any], engine_result: dict[str, Any]) -> dict[str, Any]:
    """Make engine provenance authoritative over any model-generated trace fields."""
    result = dict(ai_result)
    trace = dict(result.get("trace") or {})
    execution = engine_result.get("execution") or {}
    provenance = engine_result.get("provenance") or {}
    trace.update({
        "engine_execution_id": execution.get("execution_id", "unknown"),
        "engine_input_hash": execution.get("input_hash", "unknown"),
        "engine_content_fingerprint": provenance.get("content_fingerprint", "unknown"),
    })
    result["trace"] = trace
    return result


def _is_hexagram_payload(payload: dict[str, Any]) -> bool:
    return isinstance(payload.get("data_1"), dict) and isinstance(payload.get("data_2"), dict)


def normalize_run_payload(payload: dict[str, Any]) -> tuple[dict[str, Any], str]:
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
    core_payload = {
        "question": question.strip(), "number": int(str(number).strip()), "time": time.strip(),
        "gps": {"lat": gps["lat"], "lng": gps["lng"]}, "address": payload.get("address"),
        "image": payload.get("image"), "dong": data_1.get("dong"),
    }
    return core_payload, "hexagram"


@app.get("/")
def index():
    index_path = ROOT / "ui_test" / "index.html"
    html = index_path.read_text(encoding="utf-8")
    # The UI contract renderer is self-contained in index.html. Do not inject
    # legacy per-line adapters or runtime hotfixes that can overwrite its handler.
    return app.response_class(html, status=200, mimetype="text/html")


@app.get("/ui_test/<path:filename>")
def ui_asset(filename: str):
    return send_from_directory(ROOT / "ui_test", filename)


@app.get("/api/health")
def health():
    return jsonify({
        "status": "ok",
        "contract_version": "3.1.0",
        "runtime": "v31",
        "ai_interpretation": "configured" if __import__("os").getenv("GEMINI_API_KEY") else "not_configured",
    })


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
    return app.response_class(json.dumps(result, ensure_ascii=False, sort_keys=True), status=200, mimetype="application/json")


@app.post("/api/v31/analyze")
def v31_analyze_endpoint():
    """Run the immutable engine, then generate a separate AI interpretation."""
    if not request.is_json:
        return _error("Content-Type phải là application/json.")
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return _error("Request body phải là một JSON object.")
    try:
        core_payload, source = normalize_run_payload(payload)
        engine_result = canonical_response(run_v31(core_payload, strict_number=(source == "flat")))
    except (TypeError, ValueError, OverflowError) as exc:
        return _error(str(exc))

    try:
        ai_result = generate_ai_interpretation(
            engine_result,
            core_payload["question"],
            source_payload=payload,
        )
        ai_result = _attach_engine_trace(ai_result, engine_result)
    except GeminiConfigurationError:
        return jsonify({
            "error": "AI luận giải chưa được cấu hình ở môi trường server.",
            "code": "GEMINI_NOT_CONFIGURED",
            "engine_output": engine_result,
        }), 503
    except GeminiProviderError:
        app.logger.exception("Gemini interpretation provider failure")
        return jsonify({
            "error": "Không thể tạo luận giải AI lúc này.",
            "code": "AI_INTERPRETATION_FAILED",
            "engine_output": engine_result,
        }), 502
    except Exception:
        app.logger.exception("Unexpected AI interpretation failure")
        return jsonify({
            "error": "Không thể tạo luận giải AI lúc này.",
            "code": "AI_INTERPRETATION_FAILED",
            "engine_output": engine_result,
        }), 502

    response_payload = {
        "engine_output": engine_result,
        "ai_interpretation": ai_result,
        "ai_trace": ai_result["trace"],
    }
    return app.response_class(
        json.dumps(response_payload, ensure_ascii=False, sort_keys=True),
        status=200,
        mimetype="application/json",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
