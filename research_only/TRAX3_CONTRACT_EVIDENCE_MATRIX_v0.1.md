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

## 1. CORE FACT

Facts locked from validated input / deterministic identity. Not semantic.

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| `question` (input) | `engine.py` `_norm` | string, required | PRESENT (input only) | OBSERVED (client-supplied) | HTTP body | `input_hash` covers normalized form | YES as *input evidence*, not outcome evidence | Not re-emitted in `canonical_response` body (only in internal `layers.L1`, stripped by `canonical_response`) |
| `number` | `engine.py` `_norm`, `_bits` | non-negative int; flat requires 6 digits | PRESENT | OBSERVED → COMPUTED bits | payload | `input_hash` | YES | `369147 % 64 → root_code 59` |
| `time` | `engine.py` `_validate_time` | ISO-8601 string | PRESENT (input) | OBSERVED | payload | in `input_hash` | YES as timestamp of request | Not copied into a dedicated response field beyond hash |
| `gps` | `engine.py` `_validate_gps` | `{lat,lng}` or null | PRESENT (input validation) | OBSERVED | payload | in `input_hash` | YES as spatial input | **Not present in canonical response body** |
| `address`, `image` | `engine.py` | optional | PRESENT (accepted) | OBSERVED | payload | in `input_hash` | YES as input metadata | Not emitted in response |
| `dong` / moving line | `engine.py` `_validate_dong` | int 1–6 or null | PRESENT | OBSERVED (client) | payload / `data_1.dong` | identity | YES | Single moving line only in current engine |
| `root_bits` | `engine.py` `_bits` | length-6 array of 0/1 | PRESENT | COMPUTED | `number % 64` | `identity_hash` | YES | Deterministic |
| `root_code` | `engine.py` | int 0–63 | PRESENT | COMPUTED | `root_bits` | identity | YES | |
| `transformed_code` | `engine.py` | int 0–63 | PRESENT | COMPUTED | `root_bits` + flip if `dong` | identity | YES | Flip rule: line 1 = LSB |
| `moving_lines` | `engine.py` | `[]` or `[dong]` | PRESENT | COMPUTED from observed `dong` | `dong` | identity | YES | Empty if `dong` omitted |
| `identity_hash` | `engine.py` | `sha256:…` | PRESENT | COMPUTED | identity object | provenance chain | YES | |
| `input_hash` | `engine.py` | `sha256:…` of normalized input | PRESENT | COMPUTED | normalized payload | execution | YES | |
| `contract_version` | schema + engine | `"3.1.0"` | PRESENT | MAPPED (const) | schema | contract | YES | |
| Schema-required identity fields | schema | `root_bits`, `moving_lines`, `root_code`, `transformed_code`, `identity_hash` | PRESENT | — | — | schema G1 | YES | |

---

## 2. DERIVED STATE

