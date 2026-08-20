import unittest
from engine import run_v31, canonical_json

class V31RuntimeTests(unittest.TestCase):
    def test_end_to_end(self):
        r=run_v31({"question":"tình cảm","number":369147,"time":"2026-08-20T12:00:00+07:00"})
        self.assertEqual(r["execution"]["runtime_status"],"PASSED")
        self.assertTrue(r["layers"]["L5"]["canonical"])
        self.assertIn(r["semantic_state"]["primary_label"],("SAT","TA","NHIEU","HY","DUONG","AN"))

    def test_deterministic(self):
        p={"question":"test","number":123456,"time":"2026-08-20T12:00:00+07:00"}
        self.assertEqual(canonical_json(run_v31(p)),canonical_json(run_v31(p)))

    def test_no_force_confidence(self):
        r=run_v31({"question":"test","number":1,"time":"2026-08-20T12:00:00+07:00"})
        self.assertTrue(r["uncertainty"]["confidence"]["f_net_out_excluded"])
        self.assertEqual(r["uncertainty"]["confidence"]["score"],0.0)

    def test_required_input(self):
        with self.assertRaises(ValueError): run_v31({"number":123456})

if __name__=="__main__": unittest.main()
