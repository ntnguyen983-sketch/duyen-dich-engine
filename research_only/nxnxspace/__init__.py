"""NxNxspace research-only deterministic snapshot prototype.

This module is intentionally self-contained. It has no imports from the
Duyên Dịch runtime, specification, API, canonical store, or adapters.
"""

from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import json
import math
from collections.abc import Mapping, Sequence
from typing import Any

NAMESPACE = "research_only.nxnxspace"
STATUS = "research_only"
ROUND_DIGITS = 12


class NxNxspaceValidationError(ValueError):
    """A validation failure local to the research-only prototype."""

    def __init__(self, code: str, message: str, path: str = "") -> None:
        self.code = code
        self.path = path
        super().__init__(message)


def _fail(code: str, message: str, path: str = "") -> None:
    raise NxNxspaceValidationError(code, message, path)


def _rounded(value: float) -> float:
    rounded = round(value, ROUND_DIGITS)
    return 0.0 if rounded == 0.0 else rounded


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _utc_timestamp() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def _validate_snapshot(snapshot: Mapping[str, Any]) -> tuple[int, list[dict[str, Any]], str]:
    if not isinstance(snapshot, Mapping):
        _fail("SNAPSHOT_NOT_OBJECT", "snapshot must be an object", "snapshot")

    tick_id = snapshot.get("tick_id")
    if type(tick_id) is not int or tick_id < 0:
        _fail("INVALID_TICK_ID", "tick_id must be a non-negative integer", "tick_id")

    raw_entities = snapshot.get("entities")
    if not isinstance(raw_entities, Sequence) or isinstance(raw_entities, (str, bytes)):
        _fail("INVALID_ENTITIES", "entities must be an array", "entities")

    timestamp = snapshot.get("timestamp")
    if timestamp is not None and (not isinstance(timestamp, str) or not timestamp.strip()):
        _fail("INVALID_TIMESTAMP", "timestamp must be a non-empty string when provided", "timestamp")

    normalized: list[dict[str, Any]] = []
    seen_ids: set[str] = set()
    dimension: int | None = None

    for index, raw_entity in enumerate(raw_entities):
        path = f"entities[{index}]"
        if not isinstance(raw_entity, Mapping):
            _fail("INVALID_ENTITY", "each entity must be an object", path)

        entity_id = raw_entity.get("id")
        if not isinstance(entity_id, str) or not entity_id:
            _fail("INVALID_ENTITY_ID", "entity id must be a non-empty string", f"{path}.id")
        if entity_id in seen_ids:
            _fail("DUPLICATE_ENTITY_ID", f"duplicate entity id: {entity_id}", f"{path}.id")
        seen_ids.add(entity_id)

        raw_vector = raw_entity.get("vector")
        if not isinstance(raw_vector, Sequence) or isinstance(raw_vector, (str, bytes)):
            _fail("INVALID_VECTOR", "vector must be an array", f"{path}.vector")
        if len(raw_vector) == 0:
            _fail("INVALID_VECTOR", "vector must not be empty", f"{path}.vector")
        if dimension is None:
            dimension = len(raw_vector)
        elif len(raw_vector) != dimension:
            _fail("VECTOR_DIMENSION_MISMATCH", "all vectors must have the same dimension", f"{path}.vector")

        vector: list[float] = []
        for component_index, component in enumerate(raw_vector):
            if isinstance(component, bool) or not isinstance(component, (int, float)):
                _fail(
                    "INVALID_VECTOR_COMPONENT",
                    "vector components must be finite numbers",
                    f"{path}.vector[{component_index}]",
                )
            numeric = float(component)
            if not math.isfinite(numeric):
                _fail(
                    "INVALID_VECTOR_COMPONENT",
                    "vector components must be finite numbers",
                    f"{path}.vector[{component_index}]",
                )
            vector.append(numeric)
        normalized.append({"id": entity_id, "vector": vector})

    return tick_id, normalized, timestamp if isinstance(timestamp, str) else _utc_timestamp()


def _cosine(left: Sequence[float], right: Sequence[float]) -> float:
    left_norm_sq = math.fsum(value * value for value in left)
    right_norm_sq = math.fsum(value * value for value in right)
    if left_norm_sq == 0.0 or right_norm_sq == 0.0:
        return 0.0
    dot = math.fsum(left_value * right_value for left_value, right_value in zip(left, right))
    return _rounded(dot / math.sqrt(left_norm_sq * right_norm_sq))


def _build_matrix(vectors: Sequence[Sequence[float]]) -> list[list[float]]:
    size = len(vectors)
    matrix = [[0.0 for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for column in range(row, size):
            similarity = _cosine(vectors[row], vectors[column])
            matrix[row][column] = similarity
            matrix[column][row] = similarity
    return matrix


def _build_space_state(matrix: Sequence[Sequence[float]], vectors: Sequence[Sequence[float]]) -> dict[str, Any]:
    pairwise = [matrix[row][column] for row in range(len(matrix)) for column in range(row + 1, len(matrix))]
    return {
        "kind": "cosine_similarity_snapshot",
        "dimension": len(vectors[0]) if vectors else None,
        "zero_vector_count": sum(1 for vector in vectors if all(value == 0.0 for value in vector)),
        "pairwise_mean": _rounded(math.fsum(pairwise) / len(pairwise)) if pairwise else None,
        "pairwise_min": min(pairwise) if pairwise else None,
        "pairwise_max": max(pairwise) if pairwise else None,
    }


def compute(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    """Compute a research-only NxN cosine matrix from one snapshot.

    The returned timestamp may reflect observation time when omitted by the
    input. Matrix, state and deterministic_input_hash do not depend on it.
    """

    tick_id, entities, timestamp = _validate_snapshot(snapshot)
    hash_payload = {"entities": entities, "tick_id": tick_id}
    deterministic_input_hash = hashlib.sha256(
        _canonical_json(hash_payload).encode("utf-8")
    ).hexdigest()

    vectors = [entity["vector"] for entity in entities]
    matrix = _build_matrix(vectors)
    space_state = _build_space_state(matrix, vectors)

    return {
        "namespace": NAMESPACE,
        "status": STATUS,
        "N": len(entities),
        "tick_id": tick_id,
        "timestamp": timestamp,
        "deterministic_input_hash": deterministic_input_hash,
        "entity_vectors": entities,
        "cosine_similarity_matrix": matrix,
        "space_state": space_state,
        "time_axis": {"kind": "discrete_tick", "tick_id": tick_id, "unit": "tick"},
    }


def safe_compute(snapshot: Mapping[str, Any]) -> dict[str, Any]:
    """Return a research-only error envelope for validation failures only."""

    try:
        return compute(snapshot)
    except NxNxspaceValidationError as error:
        return {
            "namespace": NAMESPACE,
            "status": STATUS,
            "error": {
                "code": error.code,
                "message": str(error),
                "path": error.path,
            },
        }


__all__ = [
    "NAMESPACE",
    "STATUS",
    "NxNxspaceValidationError",
    "compute",
    "safe_compute",
]