Numeric / structural state derived from CORE FACT. May be provisional formulas.

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| `khi_vector` / field `{S,D,I,F,T}` | `engine.py` `_field` | floats rounded 4dp | PRESENT | COMPUTED | `root_bits` only | `field_state.operator_status=PROVISIONAL` | **LIMITED** | Formula is self-contained provisional; **not** the full SL-DIF/BEC field of the spec |
| `dynamic_state.force` | `engine.py` | same dict as `khi_vector` | PRESENT | COMPUTED (alias) | `_field` | dynamic_state | LIMITED | Duplicate of khi_vector, not matrix-derived force |
| `persistence.P` | `engine.py` | `{P: 0.0}` | PRESENT (placeholder) | COMPUTED (constant) | none | hard-coded | **NO** as real persistence | Always 0.0; no history |
| `accumulation.A` | `engine.py` | `{A: 0.0}` | PRESENT (placeholder) | COMPUTED (constant) | none | hard-coded | **NO** | Always 0.0 |
| `phase.state` | `engine.py` | `"PROVISIONAL"` | PRESENT (placeholder) | MAPPED (const) | none | hard-coded | **NO** as temporal phase | Spec lists 12 phase operators; runtime does not implement them |
| `velocity` | `engine.py` + profile `DPKE-1` | `null` | SLOT PRESENT / VALUE MISSING | — | DPKE profile not applied | profile registry only | **NO** | Formula exists in `runtime_profiles_v31.json`, not executed |
| `delay` | `engine.py` + profile `DD-DELAY-2.9.2-TF1` | `null` | SLOT PRESENT / VALUE MISSING | — | delay profile not applied | profile registry | **NO** | |
| `spacetime` | `engine.py` | `null` | SLOT PRESENT / VALUE MISSING | — | — | — | **NO** | |
| `tick` | `engine.py` | `0` always | PRESENT | COMPUTED (const) | — | execution | LIMITED | No multi-tick `observe()` loop in engine |
| `f_net_out` | `engine.py` | `null` | SLOT PRESENT / VALUE MISSING | — | — | confidence firewall scans for it | **NO** | Explicitly excluded from confidence |
| `field_state` | `engine.py` | `{bits, operator_status}` | PRESENT | COMPUTED | bits | raw_measurements | LIMITED | Marks operator provisional |
| 12-node topology graph | spec + `TOPOLOGY-MCHI-2.9.3` | defined in profile JSON | MISSING in runtime output | — | profile not executed | profile file | **NO** from live run | Spec S03; engine does not emit nodes/edges |
| Matrix force (`M_POL` etc.) | `MATRIX-2.9.3-FULL` | matrices in profile | MISSING in runtime computation | — | profile not read by engine | profile file | **NO** from live run | Profile status `CORE_PROFILE` but unused by `engine.py` |
| `interpretation.per_line[].line/bit/moving` | `engine.py` | 6 objects | PRESENT | COMPUTED | bits + moving_lines | interpretation | YES for bit/moving | Status strings: `CANONICAL_INPUT` / `CANONICAL_IDENTITY` |

---

## 3. SYMBOLIC / SEMANTIC MAPPING

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| Canonical S07 enum | `canonical_vocabulary.json` | SAT, TA, NHIEU, HY, DUONG, AN | PRESENT | MAPPED (governance enum) | vocabulary file | source_hash in vocabulary | YES as vocabulary | Locked enum |
| `primary_label` | `engine.py` `_s07` | one of CANONICAL | PRESENT | **MAPPED via provisional threshold** | `I+F` only | `semantic_state.status=THRESHOLD_PROFILE_REQUIRED` | **NO as calibrated semantic fact** | Engine **does not evaluate** S07 profile predicates; uses simple `I+F` cut points |
| S07 profile rules | `s07_mapping_profile_v31.json` | 6 predicates on S,D,I,F | PRESENT (file) | MAPPED (declared) | historical doc v2.9.1-NEW2 | profile `status=CALIBRATION_REQUIRED` | **NO until calibrated** | Rules exist but are **not applied** by engine |
| `matched_rules` | `engine.py` | `[]` always | PRESENT (empty) | — | — | mapping_provenance | NO | Confirms profile evaluator not run |
| `semantic_state.status` | `engine.py` | `THRESHOLD_PROFILE_REQUIRED` | PRESENT | MAPPED | — | engine | YES as process status | Not a semantic outcome |
| `mapping_profile` | `engine.py` `_mapping_profile` | id/version/sha256/status | PRESENT | MAPPED | profile file | file hash | YES as profile pointer | |
| Legacy aliases | vocabulary | present | PRESENT | MAPPED | vocabulary | — | LIMITED | Compatibility only |
| Natural-language interpretation | — | — | MISSING | — | — | — | NO | Explicitly out of CORE; no LLM path in runtime |

**CONTRACT GAP (SPEC ↔ CORE):** Spec L4 requires whitelist AST evaluator of profile rules, overlap → `MAPPING_AMBIGUOUS`, zero-match → `MAPPING_UNRESOLVED`. Engine instead applies independent `I+F` thresholds and still emits a `primary_label`. Label is therefore **not** evidence of profile-rule satisfaction.

---

## 4. INTERACTION / FORCE

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| `khi_vector` as force proxy | `engine.py` | S,D,I,F,T from bits | PRESENT | COMPUTED | root_bits | provisional | LIMITED | Not interaction-network force |
| `dynamic_state.force` | `engine.py` | same as khi_vector | PRESENT | COMPUTED | field | — | LIMITED | Naming overlap with true force operators in profiles |
| `interpretation.source_interaction` | `engine.py` | `[]` | PRESENT (empty) | — | — | — | **NO** | Schema allows array of objects; always empty |
| Frontend Source / Interaction fields | `dd3a_per_line_adapter.js` | always `"UNSUPPORTED"` | PRESENT as UI marker | MAPPED (constant) | moving_lines only | adapter | **NO as interaction evidence** | Adapter **rebuilds** per_line; discards engine bit/status |
| Hexagram envelope fields (`dq_g`, `truong`, `the`, …) | `app.py` adapter | stripped | MISSING in CORE path | — | data_1/data_2 | only question/time/number/gps/dong forwarded | NO | Adapter does not pass symbolic hexagram structure into engine |

