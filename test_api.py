from __future__ import annotations

import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator

from app import app
from runtime.v31 import canonical_json, run_v31

ROOT = Path(__file__).resolve().parent


class ApiV31Tests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        schema = json.loads((ROOT / "specs/v3.1/schemas/canonical_response.schema.json").read_text(encoding="utf-8"))
        cls.validator = Draft202012Validator(schema)
        cls.payload = {
            "question": "tình cảm",
            "number": 369147,
            "time": "2026-08-20T12:00:00+07:00",
            "gps": {"lat": 10.755124, "lng": 106.616242},
            "address": "test",
            "image": None,
        }

    def test_get_root_and_api_ready(self):
        root = self.client.get("/")
        self.assertEqual(root.status_code, 200)
        self.assertIn("Duyên Dịch", root.text)
        ready = self.client.get("/api/v31")
        self.assertEqual(ready.status_code, 200)
        self.assertEqual(ready.json["contract_version"], "3.1.0")

    def test_post_returns_schema_valid_canonical_response(self):
        response = self.client.post("/api/v31", json=self.payload)
        self.assertEqual(response.status_code, 200)
        result = response.get_json()
        errors = list(self.validator.iter_errors(result))
        self.assertEqual(errors, [], [error.message for error in errors])
        self.assertIn(result["semantic_state"]["primary_label"], {"SAT", "TA", "NHIEU", "HY", "DUONG", "AN"})
        self.assertTrue(result["uncertainty"]["confidence"]["f_net_out_excluded"])
        self.assertTrue(result["provenance"])

    def test_invalid_required_inputs_are_rejected(self):
        for field in ("question", "number", "time"):
            payload = dict(self.payload)
            payload.pop(field)
            response = self.client.post("/api/v31", json=payload)
            self.assertEqual(response.status_code, 400, field)
        for number in (12345, 1234567, "abc123"):
            payload = dict(self.payload, number=number)
            response = self.client.post("/api/v31", json=payload)
            self.assertEqual(response.status_code, 400, number)

    def test_gps_and_image_inputs_are_accepted(self):
        response = self.client.post(
            "/api/v31",
            json=dict(self.payload, image={"name": "test.png", "type": "image/png", "size": 12}),
        )
        self.assertEqual(response.status_code, 200)
        bad_gps = self.client.post("/api/v31", json=dict(self.payload, gps={"lat": 100, "lng": 0}))
        self.assertEqual(bad_gps.status_code, 400)

    def test_hexagram_envelope_is_adapted_without_changing_canonical_output(self):
        payload = {
            "data_1": {
                "time": "2026-08-21T01:26:43+07:00",
                "gps_show": {"lat": 10.75554, "lng": 106.611772},
                "number": "3458769",
                "dong": 3,
            },
            "data_2": {
                "question": "Ca làm việc shipper từ 01:45 AM đến 06:00 AM, số đơn và thu nhập.",
                "dq_g": "110",
                "dq_b": "100",
                "que_goc_s": "Phong Lôi Ích",
                "que_bien_s": "Phong Hỏa Gia Nhân",
                "sl_am": 8,
                "sl_duong": 10,
                "dq_gs": "Đoài (Trạch)",
                "dq_bs": "Chấn (Lôi)",
                "engine_field": "HƯỚNG Âm động chuyển Dương",
                "truong": {"Moc": 2, "Hoa": 4, "Tho": -2, "Kim": -4, "Thuy": -6},
                "the": 1,
                "quy_tac_luan": "QT LỰC 1",
            },
        }
        response = self.client.post("/api/v31", json=payload)
        self.assertEqual(response.status_code, 200)
        result = response.get_json()
        errors = list(self.validator.iter_errors(result))
        self.assertEqual(errors, [], [error.message for error in errors])
        self.assertEqual(result["contract_version"], "3.1.0")
        self.assertEqual(result["execution"]["runtime_status"], "PASSED")
        self.assertTrue(result["uncertainty"]["confidence"]["f_net_out_excluded"])

    def test_deterministic_request_and_canonical_json(self):
        first = run_v31(self.payload)
        second = run_v31(self.payload)
        self.assertEqual(canonical_json(first), canonical_json(second))
        self.assertEqual(first["execution"]["input_hash"], second["execution"]["input_hash"])


if __name__ == "__main__":
    unittest.main()
