# DD-3A-v3.4-CANONICAL-ARCHITECTURAL-ANCHOR

**Status:** `PERMANENT_ARCHITECTURAL_ANCHOR`

**Role:** Khung tham chiếu kiến trúc chuẩn hóa — không phải tuyên bố về một bản thể hay chân lý bất biến.

## 1. Nguyên tắc vận hành

Duyên Dịch mô hình hóa sự biến đổi của thế giới bằng ba phương thức biểu đạt:

**ĐỊNH DANH | ĐỊNH LƯỢNG | ĐỊNH TÍNH**

- **Định danh (ID):** ký hiệu quy chiếu để phân biệt luồng quan sát (`N_i`, `V_k`, `I_m`, ...), không gán ngã hay bản chất cố định.
- **Định lượng (QUANTITY):** đại lượng đo được trong không-thời gian (`V_k`, `t_k`, `F_in`, `F_out`, `B(V_k)`, `Δt`, `σ_rhythm`, ...).
- **Định tính (QUALITY):** mẫu hình vận động được quan sát từ dữ liệu định lượng và bằng chứng; không phải phán xét tốt/xấu hay đúng/sai.

### Nguyên lý tối giản

> Duyên Dịch không tìm kiếm bản thể. Duyên Dịch quy chiếu hiện tượng bằng Định danh, đo biến đổi bằng Định lượng, và mô tả mẫu hình bằng Định tính.

Định danh không phải ngã. Định lượng không phải bản chất. Định tính không phải phán xét. Mọi biểu diễn đều phụ thuộc cửa sổ quan sát và có thể được cập nhật khi có quan sát mới.

## 2. Ontology tổng quát N(n)

Mọi hiện tượng được quy chiếu trong tập:

`N = {N1, N2, ..., Nn}`, với `n → ∞`.

Các cấu phần máy-executable:

- `Entity (N_i)`: định danh quy chiếu của một thực thể/tác nhân/hiện tượng.
- `Observation (O_i,k)`: ghi nhận trạng thái tại `t_k` và không gian `V_k`.
- `Interaction Event (I_m)`: sự kiện tương tác có hướng giữa các định danh.
- `Space / Topology (V_k)`: nút không gian và quan hệ topology.
- `Time (t_k)`: mốc thời gian quan sát.
- `State / Transition`: mô tả trạng thái và sự chuyển dịch giữa các lần quan sát.

Không một cấu phần nào được hiểu là bản thể bất biến.

## 3. Phân tầng v3.0 ↔ 3A

| Chiều | Ontology | v3.0 Structural | 3A Dynamic |
|---|---|---|---|
| NHÂN | `N_i` | tượng, Lục thân, cấu trúc | trạng thái/dòng động lực khi có dữ liệu hợp lệ |
| ĐỊA | `V_k` | hào vị, `M_SIE[1..6]` | `B(V_k) = F_in - F_out` |
| THIÊN | `t_k` | pha thời gian, Địa Chi | `σ_rhythm`, `K_rep` |
| QUAN HỆ | `I_m` | tương sinh/xung/hợp/hại | magnitude, direction, flow |
| BIẾN HÓA | transition | quẻ biến, hào động | trạng thái động và chuyển dịch |

3A là **Dynamic Execution Layer** vận hành trên cùng ontology N(n), không phải một ontology cạnh tranh với v3.0.

## 4. Spatial Bottleneck và Entity phải tách tuyệt đối

`B(V_k)` là thuộc tính của **không gian/nút `V_k`**, không phải bản chất của `N_i`.

Với mỗi nút:

`B(V_k) = F_in(V_k) - F_out(V_k)`

Trong đó:

- `F_in(V_k)`: tổng magnitude của sự kiện có `flow_role = IN` (hoặc hướng được quy ước là nạp/tích tụ).
- `F_out(V_k)`: tổng magnitude của sự kiện có `flow_role = OUT` (hoặc hướng được quy ước là xả/thoát).

Ví dụ:

`F_in = 0.95 + 0.90 = 1.85`

`F_out = 0.30 + 0.25 = 0.55`

`B(V_3) = +1.30`

Nếu `N_3` đang ở `V_3`, không được diễn đạt rằng “N_3 có bottleneck +1.30”. Đúng là: **`V_3` có bottleneck +1.30 tại cửa sổ quan sát đó; `N_3` được quan sát tại `V_3`.**

