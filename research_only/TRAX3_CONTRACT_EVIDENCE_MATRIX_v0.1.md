# TRAX3 Contract Evidence Matrix — v0.1

**Status:** RESEARCH ONLY  
**Repository:** `ntnguyen983-sketch/duyen-dich-engine`  
**HEAD surveyed:** `7c3557b8e472507b4ccf1265199a8434f73e3a58` (`fix(ui): add DD-3A canonical per-line adapter`)  
**Date:** 2026-08-21  
**Scope:** Map what the repository *actually contains* for Trục 3  
`Evidence → Inference → Observation → Ground Truth → Calibration → Reliability`.

**Rules applied**

- No code changes, no commits, no deploys.
- No CORE modification proposals.
- Does not equate: computed = inferred, inferred = true, prediction = observation, observation = ground truth, ground truth = proof.
- Only records what exists in this repo tree and a live `run_v31` sample under the surveyed commit.

**Sample input used for CURRENT SHAPE**

```json
{
  "question": "tình cảm",
  "number": 369147,
  "time": "2026-08-21T07:25:00+07:00",
  "gps": {"lat": 10.755124, "lng": 106.616242},
  "dong": 3
}
```

---

## 0. System surface inventory (what runs)

| Layer | Path | Role | Status |
|---|---|---|---|
| Spec narrative | `specs/v3.1/DUYEN_DICH_v3.1.md` | Full L1–L6 + S00–S11 design | RELEASE_CANDIDATE text; not all implemented |
| JSON contract | `specs/v3.1/schemas/canonical_response.schema.json` | Canonical response shape | Present; `interpretation` optional |
| Vocabulary | `specs/v3.1/canonical_vocabulary.json` | S07 enum | Present |
| S07 profile | `specs/v3.1/s07_mapping_profile_v31.json` | Historical predicates | `status: CALIBRATION_REQUIRED` |
| Runtime profiles | `specs/v3.1/runtime_profiles_v31.json` | Matrix/topology/DPKE/delay formulas | Registry present; most operators not executed |
| Engine | `runtime/v31/engine.py` | Runnable L1–L6-lite | **PROVISIONAL operators** |
| API | `app.py` | Flask `/api/v31`, hexagram adapter | Present |
| Frontend | `ui_test/index.html` + `v31_runtime_fix.js` | Render + form | Present |
| DD-3A adapter | `ui_test/dd3a_per_line_adapter.js` | Client remap of `per_line` from `moving_lines` | Present; does not invent evidence fields |
| Tests | `test_api.py`, `runtime/v31/test_engine.py`, `ui_test/dd3a_per_line_adapter.test.js` | Contract + adapter | Present |
| `NxNxspace` | — | — | **NOT FOUND** anywhere in repo |

---

## PLACEHOLDER_WILL_REPLACE_WITH_FULL
