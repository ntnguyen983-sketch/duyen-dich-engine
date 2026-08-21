# Evidence Index — Interpretation Library v0.2 (supplement)

Survey of repository `ntnguyen983-sketch/duyen-dich-engine` (HEAD at survey time: `7c3557b` lineage / working tree with library only).  
No CORE changes. No fabricated fills.

## 1. Tên 64 quẻ

| Status | **MISSING_SOURCE** (canonical) |
|---|---|
| FOUND (non-canonical) | Sample strings only in UI fixture: `ui_test/index.html` default hexagram payload (`que_goc_s`: "Phong Lôi Ích", `que_bien_s`: "Phong Hỏa Gia Nhân"); mirrored in `ui_test/test_ui.spec.js`. |
| CORE usage | `app.py` `normalize_run_payload` **does not** forward `que_goc_s` / `que_bien_s` into engine. |
| Library action | Keep `hexagram_name: null`, `hexagram_name_status: MISSING_SOURCE` for all 64 ids. Do **not** promote fixture strings to canonical names. |

## 2. Tên 8 quái + Ngũ hành

| Status | **MISSING_SOURCE** (canonical table) |
|---|---|
| FOUND (non-canonical) | Fixture fragments: `dq_gs`: "Đoài (Trạch)", `dq_bs`: "Chấn (Lôi)"; `truong`: `{Moc,Hoa,Tho,Kim,Thuy}` counts in UI sample only. |
| Structural DERIVED | trigram bit triples in `structural_dataset.json` from binary model. Bits only — no traditional names. |
| Library action | No traditional bagua names or five-element map added. |

## 3. Chính / ứng vị — MISSING_SOURCE

## 4. Âm / Dương semantic — MISSING_SOURCE (CORE bit 0|1 only; S07 DUONG = DƯỠNG)

## 5. Chú giải hào cổ điển — MISSING_SOURCE

## 6. NxNxspace — MISSING_SOURCE

## 7. Golden case outcomes — MISSING_SOURCE (ground_truth always null)

## 8. S07 activation — CALIBRATION_REQUIRED (VERIFIED)

## 9. BEC / DPKE / delay — profile FOUND; live values null (VERIFIED)

## 10. Context IDs — PROVISIONAL

## 11. Thể / Dụng — BANNED

See also `SOURCE_REGISTRY.md` and `SOURCE_CONFLICTS.md`.
