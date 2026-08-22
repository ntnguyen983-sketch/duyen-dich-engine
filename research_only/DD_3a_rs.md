# DD_3a_rs

## Kính Chiếu Yêu / NxNxN

### Research Specification · Conceptual Lock

> **Trạng thái:** `RESEARCH / CONCEPTUAL_LOCK`  
> **Kernel impact:** `NONE`  
> **S07 impact:** `NONE`  
> **Calibration impact:** `NONE`  
> **Runtime status:** Non-executable ontology and architecture layer

> **Mục tiêu:** Duyên Dịch dùng Kính Chiếu Yêu / NxNxN để quan sát vận hành, quan hệ, tích tụ, topology, dấu hiệu chuyển pha, sự nổi lên và truy nguyên. Tài liệu này không dùng để phán quyết đúng–sai, không bác bỏ dự đoán và không phát biểu chắc chắn về tương lai.

## 1. Phạm vi và nguyên tắc bảo toàn

Một hệ đối kháng không có số biến số đóng. Ngoài các Actor và hào ban đầu, hệ còn có điều kiện nền, quan hệ phát sinh, phản ứng qua lại, topology, thông tin, lòng tin, kỳ vọng, phần thưởng, môi trường và các cấu trúc mới nổi lên trong lúc vận hành.

`NxNxN` không tìm cách đếm hết cái vô cực. Nó tạo một **quy trình quan sát bất biến về mặt nguyên tắc**, trong đó mỗi lát cắt hữu hạn chỉ là phần đang được mở tại thời điểm quan sát:

```text
Rₙ → Rₙ₊₁ → Rₙ₊₂ → …
```

`n` là lát cắt hiện thời, không phải giới hạn cuối cùng của hệ. Ba diện Tượng–Lượng–Tính là phép chiếu chung, không phải ba vật thể độc lập và cũng không phải ba tập giá trị hữu hạn.

## 2. Định nghĩa NxNxN

Định nghĩa khái niệm:

> **NxNxN là không gian tổ hợp mở của ba diện Tượng–Lượng–Tính, trong đó N biểu thị miền giá trị, thực thể, quan hệ, topology và cấp nổi lên có thể mở rộng; N không phải một cardinality cố định.**

Do đó:

```text
NxNxN ≠ một ma trận vô hạn phải cấp phát ngay
NxNxN ≠ một danh sách ba tập biến đóng
NxNxN ≠ 18×18
```

Sự vô hạn nằm ở ít nhất bốn miền có thể mở rộng:

| Miền mở | Ý nghĩa |
|---|---|
| `N_A` | Số Actor hoặc node đang được xét |
| `N_R` | Số quan hệ đang tồn tại, phát sinh hoặc được giả thuyết |
| `N_B` | Số điều kiện nền đang hoạt hóa |
| `N_λ` | Số cấp tổ hợp/nổi lên đang được xét |

Các miền này có thể tăng độc lập. Không dùng một chữ `N` làm cardinality thần bí đại diện cho tất cả.

## 3. Kính Chiếu Yêu: Projection

Mọi đối tượng được chấp nhận vào miền quan sát — hào, Actor, điều kiện nền, quan hệ, cụm, mạng hoặc thực thể nổi lên — có thể được mô tả thử qua phép chiếu:

```text
Πₒ(X; C, tₒ) = (Tượngₒ(X), Lượngₒ(X), Tínhₒ(X))
```

Chỉ số `o` xác định người quan sát hoặc quy trình quan sát; `C` là context tại thời điểm đó; `tₒ` là thời điểm quan sát/ghi nhận. Phép chiếu là **epistemic và có provenance**, không tuyên bố rằng ba diện đã bao phủ trọn bản thể của thực tại.

Mỗi thành phần có thể là giá trị quan sát được, một phần, `UNKNOWN`, `UNRESOLVED` hoặc `NOT_APPLICABLE`.

### 3.1. Tượng

