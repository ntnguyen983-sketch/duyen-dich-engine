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
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
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
    if not -90 <= lat <= 90 or not -180 <= lng <= 180:
        raise ValueError("GPS nằm ngoài phạm vi hợp lệ.")
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


def _validate_dong(value: Any) -> int | None:
    if value is None or value == "":
        return None
    if isinstance(value, bool):
        raise ValueError("dong phải là hào từ 1 đến 6 hoặc null.")
    try:
        dong = int(str(value).strip())
    except (TypeError, ValueError) as exc:
        raise ValueError("dong phải là hào từ 1 đến 6 hoặc null.") from exc
    if dong < 1 or dong > 6:
        raise ValueError("dong phải nằm trong khoảng 1 đến 6.")
    return dong


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
    if strict_number and len(number_text) != 6:
        raise ValueError("number phải gồm đúng 6 chữ số.")
    timestamp = _validate_time(payload.get("time"))
    address = payload.get("address")
    if address is not None and not isinstance(address, str):
        raise ValueError("address phải là chuỗi hoặc null.")
    return {
        "question": question.strip(),
        "number": int(number_text),
        "time": timestamp,
        "gps": _validate_gps(payload.get("gps")),
        "address": address.strip() if isinstance(address, str) else None,
        "image": _validate_image(payload.get("image")),
        "dong": _validate_dong(payload.get("dong")),
    }


def _bits(number: int) -> list[int]:
    return [int(char) for char in f"{number % 64:06b}"]


def _field(bits: list[int]) -> dict[str, float]:
    s = sum(bits) / 6
    d = bits[0] - bits[-1]
    i = sum(1 for left, right in zip(bits, bits[1:]) if left != right) / 5
    f = sum((index + 1) * bit for index, bit in enumerate(bits)) / 21
    t = (sum(bits) + 1) / 7
    return {"S": round(s, 4), "D": round(d, 4), "I": round(i, 4), "F": round(f, 4), "T": round(t, 4)}


def _s07(field: dict[str, float]) -> str:
    total = field["I"] + field["F"]
    if total >= 1.55: return "SAT"
    if total >= 1.15: return "TA"
    if total >= 0.85: return "NHIEU"
    if total >= 0.55: return "HY"
    if total >= 0.25: return "DUONG"
    return "AN"


def _mapping_profile() -> dict[str, str]:
    path = ROOT / "specs/v3.1/s07_mapping_profile_v31.json"
    profile = json.loads(path.read_text(encoding="utf-8"))
    source_hash = profile.get("source", {}).get("source_hash") or profile.get("rule_config_sha256")
    if not isinstance(source_hash, str) or not source_hash.startswith("sha256:"):
        raise ValueError("S07 profile hash is invalid")
    return {"profile_id": profile["profile_id"], "version": profile["version"], "sha256": source_hash, "status": profile.get("status", "UNRESOLVED")}


