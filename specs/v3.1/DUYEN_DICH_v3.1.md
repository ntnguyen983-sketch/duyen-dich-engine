# DUYÊN DỊCH v3.1

**Đặc tả hợp nhất theo lớp — bản viết lại hoàn chỉnh**
**Phiên bản:** `3.1.0`
**Trạng thái:** `RELEASE_CANDIDATE — FULL SPECIFICATION`
**Ngày:** 2026-08-20
**Tác giả:** Manus AI
**Repository:** `ntnguyen983-sketch/duyen-dich-engine`

> **Tuyên bố phạm vi.** Duyên Dịch là hệ thống tính toán điều kiện, động lực trường và ánh xạ ngữ nghĩa có truy vết. Quẻ là snapshot của điều kiện tại `t0`, không phải tác nhân gây ra sự kiện. Runtime không phát biểu chắc chắn về thực tại, không tự gán tốt/xấu, không suy ý định chủ quan và không dùng diễn giải để sửa ngược trạng thái tính toán.

## 1. Mục tiêu và cách đọc đặc tả

Sáu phụ lục được hợp nhất theo lớp thay vì gộp tuần tự theo số version. v2.5 cung cấp lineage lý thuyết `Ψ`, `F0`, `ΔF`, SDE/Bellman/MDP và 12 temporal phase operators; v2.8.6/v2.8.7 cung cấp SL-DIF, SIE, Mpol, DWL, Vector Khí, BEC, Frozen Core và gates; v2.9/v2.9.1/v2.9.3 cung cấp topology 12 node, runtime, DPKE, delay, 60 ticks và canonical serialization. [1] [2] [3] [4] [5] [6] [7]

Bản này được viết lại hoàn chỉnh về **định nghĩa, behavior, công thức, pseudocode, guards, provenance, gates, JSON contract và test vectors**. `CALIBRATION_REQUIRED` không còn là chỗ trống: nó là một trạng thái có profile, điều kiện kích hoạt, kết quả khi chưa kích hoạt và test bắt buộc. Các nội dung chưa đủ căn cứ không bị biến thành CORE.

Mỗi assertion định lượng phải gắn `source_ref`, `source_version`, `source_document_id`, `profile_id` và `content_fingerprint`. Khi hai nguồn xung đột, v3.1 tạo hai named profiles; một execution chỉ chọn một profile và ghi lựa chọn vào context.

## 2. Thứ bậc nguồn và phân loại

| Cấp | Nguồn | Quyền sử dụng | Classification |
|---|---|---|---|
| Constitutional | v3.0.0, Frozen Core, Rev.A | ontology, firewall, direction, schema authority | `CORE` |
| Theory | v2.5.3–v2.5.6 | Ψ, SDE/Bellman, 12 phase operators | `REFERENCE` |
| Field | v2.8.6 Master, BEC Unified v2.8.7 | SIE, Mpol, DWL, Vector Khí, BEC, gates | `CORE` theo profile |
| Runtime | v2.9, v2.9.1, v2.9.1_new2, Py v2.9.3 | six-line, 12-node, force, RGS, DPKE, delay, ticks | `RUNTIME_EVIDENCE` |
| Decoder | v2.9.1_new2 và canonical v3.0.0 | S07 rules, enum, decoder contract | `CALIBRATION_REQUIRED` |
| Interface | UI/Operations v3.0_dd | render, session, API boundary | `INTERFACE_ONLY` |
| Historical | merged/full spec, legacy thresholds | migration và audit | `COMPATIBILITY` |

## 3. Sáu lớp canonical

### L1 — Dynamic Theory Reference

L1 giữ ontology, `Ψ`, `F0`, `ΔF`, potential surface, SDE/Bellman/MDP và 12 phase operators. L1 giải thích lineage và cách đặt câu hỏi động lực, nhưng không được gọi trực tiếp từ Core runtime. Một adapter L1 chỉ được kích hoạt khi có `theory_adapter_id`, miền biến, numerical guard, provenance và test vector.