---

## 5. TEMPORAL

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| Request `time` | input | ISO-8601 | PRESENT | OBSERVED | client | input_hash | YES | |
| `tick` | execution | 0 | PRESENT | COMPUTED | — | — | LIMITED | Single-shot; no tick advancement |
| `velocity` | dynamic_state | null | MISSING value | — | DPKE-1 unused | profile only | NO | |
| `delay` | dynamic_state | null | MISSING value | — | DD-DELAY unused | profile only | NO | |
| `phase` | dynamic_state | `"PROVISIONAL"` | PLACEHOLDER | MAPPED | — | — | NO | Not one of 12 theory phases |
| `expected_time_windows` | interpretation | `[]` | PRESENT (empty) | — | — | — | NO | |
| Frontend Expected Time Window | DD-3A / UI | `"UNSUPPORTED"` | PRESENT as marker | MAPPED | — | — | NO | |
| Multi-tick `observe(context, evidence)` | SPEC only | defined in `DUYEN_DICH_v3.1.md` §5 | MISSING in engine | — | — | spec text | NO | No history buffer in runtime |

---

## 6. SPATIAL

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| `gps.lat/lng` | input validation | validated range | PRESENT as input | OBSERVED | client | input_hash | YES as input | **Dropped from response** |
| `address` | input | optional string | PRESENT as input | OBSERVED | client | input_hash | LIMITED | Not in response |
| Topology 12-node | profile + spec | profile JSON | MISSING in runtime | — | TOPOLOGY-MCHI-2.9.3 unused by engine | profile | NO from live run | |
| `spacetime` | dynamic_state | null | MISSING value | — | — | — | NO | |
| `NxNxspace` | — | — | **MISSING** | — | — | — | NO | Zero matches in repository |

---

## 7. INFERENCE / PREDICTION

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| Prediction model / forecast | — | — | **MISSING** | — | — | — | NO | No prediction module, no horizon, no outcome model |
| `derived_event` (frontend) | DD-3A | `"UNSUPPORTED"` | MARKER ONLY | MAPPED | — | — | NO | |
| `trigger` (frontend) | DD-3A | `"UNSUPPORTED"` | MARKER ONLY | MAPPED | — | — | NO | |
| Cross-hào relations | `interpretation.cross_line` | `[]` | EMPTY | — | — | — | NO | |
| BEC observation formula | profile `BEC-OBS-1` | formula in JSON | PROFILE ONLY | — | not executed | `CALIBRATION_REQUIRED`, `write_back: false` | NO from live run | |
| S07 label as prediction | engine | emitted | PRESENT | MAPPED (provisional) | I+F | flagged calibration | **NO as prediction of external event** | Label is field-threshold mapping, not event prediction |

---

## 8. OBSERVATION

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| Client-submitted payload fields | API | question, number, time, gps, … | PRESENT | OBSERVED | client | input_hash | YES | These are *system inputs*, not post-hoc observations of predicted events |
| `output_b.observation_status` | `engine.py` | `"PROVISIONAL"` | PRESENT | MAPPED (const) | — | — | NO as real observation | Placeholder status string |
| Spec `observe(context, evidence)` API | `DUYEN_DICH_v3.1.md` | defined | MISSING implementation | — | — | spec | NO | |
| Observable event log / evidence append | — | — | **MISSING** | — | — | — | NO | No store for external observations |
| Image upload | input | metadata accepted | PRESENT (input) | OBSERVED | client | input_hash | LIMITED | Not interpreted; no vision pipeline |

---

