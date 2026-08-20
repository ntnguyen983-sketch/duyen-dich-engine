# Duyên Dịch v3.1 Runtime

This package is the runnable integration layer for the v3.1 specification.

Status: **RUNNABLE / PROVISIONAL**.

It executes L1→L6 end-to-end with deterministic, self-contained operators. The
field and S07 mapping are explicitly provisional because the source appendices
and approved calibration/profile are not present in the v3.1 source tree.

Replacement rule: when an authoritative formula/profile arrives, replace only
the provisional operator/profile and keep the contract, provenance, gates and
regression tests intact.

Run:

```bash
python -m unittest discover -s runtime/v31 -p 'test_*.py'
```
