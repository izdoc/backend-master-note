# Từ điển thuật ngữ

[Mục lục](INDEX.md)

| Thuật ngữ | Giải thích đơn giản |
|---|---|
| Invariant | Quy tắc dữ liệu phải luôn đúng trong phạm vi đã định nghĩa |
| Grain | Một dòng đại diện đơn vị nghiệp vụ nào |
| Cardinality | Số lượng hoặc quan hệ số lượng giữa các tập dòng |
| Normalization | Tổ chức quan hệ để giảm lặp và lỗi cập nhật |
| Denormalization | Tạo bản dữ liệu dẫn xuất có chủ đích để phục vụ đọc |
| PK / FK | Khóa định danh / khóa liên kết được engine kiểm tra |
| ACID | Atomicity, consistency, isolation, durability; không thay mọi rule nghiệp vụ |
| Isolation | Mức cách ly giữa các giao dịch đồng thời |
| MVCC | Cơ chế duy trì nhiều phiên bản dòng phục vụ concurrency |
| Write skew | Giao dịch cập nhật các dòng khác nhau nhưng phá invariant chung |
| Lost update | Cập nhật mới bị ghi đè bởi kết quả tính từ dữ liệu cũ |
| Blocking / deadlock | Chờ tài nguyên / vòng chờ cần được phá |
| Ledger / journal / entry | Sổ biến động / chứng từ / từng dòng hạch toán |
| Projection | Dữ liệu dẫn xuất tối ưu cho một cách đọc |
| Hold | Khoản tiền bị giữ, chưa được dùng vào mục đích khác |
| Idempotency | Lặp cùng thao tác vẫn chỉ có hiệu ứng nghiệp vụ được quy định |
| Reconciliation | So khớp dữ liệu giữa các nguồn theo mốc và quy tắc |
| Reversal | Bút toán đảo có liên kết chứng từ gốc |
| SARGable | Predicate thuận lợi cho tìm kiếm bằng access path phù hợp |
| Execution plan | Kế hoạch engine dùng để xử lý SQL |
| Logical reads | Số lần truy cập page qua buffer pool theo cách engine thống kê |
| Statistics | Thông tin phân bố phục vụ ước lượng query |
| Parameter sensitivity | Hiệu quả plan thay đổi theo phân bố giá trị parameter |
| Partition pruning | Loại partition không cần đọc khi xử lý query |
| Watermark | Mốc đã xử lý/đã biết dùng cho incremental pipeline |
| Outbox / inbox | Event cùng transaction nguồn / record chống xử lý lặp ở đích |
| CDC | Ghi nhận thay đổi dữ liệu để consumer đọc tiếp |
| RPO / RTO | Mục tiêu mức mất dữ liệu / thời gian hồi phục |
| HA / DR | Sẵn sàng cao / phục hồi thảm họa |
| SLO | Mục tiêu đo được về chất lượng dịch vụ |
| p95 / p99 | 95% / 99% mẫu không vượt giá trị này trong tập đo |
| PITR | Khôi phục đến một thời điểm được hỗ trợ bởi chuỗi backup/log |
| Legal hold | Yêu cầu giữ lại dữ liệu chỉ định, tạm ngăn xóa theo lịch |
