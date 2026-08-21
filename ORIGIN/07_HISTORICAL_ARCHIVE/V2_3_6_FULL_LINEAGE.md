# Duyên Dịch v2.3.6 — Foundational Lineage Record

Nguồn: `Duyên Dịch v2.3.6.pdf` trong thư viện tài liệu.
Mục đích: bảo toàn nội dung kiến trúc sơ kỳ có giá trị lineage, không coi bản này là authority hiện hành của DD-3A.

## 1. Tư tưởng và mệnh đề Kernel

v2.3.6 xác định Duyên Dịch không xem sự vật là thực thể cố định; sự vật trong mô hình là thành phần được quan sát trong một lát cắt của Dòng Duyên. Mô hình hướng tới xu hướng vận động của Dòng sau snapshot hiện tại và nhấn mạnh truy vết, vô ngã, vô thường và phụ thuộc điều kiện.

Mệnh đề Kernel tối cao của v2.3.6:
> Quẻ không luận sự việc. Quẻ chỉ định vị trạng thái. Điều được luận là Actor tại giao điểm Thiên – Địa – Nhân của Snapshot ấy. Duyên Dịch không dự đoán tương lai, mà đọc khuynh hướng vận động của Actor trong Dòng.

## 2. Architecture Freeze

Phạm vi đóng băng gồm Hiến pháp, Tiên đề, Ontology, PGL/OCG, kiến trúc phân tầng, Pipeline, Firewall và Traceability. Runtime/Tick Engine, Cost Function, Adapters, Plugins, APIs và SDKs được phép mở rộng nếu không vi phạm Core.

## 3. Nền tảng Đạo – Duyên – Dịch

- Đạo: quy luật vận hành của Duyên sinh và Vô thường.
- Duyên: mẫu hình cấu trúc ổn định của mạng điều kiện khi mật độ hiện hữu vượt ngưỡng; không tồn tại biệt lập.
- Dịch: vận động, biến đổi, tiến hóa hoặc tiêu biến của mẫu hình Duyên khi điều kiện nền thay đổi.

Hiến pháp v2.3.6 giữ 5 nguyên tắc: phản ánh phi tất định; vận động/vô thường; vô ngã; truy vết tuyệt đối; phụ thuộc điều kiện.

## 4. Ontology và các tiên đề lõi

Các tiên đề xác lập: Duyên là tập điều kiện hiện diện có khả năng tham gia Dòng; không Duyên nào hoàn toàn độc lập; tương tác các Khí nền sinh Vector Khí hệ thống; Lực, Hướng và Thế chi phối chuyển hóa; Dòng là vận động liên tục; Quẻ là Snapshot chứ không sinh ra hiện tượng; dự báo là đánh giá xu hướng chuyển hóa.

A1 giới hạn hiện hữu E trong [0,1]. A2 quy định suy hao động lượng trong hệ cô lập và giới hạn khi có input mới. A3 tách Khí khỏi ngữ nghĩa. A4 yêu cầu truy vết Quẻ → Khí → toán tử → đồ thị. A5 hạ các hệ số chưa chứng minh xuống hyperparameter cần thực chứng. A6 giữ biến đổi đồ thị trong Kernel Operator. A7 mô hình hóa Observer như Node đặc biệt. A8 yêu cầu công khai bất định của phép tái dựng. A9 tuyệt đối tách Reality/OCG/Snapshot/Inference. A10 đưa Actor Localization thành nguyên lý.

## 5. UK1–UK8

UK1 Semantic Independence; UK2 Primitive Completeness; UK3 Observer Equivalence; UK4 Information Preservation; UK5 Bidirectional Traceability; UK6 Fusion Neutrality; UK7 Decoder Isolation; UK8 Extensibility.

## 6. Pipeline v2.3.6

Chuỗi khái quát: Quan sát → Nhận diện Duyên → Mạng lưới Duyên → Tính Khí → Suy diễn tương tác [L,H,T] → Snapshot/Quẻ → Định vị Actor → Dự báo Trajectory.

7-layer pipeline gồm Input/Data, Ngũ Hành operator, Lục Hào/SIE topology, hợp nhất động lực-topology, Runtime/Actor Localization, Decoder/Mai Hoa mapping và Xu hướng/Cảnh báo/Định hướng.

Firewall S06 cách ly tầng Khí khỏi ngữ nghĩa. Emergent interaction yêu cầu đồng thời mật độ I ≥ 0.75, xung lực F ≥ 0.65 và persistence Δt ≥ 2 ticks.

## 7. Vector Khí và động lực

Vector Khí mở rộng: [S,D,I,F,T]. S là spatial index; D là directional derivative; I là interaction density; F là force/momentum scalar; T là temporal phase.

Ngũ Hành được dùng như toán tử động lực tác động lên D và F; S, I, T do SIE topology điều khiển.

Actor Localization gồm: xây Snapshot Thiên–Địa–Nhân; định vị Actor; xác định vector tác động; suy diễn S_t → S_{t+1}.

## 8. Phân pha thực địa

Ba pha: Ẩn/Tích lực → Khai lực → Dẫn lực. Ngưỡng F ≥ M_t là điểm kích hoạt chuyển pha; I ≥ 0.75 là điều kiện lan truyền.

## 9. Decoder S07 lịch sử

v2.3.6 dùng 6 trạng thái Khí: DƯỠNG, HY, ÂN, NHIỄU, TÀ, SÁT, với điều kiện hình học từ [S,D,I,F]. Đây là lịch sử quan trọng để truy nguyên các phiên bản S07 sau này; không mặc nhiên coi các nhãn này là lớp cuối cùng của Anchor v3.4.

## 10. Vai trò lineage

Bản v2.3.6 cung cấp nguồn gốc cho: snapshot thay vì tiên tri; Actor Localization; Thiên–Địa–Nhân; graph/condition model; forward dynamics; semantic isolation; traceability; và ý tưởng rằng hệ thống phân tích dòng vận động thay vì bản chất cố định của vật.
