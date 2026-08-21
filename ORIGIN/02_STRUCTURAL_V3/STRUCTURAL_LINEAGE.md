# STRUCTURAL DOMAIN — LINEAGE

## 1. Snapshot và cấu trúc 6 hào
Quẻ được sử dụng như snapshot của cấu trúc tại mốc quan sát. Các bản v2.3.6/v2.8.6 xây dựng lớp Structural quanh quẻ, hào, Ngũ hành và SIE.

## 2. Ngũ hành như toán tử
Trong lineage v2.3.6, Node Element Matrix là một vector 5 thành phần `[Kim, Mộc, Thủy, Hỏa, Thổ]`. Toán tử Sinh/Khắc tác động vào các biến động lực, trong khi SIE quản lý các chiều không gian, mật độ liên kết và pha thời gian.

## 3. Vectơ Khí
Lineage v2.3.6 mô tả vectơ mở rộng:

`V_Khi = [S, D, I, F, T]`

- S: Spatial Index.
- D: Directional Derivative.
- I: Interaction Density.
- F: Force / Momentum Scalar.
- T: Temporal Phase.

Đây là cấu trúc computational lineage, không phải một tuyên bố rằng mọi phiên bản tương lai phải giữ nguyên implementation.

## 4. SIE / topology
SIE được dùng để xây dựng cấu trúc mạng lưới tương tác không gian-thời gian. Structural domain chịu trách nhiệm cung cấp cấu trúc; dynamic layer xử lý diễn tiến trên cấu trúc đó.

## 5. Architecture boundary
Structural domain không tự diễn giải kết quả thành dự đoán. Các lớp runtime/evaluation/interpretation phải nằm sau các phép tính cấu trúc và giữ traceability.

## 6. Tài sản cần bảo tồn cho worker
Khi viết implementation mới, worker phải có thể tìm thấy:
- mapping quẻ/hào;
- constants và bảng toán tử;
- schema structural state;
- SIE topology contract;
- test vectors và provenance;
- phân biệt Core với Research.

## Provenance
Nguồn chính: `Duyên Dịch v2.3.6.pdf`, `Duyên Dịch mt v2.3.7_new.pdf`, `DUYÊN DỊCH MASTER SPECIFICATION v2.8.6-6line.pdf`, `DUYEN_DICH_MASTER_v2.9.2_MERGED_FREEZE.docx`.
