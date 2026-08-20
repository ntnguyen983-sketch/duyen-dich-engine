# Duyên Dịch v3.1

**Trạng thái:** Canonical integration specification — `CORE + COMPATIBILITY + RESEARCH + PLACEHOLDER`  
**Phiên bản:** `3.1.0`  
**Chủ thể quyết định:** Manus, có phản biện kỹ thuật Gemini hai vòng  
**Phạm vi:** Hợp nhất sáu phụ lục theo lớp kiến trúc, không gộp cơ học theo số hiệu version.

> **Tuyên bố canonical:** Duyên Dịch v3.1 là một đặc tả hợp nhất về kiến trúc, ranh giới logic, ký hiệu, ngôn ngữ ánh xạ, hợp đồng dữ liệu và quy trình vận hành. Những công thức hoặc tham số của v2.5, v2.8 và v2.9.2 chưa có tài liệu gốc trong các repository đã truy xuất không được coi là CORE; chúng được ghi nhận minh bạch ở `RESEARCH` hoặc `PLACEHOLDER` để chờ bổ sung bằng chứng.

## 1. Nguyên lý hợp nhất

Duyên Dịch v3.1 không xem v2.5, v2.8 và v2.9.2 là các bản vá tuần tự. Chúng là các lớp có chức năng khác nhau: lý thuyết động lực, mô hình trường, runtime số học, mapping ngữ nghĩa, hợp đồng dữ liệu và giao diện vận hành. Vì vậy, phiên bản 3.1 khóa **quan hệ phụ thuộc và ranh giới trách nhiệm**, nhưng giữ `source_version` của từng nguồn trong provenance để có thể truy vết ngược.

Tư duy Duyên Dịch xuyên suốt được giữ bằng sáu nguyên tắc. Hệ thống là phản ánh có điều kiện, không phải bộ tiên tri tất định; trạng thái luôn có thể vận động theo tick và điều kiện; Actor không được xem như một thực thể biệt lập; mọi kết luận phải quay về input, runtime, mapping, gate và provenance; thay đổi điều kiện phải có khả năng làm thay đổi kết quả; và mọi output phải phân biệt Data, Signal, Pattern, Inference, Action, uncertainty, confidence, warning và provenance.

## 2. Sáu lớp canonical

| Lớp | Tên canonical | Nguồn/nguồn gốc | Trạng thái v3.1 | Trách nhiệm |
|---|---|---|---|---|
| L1 | Theoretical Dynamics Reference | v2.5: Ψ, SDE, Bellman/MDP, phase operators | `PLACEHOLDER` khi thiếu phụ lục gốc | Chứa lý thuyết tham chiếu; không chạy trực tiếp trong Kernel mặc định |
| L2 | Coupled Field Model | v2.8: SL-DIF/BEC, coupled field, SIE, delay, pipeline | `RESEARCH` khi thiếu phương trình và calibration | Định nghĩa mô hình trường; chỉ được kích hoạt khi đạt gate và có provenance |
| L3 | Deterministic Runtime | v2.9.2: matrix/delay runtime; phần Snapshot/TickEngine hiện hữu | `RESEARCH` cho matrix/delay chưa xác minh; contract determinism là `CORE` | Tính toán số học xác định, phát raw measurements và runtime trace |
| L4 | S07 Semantic Mapping | S07 canonical mapping | `CORE` về firewall và failure behavior; profile/rules là `RESEARCH` nếu chưa phê duyệt | Dịch số liệu runtime thành trạng thái S07 qua profile hợp lệ |
| L5 | Canonical Data Contract | Canonical JSON/validation | `CORE` | Ràng buộc input/output, enum, provenance, uncertainty và gate result |
| L6 | Operations/UI Contract | UI/Operations v3.0_dd | `CORE` về boundary | Chỉ gọi API theo L5; không chứa logic mô phỏng hoặc mapping |

### 2.1. Đồ thị phụ thuộc

```text
L1 Reference → L2 Field Model → L3 Runtime → [COMPUTE–INTERPRETATION FIREWALL]
                                           → L4 S07 Mapping → L5 Data Contract → L6 Operations/UI
```

