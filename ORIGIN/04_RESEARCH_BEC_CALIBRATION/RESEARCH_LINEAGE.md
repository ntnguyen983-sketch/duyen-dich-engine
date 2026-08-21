# RESEARCH / BEC / CALIBRATION — LINEAGE

## 1. V2.8.7+ research boundary
Rev.A establishes Frozen Core v2.8.6 versus Research Layer v2.8.7+. Research parameters/hypotheses require explicit labeling and calibration status. Deterministic means same canonical input + same research profile + same runtime policy produces the same output. Forward-only means new evidence does not rewrite a previously issued core state.

## 2. Rev.B unified policy
Rev.B states:
- one canonical core state per case;
- one initialization snapshot;
- one deterministic computation path;
- forward-only evidence flow;
- continuous context at subsequent ticks;
- Research/BEC cannot mutate Core;
- external Chu Dich/Luc Hao knowledge belongs to an adapter/knowledge layer and cannot mutate the kernel.

## 3. BEC lineage
The v2.9.2 implementation contains BEC density and BEC observation as separate mechanisms. The implementation records force, persistence, accumulation, recurrence/rhythm, thresholds, conditional projection and transition status while keeping `write_back=False` for the observation layer.

These are implementation lineage, not automatic authority for v3.4. If a formula is not part of the current canonical contract, it remains research/legacy until explicitly validated.

## 4. Calibration
Ground Truth is evidence for subsequent calibration. Prediction error is calibration data; it must not retrospectively alter a previously published Core State.

## 5. Worker rule
A new implementation must preserve provenance for every research parameter:
- source;
- version/status;
- formula;
- calibration state;
- test vector;
- whether it can mutate core state.

## Provenance
`VERSION 2.8.7+ REV.A.pdf`, `DUYEN_DICH_UNIFIED_MASTER_SPEC_2.8.7_REV.B.pdf/.docx`, `DUYEN_DICH_MASTER_v2.9.2_MERGED_FREEZE.docx`, `duyen_dich_engine_v293_full.py`.