## 9. GROUND TRUTH

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| `interpretation.ground_truth` | `engine.py` | `null` | SLOT PRESENT / VALUE MISSING | — | — | — | **NO** | Schema allows object|null; always null |
| Frontend Ground Truth fields | DD-3A / UI | `"UNSUPPORTED"` | MARKER ONLY | MAPPED | — | — | NO | Explicit non-fabrication |
| Comparison / match status | UI | UNSUPPORTED / NOT EVALUATED | UI-only | — | — | — | NO | No backend comparison |
| Labeled outcome dataset | — | — | **MISSING** | — | — | — | NO | No fixtures of (input → observed outcome) |
| Human audit records of outcomes | review JSON under `specs/v3.1/governance/review/` | Gemini review of **spec**, not case outcomes | PRESENT as process docs | OBSERVED (process) | — | review files | YES for *process* audit only | Not case-level ground truth |

---

## 10. PROVENANCE / AUDIT

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| `provenance.source_refs` | engine | list of profile/schema paths | PRESENT | MAPPED | — | — | YES | |
| `provenance.source_hashes` | engine | file sha256 of 4 artifacts | PRESENT | COMPUTED | files on disk | — | YES | |
| `provenance.engine_commit` | engine | env `GIT_COMMIT` / `VERCEL_GIT_COMMIT_SHA` or `working-tree` | PRESENT | OBSERVED (env) | deploy env | — | YES | |
| `content_fingerprint` | engine | sha256 of input+field+identity+profile | PRESENT | COMPUTED | run | — | YES | |
| `review_records` | engine | paths to gemini/decision logs | PRESENT | MAPPED | — | — | YES for process | |
| `execution_id` / `snapshot_id` | engine | derived from hashes | PRESENT | COMPUTED | input/identity | — | YES | |
| Gate results G1–G7 | engine | mostly PASSED; G4=`CALIBRATION_REQUIRED` | PRESENT | MAPPED | — | — | YES as process gates | G4 correctly flags calibration gap |
| Forward-only / core_lock flags | execution | `forward_only: true`, `core_lock_mode: LOCKED` | PRESENT | MAPPED | — | — | YES as policy flags | Policy, not empirical proof |
| Runtime trace L1–L6 | raw_measurements | statuses PASSED / PASSED_PROVISIONAL | PRESENT | MAPPED | — | — | LIMITED | Self-declared; not independent audit |

---

## 11. UNCERTAINTY / CONFIDENCE

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| `uncertainty.measurement` | engine | `0.0` | PRESENT | MAPPED (const) | — | — | **NO as calibrated uncertainty** | Hard-coded |
| `uncertainty.model` | engine | `1.0` | PRESENT | MAPPED (const) | — | — | NO | Hard-coded high model uncertainty |
| `uncertainty.semantic` | engine | `1.0` | PRESENT | MAPPED (const) | — | — | NO | Hard-coded |
| `confidence.score` | engine | `0.0` | PRESENT | MAPPED (const) | firewall method | method name | **NO as reliability score** | Always 0; firewall method, not scored performance |
| `confidence.method` | engine | `confidence_firewall_no_f_net_out` | PRESENT | MAPPED | — | — | YES as method id | Documents exclusion policy |
| `f_net_out_excluded` | engine | `true` | PRESENT | MAPPED | scan | — | YES | Contractual firewall |
| `f_net_out_found` | engine | `false` | PRESENT | COMPUTED (scan claim) | scanned_paths | — | LIMITED | Scan is declarative list, not AST proof |
| Calibrated reliability scale | — | — | **MISSING** | — | — | — | NO | No Brier/ECE/scorecard |

---

## 12. OUTPUT / RENDERING

| COMPONENT | SOURCE FILE | CURRENT SHAPE | PRESENT / MISSING | COMPUTED / MAPPED / INFERRED / OBSERVED | DEPENDENCIES | PROVENANCE | CAN BE USED AS EVIDENCE? | NOTES |
|---|---|---|---|---|---|---|---|---|
| Canonical JSON API | `app.py` | POST `/api/v31` | PRESENT | COMPUTED | engine | contract | YES as transport | Deterministic sort_keys serialization |
| `output_a` | engine | identity + dynamic_state + runtime_status | PRESENT | COMPUTED | core path | — | LIMITED | Mirrors CORE/derived |
| `output_b` | engine | semantic_state + observation_status | PRESENT | MAPPED | semantic | — | LIMITED | Provisional semantic |
| UI microscope H1–H6 | `index.html` + DD-3A + form fix | MOVING / NOT MOVING + UNSUPPORTED fields | PRESENT | MAPPED from `moving_lines` | adapter | UI only | YES for moving display | **Adapter overwrites** engine `per_line` (drops bit/status) |
| UI matrix / cross / GT / comparison | `index.html` | UNSUPPORTED tables | PRESENT | MAPPED | — | — | NO as evidence | Non-fabrication UI |
| `layers` internal object | engine | L1–L6 detail | PRESENT in `run_v31` | COMPUTED | — | — | LIMITED | **Stripped** by `canonical_response()` before API |