Mũi tên chỉ hướng dữ liệu và dependency được phép. L6 không gọi ngược L1–L4. L5 không gọi trực tiếp mô phỏng. L4 không ghi đè `raw_measurements`. L3 không phát nhãn S07. L2 không tự nhận trạng thái semantic. L1 chỉ là nền lý thuyết tham chiếu cho đến khi có phụ lục và kiểm định tương ứng.

## 3. Ký hiệu và từ vựng thống nhất

### 3.1. Ký hiệu runtime

| Ký hiệu | Ý nghĩa | Lớp | Quy tắc |
|---|---|---|---|
| `S_t` | Snapshot tại tick `t` | L3 | Trạng thái vật chất hóa đầy đủ, có thể replay |
| `I_t` | Input event tại tick `t` | L3/L5 | Dữ liệu đầu vào đã validate |
| `K` | Kernel transition operator | L3 | `S_(t+1) = K(S_t, I_t)`; deterministic khi cùng input/config |
| `R` | Runtime trace | L3 | Chuỗi snapshot và gate, không mang semantic label |
| `κ_t` | Vectơ Khí 5D raw | L3 | `κ_t = (κ.S, κ.D, κ.I, κ.F, κ.T)`; không phải trạng thái S07 |
| `f_net_out` | Lực/đại lượng lực do model phát | L2/L3 | Không được dùng trực tiếp làm confidence |
| `M` | `S07_MAPPING_PROFILE` | L4 | Phải có id, version, hash, domain, calibration và test vectors |
| `σ_t` | Trạng thái S07 semantic | L4 | Chỉ nhận sáu mã canonical hoặc `MAPPING_UNRESOLVED` ở boundary |
| `U` | Uncertainty | L3–L5 | Phân biệt measurement, model và semantic uncertainty |
| `C` | Confidence | L5 | Chỉ là tổng hợp có provenance; không đồng nhất với lực |
| `G_i` | Validation gate | L1–L6 | Mỗi gate có status và failure code |

Chữ `S` trong `κ.S` là một trục số của Vectơ Khí, không phải mã trạng thái S07. Văn bản phải viết `S07` khi nói về bộ trạng thái semantic và `κ.S` khi nói về thành phần Vectơ Khí để tránh nhập nhằng.

### 3.2. Bộ trạng thái S07 canonical

| Thứ tự | Tiếng Việt chuẩn | Mã serialize | Phân loại |
|---:|---|---|---|
| 1 | SÁT | `SAT` | `CORE` |
| 2 | TÀ | `TA` | `CORE` |
| 3 | NHIỄU | `NHIEU` | `CORE` |
| 4 | HỶ | `HY` | `CORE` |
| 5 | DƯỠNG | `DUONG` | `CORE` |
| 6 | ẨN | `AN` | `CORE` |

Chỉ sáu mã này được xuất hiện trong Kernel và canonical JSON. `DUONG` là mã serialize của **DƯỠNG**, không phải một trạng thái thứ bảy. Các nhãn lịch sử như `TỤ`, `HỢP`, `TÁN`, `LY`, `HIỆN` và `ÂN` chỉ được đọc bởi Compatibility Decoder với provenance đầy đủ; chúng không được tự động chuyển thành một mã S07 nếu chưa có profile tương đương được phê duyệt.

## 4. Compute–Interpretation Firewall

Firewall là ranh giới bắt buộc giữa L3 và L4. L3 chỉ phát `raw_measurements`, `field_state`, `runtime_trace`, `uncertainty` và `gate_results`. L3 không được phát `primary_label`, không được gọi decoder semantic và không được dùng văn bản diễn giải làm biến tính toán.

L4 chỉ được nhận output số của L3 cùng `S07_MAPPING_PROFILE`. L4 phải kiểm tra profile trước khi đánh giá rule. Nếu profile thiếu, sai hash, ngoài domain, chưa calibration hoặc không có test vectors, L4 trả `MAPPING_UNRESOLVED`, giữ nguyên raw data và ghi lý do vào `mapping_provenance`. L4 không được sửa Snapshot, lực, Vectơ Khí hoặc runtime trace.

Confidence được tính ở L5 từ các nguồn đã khai báo như gate status, mức hoàn chỉnh của provenance, measurement uncertainty và model uncertainty. `f_net_out` có thể được lưu như raw measurement nếu nguồn cho phép, nhưng luôn bị loại khỏi `confidence.inputs`; contract bắt buộc `f_net_out_excluded = true`.

