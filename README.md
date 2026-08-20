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

## Web test end-to-end

Ứng dụng Flask tại `app.py` là adapter duy nhất nối HTTP với `runtime.v31`; không có engine thứ hai trong API. Vercel nạp `api/index.py`, route `/` phục vụ `ui_test/index.html`, còn `POST /api/v31` trả strict canonical JSON theo schema v3.1.

Chạy local:

```bash
pip install -r requirements.txt
python3 app.py
```

Mở `http://127.0.0.1:8000/`. Health check là `GET /api/health`; readiness check là `GET /api/v31`.

Kiểm định đầy đủ:

```bash
python3 -m unittest discover -s specs/v3.1/tests -p 'test_*.py' -v
PYTHONPATH=runtime/v31 python3 -m unittest discover -s runtime/v31 -p 'test_*.py' -v
python3 -m unittest -v test_api.py
npm install
npx playwright install chromium
npm run test:e2e
```

Workflow `.github/workflows/v31-full.yml` chạy toàn bộ các bước trên cho mỗi push và pull request. Các file `specs/v3.1/`, `runtime/`, artifacts, schemas, compatibility decoder và baseline cũ được giữ nguyên; các operator chưa có profile nguồn vẫn được ghi rõ `PROVISIONAL`/`RESEARCH`, không được trình bày như CORE.
