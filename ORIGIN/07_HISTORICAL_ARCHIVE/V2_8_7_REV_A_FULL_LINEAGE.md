# Duyên Dịch v2.8.7+ Rev.A — Full Lineage Record

Nguồn: `VERSION 2.8.7+ REV.A.pdf`.
Vai trò: cầu nối từ Frozen Core v2.8.6 sang Research/Calibration architecture; không phải Anchor v3.4 authority.

## 1. Core philosophy

Đạo = quy luật vận hành của Duyên sinh và Vô thường. Duyên = mẫu hình cấu trúc ổn định của mạng điều kiện khi mật độ hiện hữu vượt ngưỡng. Dịch = biến đổi của mẫu hình khi điều kiện nền thay đổi. Quẻ là Snapshot tại t0, không phải nguyên nhân tất định. Không gán bản chất cố định cho node.

## 2. Kiến trúc quyền lực

Frozen Core v2.8.6 giữ Core Identity, Validation và invariant structural operators. Research Layer v2.8.7+ chứa tham số/giả thuyết chưa thực chứng và bắt buộc có calibration status. Runtime deterministic: cùng Canonical Input + Research Profile + Runtime Policy phải cho cùng kết quả. Forward-only: evidence mới có hiệu lực ở tick sau; không feedback ngược vào state đã khóa. Core Lock cấm sửa cấu trúc sau khi Canonical State được xác lập.

## 3. Từ điển hệ thống

DCGF = Computational Graph; DWL = Dynamic Weight Layer; PGL = Primitive Graph Language; OCG = Observed Conditions Graph; SIE = State Interaction Environment; KIL/UKES = Knowledge Integration; B_ij = base topology weight; P_ij = persistence index; A_ij(t) = accumulated weight; Vector Khí = [S,D,I,F,T]; Ω_Force = tổng động lượng; E_rigid/F_rigid = rigid fit error/score; T_real và σ_time = temporal projection; DPKE = Phase Kinematics; BEC = Resource Dynamics.

## 4. A0–A12 và UK1–UK8

A0 nhị nguyên; A1 E∈[0,1]; A2 động lượng không tự tăng nếu không có External Injection; A3 Khí là hình học/quan hệ; A4 semantic interpretation phải tách và truy vết qua Quẻ → Khí → toán tử → đồ thị; A5 tham số chưa thực chứng phải thành Research Parameter và Calibration; A6 chỉ Kernel Operator được biến đổi graph trong tick; A7 Observer tạo Evidence nhưng không mutate Core; A8 inverse mapping phải công khai σ; A9 tuyệt đối tách Reality/OCG/Snapshot/Inference; A10 biến không đo lường minh bạch bị cấm trong công thức; A11 thuộc tính Actor định tính và định lượng phải lưu riêng; A12 output định lượng phải qua Calibration Protocol.

UK1–UK8 tiếp tục nguyên tắc semantic independence, primitive completeness, observer equivalence, information preservation, bidirectional traceability, fusion neutrality, decoder isolation và extensibility.

## 5. Pipeline S00–S08

S00 Raw Input → Core Identity → S01 Normalize → Canonical State → Core Lock → S02–S06 Processing → S07 Emergence → S08 Output.

S00 envelope gồm snapshot_id, timestamp ISO8601, input channel, event type, context scope, runtime tick, parent snapshot; raw payload gồm hexagram data và signal components. S01 chuẩn hóa modulo quái/hào, dữ liệu thời gian, identity và provenance.

## 6. Structural / mathematical core

Quẻ được biểu diễn như vector 6 bit. Các operator gồm Động Hào (flip bit), Biến Quẻ Toàn Phần, Tông Quẻ và Hỗ Quẻ. Thiên Can dùng tọa độ 3D; Địa Chi dùng modulo Z12 và boundary convention 315° để tránh overlap.

Vector Khí [S,D,I,F,T]: Spatial, Directional, Interaction, Force, Temporal. Interaction Engine chạy qua graph → tensor → projection → Vector Khí → tick → ứng kỳ.

## 7. DWL và L2-RGS

W_ij(τ)=B_ij·K_context(τ)·K_interaction(τ)·K_time(τ). Persistence P_ij=N_active/N_observed. Accumulation A_ij(t)=ΣW_ij(τ). Force normalization: F_field_raw=ΣW_ij·D_ij; F_max=4·N_edges; F_norm=||F_field_raw||/F_max. Rigid fit error E_rigid=(1/n)Σ||R(p_i)-q_i||²; F_rigid=1-normalize(E_rigid). L2-RGS không thay tọa độ gốc.

## 8. DPKE và Spacetime

v_i=Clamp(v_base+αF_net,i−βW_resist,i,v_min,v_max), với α=0.15, β=0.20, v_base=v_final/50. Delay_i=Clamp(Round(Σ(1+μ_topology,i)/v_i),0,12). σ_time phụ thuộc Fmax/Fmin/Fnorm và v_final. T_real=t0 + τ_trigger×BASE_SCALE×(50/v_final), với v_final ∈ [20,50].

## 9. BEC Research Layer

Drain D(t)=D0·e^(γΩ_Force)·(1+ηFD_B→A). Reserve thỏa dR/dt=−D+S_recharge. Autonomous Circuit Breaker kích hoạt khi R≤Threshold_stop. H1 giả thuyết over-drain; H1b efficiency paradox; H1e autonomous circuit break.

## 10. Firewalls và validation

Anti-Semantic Leakage chặn dữ liệu ngữ nghĩa/cảm xúc khỏi tầng tính toán trước S07. Gates: G1 schema/required fields; G2 identity/range; G3 canonical state/core lock; G4 research params/calibration; G5 output completeness/hash. STOP kết thúc interaction chain hiện tại, không reset Core Identity.

## 11. Emergence và output

Các trạng thái emergence gồm NO_EMERGENCE, TRANSIENT_FORCE, LATENT_ACCUMULATION, STABLE_EMERGENCE theo I, F, P, A. Symbolic decoder dùng 6 trạng thái Khí. Canonical JSON hash bằng SHA-256, keys alphabetically sorted; Research precision 4 decimals, L2-RGS 6 decimals.

## 12. Reconciliation và legacy

Rev.A đối soát precision v2.8.6/v2.8.7, số lượng axioms, BEC Research Layer và override cascade. Legacy invariants H,L,K,T = Hào/Vị trí, Lực/Cường độ, Khí/Vượng suy, Thời/Spacetime. Rev.A ghi nhận việc tách nội suy hao khỏi External Injection, khôi phục 315° convention và thống nhất DPKE/BEC Dynamics.

## 13. Vai trò lineage

Bản này là nguồn quan trọng cho lineage của Frozen Core, DWL, SIE, DPKE, BEC, Spacetime, Firewall, deterministic forward-only, calibration và provenance. Các thành phần Research phải được giữ nguyên trạng thái nghiên cứu khi biên soạn Origin; không được nâng cấp thành fact chỉ vì xuất hiện trong một spec cũ.
