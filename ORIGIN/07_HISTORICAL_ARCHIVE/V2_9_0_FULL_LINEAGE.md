# DUYÊN DỊCH v2.9.0 — FULL LINEAGE CAPTURE

Source: `DUYEN_DICH_v2.9.0.pdf` (Library source captured 2026-08-21).

## Reconciliation generation
v2.9.0 explicitly addresses conflicts inherited from earlier versions and adds Matrix Consistency Gate G6. A matrix constant is not allowed to be frozen/canonical when two conflicting values exist for the same cell without reconciliation and confidence labeling.

## S07 canonicalization
Canonical six-state set in v2.9.0: SÁT, NHIỄU, TÀ, ẨN, DƯỠNG, HỶ. The earlier "Ân" label is renamed to "Ẩn". Threshold logic is inherited from the earlier six-state decoder. When S07 conflicts with the SIE graph, SIE retains higher priority.

## Matrix audit
v2.9.0 records unresolved dependencies instead of inventing numbers:
- M_SIE numeric matrix incomplete; retained as function/profile dependency.
- D_NgũHành numeric matrix incomplete.
- BEC repetition/rhythm/variable metrics: architecture defined, calibration metric still incomplete.

## Change classes
Examples include clarifying W_12×12 / Override Cascade and Node Space, canonicalizing S07 labels, and reconciling matrix constants. G6 is a validation gate specifically designed to prevent recurrence of unresolved matrix conflicts.

## Lineage role
v2.9.0 is retained as an important audit/reconciliation checkpoint between the 2.8.7 unified runtime and later merged architecture. It demonstrates the rule: unresolved mathematics must remain unresolved rather than be silently invented.
