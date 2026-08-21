# External Source Registry — Interpretation Library v0.2

All datasets here are **outside CORE**. Classification ≠ CORE_CANONICAL.

| dataset_id | file | classification | records | primary license | retrieved_at |
|---|---|---|---:|---|---|
| EXT-HEX-64-WIKIBOOKS-2026 | hexagrams_64_external.json | CANONICAL_EXTERNAL | 64 | CC BY-SA 3.0 / 4.0 | 2026-08-21T10:00:00+07:00 |
| EXT-TRIGRAM-8 | trigrams_8_external.json | CANONICAL_EXTERNAL | 8 | CC BY-SA 4.0 (+ secondary REF) | 2026-08-21T10:00:00+07:00 |
| EXT-POLARITY-YIN-YANG | polarity_external_profile.json | REFERENCE | 1 profile | CC BY-SA | 2026-08-21T10:00:00+07:00 |
| EXT-POSITION-ZHENG-WEI-SECONDARY | position_profiles_external.json | REFERENCE | 1 profile | unknown secondary | 2026-08-21T10:00:00+07:00 |
| EXT-LINE-TEXTS-POINTERS | line_texts_external_meta.json | REFERENCE / MISSING corpus | 0 embedded | mixed | 2026-08-21T10:00:00+07:00 |
| EXT-NXNXSPACE | nxnxspace_external.json | MISSING_SOURCE | 0 | — | 2026-08-21T10:00:00+07:00 |

## Rules of use

1. Operations Decoder may **read** these files for language layer enrichment.
2. Deterministic Kernel / `run_v31` must **not** import them.
3. `mapping_status` on each record must stay visible in any output that cites names.
4. Vietnamese hexagram names: still MISSING_SOURCE.
5. Thể/Dụng: excluded from pipeline even if found in external traditions (`excluded_traditions`).

## excluded_traditions

| term | policy |
|---|---|
| Thể / Dụng | BANNED in library inference; may only appear in source_metadata notes as excluded |
