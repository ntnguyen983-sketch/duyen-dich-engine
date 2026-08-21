# DD-3A v3.4 — ARCHITECTURAL ANCHOR

## Trạng thái
PERMANENT ARCHITECTURAL ANCHOR: khóa ở cấp khung kiến trúc, không khóa implementation.

## 1. Bộ ba biểu đạt
Mọi biểu đạt hiện hành quy về:

**ĐỊNH DANH | ĐỊNH LƯỢNG | ĐỊNH TÍNH**

### Định danh
Ký hiệu quy chiếu cho luồng quan sát: entity, space, interaction, event, v.v. Không mặc định gán bản ngã hay bản chất cố định.

### Định lượng
Đại lượng quan sát được trong không-thời gian: tọa độ, thời điểm, magnitude, Fin, Fout, B(V), Delta-t, sigma_rhythm, v.v.

### Định tính
Mẫu hình vận động rút ra từ định lượng + bằng chứng. Không tự động đồng nghĩa với tốt/xấu, đúng/sai.

## 2. N(n) ontology
Mọi hiện tượng có thể được quy chiếu trong tập mở:

`N = {N1, N2, ..., Nn}, n -> infinity`

Các cấu trúc lõi:
- Entity `N_i`.
- Observation `O_i,k` tại `t_k`, `V_k`.
- Interaction Event `I_m` có hướng giữa các luồng.
- Space / topology `V_k`.
- Time `t_k`.
- State / transition.

## 3. v3.0 và 3A
### Structural Domain — v3.0
Quẻ, hào, Ngũ hành, SIE, topology và các cấu trúc snapshot.

### Dynamic Domain — 3A
Chuỗi event, flow, force, spatial bottleneck, rhythm, repetition và state transition.

Hai miền vận hành trên cùng ontology N(n), không phải hai thế giới bản thể độc lập.

## 4. Entity ≠ Spatial Bottleneck
`B(V_k)` là thuộc tính của nút không gian `V_k`, không phải thuộc tính bản chất của entity đang ở đó.

`B(V_k) = F_in(V_k) - F_out(V_k)`

`F_in` và `F_out` phải được phân định bằng direction/flow_role của event.

Ví dụ: `F_in = 0.95 + 0.90 = 1.85`; `F_out = 0.30 + 0.25 = 0.55`; do đó `B(V_3) = +1.30`.

## 5. event_count ≠ cycle_count ≠ K_rep
- `event_count`: số event mà entity tham gia trong cửa sổ quan sát.
- `cycle_count`: số vòng khép kín có hướng trong topology.
- `K_rep`: số lần motif/quan hệ cụ thể lặp lại theo chuỗi thời gian.

Không được dùng một đại lượng làm đại diện cho hai đại lượng còn lại.

## 6. Rhythm
Với cùng một quan hệ `(source, target, relation)`, lấy chuỗi timestamp, sắp xếp theo thời gian, tính các khoảng `Delta-t`, rồi tính độ lệch `sigma_rhythm`.

ISO 8601 phải được parse bằng chuẩn datetime và quy về timestamp để không lỗi qua ngày/múi giờ.

## 7. Calibration boundary
Không được tự chế `f_BEC`, `f_net_out`, `r_t` hoặc trạng thái S07 nếu công thức/state contract chưa được truyền vào hoặc chưa được L4/ground truth xác nhận. Thiếu dữ liệu thì trả `None` / `NOT_COMPUTED`, không bịa heuristic rồi gọi là canonical.

## 8. Implementation boundary
Python/Rust/C++/Go, database, API, UI, graph parser, solver và adapter đều là implementation layer. Có thể thay đổi miễn không làm biến dạng architectural anchor.

## Provenance
Đây là bản chỉnh lý từ DD-3A v3.4 Architectural Anchor do người dùng cung cấp, đối chiếu với lineage v2.3.6–v2.9.2 trong Source Register.
