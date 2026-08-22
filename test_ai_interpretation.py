import os
import unittest
from unittest.mock import patch

from app import app
from services.ai_interpretation import GeminiProviderError


PAYLOAD = {
    "question": "Ca làm việc hôm nay có thuận lợi về số đơn và thu nhập không?",
    "number": 369147,
    "time": "2026-08-20T12:00:00+00:00",
    "gps": {"lat": 10.755124, "lng": 106.616242},
    "address": "TP.HCM",
}


class AIInterpretationEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.update(TESTING=True)
        cls.client = app.test_client()

    @patch("app.generate_interpretation")
    def test_ai_endpoint_keeps_engine_and_adds_interpretation(self, generate):
        generate.return_value = {
            "status": "provisional",
            "headline": "Có lực để tiến, nhưng cần giữ nhịp",
            "answer": "Nếu giữ điều kiện hiện tại, xu hướng là có thể tiến từng bước.",
            "reading": "Luận giải dựa trên output Engine.",
            "signals": [{
                "name": "Vector Khí",
                "direction": "mixed",
                "meaning": "Tín hiệu hỗn hợp.",
                "evidence_paths": ["raw_measurements.khi_vector"],
            }],
            "forecast": {
                "near_term": "Tiến triển từng bước.",
                "condition": "Nếu giữ cách làm hiện tại.",
                "turning_point": "Khi điều kiện thực tế thay đổi.",
            },
            "actions": ["Kiểm tra điều kiện thực tế trước khi chốt."],
            "uncertainty": {"score": 0.7, "note": "Mapping provisional."},
            "limitations": ["AI không phải CORE."],
            "trace": {"model": "test-model", "inference_layer": "AI_INTERPRETATION"},
        }
        response = self.client.post("/api/v31/interpret", json=PAYLOAD)
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertEqual(body["engine_output"]["contract_version"], "3.1.0")
        self.assertEqual(body["ai_interpretation"]["answer"], generate.return_value["answer"])
        self.assertEqual(
            body["ai_trace"]["engine_input_hash"],
            body["engine_output"]["execution"]["input_hash"],
        )
        self.assertEqual(
            body["ai_trace"]["engine_content_fingerprint"],
            body["engine_output"]["provenance"]["content_fingerprint"],
        )
        generate.assert_called_once()

    @patch("app.generate_interpretation")
    def test_provider_failure_keeps_engine_output(self, generate):
        generate.side_effect = GeminiProviderError("provider unavailable")
        response = self.client.post("/api/v31/interpret", json=PAYLOAD)
        self.assertEqual(response.status_code, 502)
        body = response.get_json()
        self.assertEqual(body["code"], "AI_INTERPRETATION_FAILED")
        self.assertEqual(body["engine_output"]["contract_version"], "3.1.0")
        self.assertNotIn("provider unavailable", body["error"])

    @patch.dict(os.environ, {"GEMINI_API_KEY": ""})
    def test_missing_key_returns_configuration_error(self):
        response = self.client.post("/api/v31/interpret", json=PAYLOAD)
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.get_json()["code"], "GEMINI_NOT_CONFIGURED")


if __name__ == "__main__":
    unittest.main()