### L2 — SL-DIF/BEC Field Mechanism

L2 xây dựng observed nodes, edges, topology, Mpol/SIE, Override Cascade, DWL, persistence, accumulation, Vector Khí, BEC density, emergence và recurrence. L2 không đọc semantic label và không nhận Output B để thay đổi lực.

### L3 — Deterministic Runtime

L3 thực hiện canonicalization, structural operators, 12-node graph, matrix lookup, force normalization, L2-RGS, DPKE, delay, tick state machine, replay và hash. L3 chỉ phát numeric state, runtime trace, uncertainty, profile IDs và gate results.

### L4 — Semantic Decoder

L4 là read-only mapping từ state sang S07. Profile lịch sử có rule đầy đủ nhưng mặc định `CALIBRATION_REQUIRED`; thiếu fingerprint/domain/test vectors thì trả `MAPPING_UNRESOLVED`. Nhiều rule match thì trả `MAPPING_AMBIGUOUS`; không phá overlap bằng thứ tự ngầm.

### L5 — Data Contract and Governance

L5 định nghĩa canonical JSON, enum, provenance, uncertainty, profile registry, compatibility decoder, errors, gates, hash và release manifest. L5 không tính lực, không chọn S07 và không sửa runtime state.

### L6 — Operations/UI

L6 gọi API theo L5, hiển thị Output A/B, warning, gate status, uncertainty và provenance. L6 không có formula, threshold hoặc mapping rule; không write-back vào L3/L4.

## 4. Bất biến và firewall

### 4.1. Frozen Core

Sau `S01`, hệ thống khóa `snapshot_id`, `root_bits`, `root_hexagram`, `moving_lines`, `initial_time`, `primary_actor`, `semantic_target` và `initial_context_hash`. `observe(state,evidence)` chỉ append evidence tại tick tiếp theo; không reset identity. Vi phạm là `CORE_IDENTITY_MISMATCH` và `HALT`.

### 4.2. Forward-only

```text
RAW → STRUCTURE → SNAPSHOT → FIELD → RUNTIME_STATE → DECODER → REPORT → ACTION
```

Cấm `Interpretation → Kernel`, `Decoder → Kernel`, `Outcome → Snapshot`, `UI → Runtime State` và `S12 → S00` trong cùng execution trace. [2] [5]

### 4.3. Semantic firewall

Trước `S10`, runtime chỉ dùng dữ liệu đã schema hóa: bits, topology, timestamp, profile, numeric evidence và context. Natural language được lưu như raw observation/provenance nhưng không được biến thành force, velocity, threshold, confidence hoặc S07.

### 4.4. Confidence firewall

`f_net_out` là raw measurement nếu profile cho phép; nó luôn bị loại khỏi `confidence.inputs`. `confidence_score` chỉ là tổng hợp có provenance từ gate status, measurement uncertainty, model uncertainty và completeness; contract bắt buộc `f_net_out_excluded=true`.

## 5. Pipeline S00–S11

| Stage | Tên | Input | Output | Quyền ghi | Gate |
|---|---|---|---|---|---|
| S00 | Raw Input | payload | raw record | tạo context | G1 |
| S01 | Canonical Core | raw record | locked identity | khóa Core | G2, G3 |
| S02 | Structural State | identity | `Q`, operators | derived structure | — |
| S03 | Topology | `Q`, relation profiles | 12-node graph | derived graph | G6 |
| S04 | Validation | graph, profiles | validated graph | gate metadata | G4, G6 |
| S05 | DWL/Force | graph, matrices | weights, force, Vector Khí | numeric | force guards |
| S06 | L2-RGS | coordinates | error, fit state | numeric | RGS guard |
| S07 | DPKE/Spacetime | force, resistance | velocity, delay, time | numeric | DPKE guard |
| S08 | Emergence | dynamic state | emergence state | numeric | threshold policy |
| S09 | BEC Observation | history, state | density, recurrence, projection | append only | no write-back |
| S10 | Knowledge Mapping | state, S07 profile | semantic result | read-only | G7 |
| S11 | Reporting | Output A/B | canonical JSON, SHA-256 | publish only | G5 |

