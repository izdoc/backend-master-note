# Mục lục

[Trang đầu](README.md)

| Category | Bài |
|---|---|
| 00 · Nền tảng | [01. Thiết kế từ workload và invariant](00-foundations/01-workload-and-invariants.md) · [02. Chọn kiến trúc lưu trữ](00-foundations/02-storage-architecture.md) |
| 01 · Mô hình dữ liệu | [03. ERD, chuẩn hóa và ranh giới](01-data-modeling/01-erd-normalization.md) · [04. Khóa và constraint](01-data-modeling/02-keys-and-constraints.md) · [05. Tiền, thời gian và lịch sử](01-data-modeling/03-money-time-history.md) |
| 02 · Nghiệp vụ tài chính | [06. Ledger và số dư](02-financial-domains/01-ledger-and-balances.md) · [07. Payment, hold và đối soát](02-financial-domains/02-payments-reconciliation.md) · [08. Ngân hàng, chứng khoán và bảo hiểm](02-financial-domains/03-banking-securities-insurance.md) |
| 03 · Tính nhất quán | [09. Transaction và isolation](03-transactions/01-isolation-and-concurrency.md) · [10. Deadlock, retry và idempotency](03-transactions/02-deadlocks-idempotency.md) |
| 04 · Tối ưu truy vấn | [11. Quy trình đo và đọc execution plan](04-query-performance/01-measurement-and-plans.md) · [12. Thiết kế index](04-query-performance/02-index-design.md) · [13. Viết SQL hiệu quả](04-query-performance/03-sql-patterns.md) · [14. Statistics và parameter sensitivity](04-query-performance/04-statistics-and-plan-cache.md) |
| 05 · Tổ chức dữ liệu | [15. Schema, file, partition và archive](05-data-organization/01-partition-archive-storage.md) · [16. Báo cáo, warehouse và capacity](05-data-organization/02-reporting-and-capacity.md) |
| 06 · Bảo mật | [17. Quyền và dữ liệu nhạy cảm](06-security/01-access-and-encryption.md) · [18. Audit, retention và chất lượng](06-security/02-audit-and-data-governance.md) |
| 07 · Vận hành | [19. Backup, restore và HA/DR](07-operations/01-backup-restore-ha.md) · [20. Monitoring và runbook sự cố](07-operations/02-monitoring-and-incidents.md) · [21. Migration và bảo trì](07-operations/03-migrations-maintenance.md) |
| 08 · Tích hợp | [22. Outbox, CDC và hệ thống cũ](08-integration/01-outbox-cdc-legacy.md) · [23. EF Core và Dapper](08-integration/02-dotnet-data-access.md) · [24. Khác biệt SQL Server/PostgreSQL](08-integration/03-postgresql-differences.md) |
| 09 · Workshop | [25. Tình huống và capstone](09-workshops/01-cases-and-capstone.md) · [26. Mẫu review/tuning/runbook](09-workshops/02-review-templates.md) |
| 10 · Lab | [Hướng dẫn](10-labs/README.md) · [01 Schema](10-labs/01-schema.sql) · [02 Posting](10-labs/02-post-transfer.sql) · [03 Smoke test](10-labs/03-smoke-tests.sql) · [04 Tuning](10-labs/04-query-tuning.sql) · [05 Diagnostics](10-labs/05-diagnostics.sql) |

## Tra theo triệu chứng

| Vấn đề | Đọc trước | Kiểm chứng |
|---|---|---|
| Trừ tiền hai lần sau timeout | Bài 10, 07 | Chạy lại cùng idempotency key |
| Số dư không khớp lịch sử | Bài 06, 18 | Rebuild từ ledger và so projection |
| Query nhanh lúc đầu, chậm lúc sau | Bài 11, 14 | So plan, tham số, cardinality |
| CPU thấp nhưng API timeout | Bài 09, 20 | Blocking, wait, connection pool |
| Bảng tăng hàng trăm triệu dòng | Bài 15, 16 | Retention, truy vấn theo thời gian, restore |
| Báo cáo EOD kéo chậm giao dịch | Bài 16, 22 | Resource isolation và watermark |
| Database/log đầy | Bài 19, 20 | Disk, log reuse wait, transaction lâu |
| Cần thêm cột trên bảng lớn | Bài 21 | Expand, backfill nhỏ, contract |
