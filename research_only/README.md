# research_only

## TRAX3_CONTRACT_EVIDENCE_MATRIX_v0.1.md

Full matrix (~28KB) lives in local commit `40d2cbf0482a4d9d7b03b9cf7d08e7ce4740dfca`.

MCP Contents API sync of the full markdown exceeded practical payload limits in this environment.

To publish from a machine with git credentials:

```bash
git checkout research/interpretation-library-v0.2
git show 40d2cbf:research_only/TRAX3_CONTRACT_EVIDENCE_MATRIX_v0.1.md > research_only/TRAX3_CONTRACT_EVIDENCE_MATRIX_v0.1.md
git add research_only/TRAX3_CONTRACT_EVIDENCE_MATRIX_v0.1.md
git commit -m "research: add TRAX3 evidence matrix"
git push origin research/interpretation-library-v0.2
```

Same applies to full verbose `structural_dataset.json` (384 line records).
