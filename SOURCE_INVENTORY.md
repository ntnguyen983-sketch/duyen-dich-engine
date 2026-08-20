# Duyên Dịch v3.1 — Source Inventory

## Phạm vi

Inventory này ghi nhận các repository được chọn trong phiên và trạng thái bằng chứng có thể truy xuất tại thời điểm hợp nhất. Đây là hồ sơ nguồn, không phải quyết định canonical cuối cùng.

## Repository

| Repository | HEAD | Trạng thái nguồn | Vai trò dự kiến |
|---|---:|---|---|
| `ntnguyen983-sketch/-_engine` | empty | Không có commit/file | Chưa có bằng chứng thực thi |
| `ntnguyen983-sketch/dd_engine` | `574a74b` | Chỉ có README tối giản | Placeholder/legacy source |
| `ntnguyen983-sketch/dd_engine1` | `5291035` | Có engine Python, SIE, Vectơ Khí 5D, semantic thresholds, TickEngine, Gemini adapter, UI và tests | Nguồn runtime/UI hiện hữu |
| `ntnguyen983-sketch/duyen-dich-engine` | empty | Không có commit/file | Chưa có bằng chứng thực thi |
| `ntnguyen983-sketch/ops-distribution-kit` | `19e8640` | Package reliability primitives, không chứa logic Duyên Dịch | Hạ tầng phụ trợ, không phải canonical DD |

## Bằng chứng tìm được trong `dd_engine1`

`kernel.py` định nghĩa Snapshot và TickEngine theo hướng stateless, deterministic và replayable. `pipeline.py` xây dựng quẻ biến, interaction network, Vectơ Khí 5D, semantic result, macro projection, delta field, force function và confidence. `sie.py` dùng các trục `S`, `D`, `I`, `F`, `T`. `semantic_thresholds.json` đang ánh xạ Vectơ Khí sang các nhãn lịch sử `TỤ`, `HỢP`, `TÁN`, `LY`, `HIỆN`, `ẨN`; điều này xung đột với bộ S07 canonical hiện hành và phải được hạ xuống Compatibility/Research hoặc thay bằng profile canonical đã được phê duyệt.

`semantic.py` hiện dùng `eval` trên điều kiện JSON và có cơ chế SIE override. Cơ chế này cần được thay bằng evaluator khai báo an toàn, có version/hash/profile/test vectors, đồng thời không được để semantic override thay đổi số liệu Kernel. `pipeline.py` hiện trả `confidence` tách khỏi Vectơ Khí, đây là hướng đúng, nhưng cần chứng minh không suy ra trực tiếp từ `f_net_out` trong v3.1 và phải bổ sung provenance, uncertainty, gate result.

`gemini_service.py` đã có adapter REST trực tiếp tới Gemini. Trong quy trình v3.1, Gemini chỉ là reviewer/proposer; không phải canonical authority. Prompt và output phải được lưu kèm model, thời điểm, input hash và quyết định Manus.

## Kết quả tìm kiếm lịch sử

Không tìm thấy file hoặc commit có tên/chuỗi `v2.5`, `v2.8`, `v2.9.2`, `SL-DIF`, `Bellman` hoặc `SDE` trong các repository đã chọn. Hai repository `-_engine` và `duyen-dich-engine` hiện rỗng; `dd_engine` chỉ có README. Vì vậy sáu phụ lục được mô tả trong yêu cầu chưa xuất hiện nguyên văn trong workspace GitHub này.

## Quyết định về bằng chứng

Các phần lý thuyết v2.5, cơ chế trường v2.8 và runtime v2.9.2 chỉ được đưa vào v3.1 dưới dạng `source_claim`/`PLACEHOLDER` cho đến khi có tài liệu gốc, công thức và test vectors. Không được Gemini tự phát minh chúng thành `CORE`. Phần có thể khóa ngay là khung phân tầng, compute–interpretation firewall, provenance, validation gates và sáu mã Khí canonical theo governance.

## Hash hồ sơ

Hash của từng repository và các artifact inventory được tạo bằng Git tại bước đóng gói cuối. Mọi bổ sung từ nguồn ngoài phải thêm vào bảng provenance, không sửa xóa lịch sử nguồn.
