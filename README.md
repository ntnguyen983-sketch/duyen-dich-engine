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
| Runtime v3.1 | `runtime/v31/` | RUNNABLE / PROVISIONAL |
| Runtime CI | `.github/workflows/v31-runtime.yml` | AUTOMATED TEST |

## Canonical boundary

Kernel v3.1 chỉ chấp nhận sáu mã `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN`. Nhãn lịch sử chỉ được đọc ở compatibility decoder và không được tự động ép sang mã canonical.

Runtime v3.1 chạy L1→L6 end-to-end. Các toán tử field và S07 mapping hiện được triển khai ở trạng thái **PROVISIONAL** để cây engine có đường chạy hoàn chỉnh; provenance và gate luôn ghi rõ trạng thái này. Khi có phụ lục/công thức/profile nguồn, chỉ thay toán tử tương ứng, không phá contract hoặc regression tests.

Các công thức SDE/Bellman, SL-DIF/BEC, matrix/delay v2.9.2 và calibration/threshold mapping chưa có nguồn gốc đủ trong repository vẫn không được trình bày như CORE.

## Kiểm định

Kiểm định đặc tả:

```bash
python3 -m unittest discover -s specs/v3.1/tests -p 'test_*.py' -v
```

Kiểm định runtime:

```bash
python3 -m unittest discover -s runtime/v31 -p 'test_*.py' -v
```

GitHub Actions tự chạy runtime regression trên push và pull request.