Runtime API:

```python
initialize(raw_input):
    validate(G1, raw_input)
    identity = canonicalize_and_lock(raw_input)
    return Context(identity=identity, tick=0, history=[])

observe(context, evidence):
    assert_hash(context.identity)
    t_next = context.tick + 1
    e = normalize_evidence(evidence, effective_tick=t_next)
    derived = run_forward_pipeline(context.identity, e, t_next)
    return Context(identity=context.identity,
                   tick=t_next,
                   history=context.history + [derived])
```

## 6. Structural model

Với `Q=(b1,…,b6)`, `bk∈{0,1}`, `Q∈Z_2^6`. `root_code` và `transformed_code` là số 0–63 từ chuỗi bit canonical; moving lines là tập tăng dần trong `1..6`.

```text
M_k(Q) = flip bit k
P(Q)   = reverse(Q)
C(Q)   = (1-b1,…,1-b6)
H(Q)   = (b2,b3,b4,b3,b4,b5)
```

Operators chỉ biến đổi cấu trúc; mỗi output lưu `operator_id`, input hash và output hash; không được sinh semantic label.

Nếu có root và transformed state, `N1..N6` là root, `N7..N12` là transformed, `N(i+6)` là cặp tương ứng. Edges được tạo từ relation profile gồm `LUC_HOP`, `LUC_XUNG`, `TUONG_HINH`, `TAM_HOP`, `TUONG_HAI`, `TY_HOA`, `ROOT_TRANSFORM_PAIR` và `ADJACENT`. Mapping 6-line→12-node là `topology_profile_id`, không phải giả định không có nguồn.

## 7. Matrices, relation và field

### 7.1. Matrix registry

`M_POL` 10×10, `M_SIE` 3×3 và `M_FLUX` 5×5 được lấy nguyên bản từ Py v2.9.3; dữ liệu và SHA-256 nằm trong `runtime_profiles_v31.json`. Runtime chỉ đọc matrices từ profile, không tái tạo numeric values.

`M_POL` canonical:

```text
[ [ 1.0,  0.8,  1.5,  1.2, -2.0, -1.5, -1.0, -0.8,  0.5,  0.3],
  [ 0.8,  0.5,  1.2,  1.0, -1.5, -1.2, -0.8, -0.6,  0.3,  0.2],
  [ 0.3,  0.2,  1.0,  0.8,  1.5,  1.2, -2.0, -1.5, -1.0, -0.8],
  [-1.0, -0.8,  0.8,  0.3,  1.2,  1.0, -1.5, -1.2, -0.8, -0.6],
  [-0.8, -0.6,  0.5,  0.3,  1.0,  0.8,  1.5,  1.2, -2.0, -1.5],
  [-2.0, -1.5,  0.3,  0.2,  0.8,  0.5,  1.2,  1.0, -1.5, -1.2],
  [-2.0, -1.2, -1.0, -0.8,  0.5,  0.3,  1.0,  0.8,  1.5,  1.2],
  [-1.0, -0.8, -0.8, -0.6,  0.3,  0.2,  0.8,  0.5,  1.2,  1.0],
  [ 1.5,  1.2, -2.0, -1.5, -1.0, -0.8,  0.5,  0.3,  1.0,  0.8],
  [ 1.2,  1.0, -1.5, -1.2, -0.8, -0.6,  0.3,  0.2,  0.8,  0.5] ]
```

### 7.2. Override Cascade

