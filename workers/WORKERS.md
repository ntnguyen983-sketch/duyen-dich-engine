# Worker Allocation — Duyên Dịch Chỉnh Lý

## Archivist
Gom và giữ nguyên tài liệu nguồn; lập timeline; không sửa nội dung lịch sử.

## Spec Worker
Đối chiếu các version, phát hiện trùng/mâu thuẫn, lập conflict log.

## Ontology Worker
Chuẩn hóa Entity/Observation/Interaction/Space/Time/State theo Anchor.

## Math Worker
Kiểm tra công thức, đơn vị, miền giá trị, biên và khả năng thực thi.

## Dynamics Worker
Kiểm tra flow, B(V), event_count, cycle_count, K_rep, rhythm và transition.

## Validation Worker
Xây test vectors, expected outputs, invariants và Ground Truth hooks.

## Code Worker
Viết Reference Implementation đúng Anchor; không phát minh công thức.

## Adapter Worker
Chuyển dữ liệu quẻ/hào và các nguồn quan sát khác vào ontology chung.

## Reviewer
Review độc lập; không tự ý thay đổi Anchor.

## Luật chung
Worker không được sửa Origin để làm cho code chạy. Khi phát hiện mâu thuẫn: ghi nhận → đối chiếu nguồn → đề xuất → quyết định kiến trúc/implementation ở tầng thích hợp.