## 5. Hợp đồng từng lớp

### L1 — Theoretical Dynamics Reference

L1 có thể chứa định nghĩa Ψ, SDE, Bellman/MDP và 12 phase operators khi phụ lục v2.5 được cung cấp. Trong bản 3.1 hiện tại, các nội dung đó là `PLACEHOLDER` vì chưa có file gốc, phương trình, miền biến và test vector trong các repository đã truy xuất. L1 không được chạy mặc định và không được đẩy nhãn semantic xuống L2–L6.

### L2 — Coupled Field Model

L2 là nơi đặt SL-DIF/BEC, coupled field, SIE, delay và pipeline trường. Bản 3.1 khóa **vị trí và contract** của L2, không khóa công thức BEC hoặc hệ số SL-DIF chưa có nguồn. Mọi tham số như hệ số tương tác, critical exponent, decay, delay kernel và boundary constant phải ghi classification `RESEARCH` hoặc `PLACEHOLDER`, cùng calibration plan.

Không được dùng công thức suy đoán như `I × F / (1 + epsilon)` để thay cho phương trình BEC gốc. BEC boundary chỉ được kiểm tra sau khi có định nghĩa nguồn; test boundary phải kiểm tra đúng các miền được tài liệu gốc quy định, trong đó tối thiểu phải chuẩn bị vector tại `R = 0.30` và `R = 0.10` theo governance, không được tự suy ra ý nghĩa vật lý từ việc clamp.

### L3 — Deterministic Runtime

L3 thực hiện transition trên Snapshot và phát dữ liệu số. Phần Snapshot/TickEngine hiện hữu chứng minh được nguyên tắc stateless history, rollback, replay và determinism ở mức implementation test. Matrix/delay runtime v2.9.2 chưa có trong các repository nên status của toán tử tương ứng là `RESEARCH`.

Pseudocode canonical ở mức contract là:

```text
validate(I_t)
S_next = K(S_t, I_t, runtime_profile)
assert tick(S_next) = tick(S_t) + 1
emit raw_measurements, field_state, runtime_trace, uncertainty, gate_results
assert no semantic_label in L3 output
```

Nếu L2 chưa đạt gate hoặc thiếu phương trình, L3 không được giả vờ tính field model; phải phát `RUNTIME_UNVERIFIED` cùng provenance và không tạo semantic inference từ phần thiếu đó.

### L4 — S07 Semantic Mapping

L4 sử dụng một profile đã đăng ký. Profile tối thiểu có `profile_id`, `version`, `sha256`, `domain`, `ordered_rules_or_model`, `parameter_calibration_status`, `test_vectors` và `review_decision_id`. Profile v3.1 hiện tại là `S07_CANONICAL_V31_UNRESOLVED`, không có rules và luôn trả `MAPPING_UNRESOLVED` cho đến khi có profile được phê duyệt.

Không được lấy trực tiếp các threshold trong `dd_engine1/semantic_thresholds.json` làm profile canonical, vì các threshold đó đang gắn nhãn lịch sử và chưa có provenance/calibration đủ điều kiện. Không dùng `eval()` trên chuỗi điều kiện; evaluator tương lai phải là declarative AST hoặc bộ toán tử whitelist, có giới hạn miền và test biên.

### L5 — Canonical Data Contract

L5 là điểm duy nhất chuẩn hóa JSON ra ngoài. Response tối thiểu gồm `contract_version`, `execution`, `raw_measurements`, `semantic_state`, `uncertainty`, `provenance` và `gate_results`. Schema chi tiết nằm tại `schemas/canonical_response.schema.json`.

`semantic_state.primary_label` chỉ nhận `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN` hoặc `MAPPING_UNRESOLVED`. Nhãn legacy, nhãn lạ, Unicode lỗi và mã không dấu sai không được pass Schema. Mọi output phải chứa `source_version`, `source_hashes`, `engine_commit`, record review, uncertainty và kết quả từng gate.

### L6 — Operations/UI