`B_ij` lấy quan hệ đầu tiên trong thứ tự: `LUC_HOP/TAM_HOP +1.5`, `LUC_XUNG −2.0`, `TUONG_HINH −1.5`, `SINH_NHAP +1.2`, `SINH_XUAT −1.0`, `TY_HOA +1.0`, không khớp `0.0` kèm `NO_RELATION`. Edge lưu `relation_source`, `precedence_rank`, `profile_id`.

### 7.3. DWL và force

```text
W_ij = B_ij * (1 + α*P_ij + β*A_ij/(A_max+ε)) * F_norm
F_field_raw = Σ_ij(W_ij * D_ij)
F_norm = ||F_field_raw||/(4*N_edges+ε)
```

Profile `DWL-0.1-REV-A-FNORM` dùng `α=0.15`, `β=0.20`, `ε=1e−6`, precision 6. Nếu `A_max≤ε`, `QUARANTINE` với `DIVISION_BY_ZERO_RISK`. Nếu `N_edges=0`, trả `NO_EDGES` tại S05. `P_ij=N_active/N_observed`; `N_observed=0` trả `PERSISTENCE_DENOMINATOR_MISSING`, không suy mặc định.

Profile legacy `DWL-V293-CONTEXT-TIME` được giữ để replay tương thích, không chạy đồng thời với profile chính.

### 7.4. Vector Khí

`V_Khi=[S,D,I,F,T]`: `S=0/0.5/1` theo line zone 1–2/3–4/5–6; `D=ΔH*ψ∈[-1,1]`; `I=active_edges/max_edges`; `F=F_norm`; `T=tick mod 12`. Đây là measurement vector phi ngữ nghĩa. `D_ij`, `ψ`, `max_edges` và Element profile phải có trong context; thiếu profile trả `INPUT_PROFILE_MISSING`.

## 8. L2-RGS

Với `P,Q∈R^(n×d)`, center hai point sets, SVD Procrustes tìm `R`; nếu `det(R)<0`, sửa reflection. `t=mean(Q)−mean(P)R`. `E_rigid=mean(||P R+t−Q||²)` là CORE numeric output. `RIGID_FIT=clamp(1−E_rigid/E_threshold,0,1)` chỉ xuất khi `normalization_profile_id` hợp lệ; nếu không, trả `RIGID_NORMALIZATION_REQUIRED` và giữ raw error.

## 9. DPKE và Spacetime

```text
require 20 ≤ v_final ≤ 50
v_base = v_final/50
v_raw  = v_base + α*f_net − β*w_resist
v_i    = round(clamp(v_raw,0.1,2.0),6)
```

`v_final` ngoài miền trả `DPKE_DOMAIN_ERROR`; clamp phải ghi `CLAMP_APPLIED` và raw value.

Execution chọn một delay profile:

```text
DD-DELAY-2.9.2-TF1:
  delay_i = clamp(round((w_resist/v_final)*(1+μ_topology)
                         + simulation_ticks/v_i),0,12)

DD-DELAY-REV-A:
  delay_i = clamp(round(sum_i((1+μ_topology,i)/v_i)),0,12)
```

Profile chính là `DD-DELAY-2.9.2-TF1`; profile Rev.A là compatibility. `T_real=t0+τ_trigger*BASE_SCALE(context)*(50/v_final)`. `σ_time=|F_max−F_min|/(F_norm+ε)*(1−v_final/100)`. Azimuth dùng `[start,end)` và 315° thuộc sector kế tiếp.

## 10. BEC, emergence và observation

Profile `BEC-OBS-1`:

```text
acc_t = acc_(t−1)*exp(−γ)+f_net_out(t)
f_BEC = sigmoid(λ*acc_t)
```

`λ=0.35`, `γ=0.08`, reporting precision 4; đây là calibration profile. Emergence states:

| State | Điều kiện |
|---|---|
| `NO_EMERGENCE` | `I<θI ∧ F<θF` |
| `TRANSIENT_FORCE` | `I<θI ∧ F≥θF` |
| `LATENT_ACCUMULATION` | `I≥θI ∧ F<θF ∧ P≥θP ∧ A≥θA` |
| `STABLE_EMERGENCE` | `I≥θI ∧ F≥θF ∧ P≥θP ∧ A≥θA` |

