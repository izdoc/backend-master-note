# 20 · Monitoring và runbook sự cố

[Mục lục](../INDEX.md) · [Diagnostics read-only](../10-labs/05-diagnostics.sql)

## Quan sát cả trải nghiệm lẫn tài nguyên

| Lớp | Theo dõi | Ý nghĩa cần kiểm tra |
|---|---|---|
| Application | p95/p99, timeout, pool wait, retry | Chậm trước hay sau khi lấy connection? |
| Query | Duration, CPU, reads, executions, plan | Một query regression hay tăng tải? |
| Concurrency | Blocking chain, deadlock, transaction age | Ai giữ tài nguyên và từ bao giờ? |
| Storage | Latency đọc/ghi, free space, log growth | Thiếu dung lượng hay I/O chậm? |
| Data movement | Replica/CDC/outbox lag, job fail | Dữ liệu trễ đến mức nào? |
| Recovery | Backup age, log chain, restore drill | Có thể phục hồi đúng mốc không? |

Wait statistics là dấu vết chờ, không phải chẩn đoán tự động. Dùng delta trong khoảng sự cố thay vì chỉ tổng từ lúc startup. CPU cao có thể do query nhiều reads, compile, function hoặc tăng TPS; không kết luận thiếu CPU ngay.

## Runbook: API timeout nhưng CPU thấp

1. Xác định phạm vi ảnh hưởng và thời điểm bắt đầu; lấy request/correlation ID.
2. Kiểm tra pool wait, số connection và command timeout; đừng chỉ tăng timeout.
3. Thu active requests, blocking session, wait type và transaction age.
4. Xác định head blocker, SQL, application/job và owner. Session sleeping vẫn có thể giữ transaction; active-request DMV không liệt kê đủ mọi blocker.
5. Chọn giảm tải/dừng job hoặc kết thúc session theo bằng chứng. `KILL` có thể gây rollback dài, phải tính tác động.
6. Sau phục hồi, sửa transaction boundary hoặc query gây contention; xác nhận không có giao dịch trùng vì retry.

## Runbook: log hoặc disk đầy

Ghi dung lượng, file growth, recovery model và `log_reuse_wait_desc`. Tìm transaction lâu, log backup failure, replica/CDC bị trễ. Bổ sung dung lượng hoặc giải phóng theo quy trình phù hợp, đồng thời xử lý nguyên nhân. Không tự chuyển SIMPLE để “chữa cháy” mà bỏ qua yêu cầu point-in-time và log chain.

## Runbook: plan regression

So sánh plan history trong Query Store, tham số, statistics và thay đổi deploy. Force plan cũ chỉ khi đã biết nó hợp workload và có theo dõi/rollback. Ghi ngày hết hạn kiểm tra lại; đừng để workaround thành cấu hình vĩnh viễn không ai hiểu.

## Điều kiện cảnh báo

Ngưỡng phải gắn baseline và tác động: ví dụ backup age vượt RPO dự kiến, oldest unpublished outbox vượt freshness SLO, disk runway dưới thời gian đủ để bổ sung. “CPU > 80%” đơn lẻ dễ báo giả hoặc bỏ sót sự cố thật.

**Bài tập:** tạo timeline từ deploy đến timeout, phân biệt nguyên nhân với hậu quả. Đáp án có thể chỉ ra retry storm làm pool cạn là hậu quả sau blocking, chứ chưa chắc pool size ban đầu là nguyên nhân.
