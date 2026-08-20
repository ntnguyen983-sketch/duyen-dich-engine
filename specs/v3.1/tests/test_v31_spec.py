from __future__ import annotations

import hashlib
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def canonical_hash(value):
    return 'sha256:' + hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')).hexdigest()


class TestV31CanonicalSpec(unittest.TestCase):
    def setUp(self) -> None:
        self.vocabulary = json.loads((ROOT / 'canonical_vocabulary.json').read_text(encoding='utf-8'))
        self.mapping = json.loads((ROOT / 's07_mapping_profile_v31.json').read_text(encoding='utf-8'))
        self.profiles = json.loads((ROOT / 'runtime_profiles_v31.json').read_text(encoding='utf-8'))
        self.schema = json.loads((ROOT / 'schemas/canonical_response.schema.json').read_text(encoding='utf-8'))
        self.decoder = json.loads((ROOT / 'compatibility/legacy_decoder.json').read_text(encoding='utf-8'))
        self.spec = (ROOT / 'DUYEN_DICH_v3.1.md').read_text(encoding='utf-8')
        self.decisions = (ROOT / 'artifacts/decision_log.md').read_text(encoding='utf-8')

    def test_exact_s07_enum(self):
        self.assertEqual([x['code'] for x in self.vocabulary['s07_states']], ['SAT', 'TA', 'NHIEU', 'HY', 'DUONG', 'AN'])
        self.assertFalse(self.vocabulary['kernel_constraints']['legacy_codes_allowed'])
        self.assertIn('MAPPING_AMBIGUOUS', self.vocabulary['non_semantic_states'])

    def test_legacy_is_not_canonical(self):
        canonical_codes = {x['code'] for x in self.vocabulary['s07_states']}
        for label in self.decoder['legacy_labels']:
            self.assertNotIn(label, canonical_codes)
        self.assertFalse(self.decoder['decode_policy']['kernel_entry_allowed'])
        self.assertIsNone(self.decoder['decode_policy']['canonical_target'])

    def test_s07_profile_has_rules_and_vectors(self):
        self.assertEqual(self.mapping['profile_id'], 'S07-HIST-2.9.1-NEW2')
        self.assertEqual(self.mapping['status'], 'CALIBRATION_REQUIRED')
        self.assertEqual(len(self.mapping['rules']), 6)
        self.assertGreaterEqual(len(self.mapping['boundary_vectors']), 9)
        self.assertTrue(self.mapping['rule_config_sha256'].startswith('sha256:'))
        overlap = next(x for x in self.mapping['boundary_vectors'] if x['id'] == 'S07-B-OVERLAP-DUONG-HY')
        self.assertEqual(overlap['expected_status'], 'MAPPING_AMBIGUOUS')
        self.assertEqual(set(overlap['expected_matches']), {'DUONG', 'HY'})

    def test_profile_hash_matches_registry(self):
        self.assertEqual(self.mapping['rule_config_sha256'], self.profiles['profiles']['S07-HIST-2.9.1-NEW2']['rule_config_sha256'])
        self.assertEqual(self.vocabulary['source']['source_hash'], 'sha256:' + hashlib.sha256((ROOT / 'runtime_profiles_v31.json').read_bytes()).hexdigest())

    def test_runtime_profiles_have_guards(self):
        dwl = self.profiles['profiles']['DWL-0.1-REV-A-FNORM']
        self.assertEqual(dwl['guards']['persistence_denominator_missing'], 'QUARANTINE')
        self.assertEqual(dwl['guards']['confidence_input_scan'], 'G7_FIREWALL_DIRECTION')
        self.assertEqual(self.profiles['profiles']['MATRIX-2.9.3-FULL']['matrices']['M_POL']['shape'], [10, 10])

    def test_schema_is_strict_about_labels_and_confidence(self):
        semantic = self.schema['properties']['semantic_state']['properties']
        self.assertEqual(set(semantic['primary_label']['enum']), {'SAT', 'TA', 'NHIEU', 'HY', 'DUONG', 'AN', 'MAPPING_UNRESOLVED', 'MAPPING_AMBIGUOUS'})
        confidence = self.schema['properties']['uncertainty']['properties']['confidence']
        self.assertTrue(confidence['properties']['f_net_out_excluded']['const'])
        self.assertEqual(confidence['properties']['f_net_out_found']['const'], False)
        self.assertIn('audit_status', confidence['required'])
        self.assertIn('scanned_paths', confidence['required'])

    def test_spec_contains_complete_runtime(self):
        for text in ['S00–S11', 'W_ij', 'F_norm', 'DPKE', 'DD-DELAY-2.9.2-TF1', 'BEC-OBS-1', 'MAPPING_AMBIGUOUS', 'SYNC_RESONANCE', 'CALIBRATION_REQUIRED']:
            self.assertIn(text, self.spec)
        self.assertIn('`CALIBRATION_REQUIRED` không còn là chỗ trống', self.spec)

    def test_spec_keeps_60_tick_and_h1_research(self):
        self.assertIn('classification `RESEARCH`', self.spec)
        self.assertIn('H1 Drain/Reserve', self.spec)
        self.assertIn('không tự phase shift', self.spec)

    def test_required_test_vectors_are_documented(self):
        for tv in ['TV-01', 'TV-07', 'TV-08', 'TV-09', 'TV-14', 'TV-15', 'TV-16']:
            self.assertIn(tv, self.spec)
        self.assertIn('S07-B-OVERLAP-DUONG-HY', json.dumps(self.mapping, ensure_ascii=False))
        self.assertIn('PERSISTENCE_DENOMINATOR_MISSING', self.spec)

    def test_decision_log_keeps_governance(self):
        for code in ['DD31-DEC-005', 'DD31-DEC-006', 'DD31-DEC-007', 'DD31-DEC-009']:
            self.assertIn(code, self.decisions)


if __name__ == '__main__':
    unittest.main()
