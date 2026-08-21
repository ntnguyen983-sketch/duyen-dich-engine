# 03 — DYNAMIC DOMAIN / 3A

## Mục đích

3A không đứng cạnh v3.0 như một hệ ontology khác. 3A là **Dynamic Execution Layer** vận hành trên cùng khung quan sát N(n).

## Bộ ba hiện tại

**Định danh | Định lượng | Định tính**

### Định danh
Ký hiệu quy chiếu: `N_i`, `V_k`, `I_m`, `t_k`... Không gán bản ngã hay bản chất cố định.

### Định lượng
Dữ liệu có thể đo/ghi: vị trí, thời gian, magnitude, F_in, F_out, B(V_k), Δt, σ_rhythm, event_count, cycle_count, K_rep.

### Định tính
Mẫu hình quan sát được từ định lượng và evidence: hội tụ, phân kỳ, lặp nhịp, lệch nhịp, chuyển trạng thái. Không mặc định tốt/xấu.

## Các ranh giới phải giữ

1. `B(V_k)` thuộc về **không gian V_k**, không phải bản thân N_i.
2. `event_count` là số sự kiện; `cycle_count` là cấu trúc vòng trong topology; `K_rep` là số lần motif/quan hệ lặp theo thời gian.
3. `sigma_rhythm` phải lấy từ chuỗi sự kiện/quan hệ, không gom mốc thời gian phẳng.
4. ISO 8601 phải được xử lý bằng timezone-aware datetime.
5. Không tự chế `f_BEC`, `r_t`, S07 hoặc G_breaker khi thiếu định nghĩa/profile/L4 hợp lệ.
6. Ground Truth và L4 Calibration là vòng phản hồi mở; không sửa dữ liệu lịch sử đã khóa.

## Anchor v3.4

DD-3A-v3.4 là **architectural anchor**, không phải lời tuyên bố rằng thế giới đã được đóng khung vĩnh viễn. Kiến trúc có thể làm điểm neo; mô hình hóa thực tại luôn có thể được quan sát lại, hiệu chỉnh và thay đổi bằng bằng chứng.
