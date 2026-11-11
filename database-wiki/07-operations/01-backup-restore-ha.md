# 19 · Backup, restore và HA/DR

[Mục lục](../INDEX.md)

## Bắt đầu bằng RPO và RTO

RPO là mức mất dữ liệu chấp nhận được tính theo thời gian. RTO là thời gian mục tiêu để khôi phục dịch vụ. Nghiệp vụ đặt mục tiêu; DBA/architect chứng minh khả năng đạt bằng diễn tập có dữ liệu đại diện.

Backup thành công không chứng minh restore thành công. HA giúp duy trì sẵn sàng khi lỗi phù hợp với topology; replica có thể nhận cả lệnh xóa sai. DR còn bao gồm credential, key, DNS, job, ứng dụng, tích hợp và quy trình quyết định failover.

## SQL Server: hiểu chuỗi khôi phục

Full backup là nền; differential chứa thay đổi từ differential base; log backup cần recovery model và log chain phù hợp. Khi restore theo full recovery: restore full, differential thích hợp nếu dùng, rồi chuỗi log liên tiếp đúng mốc; giữ `NORECOVERY` đến bước cuối, sau đó `RECOVERY`. Point-in-time cần backup/log chain phủ thời điểm đích và điều kiện hỗ trợ.

Full backup không thay thế log backup. Tăng dung lượng log không xử lý nguyên nhân log không tái sử dụng. Kiểm tra `log_reuse_wait_desc`, transaction lâu, backup log và replication/availability liên quan.

Không dùng `REPAIR_ALLOW_DATA_LOSS`, xóa file log hoặc attach tùy tiện như bước đầu khi database lỗi. Thu bằng chứng, xác định storage/quyền/file và khả năng restore trước. Các thao tác có thể mất dữ liệu cần quy trình sự cố riêng.

## Diễn tập restore

1. Chọn ngẫu nhiên mốc hồi phục; lấy backup từ nơi thực sẽ dùng khi sự cố.
2. Khôi phục vào môi trường cô lập, có key/certificate và dung lượng phù hợp.
3. Đo thời gian download, restore, recovery, kiểm tra và đưa application lên.
4. Chạy kiểm tra integrity phù hợp, kiểm tra schema, smoke flow và tổng đối soát.
5. Kiểm tra user/login mapping, job, permission, secret, integration và cơ chế không gửi thông báo/chi tiền thật từ bản phục hồi.
6. Lưu bằng chứng RPO/RTO đạt được, lỗi và người chịu trách nhiệm sửa.

`RESTORE VERIFYONLY` hữu ích nhưng không thay một lần restore và kiểm tra nghiệp vụ. Không ghi lệnh restore với đường dẫn production vào script lab để chạy nhầm.

## HA và failover

Ghi synchronous/asynchronous mode, lag, điều kiện failover, cách client reconnect và khả năng mất dữ liệu theo topology. Sau failover phải kiểm tra write authority để tránh hai nơi cùng ghi. Retry phía ứng dụng vẫn cần idempotency vì trạng thái commit có thể không rõ khi mất kết nối.

Nguồn: [Microsoft — restore/recovery overview](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver16). Kế hoạch diễn tập là đề xuất vận hành; RPO/RTO không thể suy ra từ việc đã bật replication.
