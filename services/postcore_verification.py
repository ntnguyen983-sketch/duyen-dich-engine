"""Post-core verification: deterministic audit plus isolated NxNxspace witness.

This module is deliberately after the v3.0/v3.1 engine boundary. It never writes
back to the engine result and it never turns a research matrix into a CORE value.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

from research_only.nxnxspace import compute as nxnxspace_compute
from research_only.nxnxspace import NxNxspaceValidationError

CANONICAL = ("SAT", "TA", "NHIEU", "HY", "DUONG", "AN")


def _hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _bits(number: int) -> list[int]:
    return [int(char) for char in f"{number % 64:06b}"]


def _field(bits: list[int]) -> dict[str, float]:
    return {
        "S": round(sum(bits) / 6, 4),
        "D": round(bits[0] - bits[-1], 4),
        "I": round(sum(1 for left, right in zip(bits, bits[1:]) if left != right) / 5, 4),
        "F": round(sum((index + 1) * bit for index, bit in enumerate(bits)) / 21, 4),
        "T": round((sum(bits) + 1) / 7, 4),
    }


def _label(field: dict[str, float]) -> str:
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


def _compare(mismatches: list[dict[str, Any]], path: str, expected: Any, actual: Any) -> None:
    if expected != actual:
        mismatches.append({"path": path, "expected": expected, "actual": actual})


def audit_core_numbers(core_input: dict[str, Any], engine_output: dict[str, Any]) -> dict[str, Any]:
    """Recompute v3.x numeric/identity fields from normalized input and compare.

    The audit is intentionally explicit: if a displayed numeric value cannot be
    reproduced from the normalized input and documented formulas, the AI layer is
    blocked rather than being allowed to explain it.
    """
    mismatches: list[dict[str, Any]] = []
    number = int(core_input["number"])
    bits = _bits(number)
    dong = core_input.get("dong")
    moving_lines = [dong] if dong is not None else []
    transformed_bits = bits[:]
    if moving_lines:
        transformed_bits[6 - moving_lines[0]] = 1 - transformed_bits[6 - moving_lines[0]]
    root_code = int("".join(map(str, bits)), 2)
    transformed_code = int("".join(map(str, transformed_bits)), 2)
    field = _field(bits)
    expected_input_hash = _hash(core_input)

    execution = engine_output.get("execution") or {}
    identity = engine_output.get("identity") or {}
    dynamic_force = ((engine_output.get("dynamic_state") or {}).get("force") or {})
    raw_measurements = engine_output.get("raw_measurements") or {}
    output_a = engine_output.get("output_a") or {}
    semantic_state = engine_output.get("semantic_state") or {}
    uncertainty = engine_output.get("uncertainty") or {}

    _compare(mismatches, "execution.input_hash", expected_input_hash, execution.get("input_hash"))
    _compare(mismatches, "identity.root_bits", bits, identity.get("root_bits"))
    _compare(mismatches, "identity.moving_lines", moving_lines, identity.get("moving_lines"))
    _compare(mismatches, "identity.root_code", root_code, identity.get("root_code"))
    _compare(mismatches, "identity.transformed_code", transformed_code, identity.get("transformed_code"))
    _compare(mismatches, "dynamic_state.force", field, dynamic_force)
    _compare(mismatches, "raw_measurements.khi_vector", field, raw_measurements.get("khi_vector"))
    _compare(mismatches, "output_a.identity", identity, output_a.get("identity"))
    _compare(mismatches, "semantic_state.primary_label", _label(field), semantic_state.get("primary_label"))
    _compare(mismatches, "semantic_state.primary_label.allowed", True, semantic_state.get("primary_label") in CANONICAL)
    _compare(mismatches, "raw_measurements.f_net_out", None, raw_measurements.get("f_net_out"))
    _compare(mismatches, "uncertainty.confidence.f_net_out_excluded", True, ((uncertainty.get("confidence") or {}).get("f_net_out_excluded")))

    status = "PASSED" if not mismatches else "FAILED"
    return {
        "status": status,
        "method": "independent_v31_recomputation",
        "checked_paths": 12,
        "mismatch_count": len(mismatches),
        "mismatches": mismatches,
        "source": {
            "normalized_input_hash": expected_input_hash,
            "engine_execution_id": execution.get("execution_id", "unknown"),
            "engine_content_fingerprint": (engine_output.get("provenance") or {}).get("content_fingerprint", "unknown"),
        },
    }


def build_nxnxspace_snapshot(engine_output: dict[str, Any]) -> dict[str, Any]:
    """Build a research-only snapshot from observed line bits/moving flags.

    No new score is invented. Each two-dimensional vector is exactly
    `[canonical_bit, moving_flag]` from the locked engine identity.
    """
    identity = engine_output.get("identity") or {}
    bits = identity.get("root_bits")
    moving_lines = set(identity.get("moving_lines") or [])
    execution = engine_output.get("execution") or {}
    if not isinstance(bits, list) or len(bits) != 6:
        raise NxNxspaceValidationError("INVALID_ENGINE_IDENTITY", "engine identity must contain six root bits", "identity.root_bits")
    entities = []
    for line in range(1, 7):
        bit = bits[6 - line]
        if bit not in (0, 1):
            raise NxNxspaceValidationError("INVALID_ENGINE_BIT", "engine root bit must be 0 or 1", f"identity.root_bits[{6-line}]")
        entities.append({"id": f"H{line}", "vector": [float(bit), float(1 if line in moving_lines else 0)]})
    return {
        "tick_id": int(execution.get("tick", 0)),
        "entities": entities,
    }


def run_postcore_verification(core_input: dict[str, Any], engine_output: dict[str, Any]) -> dict[str, Any]:
    execution = engine_output.get("execution") or {}
    core_lock = execution.get("core_lock_mode") in {"LOCKED", "CANONICAL_LOCKED"}
    audit = audit_core_numbers(core_input, engine_output)
    nxnxspace_result: dict[str, Any]
    try:
        snapshot = build_nxnxspace_snapshot(engine_output)
        nxnxspace_result = nxnxspace_compute(snapshot)
    except NxNxspaceValidationError as exc:
        nxnxspace_result = {
            "namespace": "research_only.nxnxspace",
            "status": "research_only",
            "error": {"code": exc.code, "message": str(exc), "path": exc.path},
        }
    except Exception as exc:
        nxnxspace_result = {
            "namespace": "research_only.nxnxspace",
            "status": "research_only",
            "error": {"code": "NXNXSPACE_FAILED", "message": str(exc)},
        }
    nx_status = "PASSED" if "error" not in nxnxspace_result else "FAILED"
    status = "PASSED" if core_lock and audit["status"] == "PASSED" and nx_status == "PASSED" else "FAILED"
    return {
        "status": status,
        "breakpoint": "DD-3.0/3.1 CORE_LOCKED → NxNxspace → AI_INTERPRETATION",
        "core_lock": core_lock,
        "core_audit": audit,
        "nxnxspace": {
            "status": nx_status,
            "namespace": nxnxspace_result.get("namespace"),
            "deterministic_input_hash": nxnxspace_result.get("deterministic_input_hash"),
            "N": nxnxspace_result.get("N"),
            "space_state": nxnxspace_result.get("space_state"),
            "time_axis": nxnxspace_result.get("time_axis"),
            "error": nxnxspace_result.get("error"),
        },
        "no_writeback": True,
        "provenance": {
            "engine_execution_id": execution.get("execution_id", "unknown"),
            "engine_content_fingerprint": (engine_output.get("provenance") or {}).get("content_fingerprint", "unknown"),
            "layer": "POSTCORE_VERIFICATION",
        },
    }