L6 chỉ render và điều phối theo L5. UI không được chứa công thức, threshold, mapping rule, gọi trực tiếp L2/L3 hoặc thay đổi canonical state. Gemini ở L6 chỉ được diễn giải canonical response; prompt phải nói rõ Engine/Core output là nguồn sự thật về số liệu và Gemini không được sửa, tính lại hoặc phủ định raw output.

## 6. Validation gates

| Gate | Điểm nối | Pass khi | Failure code |
|---|---|---|---|
| `GATE-1-THEORY-FIELD` | L1 → L2 | Có nguồn phương trình, biến, miền giá trị, version và test vectors | `PLACEHOLDER_THEORY` |
| `GATE-2-RUNTIME` | L2 → L3 | Matrix/delay deterministic, division safety đăng ký, BEC boundary có nguồn | `RUNTIME_UNVERIFIED` hoặc `RUNTIME_ERROR` |
| `GATE-3-INTERPRETATION` | L3 → L4 | Profile hợp lệ, hash đúng, trong domain, calibration/test vectors được phê duyệt | `MAPPING_UNRESOLVED` |
| `GATE-4-DATA` | L4 → L5 | JSON Schema, enum, provenance, uncertainty và type contract hợp lệ | `SCHEMA_INVALID` |
| `GATE-5-OPERATIONS` | L5 → L6 | UI/API chỉ truyền contract, không rò logic Kernel | `UI_CONTRACT_VIOLATION` |

Mỗi gate là một phần của output, không chỉ là log nội bộ. Khi gate fail, hệ thống không được làm im lặng lỗi hoặc thay bằng giá trị semantic đoán trước.

## 7. Classification và quyết định canonical

| Classification | Được phép | Không được phép |
|---|---|---|
| `CORE` | Enum, type contract, firewall, gate, failure behavior, determinism contract và invariant có căn cứ | Công thức chưa có nguồn, threshold chưa calibration, mapping profile tự bịa |
| `COMPATIBILITY` | Decoder dữ liệu cũ có source/version/hash và không sửa Kernel | Đưa nhãn legacy vào canonical JSON hoặc ép legacy thành mã mới |
| `RESEARCH` | Mô hình SL-DIF/BEC, matrix/delay, mapping rules, calibration, decay với test plan | Chạy mặc định hoặc trình bày như chân lý đã khóa |
| `PLACEHOLDER` | Điểm còn thiếu phụ lục, phương trình hoặc quyết định | Tự điền bằng suy đoán mà không gắn unresolved |

Các quyết định đã được giữ ở CORE sau hai vòng review là: sáu mã S07; firewall L3–L4; `MAPPING_UNRESOLVED` khi thiếu profile; cấu trúc năm gate; và determinism `S_(t+1) = K(S_t, I_t)`. Các đề xuất profile threshold cụ thể, công thức BEC suy đoán, epsilon cố định `1e-7` như invariant và status CORE cho matrix/delay runtime đều bị loại hoặc hạ tầng.

## 8. Test vectors tối thiểu

| ID | Trường hợp | Kỳ vọng |
|---|---|---|
| `TV-01` | Sáu mã `SAT`, `TA`, `NHIEU`, `HY`, `DUONG`, `AN` | Pass enum |
| `TV-02` | Nhãn legacy `TỤ` hoặc `ÂN` ở Kernel | Reject `SCHEMA_INVALID` |
| `TV-03` | `DƯỠNG` ↔ `DUONG` | Pass Unicode/serialize pair |
| `TV-04` | Vectơ Khí 5D không có profile | `MAPPING_UNRESOLVED` |
| `TV-05` | Profile sai SHA-256 | `MAPPING_UNRESOLVED` |
| `TV-06` | Profile ngoài domain | `MAPPING_UNRESOLVED` |
| `TV-07` | `w_resist = 0` trong DPKE | epsilon đã đăng ký hoặc controlled error; không crash, không coi epsilon là vật lý |
| `TV-08` | `w_resist` rất nhỏ | kiểm tra overflow/underflow và provenance |
| `TV-09` | `f_net_out` tại hai biên | không thay đổi quy tắc confidence |
| `TV-10` | BEC tại `R = 0.30` và `R = 0.10` | đánh giá theo phương trình gốc khi được cung cấp; hiện giữ unresolved |
| `TV-11` | Replay 60 ticks | hai lần chạy cùng input/config cho cùng hash Snapshot |
| `TV-12` | L3 output chứa `HY` hoặc `primary_label` | fail firewall |

