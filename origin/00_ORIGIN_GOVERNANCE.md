# ORIGIN GOVERNANCE — Duyên Dịch

## Mục đích

Đây là quy ước quản trị kho ORIGIN. Nó không tuyên bố rằng một phiên bản hiện tại đã bao phủ toàn bộ lịch sử Duyên Dịch.

## Tiêu chuẩn "đủ"

Đủ được đánh giá theo **nội dung và khả năng truy nguyên**, không theo số lượng file.

Một miền nội dung chỉ được coi là đã thu thập đủ khi:
- có nguồn hoặc bằng chứng truy nguyên được;
- biết nó thuộc giai đoạn nào;
- biết nó là nguyên lý, định nghĩa, công thức, ví dụ, implementation, test, hay diễn giải;
- các mâu thuẫn đã được ghi nhận thay vì âm thầm hợp nhất;
- phần chưa có căn cứ được giữ nguyên trạng thái UNRESOLVED/RESEARCH.

## Bộ ba biểu đạt

**Định danh | Định lượng | Định tính** là cách biểu đạt quan sát, không phải ba bản thể cố định.

- Định danh: ký hiệu quy chiếu để theo dõi một luồng/điểm quan sát.
- Định lượng: những đại lượng có thể ghi nhận/tính toán.
- Định tính: mẫu hình được quy chiếu từ dữ liệu định lượng và bằng chứng; không tự biến thành phán quyết bản thể.

## Tính vô thường và bất nhị

Không gắn nhãn "bản chất cố định" cho N_i, trạng thái, quan hệ hoặc kết quả. Một nhãn nếu xuất hiện trong tài liệu lịch sử phải được giữ như **dữ liệu lịch sử/thuật ngữ nguồn**, không mặc nhiên trở thành ontology hiện hành.

## Ranh giới nguồn

- `CANONICAL`: đã được xác lập trong anchor/spec với nguồn truy nguyên.
- `DERIVED`: suy ra được từ canonical và có đường dẫn suy luận.
- `RESEARCH`: giả thuyết hoặc nghiên cứu.
- `IMPLEMENTATION`: cách thực thi.
- `COMPATIBILITY`: giữ để đọc/đối chiếu lịch sử.
- `UNRESOLVED`: chưa đủ bằng chứng.

Không được nâng `RESEARCH`, `IMPLEMENTATION` hoặc `COMPATIBILITY` thành canonical bằng cách đổi tên.

## Quy tắc hợp nhất

ORIGIN bảo toàn lineage. Các implementation tương lai được tách ra từ ORIGIN; implementation không được viết ngược để sửa lịch sử hoặc phát minh ontology mới mà không có quyết định kiến trúc riêng.