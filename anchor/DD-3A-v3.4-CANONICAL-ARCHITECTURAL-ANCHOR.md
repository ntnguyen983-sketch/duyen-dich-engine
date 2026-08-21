# DD-3A v3.4 — CANONICAL ARCHITECTURAL ANCHOR

Status: `PERMANENT_ARCHITECTURAL_ANCHOR`

## 1. Nguyên tắc
Duyên Dịch không mô hình hóa vật thể hay chân lý cố định. Duyên Dịch mô hình hóa sự tồn tại, vị trí, thời điểm, trạng thái và tương tác của các luồng quan sát trong một hệ mở; từ chuỗi tương tác mô tả động lực, nhịp và chuyển dịch.

## 2. Bộ ba phép biểu đạt
- **Định danh (ID):** ký hiệu quy chiếu để truy vết luồng quan sát; không gán bản ngã hay bản chất cố định.
- **Định lượng (QUANTITY):** đại lượng đo được trong không-thời gian: vị trí, thời điểm, lực, dòng vào/ra, chênh lệch, khoảng thời gian, nhịp...
- **Định tính (QUALITY):** mẫu hình vận động quan sát được; luôn có nguồn định lượng/bằng chứng đi kèm và có điều kiện.

## 3. Ontology
Các thành phần tham chiếu: Entity/stream, Observation, Interaction Event, Space/Topology, Time, State/Transition.

## 4. v3.0 ↔ 3A
- v3.0: structural domain — cấu trúc, quẻ/hào, quy chiếu Ngũ hành, topology.
- 3A: dynamic execution layer — event sequence, flow, spatial bottleneck, rhythm, repetition, transition.

## 5. Spatial bottleneck
`B(V_k) = F_in(V_k) - F_out(V_k)`.

Bottleneck thuộc nút không gian `V_k`, không thuộc bản thể của một Entity chỉ vì Entity đang ở đó.

## 6. Ba đại lượng không được đánh tráo
- `event_count`: số event mà luồng/Entity tham gia.
- `cycle_count`: số chu trình có hướng khép kín trong topology.
- `K_rep`: số lần motif/quan hệ cụ thể lặp lại theo chuỗi thời gian.
- `sigma_rhythm`: độ lệch của các khoảng thời gian trong cùng motif/quan hệ.

## 7. Canonical discipline
Không tự chế công thức chưa có trong Anchor/Spec. Nếu một đại lượng cần L4/Calibration/Ground Truth nhưng chưa có dữ liệu, để `None`/uncomputed thay vì ước lượng.

## 8. Ranh giới
### Khóa ở cấp kiến trúc
Ontology, bộ ba biểu đạt, phân tách structural/dynamic, Entity/Space, event/cycle/K_rep, L4 feedback.

### Không khóa ở cấp thực thi
Ngôn ngữ, DB, API, UI, parser, solver, adapter và implementation details.

## 9. Nguyên tắc vô thường / vô ngã
Các nhãn chỉ là phương tiện quy chiếu và truy vết. Không dùng nhãn để biến một dòng quan sát thành một bản thể cố định. Định tính là mô tả mẫu hình của quan hệ và biến đổi, không phải phán quyết bản thể hay giá trị.
