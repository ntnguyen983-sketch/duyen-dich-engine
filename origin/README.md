# Duyên Dịch — ORIGIN / CHỈNH LÝ

Branch: `chinh-ly`

Đây là xưởng chỉnh lý và kho nguồn của Duyên Dịch. Không phải production engine.

## Quy tắc
- `origin/` giữ lịch sử và tài liệu nguồn; không viết lại lịch sử để làm đẹp.
- `anchor/` chứa Architectural Anchor hiện tại.
- `archive/` chứa các bản Spec/Implementation đã từng tồn tại.
- `workers/` mô tả nhiệm vụ cho các công nhân theo chức năng.
- Mọi mâu thuẫn được ghi nhận, không tự ý sửa Origin để ép khớp code.
- Implementation chỉ là nhánh thực thi; không được dùng code để định nghĩa ngược kiến trúc.

## Anchor hiện tại
DD-3A-v3.4-CANONICAL-ARCHITECTURAL-ANCHOR

Bộ ba biểu đạt cuối cùng:

**ĐỊNH DANH | ĐỊNH LƯỢNG | ĐỊNH TÍNH**

Định tính chỉ là mẫu hình quan sát được, phải quy chiếu về định lượng và bằng chứng; không gán bản thể cố định, không áp đặt tốt/xấu hay đúng/sai.

## Raw library
Danh mục nguồn được ghi tại `origin/LIBRARY_INVENTORY.md`. Các file nguồn vẫn được giữ nguyên trong GPT Library; branch này là kho chỉnh lý GitHub.