---

## Special-term findings

| Term | Finding |
|---|---|
| `identity` | Present; CORE FACT bundle |
| `root_code` / `transformed_code` | Present; computed |
| `moving_lines` / H1–H6 | Present; H3 moving when `dong=3` |
| `khi_vector` / force | Present as provisional 5D from bits; not matrix force |
| `persistence` / `accumulation` | Placeholder zeros |
| `phase` / `velocity` / `delay` / `spacetime` | phase placeholder; others null |
| `topology` | Profile exists; not executed |
| `S07` | Enum + profile file present; engine uses alternate threshold; calibration required |
| `source` / `interaction` / `trigger` / `expected_time_window` / `ground_truth` | UI/adapter UNSUPPORTED or null; not produced by CORE |
| `uncertainty` / `confidence` | Present as firewall constants, not empirical scores |
| `provenance` | Strong relative to other layers |
| `NxNxspace` | **Absent** |
| `prediction` | **Absent** |
| `observation` (post-event) | **Absent** (only input observations + placeholder status) |
| `calibration` | Declared required; no calibration dataset or decision artifact activating profiles |

---

## Contract gaps (do not auto-fix)

### GAP-1 — SPEC ↔ CORE (field / runtime operators)

Spec and `runtime_profiles_v31.json` define topology, matrices, DPKE, delay, BEC, multi-tick observe.  
`engine.py` implements a **self-contained provisional** path: bits → simple field → I+F label.  
Profiles are **referenced by ID** in execution metadata but **not loaded for numeric computation**.

### GAP-2 — SPEC / PROFILE ↔ CORE (S07)

Profile predicates (multi-axis, overlap policy) are not evaluated.  
Engine `_s07(I+F)` can disagree with profile rules for the same vector.  
`matched_rules` always `[]` while `primary_label` is still set.

### GAP-3 — CORE ↔ API surface

`canonical_response()` drops `layers` (and thus any residual input echo).  
`gps`, `address`, `image`, `question` are not returned as explicit fields (only via `input_hash`).  
Downstream TRAX3 cannot recover GPS/question without external log of the request.

### GAP-4 — API ↔ FRONTEND (per_line)

Engine `interpretation.per_line`: `{line, bit, moving, status}`.  
DD-3A adapter **rebuilds** from `identity.moving_lines` only → `{id, index, moving, source…=UNSUPPORTED}`.  
Bit and engine status are discarded on the client path.  
Moving display can still match when `moving_lines` is correct, but shapes diverge.

### GAP-5 — Schema optionality

`interpretation` is **not** in schema `required[]`.  
Empty arrays / null ground_truth are schema-valid; they do not encode “unsupported” vs “not applicable” vs “failed lookup”.

### GAP-6 — MAIN ↔ PRODUCTION drift (historical note)

During earlier UI work, production briefly served a placeholder `index.html` while `main` moved; surveyed HEAD `7c3557b` restores full UI + adapter.  
Always verify production commit SHA against `provenance.engine_commit` / Vercel meta before treating UI behavior as contract evidence.

### GAP-7 — Source inventory vs this repo

`SOURCE_INVENTORY.md` still describes `duyen-dich-engine` as empty (stale relative to current tree).  
Historical lineage claims (`v2.5`, `v2.8`, `v2.9.2`) are documented as **not found** as original files in GitHub sources; profiles hold transcribed claims.

---

## A. Nguyên liệu hiện có để xây prediction model?

**Có (yếu / nền):**

1. Deterministic identity features: `root_bits`, `root_code`, `transformed_code`, `moving_lines`.
2. Provisional numeric features: `khi_vector` `{S,D,I,F,T}` (bit-derived only).
3. Optional input context features: `time`, `gps`, `question` (in request; not all in response).
4. Strong **process** provenance: hashes, execution/snapshot IDs, profile IDs, gate flags.
5. Explicit **non-claims**: empty interaction, null GT, confidence score fixed at 0, G4=`CALIBRATION_REQUIRED`.