**Tượng** là diện nhận thức và hình thái: cái được biểu hiện, nhận diện, hình dung, dựng lên, kỳ vọng hoặc phát lộ. Tượng có thể chứa sơ đồ chiến thuật, hình thái sân bãi, truyền thông, thông tin, lòng tin, kỳ vọng, biểu diện thế trận và các dấu hiệu mà một quan sát viên có thể nhận ra.

Tượng không đồng nhất với “ảo giác” hay “bề mặt”. Nó là cách một trạng thái được hình thành và có thể trở thành hình thái quan sát được.

### 3.2. Lượng

**Lượng** là diện động năng và biên độ: mức độ, nạp, rút, tích tụ, tiêu hao, mật độ, tốc độ, áp lực, va chạm, hướng dòng, độ bền và tần suất chuyển trạng thái.

Ở tầng Research, Lượng có thể được mô tả bằng descriptor, chưa phải công thức số hóa:

```text
L_obs = (magnitude, direction, persistence,
         accumulation, dispersion, flow)
```

Tổng Lượng tức thời không đủ mô tả vận hành. Cùng một tổng lực nhưng dồn vào một vùng, phân tán trên nhiều vùng, chuyển hướng liên tục hoặc duy trì ổn định sẽ có khả năng phát lộ khác nhau.

### 3.3. Tính

**Tính** là diện quy luật, constraint và grammar của quan hệ: các cấu trúc Can Chi, Ngũ Hành, Lục Thân, Sinh–Khắc, Cục, Tương Hình và các điều kiện biến đổi đã được quy ước trong phạm vi profile tương ứng.

Tính không phải State:

```text
Tinh_rule ≠ State_current
```

Tính quy định hoặc giới hạn khả năng biến đổi trong một scope và version. State là cấu hình hiện thời đang được quan sát hoặc suy luận. `Tinh_rule` có thể giữ nguyên trong khi `State_t` thay đổi; các rule đang được áp dụng có thể thay đổi theo context mà không làm định nghĩa rule gốc biến thành một State thông thường.

Trong bản này, dùng `Tinh` hoặc viết đầy đủ **Tính**; không dùng `K` làm ký hiệu mặc định để tránh nhầm với Kernel, cardinality, calibration key hoặc điều kiện nền.

## 4. Projection và Composition

NxNxN có hai phép lõi, được lặp lại đệ quy:

```text
Projection:
X → Πₒ(X) = (Tượng, Lượng, Tính)

Composition:
{X₁, X₂, …, Xₚ} + Background + Context
→ Relation / Cluster / Graph / Network
```

**Phân giải không phải đích đến. Tổ hợp không phải phép cộng.** Các thành phần đã được chiếu có thể cộng hưởng, triệt tiêu, chuyển hóa, bắc cầu, dồn cụm, phân tán, gây nhiễu, khóa đường truyền hoặc mở đường truyền.

Một quan hệ yếu có thể trở thành thành phần của một cụm mạnh. Một quan hệ mạnh có thể không phát lộ nếu topology triệt tiêu, phân tán hoặc chuyển hướng nó.

## 5. Ontology theo cấp nổi lên `λ`

`λ` là **Emergence Level**, một chỉ số của đối tượng đang được quan sát trong một analysis profile. `λ` không phải chiều thứ tư của NxNxN, không phải trục Tượng–Lượng–Tính và không phải một ladder toàn cục bắt buộc.

| Cấp minh họa | Đối tượng | Ghi chú |
|---|---|---|
| `λ0` | Hào / Actor / Background | Đối tượng nguyên tử của lát cắt |
| `λ1` | Relation | Quan hệ giữa các đối tượng |
| `λ2` | Cluster | Cụm quan hệ có cấu trúc |
| `λ3` | Network | Mạng và topology truyền lực |
| `λ4` | Emergent candidate/state | Cấu trúc mới được nhận diện ở cấp cao hơn |
| `λn` | Thực thể mới | Cấp mở, có thể branch, skip hoặc overlap |

Mỗi cấp đều có thể được tái chiếu:

```text
X⁽λ⁾ → Πₒ → Compose → X⁽λ′⁾
```

