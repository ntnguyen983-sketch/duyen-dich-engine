# NxNxspace — Research Branch

**Namespace:** `research_only.nxnxspace`
**Status:** `research_only`
**Scope:** Phase 1–2 prototype, chỉ đọc snapshot/mock data.

NxNxspace là mô-đun nghiên cứu độc lập để tính **ma trận cosine similarity NxN** từ các vector thực thể trong một snapshot. Mô-đun này không phải thành phần của CORE v3.1, không phải canonical response, không phải DD-3A adapter, không có API production và không tạo projection/forecasting, UI, Ground Truth integration hoặc feedback loop.

> **Nguyên tắc cô lập:** Mọi file của NxNxspace nằm dưới `research_only/nxnxspace/`; module không import, gọi, ghi hoặc đăng ký vào `specs/`, `runtime/`, API, canonical store hay adapter hiện hành.

## Cấu trúc

| Thành phần | Đường dẫn | Vai trò |
|---|---|---|
| Runtime thuần deterministic | `research_only/nxnxspace/__init__.py` | Validate snapshot, tính cosine matrix và tạo output research-only |
| Input schema | `research_only/nxnxspace/schema/input_snapshot.schema.json` | Hợp đồng snapshot tối thiểu |
| Output schema | `research_only/nxnxspace/schema/output.schema.json` | Hợp đồng output prototype, tách khỏi canonical schema |
| Mock/example | `research_only/nxnxspace/examples/sample_snapshot.json` | Dữ liệu đọc thử, không phải production fixture |
| Test | `research_only/nxnxspace/tests/test_nxnxspace.py` | Test bắt buộc của Phase 2 |
| Đặc tả ngắn | `research_only/nxnxspace/SPEC.md` | Quy tắc tính và failure behavior |

## Chạy prototype

Từ root repository:

```bash
PYTHONPATH=research_only python3 -m unittest discover \
  -s research_only/nxnxspace/tests -p 'test_*.py' -v
```

Prototype chỉ sử dụng Python standard library. Không có HTTP route, background process, API call, AI model call hoặc file write-back. Hàm `compute(snapshot)` là hàm tính chính; `safe_compute(snapshot)` chuyển lỗi validation thành một error envelope có `status="research_only"` để lỗi nghiên cứu không lan sang bất kỳ pipeline nào khác.

## Determinism

`deterministic_input_hash` được tạo từ canonical JSON của `tick_id` và danh sách entity theo đúng thứ tự snapshot, sử dụng UTF-8, `sort_keys=True`, separators ổn định và SHA-256. `timestamp` là metadata quan sát; nếu snapshot không cung cấp timestamp, runtime tạo timestamp UTC hiện tại nhưng không đưa timestamp sinh tự động vào matrix, `space_state` hoặc hash. Vì vậy cùng input cho cùng **matrix, space_state và hash**.

Vector không hợp lệ bị từ chối bằng lỗi research-local. Vector 0 được giữ lại trong output và mọi cosine liên quan được quy ước là `0.0`, tránh phép chia cho 0. Entity ID trùng nhau bị từ chối để không tạo không gian định danh mơ hồ; đây là validation của prototype, không phải thay đổi canonical contract.

## Non-goals của Phase 1–2

Prototype chưa có production API, realtime snapshot, projection forecasting, Ground Truth integration, UI, canonical integration hoặc feedback loop. Không deploy production và không merge branch này vào `main`.
