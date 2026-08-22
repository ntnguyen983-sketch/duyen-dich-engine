import os
import unittest
from unittest.mock import patch

from app import app
from services.ai_inference import GeminiProviderError


PAYLOAD = {
    "question": "Ca làm việc hôm nay có thuận lợi không?",
    "number": 369147,
    "time": "2026-08-20T12:00:00+00:00",
    "gps": {"lat": 10.755124, "lng": 106.616242},
    "address": "test",
}


AI_RESULT = {
    "status": "provisional",
    "headline": "Có lực để tiến, nhưng cần giữ nhịp",
    "answer": "Nếu giữ điều kiện hiện tại, xu hướng là có thể tiến từng bước; tránh quyết định vội.",
    "reading": "Hào động và vector hiện tại gợi ý nên ưu tiên kiểm soát nhịp hành động.",
    "signals": [
        {
            "name": "Vector Khí",
            "direction": "mixed",
            "evidence_paths": ["raw_measurements.khi_vector"],
            "meaning": "Có tín hiệu hỗn hợp nên cần quan sát thêm.",
        }
    ],
    "forecast": {
        "near_term": "Tiến triển từng bước.",
        "condition": "Nếu giữ cách làm hiện tại.",
        "turning_point": "Khi điều kiện thực địa thay đổi.",
    },
    "actions": ["Kiểm tra điều kiện thực tế trước khi chốt."],
    "uncertainty": {"score": 0.7, "note": "Mapping còn provisional."},
    "limitations": ["Luận giải AI không phải kết luận CORE."],
    "trace": {
        "model": "test-model",
        "engine_execution_id": "placeholder",
        "engine_input_hash": "placeholder",
        "engine_content_fingerprint": "placeholder",
        "source_version": "v3.0dd-architecture + v3.1-runtime",
        "inference_layer": "AI_INTERPRETATION",
        "generated_at": "2026-08-22T00:00:00+00:00",
    },
}


class AIInterpretationEndpointTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        app.config.update(TESTING=True)
        cls.client = app.test_client()

    @patch("app.generate_ai_interpretation")
    def test_ai_endpoint_keeps_engine_and_overlays_ai(self, generate):
        generate.return_value = AI_RESULT
        response = self.client.post("/api/v31/analyze", json=PAYLOAD)
        self.assertEqual(response.status_code, 200)
        body = response.get_json()
        self.assertEqual(body["engine_output"]["contract_version"], "3.1.0")
        self.assertEqual(body["ai_interpretation"]["answer"], AI_RESULT["answer"])
        self.assertEqual(
            body["ai_trace"]["engine_input_hash"],
            body["engine_output"]["execution"]["input_hash"],
        )
        self.assertEqual(
            body["ai_interpretation"]["trace"]["engine_execution_id"],
            body["engine_output"]["execution"]["execution_id"],
        )
        generate.assert_called_once()

    @patch("app.generate_ai_interpretation")
    def test_provider_failure_does_not_hide_engine_output(self, generate):
        generate.side_effect = GeminiProviderError("provider unavailable")
        response = self.client.post("/api/v31/analyze", json=PAYLOAD)
        self.assertEqual(response.status_code, 502)
        body = response.get_json()
        self.assertEqual(body["code"], "AI_INTERPRETATION_FAILED")
        self.assertEqual(body["engine_output"]["contract_version"], "3.1.0")
        self.assertNotIn("provider unavailable", body["error"])

    @patch.dict(os.environ, {"GEMINI_API_KEY": ""})
    def test_missing_key_returns_configuration_error(self):
        response = self.client.post("/api/v31/analyze", json=PAYLOAD)
        self.assertEqual(response.status_code, 503)
        self.assertEqual(response.get_json()["code"], "GEMINI_NOT_CONFIGURED")


if __name__ == "__main__":
    unittest.main()
