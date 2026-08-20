# Changelog

## [3.1.0-full-rewrite] — 2026-08-20

### Added

Đặc tả hợp nhất sáu lớp đã được viết lại đầy đủ từ corpus Google Docs v2.5.3, v2.5.6, v2.8.6, BEC Unified v2.8.7, v2.9 overview, v2.9.1 NEW2, Py v2.9.3 và canonical v3.0.0. Bản release bao gồm công thức, pseudocode S00–S11, Frozen Core, forward-only pipeline, matrix/runtime profiles, DWL, Vector Khí, L2-RGS, DPKE, delay, BEC observation, S07 predicates, gates, errors, provenance, JSON Schema và test vectors.

### Retained as CORE

Sáu mã `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN`; Frozen Core; compute–interpretation firewall; forward-only direction; deterministic structural/runtime contract; matrix profiles khi được pin bằng hash; schema, provenance, gate architecture, error behavior và confidence firewall.

### Implemented as profiled but not yet active CORE

S07 `S07-HIST-2.9.1-NEW2` có sáu predicate, miền giá trị, chín boundary vectors, overlap policy, `rule_config_sha256` và behavior `MAPPING_UNRESOLVED`/`MAPPING_AMBIGUOUS`; trạng thái vẫn là `CALIBRATION_REQUIRED`. RGS normalization, BEC lambda/gamma và threshold profile cũng giữ `CALIBRATION_REQUIRED`.

### Research or compatibility

Chu kỳ đồng pha `ΦSystem=60` ticks chỉ phát cờ `SYNC_RESONANCE` và không tự tạo action; H1 Drain/Reserve, causal claims và phase-shift interpretation là `RESEARCH`. Legacy labels và delay Rev.A là `COMPATIBILITY`.

### Gemini review changes

Sau Gemini Vòng 2, đã thêm S07 boundary vectors và profile hash, guard `persistence_denominator_missing=QUARANTINE`, confidence tree audit (`f_net_out_found=false`), TV-017 overlap, TV-018 denominator missing và manual write-back audit requirement.

### Traceability

Bản ghi Gemini Vòng 1/2, source matrix, source findings, decision log, release handoff và test logs được lưu cùng workspace/repository. Nội dung thiếu approval không được nâng thành CORE bằng suy đoán.

## [3.1.0] — Canonical layer integration

Bản khung ban đầu của đặc tả hợp nhất sáu lớp, compute–interpretation firewall, canonical S07 vocabulary, canonical response schema, legacy compatibility decoder và registry mapping. Bản này đã được thay thế bởi `3.1.0-full-rewrite`.
