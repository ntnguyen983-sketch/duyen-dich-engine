# Duyên Dịch — ORIGIN / Unified Lineage Workspace

Trạng thái: ARCHITECTURAL ANCHOR — không phải production implementation.

Mục đích: làm kho gốc để chỉnh hợp toàn bộ tư liệu Duyên Dịch từ các lớp sơ khai đến hiện tại, trước khi tách các implementation.

## Nguyên tắc hợp nhất

- Không coi bất kỳ implementation hiện tại nào là toàn bộ lịch sử.
- Phân biệt nguồn gốc, đặc tả, diễn giải, thử nghiệm, runtime và calibration.
- Bộ ba biểu đạt cuối cùng: **Định danh | Định lượng | Định tính**.
- Không áp đặt bản thể cố định; mọi mô hình là quy chiếu theo điều kiện và dữ liệu quan sát.
- B(V_k) thuộc không gian; không gán điểm nghẽn không gian trực tiếp thành bản chất của N_i.
- event_count, cycle_count và K_rep là ba đại lượng khác nhau.
- Công thức chưa có nguồn canonical hoặc chưa được chứng minh phải được đánh dấu chưa xác lập, không tự chế.
- Ground Truth/L4 có quyền cập nhật phần hiệu chỉnh; không viết ngược làm biến đổi lịch sử nguồn.

## Cấu trúc dự kiến

- `origin/01_early_doctrine/` — tư liệu Đạo Duyên Dịch và các bản sơ khai
- `origin/02_conceptual_evolution/` — quá trình hình thành khái niệm
- `origin/03_v30_structural/` — Structural Domain/v3.0
- `origin/04_3a_dynamic/` — Dynamic Execution Layer/3A
- `origin/05_unified_ontology/` — N(n), Entity/Observation/Interaction/Space/Time/State
- `origin/06_canonical_anchor/` — Architectural Anchor và bộ ba biểu đạt
- `origin/07_formulas_and_operators/` — công thức, toán tử, nguồn và trạng thái xác lập
- `origin/08_reference_implementations/` — reference code, chỉ là implementation
- `origin/09_validation_and_ground_truth/` — test vectors, validation, calibration
- `origin/10_runtime_adapters/` — adapters/API/UI, không được nâng thành ontology
- `origin/11_lineage_and_gap_audit/` — ma trận nguồn, gap, quyết định chỉnh lý

## Trạng thái

`CANONICAL` = đã có căn cứ nguồn và được xác định trong kiến trúc.
`DERIVED` = suy ra từ canonical, phải truy nguyên được.
`RESEARCH` = giả thuyết/thử nghiệm.
`IMPLEMENTATION` = cách thực thi, không làm thay đổi kiến trúc.
`UNRESOLVED` = chưa đủ căn cứ; không được lấp bằng suy đoán.

Nhánh này là **origin workspace**. Các engine chạy thực tế sẽ được tách riêng sau khi lineage và gap audit hoàn tất.