## 5. Ba đại lượng độc lập

Không được đồng nhất:

- `event_count`: số sự kiện `I_m` mà định danh tham gia trong cửa sổ quan sát.
- `cycle_count`: số chu trình khép kín có hướng trong topology, ví dụ `N_i → N_j → ... → N_i`.
- `K_rep`: số lần một motif/quan hệ cụ thể lặp lại theo chuỗi thời gian.

`cycle_count` là thuộc tính topology; `K_rep` là thuộc tính nhịp/hành vi theo thời gian.

## 6. Rhythm

Nhịp phải được đo trên **event sequence / relation sequence**, không gom phẳng mọi timestamp của một entity.

Với cùng motif `(source, target, relation)`:

`t_1, t_2, ..., t_K`

có thể tính các khoảng:

`Δt_i = t_(i+1) - t_i`

và độ lệch nhịp:

`σ_rhythm = std(Δt_i)`

`σ_rhythm` chỉ có ý nghĩa trong phạm vi chuỗi sự kiện được chọn. Không được suy diễn thành bản chất của entity.

ISO 8601 phải được parse bằng timezone-aware `datetime.fromisoformat()` (với `Z` chuyển thành `+00:00`) và quy đổi về Unix timestamp để tránh lỗi qua ngày/múi giờ.

## 7. Evidence và Ground Truth

Định tính phải quy chiếu về định lượng và evidence. Không được tạo trạng thái bằng công thức tự chế chỉ để lấp output.

Nếu một đại lượng phụ thuộc vào L4/Calibrator/Ground Truth nhưng dữ liệu chưa tồn tại:

- trả về `None`, hoặc
- trạng thái rõ ràng `NOT_COMPUTED_WITHOUT_L4_STATE`.

Không hardcode một trạng thái như thể đó là kết quả tính toán.

Ground Truth là quan sát mới dùng để kiểm chứng/hiệu chỉnh; không được đồng nhất Ground Truth với một “chân lý siêu hình”.

## 8. Tie-breaking

Khi ranking candidate đã được định nghĩa, thứ tự chuẩn là:

1. `P_raw` giảm dần
2. `B_v`/`spatial_B_v` giảm dần
3. `E_cov` giảm dần
4. `entity_id` tăng dần theo thứ tự từ điển A→Z

Không tự ý thêm tiêu chí tie-break mới.

## 9. Architectural boundaries

### Anchor Core — ổn định ở cấp kiến trúc

- Ontology N(n).
- Bộ ba `Định danh | Định lượng | Định tính`.
- Phân biệt Entity và Space.
- `B(V_k) = F_in - F_out` thuộc Space.
- Tách `event_count`, `cycle_count`, `K_rep`.
- Rhythm được đo từ event/relation sequence.
- L4/Calibrator nhận Ground Truth như vòng phản hồi mở.
- v3.0 là Structural Domain; 3A là Dynamic Execution Layer.

### Flexible Implementation — không khóa

- Python/Rust/C++/Go/...
- database và API schema.
- graph parser, matrix solver, optimizer.
- UI/UX.
- loại entity và relation mới.
- cách lưu trữ và triển khai phân tán.

**Anchor ≠ Mathematical Finality ≠ Ontological Truth.**

## 10. Canonical payload mẫu