Không mặc định `λ′ = λ + 1`. Một tổ hợp có thể chưa đủ tư cách để thành thực thể; một thực thể mới có thể xuất hiện ở cấp phân tích khác; các cấp có thể chồng lấn hoặc có quan hệ cross-level.

### 5.1. Điều kiện ứng viên nổi lên

Một tổ hợp chỉ được ghi nhận là **Emergent Candidate** khi có bằng chứng cho ba điều kiện tối thiểu:

```text
Identity + Boundary + Internal Structure
```

Trong đó:

| Điều kiện | Yêu cầu quan sát |
|---|---|
| **Identity** | Có thể được quy chiếu như một đơn vị tương đối ổn định trong cửa quan sát đã khai báo |
| **Boundary** | Có ranh giới với phần còn lại; phải ghi loại ranh giới: không gian, quan hệ, nhân quả, thông tin, thời gian hoặc analyst-defined |
| **Internal Structure** | Có các quan hệ nội tại có tổ chức, không chỉ là một tập rời rạc |

**Role/Effect** — tác động của tổ hợp lên dòng quan hệ, tích tụ, ngưỡng hoặc diễn giải — là thuộc tính hỗ trợ quan trọng cho việc dùng operational, nhưng không tự động là điều kiện duy nhất để xác định bản thể nổi lên.

Khả năng tái chiếu chỉ là điều kiện để tiếp tục quan sát, không tự nó chứng minh rằng emergence đã xảy ra. Việc promotion phải qua evidence gate ở tầng Research.

## 6. Lớp `6×6×3×3` và lát cắt `18×18`

Với một Actor được biểu diễn bằng sáu hào, mỗi hào có ba thành phần quan sát:

```text
6 hào × 3 diện = 18 thành phần
```

Cho hai Actor A và B:

```text
A_index = {(i,a) | i ∈ 1..6, a ∈ {Tượng,Lượng,Tính}}
B_index = {(j,b) | j ∈ 1..6, b ∈ {Tượng,Lượng,Tính}}
```

Trường quan hệ có thể biểu diễn tương đương dưới hai dạng:

```text
Q[i,j,a,b]       ∈ 6 × 6 × 3 × 3
R[(i,a),(j,b)]   ∈ 18 × 18
```

`18×18` là **lát cắt index/relation space** gồm 324 candidate component-pair slots. Nó không phải toàn bộ NxNxN, không phải 324 biến bắt buộc và không phải một ma trận đã khẳng định mọi quan hệ đều tồn tại.

`6×6×3×3` và `18×18` là hai cách biểu diễn của cùng trường thành phần. `3×3` là kiểu giao diện giữa hai diện, đã được mã hóa trong cặp chỉ số `(i,a)` và `(j,b)`; không được nhân thêm thành `18×18×3×3` như một cardinality độc lập.

### 6.1. Chín kiểu giao diện

| A \ B | Tượng | Lượng | Tính |
|---|---|---|---|
| **Tượng** | Tượng–Tượng | Tượng–Lượng | Tượng–Tính |
| **Lượng** | Lượng–Tượng | Lượng–Lượng | Lượng–Tính |
| **Tính** | Tính–Tượng | Tính–Lượng | Tính–Tính |

Đây là **interface taxonomy**, không phải chín tầng ontology và không phải thêm một chiều cardinality.

### 6.2. Relation cell

Một ô là một candidate comparison slot trong context, thời điểm và cấp quan sát cụ thể:

```text
R_obs[(i,a),(j,b) | C, t_e, t_o, λ]
  = <status, type, direction, evidence,
     uncertainty, provenance>
```

Trong đó `t_e` là event time và `t_o` là observation/recording time. `status` có thể là:

```text
OBSERVED | INFERRED | UNRESOLVED | NOT_OBSERVED | NOT_APPLICABLE
```

Một ô không mặc định là một quan hệ có thật. Không có dữ liệu không được tự động đổi thành `0`, `false`, “không có quan hệ” hoặc lực bằng không.

## 7. Background và Context

Điều kiện nền là đối tượng có thể được chiếu, không chỉ là danh sách biến ngoài hệ:

