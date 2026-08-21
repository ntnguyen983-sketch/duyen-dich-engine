# DD-3A v3.4 — CANONICAL ARCHITECTURAL ANCHOR

## Trạng thái

`PERMANENT_ARCHITECTURAL_ANCHOR`

Đây là khung tham chiếu kiến trúc, không phải tuyên bố rằng lý luận về thế giới đã bất biến.

## Bộ ba biểu đạt

**ĐỊNH DANH | ĐỊNH LƯỢNG | ĐỊNH TÍNH**

### Định danh
Ký hiệu quy chiếu để phân biệt luồng quan sát: `N_i`, `V_k`, `I_m`, `t_k`.

### Định lượng
Đại lượng đo/ghi trong không-thời gian: vị trí, timestamp, magnitude, `F_in`, `F_out`, `B(V_k)`, `Δt`, `σ_rhythm`, `event_count`, `cycle_count`, `K_rep`.

### Định tính
Mẫu hình vận động quan sát được và quy chiếu về dữ liệu/evidence. Không gán tốt/xấu hay bản chất cố định.

## N(n) ontology

`Entity → Observation → Interaction → State/Transition`, được đặt trong `Space` và `Time`.

## V3.0 ↔ 3A

- v3.0: Structural Domain — quẻ, hào, Ngũ hành, Lục hào, SIE, topology.
- 3A: Dynamic Domain — interaction sequence, flow, spatial bottleneck, rhythm và transition.

Hai tầng dùng cùng một ontology; 3A không tạo một ontology cạnh tranh với v3.0.

## Space ≠ Entity

`B(V_k) = F_in(V_k) - F_out(V_k)` là thuộc tính của nút không gian `V_k`.

Một `N_i` có thể đang ở `V_k`, đi qua `V_k` hoặc tương tác tại `V_k`; điều đó không biến `B(V_k)` thành thuộc tính bản thể của `N_i`.

## Ba đại lượng phải tách

- `event_count`: số sự kiện có sự tham gia của N_i.
- `cycle_count`: số chu trình khép kín có hướng trong topology.
- `K_rep`: số lần motif/chuỗi quan hệ lặp lại theo thời gian.

## Vô thường và implementation

Kiến trúc là điểm neo để các implementation có thể cùng nói một ngôn ngữ. Nó không được dùng để biến các mô hình, nhãn hoặc trạng thái quan sát thành bản thể cố định.

Nếu dữ liệu mới làm mô hình hiện tại không còn phù hợp, không sửa dữ liệu để bảo vệ nhãn; ghi nhận sai khác, đưa vào validation/research và hiệu chỉnh bằng evidence/Ground Truth.
