# Nguồn tham khảo và cách cập nhật

[Mục lục](INDEX.md)

Rà soát ngày **11/11/2026**. Wiki là nội dung biên soạn và ví dụ tự thiết kế; không chép lại nguyên tài liệu hãng. Các nguồn sau dùng để đối chiếu hành vi engine. Thiết kế ledger, rule sản phẩm, workshop và runbook cần được review theo hệ thống thực tế.

| Chủ đề | Nguồn chính thức | Dùng khi |
|---|---|---|
| Index | [SQL Server index design guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver16) | Kiểm tra cấu trúc, key, INCLUDE và trade-off |
| Concurrency | [Locking and row versioning](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver16) | Isolation, khóa và versioning |
| Decimal | [decimal/numeric](https://learn.microsoft.com/en-us/sql/t-sql/data-types/decimal-and-numeric-transact-sql?view=sql-server-ver16) | Precision, scale, chuyển đổi |
| Concurrency token | [rowversion](https://learn.microsoft.com/en-us/sql/t-sql/data-types/rowversion-transact-sql?view=sql-server-ver16) | Token không phải ngày giờ |
| Statistics | [Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver16) | Histogram và estimate |
| Query history | [Query Store best practices](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?view=sql-server-ver16) | Theo dõi plan/runtime |
| Plan variants | [PSP optimization](https://learn.microsoft.com/en-us/sql/relational-databases/performance/parameter-sensitive-plan-optimization?view=sql-server-ver16) | Tính năng phụ thuộc compatibility |
| Hint | [Query Store hints](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-hints-best-practices?view=sql-server-ver16) | Workaround và đánh giá lại |
| Partition | [Partitioned tables/indexes](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver16) | Alignment và lifecycle |
| Encryption | [TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16) | Mã hóa lưu trữ và key recovery |
| Audit | [SQL Server Audit](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine?view=sql-server-ver16) | Audit engine |
| Recovery | [Restore and recovery overview](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/restore-and-recovery-overview-sql-server?view=sql-server-ver16) | Restore chain và scenario |
| CDC | [About CDC](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-ver16) | Capture, cleanup, change tables |
| Messaging | [Transactional outbox example — Cosmos DB](https://learn.microsoft.com/en-us/azure/architecture/databases/guide/transactional-out-box-cosmos) | Nguyên lý atomic business/event write |
| EF Core | [Efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying) · [Transactions](https://learn.microsoft.com/en-us/ef/core/saving/transactions) | Kiểm tra theo EF/provider đang dùng |
| PostgreSQL | [Isolation](https://www.postgresql.org/docs/18/transaction-iso.html) · [numeric](https://www.postgresql.org/docs/18/datatype-numeric.html) · [partitioning](https://www.postgresql.org/docs/18/ddl-partitioning.html) · [vacuum](https://www.postgresql.org/docs/18/routine-vacuuming.html) | Đối chiếu khác biệt với SQL Server |

## Quy trình duy trì

1. Khi đổi engine major version, compatibility, provider hoặc tính năng, mở lại tài liệu đúng phiên bản và release note liên quan.
2. Ghi thay đổi vào PR với bài bị ảnh hưởng, hành vi trước/sau và kết quả kiểm chứng.
3. Chạy lại lab trên engine thực; lưu build, database options, output và evidence concurrency/performance.
4. Cập nhật mốc rà soát chỉ cho phần thực sự đã kiểm tra; không đổi ngày để tạo cảm giác mới.
5. Rule pháp lý/kế toán phải có nguồn chuyên ngành hiện hành và người chịu trách nhiệm xác nhận trước khi dùng trong production.

## Giới hạn lần xuất bản

- Đã đối chiếu tài liệu hãng, review nội dung và kiểm tra file/link nội bộ.
- Chưa chạy SQL Server, benchmark tải, thử failover hay restore trong môi trường xuất bản.
- Không có dữ liệu thật, credential, công thức sản phẩm độc quyền hoặc số đo production.