```text
Bₖ → Πₒ(Bₖ) = (Tượngₖ, Lượngₖ, Tínhₖ)
```

Các nền có thể gồm sân bãi, chiến thuật, thông tin/lòng tin, sự ủng hộ, phần thưởng, kỳ vọng và các điều kiện mới phát sinh. Một nền có thể khuếch đại, triệt tiêu, làm chậm, làm lệch, che tín hiệu hoặc thay đổi điều kiện phát lộ.

Trong tài liệu này:

- `B_k` là một background object cụ thể.
- `C_t` là context đang hoạt hóa tại thời điểm `t`, có thể được cấu thành từ nhiều `B_k` và các điều kiện quan sát khác.
- Background và Context không mặc định là cùng một khái niệm.

Quan hệ nên được hiểu theo dạng:

```text
Relation_obs = Relation(A, B | C_t, t_e, t_o, λ)
```

## 8. Relation Graph và Topology

Các quan hệ được tổ chức thành graph động:

```text
G_t = (V_t, E_t, τ_struct, a_t, F_t)
```

| Thành phần | Ý nghĩa |
|---|---|
| `V_t` | Actor, hào, background, relation, cluster, network hoặc emergent candidate đang mở |
| `E_t` | Các cạnh/quan hệ được quan sát, suy luận hoặc chưa giải quyết |
| `τ_struct` | Topology tương đối ổn định theo profile: trung tâm, cầu, nhánh, vòng, cụm và đường nối |
| `a_t` | Trạng thái active/inactive của cạnh hoặc quan hệ tại thời điểm `t` |
| `F_t` | Dòng Lượng đang chạy: hướng, cường độ, duy trì, tích tụ, phân tán |

Topology không phải một bước tĩnh luôn đứng trước Accumulation. Quan hệ, topology và dòng lực có thể đồng biến:

```text
Compose ↔ Topology ↔ Accumulation
                         ↓
                      Threshold
```

Cùng số Actor, cùng số quan hệ hoặc cùng tổng Lượng vẫn có thể tạo trạng thái khác nhau nếu topology, hướng dòng, mật độ hoặc độ bền khác nhau.

## 9. Snapshot, Dynamics, Transition và Emergence

Bốn loại hồ sơ phải được tách riêng:

| Loại | Câu hỏi | Không được suy ra tự động |
|---|---|---|
| **Snapshot** | Hệ đang ở đâu và có cấu hình gì tại lát cắt này? | Không tự suy ra Dynamics |
| **Dynamics** | Cái gì đang thay đổi, theo hướng nào, với tốc độ nào? | Không tự suy ra tương lai chắc chắn |
| **Transition** | Hệ có dấu hiệu chuyển cấu hình/pha không? | Không tự suy ra Emergence |
| **Emergence** | Có cấu trúc mới đủ điều kiện làm ứng viên ở cấp cao hơn không? | Không tự suy ra Transition scalar |

Một snapshot đơn không đủ để khẳng định dynamics. Transition và Emergence có thể cùng xảy ra, nhưng không cái nào bắt buộc kéo theo cái kia.

## 10. Accumulation và Threshold

Lượng là quá trình trên graph, không chỉ là giá trị tức thời. Tích tụ có thể tăng, giảm, duy trì, chuyển hướng, dồn cụm, phân tán hoặc bị triệt tiêu.

Ngưỡng là thuộc tính của cấu hình:

```text
Θ_config = Θ(rule-scope, active-background,
             topology, flow, history, evidence)
```

Biểu thức dưới đây chỉ là một **mô hình Research có thể có**, không phải invariant:

```text
Q_eff ≥ Θ_config
```

Không được mặc định `Q_eff` là scalar, không được mặc định mọi transition là crossing scalar và không được chọn số ngưỡng tiên nghiệm trong bản Conceptual Lock.

Các trạng thái quan sát tối thiểu:

```text
PRE_THRESHOLD
THRESHOLD_CROSSING
POST_THRESHOLD
UNKNOWN
```

Các nhãn này không phải S07 Khí. Chúng chỉ mô tả trạng thái nghiên cứu của điều kiện chuyển pha.