Nếu threshold profile chưa active, trả `THRESHOLD_PROFILE_REQUIRED`; không dùng `0.75` ngầm. H1 Drain/Reserve là Research:

```text
D(t)=D0*exp(γ*ΩForce)*(1+η*FD_drag)
R(t+1)=max(0,R(t)−D(t)*Δt)
CircuitBreaker=(R(t)≤Threshold_stop)
```

H1 không mutate Core. `ΦSystem=LCM(12,5,12)=60` được giữ ở classification `RESEARCH`; runtime chỉ có thể phát cờ `SYNC_RESONANCE` khi `tick mod 60=0`, không tự phase shift, transmutation hoặc action. Cờ này là derived schedule marker, không phải bằng chứng vật lý hay semantic conclusion.

## 11. S07 mapping

Profile `S07-HIST-2.9.1-NEW2` có sáu rule đầy đủ:

| Code | Predicate |
|---|---|
| `DUONG` | `I≥0.70 ∧ D>0.2 ∧ F≥0.5` |
| `HY` | `I≥0.60 ∧ D>0.5 ∧ S≥0.5` |
| `AN` | `I*S<0.30 ∧ F≤0.4` |
| `NHIEU` | `|D|≤0.2 ∧ F>0.6 ∧ 0.3≤I≤0.6` |
| `TA` | `D<−0.3 ∧ F≥0.7 ∧ S<0.30` |
| `SAT` | `I<0.30 ∧ D<−0.5 ∧ F≥0.6` |

Resolver phải kiểm `profile_id`, SHA-256, domain, calibration status và test vectors. Không match trả `MAPPING_UNRESOLVED`; nhiều match trả `MAPPING_AMBIGUOUS`; chỉ một match mới trả code. Legacy `TỤ/HỢP/TÁN/LY/HIỆN/ÂN` chỉ compatibility.

## 12. Gates, errors và JSON

Gates gồm `G1_SCHEMA`, `G2_IDENTITY`, `G3_CORE_LOCK`, `G4_RESEARCH_CALIBRATION`, `G5_CANONICAL_HASH`, `G6_MATRIX_LOGIC_CONSISTENCY`, `G7_FIREWALL_DIRECTION`. Error codes gồm `SCHEMA_REJECTED`, `CORE_IDENTITY_MISMATCH`, `NO_EDGES`, `DIVISION_BY_ZERO_RISK`, `PERSISTENCE_DENOMINATOR_MISSING`, `DPKE_DOMAIN_ERROR`, `CLAMP_APPLIED`, `PROFILE_SELECTION_CONFLICT`, `PROFILE_HASH_MISMATCH`, `RIGID_NORMALIZATION_REQUIRED`, `THRESHOLD_PROFILE_REQUIRED`, `MAPPING_UNRESOLVED`, `MAPPING_AMBIGUOUS`, `SEMANTIC_LEAKAGE`, `PROVENANCE_INCOMPLETE` và `HASH_MISMATCH`.

Canonical JSON bắt buộc có `spec_version`, `execution_id`, `snapshot_id`, `runtime_profile_id`, `topology_profile_id`, `mapping_profile_id`, `source_refs`, `content_fingerprint`, `generated_at`, `runtime_tick`, `identity`, `dynamic_state`, `vector_khi`, `uncertainty`, `gate_results`, `error_codes`, `output_a`, `output_b`. Sort keys alphabetically, serialize UTF-8, rồi SHA-256. `output_a` là structural/runtime; `output_b` là observation/projection/semantic read-only.

## 13. Test vectors