Các test `TV-04`, `TV-05`, `TV-06` phải kiểm tra behavior unresolved, không được dùng threshold đoán. Các test BEC chỉ được pass canonical sau khi phụ lục v2.8 bổ sung phương trình và miền biên; trước thời điểm đó, gate phải ghi `RUNTIME_UNVERIFIED` hoặc `PLACEHOLDER_THEORY` tùy điểm thiếu.

## 9. Ma trận giữ, sửa, loại

| Nguồn/điểm | Quyết định | Phân loại | Lý do |
|---|---|---|---|
| Snapshot/TickEngine deterministic/replay | Giữ contract | `CORE` ở mức invariant | Có implementation và baseline tests |
| Vectơ Khí 5D `S,D,I,F,T` | Giữ như raw measurement implementation | `RESEARCH` cho ý nghĩa canonical | Có trong code, chưa đủ phụ lục model |
| Threshold legacy trong `semantic_thresholds.json` | Không dùng làm canonical profile | `COMPATIBILITY/RESEARCH` | Nhãn và provenance không đạt canonical |
| `eval()` trong semantic evaluator | Loại khỏi thiết kế v3.1 | Security/architecture fix | Không phù hợp evaluator khai báo an toàn |
| SDE/Bellman/12 phase operators | Giữ tên lớp, chưa khóa công thức | `PLACEHOLDER` | Không tìm thấy phụ lục v2.5 |
| SL-DIF/BEC | Giữ vị trí lớp, chưa khóa phương trình | `RESEARCH` | Không tìm thấy phụ lục v2.8 |
| Matrix/delay v2.9.2 | Giữ boundary runtime, chưa khóa toán tử | `RESEARCH` | Không tìm thấy phụ lục v2.9.2 |
| S07 profile threshold | Không tự tạo | `RESEARCH` | Thiếu calibration, hash, test vectors |
| UI/Operations | Giữ boundary theo L5 | `CORE` | Không được chứa logic tính toán |

## 10. Provenance và nhật ký review

Bản hợp nhất phải đi kèm `source_inventory.md`, `gemini_round1.json`, `gemini_round2.json`, `decision_log.md`, commit hash của repository và hash của các profile/schema. Gemini được ghi nhận là reviewer đề xuất/phản biện, không phải người quyết định canonical. Mọi bổ sung về sau phải tạo decision record mới, không sửa xóa provenance cũ.

## 11. Các điểm mở cần bổ sung

Để nâng v3.1 từ trạng thái hợp đồng kiến trúc lên runtime đầy đủ, cần bổ sung sáu phụ lục nguyên văn hoặc artifact có hash. Cụ thể là công thức và miền biến của Ψ/SDE/Bellman/12 phase operators; phương trình SL-DIF và BEC; toán tử matrix/delay và boundary; profile ánh xạ 5D → S07; calibration dataset/parameters; và API/UI contract đang được Operations phê duyệt. Khi một điểm được bổ sung, phải chạy lại gate liên quan, test vectors và vòng review hai bước.

## References

[1]: https://github.com/ntnguyen983-sketch/dd_engine1 "Repository dd_engine1 — runtime, mapping và UI hiện hữu"
[2]: https://github.com/ntnguyen983-sketch/dd_engine "Repository dd_engine — nguồn tối giản"
[3]: https://github.com/ntnguyen983-sketch/duyen-dich-engine "Repository duyen-dich-engine — repository trung tâm cho đặc tả v3.1"
[4]: ./canonical_vocabulary.json "Duyên Dịch v3.1 canonical vocabulary"
[5]: ./s07_mapping_profile_v31.json "S07 mapping profile registry — unresolved"
[6]: ./schemas/canonical_response.schema.json "Duyên Dịch v3.1 canonical response schema"
[7]: ./compatibility/legacy_decoder.json "Legacy compatibility decoder"
[8]: ./../../SOURCE_INVENTORY.md "Inventory nguồn và giới hạn bằng chứng"
[9]: ./../../gemini_round1.json "Gemini review round 1"
[10]: ./../../gemini_round2.json "Gemini review round 2"
