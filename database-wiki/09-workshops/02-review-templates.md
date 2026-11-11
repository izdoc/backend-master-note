# 26 · Mẫu dùng khi review và vận hành

[Mục lục](../INDEX.md)

Sao chép mục phù hợp vào issue/PR. Các ô chưa có số đo phải ghi “chưa đo”, không điền số ước lượng vào cột kết quả thực.

## A. Data dictionary

| Table.Column | Kiểu/null | Ý nghĩa và đơn vị | Nguồn/owner | PII | Constraint | Lifecycle |
|---|---|---|---|---|---|---|
| Account.Balance | decimal(19,4), NOT NULL | Book balance, theo Currency | Posting | Không trực tiếp | Không âm trong lab | Projection từ ledger |

## B. Invariant matrix

| Quy tắc | Phạm vi | Nơi thực thi | Writer được phép | Cách kiểm thử | Đối soát |
|---|---|---|---|---|---|
| Không posting hai lần | Tenant + operation + key | Unique + transaction | Posting procedure | Hai session cùng key | Đếm key/journal |

## C. Báo cáo tuning

**Vấn đề:** endpoint/query, tác động, khoảng thời gian.  
**Môi trường:** engine/build/compatibility, CPU/RAM/storage, cấu hình liên quan.  
**Dataset:** số dòng, phân bố, tenant/account lớn, thống kê dữ liệu, cache state.  
**Baseline:** SQL/parameters, plan ID, logical reads, CPU, elapsed, executions và concurrency.  
**Giả thuyết:** operator/wait nào gây chi phí, bằng chứng.  
**Thay đổi:** SQL/index/statistics cụ thể, giải thích tác động dự kiến.  
**Tính đúng:** row count, keys, totals theo currency và edge cases.  
**Kết quả:** cùng điều kiện, nhiều parameter set, p95/p99 từ mẫu request.  
**Chi phí:** write throughput, index size, log, deploy lock.  
**Rollout/rollback:** người theo dõi, mốc, điều kiện dừng và câu lệnh/commit hoàn tác.

## D. ADR thiết kế

- Bối cảnh và workload đã biết; điều chưa biết.
- Invariant và consistency boundary.
- Các phương án, lợi ích, chi phí vận hành, failure mode.
- Quyết định và lý do; điều kiện xem lại.
- Kế hoạch chứng minh qua benchmark/recovery/concurrency test.

## E. Checklist schema/migration

- [ ] Khóa nghiệp vụ và tenant scope đúng; constraint xử lý NULL đúng.
- [ ] Precision/scale, currency, timezone, business date đã định nghĩa.
- [ ] History/retention/PII/ownership đã rõ.
- [ ] Index gắn với query và đã xét write overhead.
- [ ] Migration tương thích phiên bản cũ/mới, backfill có checkpoint.
- [ ] Có rehearsal, headroom log/tempdb, rollout và rollback thực tế.
- [ ] Direct DML vào ledger bị hạn chế; audit thử bằng app identity.
- [ ] Có restore drill và mốc dữ liệu phù hợp RPO/RTO.

## F. Runbook sự cố

**Tên triệu chứng / mức ảnh hưởng:** ...  
**Dấu hiệu xác nhận:** dashboard, query, log và thời điểm.  
**Thu bằng chứng:** SQL, plan, wait, blocking, capacity; bảo vệ PII.  
**Biện pháp giảm tác động:** ai thực hiện, tác động rollback/lag/traffic.  
**Điều kiện cần nâng cấp xử lý:** ...  
**Kiểm tra sau phục hồi:** integrity, duplicate, ledger/projection, backlog.  
**Timeline / nguyên nhân / hành động theo dõi:** có owner và hạn hoàn thành.
