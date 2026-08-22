from __future__ import annotations

import ast
import copy
from pathlib import Path
import unittest

from research_only.nxnxspace import (
    NxNxspaceValidationError,
    compute,
    safe_compute,
)


class TestNxNxspacePrototype(unittest.TestCase):
    def test_n_zero(self) -> None:
        result = compute({"tick_id": 0, "entities": [], "timestamp": "2026-08-21T00:00:00Z"})
        self.assertEqual(result["N"], 0)
        self.assertEqual(result["cosine_similarity_matrix"], [])
        self.assertIsNone(result["space_state"]["dimension"])
        self.assertIsNone(result["space_state"]["pairwise_mean"])
        self.assertEqual(result["time_axis"]["tick_id"], 0)

    def test_n_one(self) -> None:
        result = compute(
            {
                "tick_id": 1,
                "entities": [{"id": "one", "vector": [3.0, 4.0]}],
                "timestamp": "2026-08-21T00:00:00Z",
            }
        )
        self.assertEqual(result["N"], 1)
        self.assertEqual(result["cosine_similarity_matrix"], [[1.0]])
        self.assertIsNone(result["space_state"]["pairwise_min"])

    def test_n_three_example(self) -> None:
        snapshot = {
            "tick_id": 42,
            "entities": [
                {"id": "entity_A", "vector": [0.2, 0.8]},
                {"id": "entity_B", "vector": [0.6, 0.4]},
                {"id": "entity_C", "vector": [0.9, 0.1]},
            ],
            "timestamp": "2026-08-21T00:00:00Z",
        }
        result = compute(snapshot)
        matrix = result["cosine_similarity_matrix"]
        self.assertEqual(result["N"], 3)
        self.assertEqual(result["tick_id"], 42)
        self.assertEqual(result["entity_vectors"], snapshot["entities"])
        self.assertAlmostEqual(matrix[0][1], 0.739940073396)
        self.assertAlmostEqual(matrix[0][2], 0.348186529604)
        self.assertAlmostEqual(matrix[1][2], 0.888217643156)
        self.assertEqual(result["namespace"], "research_only.nxnxspace")
        self.assertEqual(result["status"], "research_only")

    def test_duplicate_entity_is_rejected(self) -> None:
        with self.assertRaises(NxNxspaceValidationError) as context:
            compute(
                {
                    "tick_id": 2,
                    "entities": [
                        {"id": "same", "vector": [1.0]},
                        {"id": "same", "vector": [2.0]},
                    ],
                }
            )
        self.assertEqual(context.exception.code, "DUPLICATE_ENTITY_ID")

    def test_invalid_vector_is_rejected(self) -> None:
        invalid_snapshots = [
            {"tick_id": 3, "entities": [{"id": "x", "vector": [1.0, "bad"]}]},
            {"tick_id": 3, "entities": [{"id": "x", "vector": []}]},
            {"tick_id": 3, "entities": [{"id": "x", "vector": [float("nan")]}]},
            {
                "tick_id": 3,
                "entities": [
                    {"id": "x", "vector": [1.0, 2.0]},
                    {"id": "y", "vector": [1.0]},
                ],
            },
        ]
        for snapshot in invalid_snapshots:
            with self.subTest(snapshot=snapshot):
                with self.assertRaises(NxNxspaceValidationError):
                    compute(snapshot)

    def test_zero_vector_is_safe_and_explicit(self) -> None:
        result = compute(
            {
                "tick_id": 4,
                "entities": [
                    {"id": "zero", "vector": [0.0, 0.0]},
                    {"id": "nonzero", "vector": [1.0, 0.0]},
                ],
                "timestamp": "2026-08-21T00:00:00Z",
            }
        )
        self.assertEqual(result["space_state"]["zero_vector_count"], 1)
        self.assertEqual(result["cosine_similarity_matrix"], [[0.0, 0.0], [0.0, 1.0]])

    def test_repeat_same_input_has_same_matrix_state_and_hash(self) -> None:
        snapshot = {
            "tick_id": 42,
            "entities": [
                {"id": "entity_A", "vector": [0.2, 0.8]},
                {"id": "entity_B", "vector": [0.6, 0.4]},
                {"id": "entity_C", "vector": [0.9, 0.1]},
            ],
            "timestamp": "2026-08-21T00:00:00Z",
        }
        first = compute(snapshot)
        second = compute(copy.deepcopy(snapshot))
        self.assertEqual(first["cosine_similarity_matrix"], second["cosine_similarity_matrix"])
        self.assertEqual(first["space_state"], second["space_state"])
        self.assertEqual(first["deterministic_input_hash"], second["deterministic_input_hash"])
        self.assertEqual(first, second)

    def test_repeat_without_timestamp_keeps_math_deterministic(self) -> None:
        snapshot = {
            "tick_id": 7,
            "entities": [
                {"id": "a", "vector": [1.0, 0.0]},
                {"id": "b", "vector": [0.0, 1.0]},
            ],
        }
        first = compute(snapshot)
        second = compute(copy.deepcopy(snapshot))
        self.assertEqual(first["cosine_similarity_matrix"], second["cosine_similarity_matrix"])
        self.assertEqual(first["space_state"], second["space_state"])
        self.assertEqual(first["deterministic_input_hash"], second["deterministic_input_hash"])
        self.assertRegex(first["timestamp"], r"^\d{4}-\d{2}-\d{2}T")

    def test_matrix_is_symmetric(self) -> None:
        result = compute(
            {
                "tick_id": 5,
                "entities": [
                    {"id": "a", "vector": [1.0, 2.0, 3.0]},
                    {"id": "b", "vector": [-1.0, 0.5, 2.0]},
                    {"id": "c", "vector": [2.0, 0.0, 1.0]},
                ],
            }
        )
        matrix = result["cosine_similarity_matrix"]
        for row in range(len(matrix)):
            for column in range(len(matrix)):
                self.assertEqual(matrix[row][column], matrix[column][row])

    def test_failure_is_research_local(self) -> None:
        result = safe_compute(
            {"tick_id": 6, "entities": [{"id": "bad", "vector": [1.0, "bad"]}]}
        )
        self.assertEqual(result["namespace"], "research_only.nxnxspace")
        self.assertEqual(result["status"], "research_only")
        self.assertEqual(result["error"]["code"], "INVALID_VECTOR_COMPONENT")
        self.assertNotIn("canonical", result)

    def test_no_writeback_or_core_import_boundary(self) -> None:
        module_path = Path(__import__("research_only.nxnxspace", fromlist=["__file__"]).__file__)
        source = module_path.read_text(encoding="utf-8")
        tree = ast.parse(source)
        allowed_roots = {"__future__", "collections", "datetime", "hashlib", "json", "math", "typing"}
        imported_roots = set()
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_roots.update(alias.name.split(".")[0] for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module:
                imported_roots.add(node.module.split(".")[0])
        self.assertTrue(imported_roots <= allowed_roots)
        self.assertNotIn("specs/v3.1", source)
        self.assertNotIn("runtime/v31", source)
        self.assertNotIn("canonical_response", source)
        self.assertNotIn("dd-3a", source.lower())
        self.assertNotIn("open(", source)
        self.assertNotIn(".write(", source)
        self.assertNotIn("f_" + "net_out", source)

        repo_root = module_path.parents[3]
        self.assertTrue((repo_root / "research_only" / "nxnxspace").is_relative_to(repo_root / "research_only"))
        self.assertFalse(module_path.is_relative_to(repo_root / "runtime"))
        self.assertFalse(module_path.is_relative_to(repo_root / "specs"))


if __name__ == "__main__":
    unittest.main()
