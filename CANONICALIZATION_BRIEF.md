# Duyên Dịch v3.1 — Canonicalization Brief

## 1. Quyết định kiến trúc

Duyên Dịch v3.1 được tổ chức theo lớp, không theo thứ tự version. Luồng phụ thuộc chuẩn là:

```text
UI/Operations (L6)
        ↓ schema-validated API
Canonical Data Contract (L5)
        ↓ typed data only
S07 Semantic Mapping (L4)
        ↓ raw runtime measurements only
Deterministic Matrix/Delay Runtime (L3)
        ↓ field model
SL-DIF/BEC Coupled Field Model (L2)
        ↓ theory/reference boundary
SDE/Bellman/MDP and phase operators (L1, reference only)
```

Mỗi lớp chỉ được phụ thuộc vào lớp thấp hơn thông qua contract đã version hóa. Lớp 6 không được chứa công thức; lớp 5 không được gọi trực tiếp mô phỏng; lớp 4 không được sửa số liệu runtime; lớp 3 không phát nhãn ngữ nghĩa; lớp 1 không chạy trong Kernel mặc định của v3.1.

## 2. Compute–interpretation firewall

Firewall đặt giữa L3 và L4. L3 chỉ phát `raw_measurements`, `field_state`, `runtime_trace`, `uncertainty` và `gate_result`. L4 nhận các trường số đó cùng một `S07_MAPPING_PROFILE` hợp lệ và phát `semantic_state`. Nếu không có profile hợp lệ, L4 phải trả `MAPPING_UNRESOLVED`, không ép Vectơ Khí 5D thành nhãn.

`force`, `f_net_out`, `field_state`, `uncertainty` và `confidence` là các khái niệm khác nhau. Không được suy ra `confidence_score` trực tiếp từ `f_net_out`. Confidence chỉ có thể là một trường tổng hợp có provenance về các level/gate đã dùng.

## 3. Từ vựng canonical

Trong Kernel, S07 chỉ dùng sáu trạng thái theo đúng thứ tự và mã:

| Văn bản | Mã serialize | Phân loại |
|---|---|---|
| SÁT | `SAT` | CORE |
| TÀ | `TA` | CORE |
| NHIỄU | `NHIEU` | CORE |
| HỶ | `HY` | CORE |
| DƯỠNG | `DUONG` | CORE |
| ẨN | `AN` | CORE |

Các nhãn lịch sử `TỤ`, `HỢP`, `TÁN`, `LY`, `HIỆN`, `ÂN` không vào Kernel, JSON canonical hoặc công thức. Nếu cần đọc dữ liệu cũ, decoder phải gắn `source_version`, `source_hash`, `compatibility_rule_id` và provenance; decoder không được thay đổi canonical state.

## 4. Phân tầng ngữ nghĩa

Dữ liệu đi theo chuỗi `Data → Signal → Pattern → Inference → Action`. `Data` là input quan sát và metadata; `Signal` là đại lượng do runtime tính; `Pattern` là cấu trúc/quan hệ đã kiểm định; `Inference` là semantic S07 có mapping profile; `Action` là tư vấn vận hành, không quay ngược thành input toán học.

## 5. Các gate bắt buộc

| Gate | Điểm nối | Điều kiện tối thiểu | Khi thất bại |
|---|---|---|---|
| `GATE-1-THEORY-FIELD` | L1 → L2 | Nguồn công thức, định nghĩa biến, miền giá trị và test vector được ghi | `PLACEHOLDER` hoặc `RESEARCH`, không chạy mặc định |
| `GATE-2-RUNTIME` | L2 → L3 | Ma trận/delay deterministic, biên BEC và division safety đã đăng ký | `RUNTIME_UNVERIFIED` |
| `GATE-3-INTERPRETATION` | L3 → L4 | Profile S07 có id/version/hash/domain/calibration/test vectors | `MAPPING_UNRESOLVED` |
| `GATE-4-DATA` | L4 → L5 | JSON Schema, enum, provenance, uncertainty và source/version hợp lệ | `SCHEMA_INVALID` |
| `GATE-5-OPERATIONS` | L5 → L6 | API chỉ nhận/trả contract, không rò logic Kernel | `UI_CONTRACT_VIOLATION` |

## 6. Invariants khóa ở v3.1

Các bất biến CORE gồm: Kernel chỉ chấp nhận sáu mã S07; Unicode tiếng Việt và mã serialize phải nhất quán; mọi output có provenance, source/version, uncertainty và gate result; runtime deterministic với cùng snapshot/input; không dùng nhãn legacy trong Kernel; không dùng lực làm confidence; không map vector 5D nếu thiếu profile; DPKE không chia cho 0; epsilon chỉ là safety parameter đã đăng ký; và tham số chưa calibration không được ghi là invariant.

## 7. Khoảng trống phải giao Gemini phản biện

Các tài liệu gốc v2.5, v2.8 và v2.9.2 không có trong các repository hiện đã truy xuất. Do đó Gemini được phép đề xuất cấu trúc, test plan, pseudocode và câu hỏi cần khóa cho SDE/Bellman, SL-DIF/BEC, matrix/delay runtime, profile S07, schema và UI contract; Gemini không được tự nâng các đề xuất đó thành CORE. Mọi đề xuất thiếu công thức gốc, calibration hoặc test vector phải giữ ở `RESEARCH` hoặc `PLACEHOLDER`.

## 8. Chuẩn provenance

Mỗi quyết định phải có `decision_id`, `classification`, `source_refs`, `source_hashes`, `review_model`, `review_round`, `assumptions`, `test_vectors`, `uncertainty`, `gate_result` và `decided_by`. Artifact Gemini phải lưu nguyên prompt, output và quyết định giữ/sửa/loại.
