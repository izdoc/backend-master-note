# 24 · SQL Server và PostgreSQL: không chuyển cú pháp máy móc

[Mục lục](../INDEX.md)

Mốc so sánh: SQL Server 2022/compatibility 160 và PostgreSQL 18. Các phiên bản khác cần xem tài liệu tương ứng; đây không phải bảng benchmark sản phẩm.

| Chủ đề | SQL Server | PostgreSQL |
|---|---|---|
| Đọc READ COMMITTED | Có thể dùng khóa hoặc RCSI theo cấu hình | MVCC, snapshot theo statement |
| READ UNCOMMITTED | Có semantics đọc chưa commit | Hành vi tương đương READ COMMITTED |
| Token optimistic | `rowversion` nhị phân do engine sinh | Thiết kế token ứng dụng hoặc dùng cơ chế hệ thống với hiểu biết giới hạn |
| Phân trang | `TOP`, `OFFSET/FETCH` | `LIMIT`, `OFFSET` |
| ID tự sinh | `IDENTITY`/sequence | Identity/sequence |
| Index có điều kiện | Filtered index | Partial index |
| Upsert | Chọn pattern transaction theo invariant | `INSERT ... ON CONFLICT` theo constraint |
| Maintenance phiên bản dòng | Version store tùy chế độ/cấu hình | VACUUM/autovacuum là phần quan trọng |

## Khác biệt có thể đổi tính đúng

PostgreSQL REPEATABLE READ dùng snapshot và có đặc tính khác với SQL Server REPEATABLE READ kiểu khóa. PostgreSQL SERIALIZABLE có thể abort giao dịch cần retry; SQL Server cũng có deadlock/khóa phạm vi tùy câu lệnh. Tên isolation giống nhau không đảm bảo cách thực thi giống nhau.

Không chuyển `WITH (UPDLOCK, HOLDLOCK)` thành `FOR UPDATE` rồi cho rằng khóa khoảng trống/missing row giống hệt. Khi chống insert trùng, vẫn cần unique constraint và một protocol được kiểm thử trên engine đích.

`timestamptz` biểu diễn instant và chuyển cách hiển thị theo session timezone; không tự lưu tên timezone gốc. Nếu hợp đồng cần giờ địa phương và zone quy tắc, lưu riêng thông tin cần thiết. PostgreSQL `numeric` cũng cần precision/scale được thiết kế theo sản phẩm.

## Chuyển hệ thống cần kiểm tra thêm

- Collation, case sensitivity, accent và unique trên chuỗi.
- NULL trong unique key và khả năng cấu hình theo phiên bản.
- Generated ID có thể có khoảng trống; không dùng làm số chứng từ pháp định liên tục nếu chưa có quy trình riêng.
- Decimal overflow, rounding, phép chia và cast.
- Date/time conversion, JSON, function và stored procedure.
- Query plan mới, statistics, index size và write amplification.
- Backup/PITR, replication, failover và công cụ trực vận hành.

`EXPLAIN ANALYZE` thực sự chạy statement; với DML phải hiểu side effect trước khi dùng. Không mang thói quen rebuild index định kỳ của hệ khác sang PostgreSQL để thay VACUUM.

**Bài tập:** di chuyển procedure giữ tiền. Nghiệm thu phải chạy đồng thời, retry, duplicate, failover simulation và đối soát; chỉ kiểm tra SQL compile chưa đủ.

Nguồn: [PostgreSQL isolation](https://www.postgresql.org/docs/18/transaction-iso.html), [routine vacuuming](https://www.postgresql.org/docs/18/routine-vacuuming.html), [numeric](https://www.postgresql.org/docs/18/datatype-numeric.html), [Microsoft locking guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver16).