**Không có:**

- Labeled outcomes (what happened after a run).
- Multi-tick state trajectories.
- Executed topology / matrix / DPKE / delay features.
- Observation intake API for post-hoc events.
- Any prediction head or horizon definition.

---

## B. Những lớp suy diễn nào hiện chưa tồn tại?

1. **Interaction inference** (source × interaction matrix with evidence) — empty / UNSUPPORTED.  
2. **Cross-line inference** — empty.  
3. **Temporal inference** (velocity, delay, expected time window, phase operators) — null / placeholder.  
4. **Event prediction** (derived_event, trigger, forecast) — missing.  
5. **Calibrated S07 semantic inference** under approved profile evaluator — missing (provisional substitute only).  
6. **Observation-to-state update** (`observe()`) — missing.  
7. **Ground-truth matching / residual** — missing.  
8. **Reliability / calibration scores** tied to outcomes — missing.

---

## C. Ground Truth hiện có đến đâu?

- Schema slot: `interpretation.ground_truth: null`.  
- UI: explicitly `UNSUPPORTED`.  
- No case dataset, no observation store, no comparison engine.  
- Review artifacts under `specs/v3.1/governance/review/` are **spec governance** reviews, not empirical case labels.  

**Ground Truth = not started at the data layer.** Only structural placeholders and process provenance exist.

---

## D. Muốn xây RELIABILITY SCALE thì cần thêm dữ liệu gì?

Minimum data not present today:

1. **Case log**: stable `execution_id` / `input_hash` + full normalized input + frozen identity + emitted features.  
2. **Observation records**: timestamped external events linked to a case (who observed, source, raw payload).  
3. **Ground-truth labels**: agreed schema for outcome fields (binary / categorical / time-to-event) with labeler provenance.  
4. **Decision policy snapshot**: which profile IDs and code commit produced the score being judged.  
5. **Holdout / time-split protocol**: so scores are not fit on the same runs used to invent thresholds.  
6. Optionally: multi-tick trajectories if reliability is defined on dynamics rather than single-shot labels.

Without (1)–(3), a “reliability scale” would only restate hard-coded uncertainty constants.

---

## E. Có thể bắt đầu calibration từ dữ liệu hiện tại không?

**Không** — not in the sense of calibrating predictive or S07 thresholds against external truth.

What *can* be done with current artifacts (still research, not activation):

- Reproduce deterministic identity and provisional field vectors for any stored input.  
- Diff engine `_s07(I+F)` labels against profile-rule outcomes **on synthetic vectors** (internal consistency study only).  
- Inventory profile formulas (DPKE, delay, BEC) as **candidates** pending source validation.  

That is **reproducibility / consistency research**, not calibration against ground truth.

---

## F. Nếu chưa, thiếu chính xác cái gì?

| Missing item | Why it blocks calibration |
|---|---|
| Outcome-labeled cases | No target variable |
| Observation intake + storage | No way to attach post-run evidence to `execution_id` |
| Binding of response fields for input context (or external request log) | Cannot recover GPS/question later from response alone |
| Executed (or version-pinned alternative) feature pipeline aligned with profiles | Profile IDs claim operators that never ran |
| Approved S07 evaluator path | Profile rules unused; label not attributable to profile |
| Explicit definition of the event being predicted | “Reliability” has no referent |
| Human/process protocol for GT | Placeholder UI cannot become GT without policy |

---

## Closing statement

Duyên Dịch v3.1 in this repository is a **deterministic identity + provisional field + governance firewall** system with a rich **spec and profile registry**.  

For Trục 3, the only materials that currently qualify as **evidence** (with caveats) are:

- CORE identity computations,  
- input-side observations (as request data),  
- provenance/gate process artifacts,  
- explicit empty/null/UNSUPPORTED markers that prevent fabrication.

Everything in the chain **Inference → Observation (post-event) → Ground Truth → Calibration → Reliability** is either **absent**, **placeholder**, or **declared `CALIBRATION_REQUIRED` without activating data**.

This document maps that state; it does not invent the missing layers.

---

*End of research_only/TRAX3_CONTRACT_EVIDENCE_MATRIX_v0.1.md*  
*No code modified. No commit. No deploy.*
