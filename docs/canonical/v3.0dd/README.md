# Duyên Dịch v3.0_dd — canonical architecture sources

## Quyết định nguồn

Bộ tài liệu này được lấy từ thư mục Google Drive của dự án và được đưa vào repository để code, AI và reviewer cùng đọc một nguồn có version. Nguồn authority cho lõi là **DD-SPEC-UNIFIED-v3.0_dd**; không trộn công thức hoặc enum của bản cũ vào Kernel.

| Tài liệu | Nguồn Drive | Hash bản đưa vào repo | Phạm vi |
|---|---|---|---|
| `modular-architecture.md` | [`duyen-dich-modular-architecture.md`](https://drive.google.com/file/d/19fwYtUWCz6djk46vibzAR5YN1VZ309bc/view?usp=drivesdk) | `7911e1352fb29172909a41bfdecb716a83e4c13a1e3e2734ba6757f6ed673d42` | Architecture, ontology, Node Space, Vector Khí, MSIE, pipeline, gates và canonical JSON |
| `force-interaction-registry.txt` | Bản export registry/toán tử từ Drive | `e76ee692b50a1a0a9051c0090280dd5a4f9f970aa72643755915035425f979a5` | Registry tham khảo; phải phân loại Core/Research/Legacy trước khi dùng |

`modular-architecture.md` được cập nhật trên Drive vào `2026-08-18T14:15:51.770Z`. Bản PDF master specification cũng được giữ local để đối chiếu nhưng không đưa vào commit này vì bản extract có lỗi mã hóa; khi cần phát hành tài liệu, phải dùng bản gốc hoặc export có encoding chuẩn.

## Tầng áp dụng

Architecture định nghĩa chuỗi `QUAN SÁT → TIẾP NHẬN → CHUẨN HÓA → ÁNH XẠ → TÍNH TOÁN → SUY DIỄN → THỰC CHỨNG`. Engine runtime chịu trách nhiệm các tầng từ input đến canonical calculation. AI chịu trách nhiệm lớp suy diễn/luận giải sau engine, tạo dự báo có điều kiện và action. AI không được ghi ngược dữ liệu vào Kernel và không được thay thế canonical JSON.

Sáu mã S07 serialize chuẩn là `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN`. `DUONG` là mã serialize của DƯỠNG. Các nhãn cũ chỉ được đọc qua compatibility decoder. Mapping Vector Khí 5 chiều sang S07 chỉ được dùng khi có mapping profile hợp lệ; nếu không phải trả `MAPPING_UNRESOLVED` hoặc `CALIBRATION_REQUIRED`, không tự ép nhãn.

## Cách dùng với AI

Prompt AI phải nhận câu hỏi gốc, source input và nguyên bản engine output. AI được phép suy diễn theo phân tầng `Data → Signal → Pattern → Inference → Action`, nhưng mọi nhận định phải có evidence path về JSON engine. Trạng thái `CALIBRATION_REQUIRED` không chặn luận giải; nó hạ trạng thái luận giải thành `provisional` và phải xuất hiện trong limitations.

Không đưa khóa API vào tài liệu này. Khóa Gemini chỉ được cấu hình ở server-side environment variables. Không lưu raw prompt hoặc raw provider response trong repository.

## Provenance

- Drive file ID của architecture: `19fwYtUWCz6djk46vibzAR5YN1VZ309bc`.
- Repository baseline trước rebuild: branch `main`, commit `854ec71`.
- Bản thử nghiệm cũ được giữ ở branch `archive/test/gemini-review-smoke-20260821-20260822` và tag `archive-20260822-gemini-ai-layer`.
- Nhánh rebuild hiện tại được tạo độc lập từ `main` để tránh xóa lịch sử và cho phép rollback.