| ID | Case | Expected |
|---|---|---|
| TV-01 | sáu mã canonical | Schema pass |
| TV-02 | legacy label trong Kernel | reject |
| TV-03 | Unicode `DƯỠNG`/`DUONG` | serialize/hash ổn định |
| TV-04 | thiếu S07 profile | `MAPPING_UNRESOLVED` |
| TV-05 | profile hash sai | `PROFILE_HASH_MISMATCH` |
| TV-06 | profile ngoài domain | `MAPPING_UNRESOLVED` |
| TV-07 | `N_edges=0` | `NO_EDGES`, dừng S05 |
| TV-08 | `A_max≤ε` | quarantine `DIVISION_BY_ZERO_RISK` |
| TV-09 | `v_final=15` | `DPKE_DOMAIN_ERROR` |
| TV-10 | `v_raw<0` | clamp 0.1, ghi audit |
| TV-11 | `F_norm=0` | sigma dùng ε, không NaN/Inf |
| TV-12 | BEC biên | chỉ evaluate khi threshold profile active |
| TV-13 | tick 60 | `SYNC_RESONANCE`, không action |
| TV-14 | `f_net_out` | không làm confidence |
| TV-15 | 60 tick replay | hash history giống nhau |
| TV-16 | decoder write-back | `SEMANTIC_LEAKAGE`, HALT |

## 14. Classification cuối

`CORE`: Frozen Core, forward-only, firewall, structural operators, deterministic contract, six enum, gates, error behavior, canonical JSON và M_POL/M_SIE/M_FLUX khi được pin bằng profile hash. `RESEARCH`: chu kỳ đồng pha 60 ticks, H1 Drain/Reserve và các causal/phase interpretations. `COMPATIBILITY`: legacy labels, legacy delay và old output. `CALIBRATION_REQUIRED`: S07 activation, threshold profile, BEC lambda/gamma, RGS normalization. `RESEARCH`: H1 Drain/Reserve, phase-shift interpretation và causal claims. Không còn placeholder không có behavior.

## References

[1]: https://docs.google.com/document/d/1T_VN8r5g2uKzT7vgL3Us4Fp-w2V_NNYRMTfA6PTHKsQ/edit "v2.5.3 Engine Specification"
[2]: https://docs.google.com/document/d/15TXjkKCeZx3hqLj1_vm_uzp6pc-jk95mFWUlbDSqacA/edit "v2.5.6 Master B"
[3]: https://docs.google.com/document/d/1LgvaWOndVxnBpi7p-6OPARZqJZ47TgmhB-Ii-b1losc/edit "v2.8.6 Master"
[4]: https://docs.google.com/document/d/112YN7bwAHHebKLa5Amd_fFtVkQ5079Z-AZQk3XzVHBM/edit "BEC Unified Logic v2.8.7"
[5]: https://docs.google.com/document/d/1JuxJGg6MQLsn5Jfz3wT4x2BQArtqjsCOzN_by2hNWLo/edit "v2.9 Architecture Overview"
[6]: https://docs.google.com/document/d/1nGmMp7Gg5PVc9QeYpmTr7HKIVpGXcBNqDQ52vrO3LX8/edit "Py v2.9.3 Full Runtime"
[7]: https://docs.google.com/document/d/180a8LwwV1OH3H2claoO89xih8h55lUY9tdbNgp0vTY0/edit "v2.9.1 NEW2"
[8]: https://docs.google.com/document/d/1OaIykatXspd9HlDds6WeBHtQC0P7DAv3DEc93wKi_Dg/edit "Duyên Dịch v3.0.0 Canonical"


### 12.1. Confidence audit bắt buộc

G7 phải quét toàn bộ cây `uncertainty.confidence.inputs`, `output_a`, `output_b` và các trường dẫn xuất. Output chỉ pass khi `f_net_out_excluded=true`, `f_net_out_found=false`, `audit_status=PASSED` và `scanned_paths` không rỗng. Phát hiện chuỗi `f_net_out` trong danh sách input confidence là `SEMANTIC_LEAKAGE` và chặn publication.
