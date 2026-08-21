# Duyên Dịch v2.9.2-MERGED — Full Lineage Record

Nguồn: `DUYEN_DICH_MASTER_v2.9.2_MERGED_FREEZE.docx` và các nguồn v2.9.2 liên quan trong thư viện.
Trạng thái nguồn: CANDIDATE FREEZE, cần Gate/test trước absolute freeze. Trong Origin, tài liệu này là historical evidence, không được nhập nhầm thành Anchor v3.4.

## 1. Mục tiêu hợp nhất

v2.9.2-MERGED giữ Core Algebra của v2.9.2 và khôi phục pipeline/runtime/observation gồm DWL, DPKE, BEC Observation, Emergence, Spacetime, Forecast, Warning, Recommendation và Canonical Output. Nó phân biệt Input/Runtime, Deterministic Core, Observation/Emergence và Interpretation/Output.

## 2. Bất biến kiến trúc

Core Calculation deterministic và forward-only. Observation không sửa Quẻ Gốc, Hào Động, Nạp Giáp, Ngũ Hành hoặc Core đã chốt. BEC Density Core và BEC Observation là hai tầng. DWL là điều phối trọng số động, không đồng nhất với W matrix. ROM, Warning và Recommendation là ba lớp riêng. Mọi output phải truy nguyên về node, force, relation, time và actor.

## 3. Pipeline canonical lịch sử

S00 RAW INPUT → S01 NORMALIZE/FILTER/DATA INGESTION → S02 SIX-LINE OPERATOR → S03 INTERACTION FIELD/SIE + MATRIX CORE → S04 FIREWALL/SAFETY/CONSISTENCY → S05 DWL-0.1 → S06 DPKE → S07 SPACETIME + CALIBRATION + TEMPORAL PROJECTION → S08 OBSERVATION → EMERGENCE → ROM → WARNING → FORECAST → RECOMMENDATION → Canonical JSON/KIL/HASH/REPORT.

Mỗi stage nhận snapshot bất biến của stage trước; inconsistency tạo Diagnostic/Gate Failure thay vì tự sửa dữ liệu.

## 4. S00/S01

S00 yêu cầu Query Target, Timestamp t0, Location/GPS tùy bài toán, Signal Number/Seed, Quẻ Gốc, Hào Động, Quẻ Biến nếu có, Context. S00 không diễn giải và không tự sinh tín hiệu thiếu.

S01 chuẩn hóa timestamp ISO8601, thứ tự hào 1→6, Gốc/Biến, số hào động, Ngũ Hành/Địa Chi/Can Chi/node keys và provenance. Bất thường không được âm thầm sửa raw value.

## 5. S02 và Deterministic Matrix Core

NodeSpace = {N1…N6}_QuẻGốc ∪ {N7…N12}_QuẻBiến. W12×12 mô tả tương tác vị trí/Gốc-Biến/Ứng-Kề. Mpol 10×10 mô tả tương tác Ngũ Hành phân cực.

Vector lực lịch sử: F_i(t)=[f_net_out,f_BEC,L_Element]^T. Override cascade: Tam Hợp/Lục Hợp, Khắc Nhập, Khắc Xuất, Sinh Nhập, Sinh Xuất, Tỷ Hòa.

W_ij(τ)=B_ij×(1+αP_ij+βA_ij(t)/(A_max+ε))×F_norm, với α=0.15, β=0.20, ε=10^-6. F_norm phải có một định nghĩa canonical trong implementation.

MChi_Rel biểu diễn Lục Hợp, Tam Hợp Cục, Lục Xung, Tương Hình, Tương Hại, Tỷ Hòa. KTime xử lý Nguyệt Kiến/Nhật Kiến. MTransform xử lý Hóa Tiến, Hóa Thoái, Hóa Hồi Đầu Sinh, Hóa Hồi Đầu Khắc, Hóa Mộ, Hóa Tuyệt. Special operators gồm Tuần Không/Không Vong, Phục Thần/Phi Thần và Nhập Mộ/Mở Kho.

## 6. Force contract

ForceScore_i = Σ_j[W_ij(τ)×MChi_Rel(i,j)]×K_Nguyệt(i)×K_Nhật(i)×T_Transform(i). Sau đó F_i(t)=Vectorize(ForceScore_i,BEC_i,L_Element_i). Nguồn nhấn mạnh phải tách scalar ForceScore khỏi vectorization để tránh ambiguity.

## 7. DWL/DPKE

DWL sử dụng dynamic weight, persistence, topology và calibration cho observation/forward calculations nhưng không sửa Core constants và không feedback loop. DPKE là cầu nối xác định Core → node/force mapping → actor mapping → event candidate → evidence chain → interpretation-ready state.

## 8. BEC

BEC Density Core được mô tả bởi f_BEC(t)=σ(λΣ f_net_out(τ)e^{-γ(t−τ)}), với λ mặc định 0.35 và γ mặc định 0.08 trong nguồn. BEC Observation tách riêng các chiều Force State, Repetition, Accumulation, Quantity, Quality, Form, Persistence, Transition, Early Transition Risk và Actor Status. Chuỗi quan sát: Force → Repetition → Accumulation → Quantity → Quality → Form. Observation không được sửa f_BEC Core.

## 9. S07 lịch sử

Bộ trạng thái canonical: SÁT, NHIỄU, TÀ, ẨN, DƯỠNG, HỶ. Nguồn ghi điều kiện định lượng cho từng trạng thái và yêu cầu precedence canonical khi nhiều điều kiện cùng thỏa.

## 10. PhiSystem và Spacetime

Φ_System(N_i,E,t)=LCM(T_Node(12),T_Hành(5),T_Chi(12))=60 ticks. Spacetime Engine tạo temporal windows, actor delay, topology adjustment, spatial impact và calibration window; output Spacetime không được sửa Core snapshot.

## 11. ROM / Emergence / Warning

ROM ánh xạ KHÍ → Ngũ Hành + Lục Thân → Tam Tài → Quái/Quẻ. Force/Pattern/Emergence phân biệt DOMINANT, RECURRENT, PERSISTENT, EMERGING và SUPPRESSED. Warning phải có evidence chain node → force → condition → time → actor → source.

## 12. Implication / Forecast / Recommendation

Implication theo chuỗi FACT/STATE → PATTERN → MECHANISM → LIKELY EXPRESSION → IMPLICATION → CONFIDENCE/UNCERTAINTY. Forecast phải trả về window, direction, magnitude/range nếu tính được, actor, confidence và evidence chain. Recommendation chỉ chạy sau Warning/Forecast và gắn Risk Source → Controllable Actor → Available Action → Expected Effect → Constraint.

## 13. Các điểm còn phải giữ là lịch sử chưa đóng

Nguồn tự đánh dấu một số điểm cần verify trước freeze: L_Element mapping; MChi_Rel canonical conditions; scalar ForceScore → vector contract; S07 precedence; F_norm/calibration contract; DPKE mapping. Vì vậy Origin phải lưu chúng như unresolved historical decisions, không tự biến thành canonical facts.