## 11. Máy trạng thái đệ quy

```text
INPUT / SNAPSHOT
       │
       ▼
IDENTIFY ENTITY
       │
       ▼
Πₒ : TƯỢNG–LƯỢNG–TÍNH
       │
       ▼
RELATION COMPOSITION
       │
       ▼
GRAPH / TOPOLOGY
       │
       ▼
ACCUMULATION / FLOW
       │
       ▼
TRANSITION ASSESSMENT
       │
   ┌───┴───────────────────┐
   │                       │
 chưa nhận diện            có ứng viên chuyển/đổi cấu hình
   │                       │
   │                       ▼
   │               PHASE TRANSITION CANDIDATE
   │                       │
   │                       ▼
   │               EMERGENT CANDIDATE?
   │                       │
   └───────────────────────┤
                           ▼
                    EVIDENCE GATE
                           │
                  nếu đủ căn cứ: X⁽λ′⁾
                           │
                           ▼
                    RE-PROJECTION Πₒ
                           │
                           └────→ …
```

Đây là **máy trạng thái đệ quy**, không phải calculator. “Chưa nhận diện” không có nghĩa là thất bại; nó chỉ tiếp tục mở context, graph và lịch sử. `λ′ > λ` chỉ được ghi khi cấp phân tích mới có căn cứ; không tự động tăng một cấp sau mỗi vòng.

## 12. Năm nguyên lý vận hành và hai guardrail

### Principle 1 — Projection

> Trong phạm vi profile quan sát, mọi đối tượng được chấp nhận vào miền quan sát có thể được mô tả thử qua Tượng–Lượng–Tính; phép chiếu có thể một phần, chưa xác định hoặc không áp dụng.

### Principle 2 — Composition

> Các thành phần đã được chiếu có thể tổ hợp thành quan hệ, cụm, topology và mạng; tổ hợp không bị giản lược thành phép cộng lực.

### Principle 3 — Emergence

> Một tổ hợp có identity tương đối, boundary có khai báo và internal structure có ý nghĩa có thể được ghi nhận như ứng viên thực thể ở cấp quan sát cao hơn.

### Principle 4 — Accumulation

> Lượng là dòng vận động trên topology: có thể nạp, rút, duy trì, tích tụ, phân tán, chuyển hướng hoặc bị triệt tiêu; tổng lượng tức thời không đủ mô tả hệ.

### Principle 5 — Transition

> Khi cấu hình quan hệ, Tính, nền, topology, lịch sử và dòng Lượng tạo ra dấu hiệu đủ để ghi nhận một khả năng chuyển pha, hệ có thể được đánh dấu là Transition Candidate; điều này không phải lời khẳng định chắc chắn về tương lai.

### Guardrail 0 — Open Field

> Trường vận hành không đóng trước số Actor, quan hệ, nền, topology hoặc cấp nổi lên. `n` là lát cắt đang mở, không phải giới hạn của thực tại.

### Guardrail 6 — Traceability

> Mọi phép chiếu, quan hệ, topology update, transition marker và emergence candidate phải giữ được provenance, source/version, thời điểm, snapshot reference, context, cấp `λ`, uncertainty và layer; quan sát sau không được sửa ngược snapshot trước.

Năm Principle là lõi vận hành khái niệm. Hai Guardrail bảo vệ tính mở và tính truy vết của toàn hệ. Tất cả đều là **document-level research commitments**, không phải Kernel invariants.

## 13. Phân tầng và ranh giới governance

Dòng phân tầng bắt buộc:

```text
Data → Signal → Pattern → Inference → Action
```

`DD_3a_rs` thuộc `RESEARCH / ARCHITECTURE`. Nó có thể khóa vocabulary khái niệm, flow, relation-cell semantics, emergence criteria và traceability requirements.

Nó không được tự ý:

