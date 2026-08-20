# Duyên Dịch v3.1

Đây là repository canonical integration cho đặc tả **Duyên Dịch v3.1**. Bản hợp nhất được tổ chức theo lớp kiến trúc thay vì gộp trực tiếp các version cũ. Mục tiêu là giữ logic Duyên Dịch nhất quán, bảo vệ compute–interpretation firewall, thống nhất S07 vocabulary và cung cấp data contract có provenance.

## Thành phần

| Thành phần | Đường dẫn | Trạng thái |
|---|---|---|
| Đặc tả hợp nhất | `specs/v3.1/DUYEN_DICH_v3.1.md` | Canonical integration |
| Từ vựng S07 | `specs/v3.1/canonical_vocabulary.json` | CORE |
| S07 profile | `specs/v3.1/s07_mapping_profile_v31.json` | RESEARCH / `MAPPING_UNRESOLVED` |
| Legacy decoder | `specs/v3.1/compatibility/legacy_decoder.json` | COMPATIBILITY |
| JSON Schema | `specs/v3.1/schemas/canonical_response.schema.json` | CORE contract |
| Decision log | `specs/v3.1/artifacts/decision_log.md` | Provenance |
| Gemini Vòng 1/2 | `gemini_round1.json`, `gemini_round2.json` | Review artifacts |
| Inventory nguồn | `SOURCE_INVENTORY.md` | Source traceability |

## Canonical boundary

Kernel v3.1 chỉ chấp nhận sáu mã `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN`. Nhãn lịch sử chỉ được đọc ở compatibility decoder và không được tự động ép sang mã canonical. Runtime chỉ phát số liệu thô; mapping S07 chỉ chạy khi có profile hợp lệ. Nếu thiếu profile, kết quả là `MAPPING_UNRESOLVED`.

Các công thức SDE/Bellman, SL-DIF/BEC, matrix/delay v2.9.2 và threshold mapping chưa có trong các repository đã truy xuất được giữ ở `RESEARCH` hoặc `PLACEHOLDER`, không được trình bày như CORE.

## Kiểm định

Chạy kiểm định đặc tả bằng:

```bash
python3 -m unittest discover -s specs/v3.1/tests -p 'test_*.py' -v
```

Bộ kiểm định hiện xác nhận enum canonical, loại legacy khỏi Kernel, behavior unresolved của mapping, schema confidence firewall, compute–interpretation firewall và decision log.
