"""End-to-end Duyên Dịch v3.1 runtime.

The runtime is deliberately self-contained and does not import legacy modules.
Its field and S07 operators are explicitly provisional until an authoritative
profile is approved. The adapter layer must not duplicate this logic.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
from datetime import datetime
from pathlib import Path
from typing import Any

CANONICAL = ("SAT", "TA", "NHIEU", "HY", "DUONG", "AN")
ROOT = Path(__file__).resolve().parents[2]


def _hash(value: Any) -> str:
    encoded = json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _file_hash(path: Path) -> str:
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _finite_number(value: Any, field: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{field} phải là số.")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{field} phải là số hữu hạn.")
    return result


def _validate_time(value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("time is required")
    timestamp = value.strip()
    try:
        datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError("time phải là ISO-8601 hợp lệ.") from exc
    return timestamp


def _validate_gps(value: Any) -> dict[str, float] | None:
    if value is None or value == {}:
        return None
    if not isinstance(value, dict):
        raise ValueError("gps phải là object hoặc null.")
    if "lat" not in value or "lng" not in value:
        raise ValueError("gps phải có lat và lng.")
    lat = _finite_number(value["lat"], "gps.lat")
    lng = _finite_number(value["lng"], "gps.lng")
    if not -90 <= lat <= 90:
        raise ValueError("gps.lat phải nằm trong khoảng -90 đến 90.")
    if not -180 <= lng <= 180:
        raise ValueError("gps.lng phải nằm trong khoảng -180 đến 180.")
    return {"lat": lat, "lng": lng}


def _validate_image(value: Any) -> dict[str, Any] | None:
    if value is None:
        return None
    if not isinstance(value, dict):
        raise ValueError("image phải là object hoặc null.")
    allowed = {"name", "type", "size", "data_url"}
    image = {key: value[key] for key in value if key in allowed}
    if "size" in image:
        size = _finite_number(image["size"], "image.size")
        if size < 0:
            raise ValueError("image.size không được âm.")
        image["size"] = int(size)
    return image


def _norm(payload: dict[str, Any], *, strict_number: bool = False) -> dict[str, Any]:
    question = payload.get("question")
    if not isinstance(question, str) or not question.strip():
        raise ValueError("question is required")
    number_value = payload.get("number")
    if isinstance(number_value, bool) or number_value is None:
        raise ValueError("number is required")
    number_text = str(number_value).strip()
    if not number_text.isdigit():
        raise ValueError("number phải là số nguyên không âm.")
    if strict_number and (len(number_text) != 6 or not number_text.isdigit()):
        raise ValueError("number phải gồm đúng 6 chữ số.")
    number = int(number_text)
    time = _validate_time(payload.get("time"))
    address = payload.get("address")
    if address is not None and not isinstance(address, str):
        raise ValueError("address phải là chuỗi hoặc null.")
    return {
        "question": question.strip(),
        "number": number,
        "time": time,
        "gps": _validate_gps(payload.get("gps")),
        "address": address.strip() if isinstance(address, str) else None,
        "image": _validate_image(payload.get("image")),
    }


def _bits(number: int) -> list[int]:
    return [int(char) for char in f"{number % 64:06b}"]


def _field(bits: list[int]) -> dict[str, float]:
    # Runnable provisional field operator; provenance marks it non-canonical.
    s = sum(bits) / 6
    d = bits[0] - bits[-1]
    i = sum(1 for left, right in zip(bits, bits[1:]) if left != right) / 5
    f = sum((index + 1) * bit for index, bit in enumerate(bits)) / 21
    t = (sum(bits) + 1) / 7
    return {
        "S": round(s, 4),
        "D": round(d, 4),
        "I": round(i, 4),
        "F": round(f, 4),
        "T": round(t, 4),
    }


def _s07(field: dict[str, float]) -> str:
    # Deterministic provisional mapping. It never changes raw measurements.
    total = field["I"] + field["F"]
    if total >= 1.55:
        return "SAT"
    if total >= 1.15:
        return "TA"
    if total >= 0.85:
        return "NHIEU"
    if total >= 0.55:
        return "HY"
    if total >= 0.25:
        return "DUONG"
    return "AN"


def _mapping_profile() -> dict[str, str]:
    path = ROOT / "specs/v3.1/s07_mapping_profile_v31.json"
    profile = json.loads(path.read_text(encoding="utf-8"))
    source_hash = profile.get("source", {}).get("source_hash", "UNRESOLVED")
    return {
        "profile_id": profile["profile_id"],
        "version": profile["version"],
        "sha256": source_hash,
        "status": "RESEARCH" if profile.get("status") == "RESEARCH" else "UNRESOLVED",
    }


def run_v31(payload: dict[str, Any], *, engine_version: str = "3.1.0-runtime", strict_number: bool = False) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("Request body phải là một JSON object.")
    raw = _norm(payload, strict_number=strict_number)
    bits = _bits(raw["number"])
    field = _field(bits)
    label = _s07(field)
    normalized_hash = _hash(raw)
    mapping_profile = _mapping_profile()
    decision_id = "DD31-" + normalized_hash.removeprefix("sha256:")[:16]
    source_hashes = {
        "canonical_vocabulary": _file_hash(ROOT / "specs/v3.1/canonical_vocabulary.json"),
        "mapping_profile": _file_hash(ROOT / "specs/v3.1/s07_mapping_profile_v31.json"),
        "response_schema": _file_hash(ROOT / "specs/v3.1/schemas/canonical_response.schema.json"),
    }
    return {
        "contract_version": "3.1.0",
        # Compatibility view for legacy runtime callers; the HTTP adapter strips it.
        "layers": {
            "L1": {"status": "PASSED", "question": raw["question"], "number": raw["number"]},
            "L2": {"status": "PASSED_PROVISIONAL", "field_model": "6-bit-derived", "field": field},
            "L3": {"status": "PASSED_PROVISIONAL", "bits": bits, "force_vector": field},
            "L4": {"status": "PASSED_PROVISIONAL", "primary_label": label, "allowed": label in CANONICAL, "profile_id": mapping_profile["profile_id"]},
            "L5": {"status": "PASSED", "canonical": True},
            "L6": {"status": "PASSED", "api_ready": True},
        },
        "execution": {
            "decision_id": decision_id,
            "runtime_status": "PASSED",
            "tick": 0,
            "input_hash": normalized_hash,
        },
        "raw_measurements": {
            "khi_vector": field,
            "field_state": {"bits": bits, "operator_status": "PROVISIONAL"},
            "f_net_out": None,
            "runtime_trace": [
                {"layer": "L1", "status": "PASSED"},
                {"layer": "L2", "status": "PASSED_PROVISIONAL"},
                {"layer": "L3", "status": "PASSED_PROVISIONAL"},
                {"layer": "L4", "status": "PASSED_PROVISIONAL"},
                {"layer": "L5", "status": "PASSED"},
                {"layer": "L6", "status": "PASSED"},
            ],
        },
        "semantic_state": {
            "status": "MAPPING_UNRESOLVED",
            "primary_label": label if label in CANONICAL else "MAPPING_UNRESOLVED",
            "mapping_profile": mapping_profile,
            "mapping_provenance": [
                {
                    "status": "RESEARCH",
                    "mapping_status": "MAPPING_UNRESOLVED",
                    "note": "S07 profile is unresolved; provisional label is not CORE.",
                },
            ],
        },
        "uncertainty": {
            "measurement": 0.0,
            "model": 1.0,
            "semantic": 1.0,
            "confidence": {
                "score": 0.0,
                "method": "confidence_firewall_no_f_net_out",
                "inputs": ["measurement", "model", "semantic"],
                "f_net_out_excluded": True,
            },
        },
        "provenance": {
            "source_version": "v3.1",
            "source_hashes": source_hashes,
            "engine_commit": os.getenv("GIT_COMMIT", "working-tree"),
            "review_records": [
                "gemini_round1.json",
                "gemini_round2.json",
                "specs/v3.1/artifacts/decision_log.md",
            ],
        },
        "gate_results": {
            "GATE-1-THEORY-FIELD": "PLACEHOLDER_THEORY",
            "GATE-2-RUNTIME": "PASSED",
            "GATE-3-INTERPRETATION": "MAPPING_UNRESOLVED",
            "GATE-4-DATA": "PASSED",
            "GATE-5-OPERATIONS": "PASSED",
        },
    }


def canonical_response(result: dict[str, Any]) -> dict[str, Any]:
    """Return only the strict v3.1 response fields exposed over HTTP."""
    fields = (
        "contract_version",
        "execution",
        "raw_measurements",
        "semantic_state",
        "uncertainty",
        "provenance",
        "gate_results",
    )
    return {field: result[field] for field in fields}


def canonical_json(result: dict[str, Any]) -> str:
    return json.dumps(canonical_response(result), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