- sửa Kernel v3.0_dd;
- tạo, đổi tên hoặc mở rộng S07;
- map Vectơ Khí 5D → S07 khi chưa có `S07_MAPPING_PROFILE` hợp lệ;
- đưa trọng số, decay, topology metric, Combine function hoặc threshold number vào Core;
- dùng lực, `f_net_out`, transition score hoặc magnitude làm `confidence_score`;
- tự động biến `UNKNOWN` thành zero, false, absence hoặc no relation;
- tự động promotion relation/cluster thành emergent entity;
- để Action quay ngược thành bằng chứng cho Inference nếu không có Data mới độc lập.

S07 canonical của Kernel vẫn giữ nguyên:

```text
SÁT, TÀ, NHIỄU, HỶ, DƯỠNG, ẨN
SAT, TA, NHIEU, HY, DUONG, AN
```

Tài liệu này không tạo mapping S07 mới và không đưa trạng thái `PRE_THRESHOLD`, `THRESHOLD_CROSSING` hoặc `POST_THRESHOLD` vào S07.

## 14. Snapshot và provenance tối thiểu

Mọi record Research nên giữ ít nhất:

```json
{
  "record_id": "...",
  "level_lambda": null,
  "entity_kind": "ACTOR|BACKGROUND|RELATION|CLUSTER|NETWORK|EMERGENT_CANDIDATE",
  "layer": "DATA|SIGNAL|PATTERN|INFERENCE|ACTION",
  "snapshot_id": "...",
  "observation_time": "...",
  "event_time": null,
  "context_ids": [],
  "source_ids": [],
  "projection": {
    "tuong": null,
    "luong": {
      "magnitude": null,
      "direction": null,
      "persistence": null,
      "accumulation": null,
      "dispersion": null
    },
    "tinh_rule": null
  },
  "relation_status": "OBSERVED|INFERRED|UNRESOLVED|NOT_OBSERVED|NOT_APPLICABLE",
  "topology_ref": null,
  "threshold_phase": "PRE_THRESHOLD|THRESHOLD_CROSSING|POST_THRESHOLD|UNKNOWN",
  "transition_status": "IDENTIFIED|NOT_IDENTIFIED|UNRESOLVED",
  "emergence_status": "CANDIDATE|NOT_IDENTIFIED|UNRESOLVED",
  "uncertainty": null,
  "provenance": [],
  "classification": "RESEARCH|PLACEHOLDER"
}
```

Đây là schema Research tối thiểu, không thay thế JSON canonical của Kernel. Các trường chưa có định nghĩa hoặc calibration phải giữ `null`, `UNKNOWN`, `UNRESOLVED` hoặc `PLACEHOLDER`.

## 15. Test vectors khái niệm

| Test | Điều kiện | Kết quả mong đợi |
|---|---|---|
| Flattening | Hai Actor, mỗi Actor 6 hào × 3 diện | Có thể biểu diễn `6×6×3×3` hoặc `18×18`; không tạo `18×18×3×3` như cardinality mới |
| Tính/State | Rule scope giữ nguyên, Lượng và State thay đổi | State/Dynamics được ghi; Tính không bị viết lại |
| Snapshot/Dynamics | Chỉ có một snapshot | Snapshot được ghi; Dynamics và Transition là `UNKNOWN/INSUFFICIENT_DATA` |
| Equal total, different topology | Tổng Lượng tương đương, graph khác topology | Có thể có graph/transition khác; không suy ra kết quả từ tổng lực |
| Aggregate without entity | Nhiều relation ngắn, rời rạc | Ghi pattern/cluster candidate; không tự promotion |
| Emergence | Có identity, boundary, internal structure và provenance | Có thể ghi `EMERGENT_CANDIDATE`, qua evidence gate rồi mới tái chiếu |
| Transition without emergence | Cấu hình đổi nhưng chưa có identity mới | Ghi Transition Candidate; không ghi Emergence tự động |
| Emergence without scalar threshold | Cấu trúc mới rõ nhưng chưa có Q/Theta | Có thể ghi Emergent Candidate; cơ chế ngưỡng là `UNRESOLVED` |
| Missing relation | Ô không có bằng chứng | `NOT_OBSERVED` hoặc `UNRESOLVED`, không mặc định zero |
| Inapplicable relation | Cặp component không có nghĩa trong profile | `NOT_APPLICABLE`, khác với absence |
| Observer disagreement | Hai quan sát viên chiếu Tượng khác nhau từ cùng Data | Giữ cả hai projection, provenance và uncertainty |
| Background modulation | Background làm thay đổi visibility/flow | Ghi background projection và liên kết provenance; không khẳng định causal certainty |
| De-emergence | Cấu trúc đã ghi nhận mất boundary/internal organization | Ghi dissolution/change; không xóa emergence record cũ |
| Recursive explosion | Mọi cặp bị tự động promotion | Evidence gate và recursion control phải chặn promotion không đủ căn cứ |
| S07 pressure | Có vector 5D nhưng thiếu mapping profile | `MAPPING_UNRESOLVED`; không ép nhãn S07 |
| Force/confidence | Lượng hoặc force magnitude cao | Ghi intensity; không sao chép sang `confidence_score` |
| Future claim | Dynamics tiến gần một điều kiện | Chỉ ghi trajectory/candidate/uncertainty, không khẳng định sự kiện tương lai |