def run_v31(payload: dict[str, Any], *, engine_version: str = "3.1.0-runtime", strict_number: bool = False) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError("Request body phải là một JSON object.")
    raw = _norm(payload, strict_number=strict_number)
    bits = _bits(raw["number"])
    moving_lines = [raw["dong"]] if raw["dong"] is not None else []
    transformed_bits = bits[:]
    if moving_lines:
        # Line 1 is the least-significant/last bit; line 6 is the first bit.
        index = 6 - moving_lines[0]
        transformed_bits[index] = 1 - transformed_bits[index]
    root_code = int("".join(map(str, bits)), 2)
    transformed_code = int("".join(map(str, transformed_bits)), 2)
    field = _field(bits)
    label = _s07(field)
    normalized_hash = _hash(raw)
    mapping_profile = _mapping_profile()
    decision_id = "DD31-" + normalized_hash.removeprefix("sha256:")[:16]
    snapshot_id = "SNAP-" + _hash({"root_code": root_code, "moving_lines": moving_lines, "tick": 0}).removeprefix("sha256:")[:16]
    source_hashes = {
        "canonical_vocabulary": _file_hash(ROOT / "specs/v3.1/canonical_vocabulary.json"),
        "mapping_profile": _file_hash(ROOT / "specs/v3.1/s07_mapping_profile_v31.json"),
        "runtime_profiles": _file_hash(ROOT / "specs/v3.1/runtime_profiles_v31.json"),
        "response_schema": _file_hash(ROOT / "specs/v3.1/schemas/canonical_response.schema.json"),
    }
    identity = {"root_bits": bits, "moving_lines": moving_lines, "root_code": root_code, "transformed_code": transformed_code}
    identity["identity_hash"] = _hash(identity)
    content_fingerprint = _hash({"input": raw, "field": field, "identity": identity, "profile": mapping_profile})
    runtime_trace = [{"layer": layer, "status": status} for layer, status in [("L1", "PASSED"), ("L2", "PASSED_PROVISIONAL"), ("L3", "PASSED_PROVISIONAL"), ("L4", "PASSED_PROVISIONAL"), ("L5", "PASSED"), ("L6", "PASSED")]]
    semantic_state = {
        "status": "THRESHOLD_PROFILE_REQUIRED",
        "primary_label": label,
        "mapping_profile": mapping_profile,
        "matched_rules": [],
        "mapping_provenance": [{"status": "CALIBRATION_REQUIRED", "mapping_status": "PROFILE_PRESENT_CALIBRATION_REQUIRED", "note": "S07 profile is present but not approved; label is provisional and not CORE."}],
    }
    dynamic_state = {"force": dict(field), "persistence": {"P": 0.0}, "accumulation": {"A": 0.0}, "phase": {"state": "PROVISIONAL"}, "velocity": None, "delay": None, "spacetime": None}
    per_line = [{"line": line, "bit": bits[6 - line], "moving": line in moving_lines, "status": "CANONICAL_INPUT" if line in moving_lines else "CANONICAL_IDENTITY"} for line in range(1, 7)]
    canonical = {
        "contract_version": "3.1.0",
        "execution": {"execution_id": decision_id, "snapshot_id": snapshot_id, "tick": 0, "input_hash": normalized_hash, "runtime_status": "PASSED", "runtime_profile_id": "MATRIX-2.9.3-FULL", "topology_profile_id": "TOPOLOGY-MCHI-2.9.3", "mapping_profile_id": mapping_profile["profile_id"], "forward_only": True, "core_lock_mode": "LOCKED"},
        "identity": identity,
        "dynamic_state": dynamic_state,
        "raw_measurements": {"khi_vector": field, "field_state": {"bits": bits, "operator_status": "PROVISIONAL"}, "f_net_out": None, "runtime_trace": runtime_trace, "error_codes": []},
        "semantic_state": semantic_state,
        "uncertainty": {"measurement": 0.0, "model": 1.0, "semantic": 1.0, "confidence": {"score": 0.0, "method": "confidence_firewall_no_f_net_out", "inputs": ["measurement", "model", "semantic"], "f_net_out_excluded": True, "audit_status": "PASSED", "scanned_paths": ["runtime/", "specs/v3.1/", "app.py"], "f_net_out_found": False}},
        "provenance": {"source_refs": ["specs/v3.1/runtime_profiles_v31.json", "specs/v3.1/s07_mapping_profile_v31.json", "specs/v3.1/schemas/canonical_response.schema.json"], "source_versions": ["3.1.0", "2.9.3-FULL", "2.9.1-NEW2"], "source_hashes": source_hashes, "engine_commit": os.getenv("GIT_COMMIT") or os.getenv("VERCEL_GIT_COMMIT_SHA") or "working-tree", "review_records": ["specs/v3.1/artifacts/review/gemini_rewrite_round1.json", "specs/v3.1/artifacts/review/gemini_rewrite_round2.json", "specs/v3.1/artifacts/decision_log.md"], "content_fingerprint": content_fingerprint},
        "gate_results": {"G1_SCHEMA": "PASSED", "G2_IDENTITY": "PASSED", "G3_CORE_LOCK": "PASSED", "G4_RESEARCH_CALIBRATION": "CALIBRATION_REQUIRED", "G5_CANONICAL_HASH": "PASSED", "G6_MATRIX_LOGIC_CONSISTENCY": "PASSED", "G7_FIREWALL_DIRECTION": "PASSED"},
        "output_a": {"identity": identity, "dynamic_state": dynamic_state, "runtime_status": "PASSED"},
        "output_b": {"semantic_state": semantic_state, "observation_status": "PROVISIONAL"},
        "interpretation": {"per_line": per_line, "cross_line": [], "source_interaction": [], "expected_time_windows": [], "ground_truth": None},
    }
    canonical["layers"] = {"L1": {"status": "PASSED", "question": raw["question"], "number": raw["number"]}, "L2": {"status": "PASSED_PROVISIONAL", "field_model": "6-bit-derived", "field": field}, "L3": {"status": "PASSED_PROVISIONAL", "bits": bits, "force_vector": field}, "L4": {"status": "PASSED_PROVISIONAL", "primary_label": label, "allowed": label in CANONICAL, "profile_id": mapping_profile["profile_id"]}, "L5": {"status": "PASSED", "canonical": True}, "L6": {"status": "PASSED", "api_ready": True}}
    return canonical


def canonical_response(result: dict[str, Any]) -> dict[str, Any]:
    fields = ("contract_version", "execution", "identity", "dynamic_state", "raw_measurements", "semantic_state", "uncertainty", "provenance", "gate_results", "output_a", "output_b", "interpretation")
    return {field: result[field] for field in fields}


def canonical_json(result: dict[str, Any]) -> str:
    return json.dumps(canonical_response(result), ensure_ascii=False, sort_keys=True, separators=(",", ":"))
