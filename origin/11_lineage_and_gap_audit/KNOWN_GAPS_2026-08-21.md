# KNOWN CONTENT GAPS — 2026-08-21

Đây là gap audit nội dung, không phải tuyên bố hoàn tất.

## Đã có bằng chứng trong workspace GitHub

- Duyên Dịch v3.1 full rewrite và các artifact review.
- Anchor DD-3A v3.4.
- Runtime v3.1 và tests.
- Source inventory và provenance artifacts.
- Gemini review artifacts.
- Các nguyên tắc phân tầng structural/dynamic đã được ghi nhận.

## Chưa đủ bằng chứng nguyên văn trong workspace hiện tại

Theo SOURCE_INVENTORY, các bản/khối lịch sử được nhắc tới như v2.5, v2.8, v2.9.2, SL-DIF, Bellman, SDE chưa xuất hiện nguyên văn trong các repository đã được inventory tại thời điểm ghi nhận. Vì vậy chúng **không được tái dựng bằng trí nhớ hoặc suy đoán**.

## Nội dung cần tiếp tục thu thập

1. Các tài liệu sơ khai về Đạo Duyên Dịch.
2. Toàn bộ lineage từ các bản sơ khai tới các spec v2.x.
3. Bản gốc của các công thức v2.x/v2.8/v2.9.x nếu tồn tại ngoài GitHub hiện tại.
4. Tư liệu hình thành S01–S08 và các pipeline/gate lịch sử.
5. Nguồn gốc của các toán tử Vectơ Khí 5D, SIE, DWL, DPKE, Spacetime và BEC.
6. Nguồn gốc và tiến hóa của S07 cùng các profile mapping.
7. Test vectors và ground-truth cases tương ứng với từng công thức.
8. Các bản reference implementation trước v3.1 và các hardcode/simplification từng bị phát hiện.
9. Các tài liệu giải thích sự chuyển đổi từ mô hình quẻ/hào sang N(n).
10. Các ví dụ thực địa và kết quả đối chiếu dùng để calibrate.

## Quy tắc xử lý gap

Không điền gap bằng công thức mới. Nếu chưa có nguồn: `UNRESOLVED`. Nếu chỉ có diễn giải: `INTERPRETATION_ONLY`. Nếu chỉ có code: `IMPLEMENTATION_ONLY`. Nếu có test nhưng thiếu công thức gốc: `EVIDENCE_WITHOUT_SOURCE_FORMULA`.

Gap chỉ được đóng khi có bằng chứng nội dung đủ để truy nguyên và kiểm tra.