## 16. Những gì chưa khóa

Các nội dung sau vẫn thuộc `RESEARCH` hoặc `PLACEHOLDER`:

- công thức định lượng Tượng, Lượng và Tính;
- định nghĩa scalar/vector của `Q_eff`;
- hàm `Θ_config` và mọi ngưỡng số;
- trọng số giữa Tượng–Lượng–Tính;
- hàm Combine và hàm triệt tiêu/cộng hưởng/chuyển hóa;
- topology metric, centrality, edge activation và cluster detection;
- boundary detection, identity persistence và de-emergence;
- thuật toán phát hiện Emergence hoặc promotion gate cụ thể;
- decay, persistence, accumulation và flow equation;
- maximum recursion depth và runtime enum bắt buộc cho `λ`;
- deterministic State function;
- prediction formula hoặc Action mapping;
- mapping từ Vectơ Khí 5D sang S07;
- bất kỳ S07 state, alias hoặc enum mới nào;
- mặc định biến thiếu bằng zero/false/absence;
- mọi runtime behavior có khả năng biến candidate thành action tự động.

## 17. Đúc kết final

> **Kính Chiếu Yêu không phải ma trận để tính hết thực tại. Nó là một phép chiếu để biến thực tại thành quan hệ có thể truy vết; một phép tổ hợp để quan hệ sinh topology, cụm và mạng; một phép tái chiếu để quan sát cấu trúc mới ở cấp cao hơn; và một cơ chế ghi nhận ngưỡng, chuyển pha, phát lộ cùng độ lệch mà không cần phán quyết đúng–sai.**

```text
Open Field
  → Identify Entity
  → Project Tượng/Lượng/Tính
  → Compose Relations
  → Build/Update Topology
  → Observe Accumulation and Flow
  → Mark Transition Candidate
  → Qualify Emergent Candidate
  → Evidence Gate
  → Re-project at an analysis level λ′
  → Trace without retroactive rewriting
```

Công thức tối giản:

```text
X⁽λ⁾
  ──Πₒ──→ P⁽λ⁾
  ──Compose──→ R⁽λ⁾
  ──Topology──→ G⁽λ⁾ₜ
  ──Δ-Observe──→ {TransitionCandidate, EmergentCandidate, Unresolved}
  ──Evidence Gate──→ X⁽λ′⁾
  ──Πₒ──→ …
```

**DD_3a_rs là khung ontology/architecture Research. `18×18` là lát cắt. Tượng–Lượng–Tính là hệ quy chiếu đệ quy. `λ` là cấp nổi lên tương đối. Topology là cấu trúc truyền lực. Lượng là quá trình. Ngưỡng là điều kiện cấu hình. Emergence là ứng viên có bằng chứng. Traceability là điều kiện bảo toàn toàn bộ vòng vận hành.**

## Appendix A — Quyết định giữ/sửa/để mở

