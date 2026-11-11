# 01 · Bắt đầu từ workload và quy tắc bất biến

[Mục lục](../INDEX.md) · Tiếp: [Kiến trúc lưu trữ](02-storage-architecture.md)

## Bài toán trước bảng dữ liệu

Một ERD đẹp chưa chứng minh hệ thống chịu được giờ cao điểm. Trước khi tạo bảng, mô tả các luồng: tạo khách hàng, đặt lệnh, giữ tiền, thanh toán, đối soát và báo cáo. Mỗi luồng phải có lượng dữ liệu đọc/ghi, tần suất, độ trễ mong muốn và yêu cầu nhất quán.

Ví dụ sau là giả định phục vụ bài tập, không phải sizing sản xuất:

| Luồng | Tải cần khảo sát | Điều không được sai |
|---|---|---|
| Rút tiền | TPS đỉnh, số request trên cùng tài khoản | Không chi vượt available balance |
| Callback ngân hàng | Burst, số lần gửi lại | Một sự kiện không tạo hai lần hạch toán |
| Tra lịch sử | Số dòng mỗi khách, trang sâu | Thứ tự ổn định, không lộ khách khác |
| EOD | Dung lượng/ngày, giờ hoàn tất | Tổng theo tiền tệ khớp nguồn đã chốt |

Một khách có hàng triệu giao dịch khác hẳn một triệu khách mỗi người có vài giao dịch. Độ lệch phân bố này ảnh hưởng index, plan và hot row.

## Phân loại invariant

- **Trong một dòng:** số tiền dương; ngày hết hạn sau ngày bắt đầu. Dùng `CHECK` và `NOT NULL`.
- **Giữa các dòng:** cùng tenant không trùng mã tài khoản. Dùng `UNIQUE`.
- **Giữa các bảng:** entry phải thuộc journal tồn tại. Dùng foreign key.
- **Trên nhiều thay đổi:** cập nhật balance và journal phải cùng commit. Dùng transaction và giới hạn đường ghi.
- **Giữa hệ thống:** ledger nội bộ và sao kê ngân hàng phải khớp. Cần workflow, idempotency và đối soát; một FK không giải quyết được.

Viết invariant theo câu có thể kiểm tra: “Sau mọi transfer đã commit, tổng balance hai ví cùng tiền tệ không đổi”. Tránh câu mơ hồ như “dữ liệu phải chính xác”.

## Chỉ số thiết kế cần có

Đo p50/p95/p99 latency, throughput, tỷ lệ lỗi, logical reads, CPU/query, lock wait, log bytes và tăng trưởng dung lượng. p95 của trung bình từng phút không phải p95 của tất cả request. Thu histogram hoặc dữ liệu request phù hợp để tính percentile.

Ghi SLO cùng điều kiện tải, ví dụ “p95 dưới 200 ms ở tải mục tiêu với dữ liệu 12 tháng”; đây là mục tiêu phải kiểm chứng, không phải lời hứa từ thiết kế.

## Bài tập

Chọn luồng rút tiền. Ghi năm invariant, xác định nơi thực thi và viết một trường hợp phá vỡ từng invariant. Gợi ý: hai request đồng thời, retry sau mất kết nối, callback đến muộn, sai currency, sai tenant. Đầu ra là bảng workload và bộ tiêu chí nghiệm thu, dùng lại ở capstone.