```json
{
  "case_id": "CANONICAL-TEST-001",
  "observation_window": {
    "start": "2026-08-21T08:00:00Z",
    "end": "2026-08-21T08:30:00Z"
  },
  "entities": [
    {
      "entity_id": "N1",
      "entity_type": "ACTOR",
      "label": "Shipper Lý Nhật An",
      "structural_ref": {"hexagram": "Khảm", "line": 5, "element": "Thuy"},
      "observations": [{
        "timestamp": "2026-08-21T08:00:00Z",
        "where": {"node_ref": "V1", "coords": [10.776, 106.700, 0.0]},
        "physical_proxy": ["shipper_ly_nhat_an"],
        "evidence_refs": ["gps-tracker-n1"]
      }]
    },
    {
      "entity_id": "N2",
      "entity_type": "VEHICLE",
      "label": "Xe máy giao hàng",
      "structural_ref": {"hexagram": "Cấn", "line": 2, "element": "Tho"},
      "observations": [{
        "timestamp": "2026-08-21T08:02:00Z",
        "where": {"node_ref": "V2", "coords": [10.776, 106.701, 0.0]},
        "physical_proxy": ["xe_may_hop_chuyen_dung"],
        "evidence_refs": ["cam-v2-01"]
      }]
    },
    {
      "entity_id": "N3",
      "entity_type": "OBJECT",
      "label": "Túi thuốc đặc trị",
      "structural_ref": {"hexagram": "Tốn", "line": 1, "element": "Moc"},
      "observations": [{
        "timestamp": "2026-08-21T08:05:00Z",
        "where": {"node_ref": "V3", "coords": [10.776, 106.701, 0.8]},
        "physical_proxy": ["tui_thuoc_niem_phong_xanh"],
        "evidence_refs": ["photo-bag-01", "qr-scan-n3"]
      }]
    }
  ],
  "interactions": [
    {"interaction_id":"I-01","source":"N1","target":"N3","relation":"SO_HUU_DIEU_CHUYEN","direction":"FORWARD","flow_role":"IN","magnitude":0.90,"timestamp":"2026-08-21T08:05:00Z","location_node":"V1"},
    {"interaction_id":"I-02","source":"N1","target":"N2","relation":"VAN_HANH","direction":"FORWARD","flow_role":"IN","magnitude":0.85,"timestamp":"2026-08-21T08:10:00Z","location_node":"V2"},
    {"interaction_id":"I-03","source":"N3","target":"N2","relation":"DAT_TRON_CAP","direction":"FORWARD","flow_role":"IN","magnitude":0.95,"timestamp":"2026-08-21T08:12:00Z","location_node":"V3"},
    {"interaction_id":"I-04","source":"N2","target":"N3","relation":"PHAN_HOI_VI_TRI","direction":"BACKWARD","flow_role":"OUT","magnitude":0.30,"timestamp":"2026-08-21T08:17:00Z","location_node":"V3"},
    {"interaction_id":"I-05","source":"N3","target":"N2","relation":"DAT_TRON_CAP","direction":"FORWARD","flow_role":"IN","magnitude":0.90,"timestamp":"2026-08-21T08:22:00Z","location_node":"V3"},
    {"interaction_id":"I-06","source":"N2","target":"N3","relation":"PHAN_HOI_VI_TRI","direction":"BACKWARD","flow_role":"OUT","magnitude":0.25,"timestamp":"2026-08-21T08:27:00Z","location_node":"V3"}
  ],
  "threshold_profile": {"tau_B": 0.45, "kappa_B": 2},
  "provenance": {
    "source_version": "DD-3A-v3.4-CANONICAL-ARCHITECTURAL-ANCHOR",
    "input_hash": "sha256_canonical_test_hash"
  }
}
```

## 11. Reference implementation policy

Reference implementation chỉ là **executable interpretation của Anchor**, không phải nguồn để tự phát sinh ontology mới.

Mọi implementation đầy đủ phải:

1. ingest/validate canonical payload;
2. bảo toàn định danh, space, time và event;
3. tính `F_in/F_out` theo `flow_role`;
4. tính `B(V_k)` tại Space;
5. tính `event_count`, `cycle_count`, `K_rep` độc lập;
6. tính rhythm trên relation sequence;
7. giữ timezone chính xác;
8. áp dụng tie-breaking chuẩn;
9. không tự chế `f_BEC`, `f_net_out`, `S07`, `G_breaker` khi công thức/trạng thái đầu vào chưa được đóng và chứng minh;
10. trả về `None`/not-computed thay vì bịa kết quả;
11. cung cấp provenance và test vectors;
12. chứng minh bằng test suite trước khi gọi production-ready.

## 12. Culi implementation contract

Đây là **nguồn tham chiếu để viết bản full engine**, không phải giấy phép thay đổi Anchor.

Culi phải làm việc theo thứ tự:

`Anchor → Schema → Validator → Core Engine → Dynamic Layer → Test Suite → Ground Truth/L4 hooks → API → UI adapter → Production verification`

Không được:

- tạo v3.5/v3.6 chỉ để vá implementation;
- đưa công thức giả định vào core;
- gắn bottleneck lên entity;
- đồng nhất cycle với repetition;
- hardcode trạng thái chưa tính được;
- biến label/label text thành ontology;
- tự đổi meaning của Anchor để làm test pass.

**Mục tiêu:** một implementation hoàn chỉnh, kiểm thử được, có thể thay Python bằng Rust/C++ mà không thay đổi kiến trúc quy chiếu.