| Hạng mục | Quyết định trong DD_3a_rs | Tầng |
|---|---|---|
| NxNxN là trường mở | Giữ và khóa khái niệm | `RESEARCH / CONCEPTUAL_LOCK` |
| Projection Tượng–Lượng–Tính | Giữ, làm rõ là projection epistemic/partial | `RESEARCH / CONCEPTUAL_LOCK` |
| 18×18 | Giữ như flattened relation/index slice | `RESEARCH / CONCEPTUAL_LOCK` |
| 3×3 | Giữ như interface taxonomy, không nhân cardinality | `RESEARCH / CONCEPTUAL_LOCK` |
| λ | Giữ như relative emergence-level index, không phải dimension | `RESEARCH / CONCEPTUAL_LOCK` |
| Topology | Đưa thành lớp chính thức và tách structural/current graph state | `RESEARCH / CONCEPTUAL_LOCK` |
| Snapshot/Dynamics/Transition/Emergence | Tách thành record categories độc lập | `RESEARCH / CONCEPTUAL_LOCK` |
| Identity/Boundary/Internal Structure | Giữ như điều kiện ứng viên emergence | `RESEARCH` |
| Q ≥ Θ | Chỉ giữ như ví dụ mô hình có thể calibration | `PLACEHOLDER` |
| Trọng số, decay, metrics | Chưa định nghĩa | `PLACEHOLDER` |
| S07/Kernel | Không thay đổi | `CORE UNCHANGED` |

## Appendix B — Provenance phản biện đa mô hình

Vòng phản biện dùng cùng một corpus gồm đề xuất `DD_3a_rs` do người dùng cung cấp, Proto v0.3 trước đó và quy tắc governance canonical hiện hành. Các reviewer được giao vai trò độc lập, không dùng đầu ra của reviewer này làm thẩm quyền cho reviewer khác.

| Reviewer | Model/route | Trạng thái | Đóng góp được dùng |
|---|---|---|---|
| Gemini | `gemini-3.1-pro-preview` qua proxy | Hoàn tất | Circularity relation/topology; background/context; time-stepping; 5 axioms; test topology-vs-summation |
| Claude | `claude-opus-4-7` qua proxy | Hoàn tất | Tách transition/emergence; identity/boundary/internal structure; partial observation; rule/state; snapshot/dynamics; runtime risks |
| OpenAI | `gpt-5.5` qua proxy retry | Hoàn tất | Kiến trúc hệ thống; ký hiệu `K`; schema relation cell; S07 boundary; layer/provenance; test vectors |
| Grok | Direct SDK và OpenRouter route | Chưa khả dụng | Direct route trả lỗi API key; OpenRouter route trả lỗi 401; không dùng đầu ra giả |
| DeepSeek | Direct API | Chưa khả dụng | API trả 402 Payment Required; không dùng đầu ra giả |
| Cohere | OpenRouter route | Chưa khả dụng | OpenRouter route trả lỗi 401; không dùng đầu ra giả |
| Perplexity | OpenRouter route | Chưa khả dụng | OpenRouter route trả lỗi 401; không dùng đầu ra giả |

Các thất bại kết nối được ghi rõ để bảo toàn provenance. Bản final không tuyên bố rằng các mô hình chưa trả lời đã đồng thuận.

## Appendix C — Governance statement

`DD_3a_rs` là bản **RESEARCH / CONCEPTUAL_LOCK**, không phải Kernel update. Nó không sửa bộ S07 canonical, không tạo mapping 5D → S07, không đưa công thức chưa calibration vào Core và không dùng lực làm confidence. Mọi triển khai operational sau này phải tạo profile, provenance, test vectors, uncertainty và gate riêng trước khi được xem xét ở tầng cao hơn.

## References

[1] [Proto v0.3 — Kính Chiếu Yêu / NxNxN](https://github.com/ntnguyen983-sketch/duyen-dich-engine/blob/research/dd3a-interpretation-library-v0.2/research_only/Kinh_Chieu_Yeu_NxNxN.docx)
[2] Duyên Dịch Canonical Governance Rules và Review Protocol — tài liệu nội bộ dùng làm authority cho ranh giới `CORE / COMPATIBILITY / RESEARCH / PLACEHOLDER` trong phiên này.
