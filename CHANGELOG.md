# Changelog

## [3.1.0] — Canonical layer integration

### Added

Đặc tả hợp nhất sáu lớp kiến trúc, compute–interpretation firewall giữa L3 và L4, canonical S07 vocabulary, canonical response schema, năm validation gates, legacy compatibility decoder và registry cho S07 mapping profile.

### Retained as CORE

Sáu mã `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN`; determinism contract `S_(t+1)=K(S_t,I_t)`; provenance; uncertainty/confidence separation; và behavior `MAPPING_UNRESOLVED` khi profile thiếu hoặc không hợp lệ.

### Downgraded or rejected

Threshold mapping cụ thể trong nguồn hiện hữu, công thức BEC suy đoán, epsilon cụ thể chưa đăng ký, matrix/delay runtime chưa có spec gốc và legacy labels trong canonical vocabulary không được đưa vào CORE.

### Traceability

Bản ghi Gemini Vòng 1 và Vòng 2, inventory repository, decision log và test vectors được lưu cùng repository. Những phụ lục gốc chưa tìm thấy được ghi rõ là unresolved, không bị thay thế bằng suy đoán.
