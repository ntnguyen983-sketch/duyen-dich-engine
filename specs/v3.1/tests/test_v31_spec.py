from __future__ import annotations

import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestV31CanonicalSpec(unittest.TestCase):
    def setUp(self) -> None:
        self.vocabulary = json.loads((ROOT / 'canonical_vocabulary.json').read_text(encoding='utf-8'))
        self.mapping = json.loads((ROOT / 's07_mapping_profile_v31.json').read_text(encoding='utf-8'))
        self.decoder = json.loads((ROOT / 'compatibility/legacy_decoder.json').read_text(encoding='utf-8'))
        self.schema = json.loads((ROOT / 'schemas/canonical_response.schema.json').read_text(encoding='utf-8'))
        self.spec = (ROOT / 'DUYEN_DICH_v3.1.md').read_text(encoding='utf-8')
        self.decisions = (ROOT / 'artifacts/decision_log.md').read_text(encoding='utf-8')

    def test_exact_s07_enum(self):
        self.assertEqual(
            [item['code'] for item in self.vocabulary['s07_states']],
            ['SAT', 'TA', 'NHIEU', 'HY', 'DUONG', 'AN'],
        )
        self.assertFalse(self.vocabulary['kernel_constraints']['legacy_codes_allowed'])

    def test_legacy_is_not_canonical(self):
        canonical_codes = {item['code'] for item in self.vocabulary['s07_states']}
        for label in self.decoder['legacy_labels']:
            self.assertNotIn(label, canonical_codes)
        self.assertFalse(self.decoder['decode_policy']['kernel_entry_allowed'])
        self.assertIsNone(self.decoder['decode_policy']['canonical_target'])

    def test_mapping_is_unresolved_without_rules(self):
        self.assertEqual(self.mapping['mapping_status'], 'MAPPING_UNRESOLVED')
        self.assertEqual(self.mapping['rules'], [])
        self.assertEqual(self.mapping['unresolved_behavior']['missing_profile'], 'MAPPING_UNRESOLVED')
        self.assertEqual(self.mapping['unresolved_behavior']['invalid_hash'], 'MAPPING_UNRESOLVED')

    def test_schema_is_strict_about_labels_and_confidence(self):
        semantic = self.schema['properties']['semantic_state']['properties']
        labels = semantic['primary_label']['enum']
        self.assertEqual(set(labels), {'SAT', 'TA', 'NHIEU', 'HY', 'DUONG', 'AN', 'MAPPING_UNRESOLVED'})
        confidence = self.schema['properties']['uncertainty']['properties']['confidence']['properties']
        self.assertTrue(confidence['f_net_out_excluded']['const'])

    def test_spec_contains_firewall_and_failure_behavior(self):
        self.assertIn('Compute–Interpretation Firewall', self.spec)
        self.assertIn('MAPPING_UNRESOLVED', self.spec)
        self.assertIn('f_net_out', self.spec)
        self.assertIn('Không được dùng công thức suy đoán', self.spec)

    def test_decision_log_rejects_speculation(self):
        self.assertIn('DD31-DEC-005', self.decisions)
        self.assertIn('DD31-DEC-006', self.decisions)
        self.assertIn('DD31-DEC-007', self.decisions)
        self.assertIn('DD31-DEC-009', self.decisions)


if __name__ == '__main__':
    unittest.main()
