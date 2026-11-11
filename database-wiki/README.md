# Database Engineering Wiki

Wiki tiếng Việt về thiết kế, tối ưu và vận hành cơ sở dữ liệu trong ngân hàng, chứng khoán, bảo hiểm và fintech. Dành cho backend engineer, DBA và solution architect. Trọng tâm: dữ liệu đúng, truy vấn đo được, vận hành có thể khôi phục.

**Phiên bản nội dung:** 1.0 · **Ngày rà soát:** 11/11/2026.

## Cách dùng

- Bắt đầu với [mục lục](INDEX.md), đọc theo thứ tự category hoặc tra theo vấn đề.
- Ví dụ chính: SQL Server 2022, compatibility level 160. Các tính năng phụ thuộc edition, bản vá và cấu hình cần đối chiếu môi trường thực tế. PostgreSQL được so sánh ở bài riêng, không dùng lẫn cú pháp.
- SQL trong bài là minh họa, trừ bộ [lab SQL Server](10-labs/README.md) có schema và trình tự chạy riêng. Bộ lab đã được rà soát tĩnh; chưa được thực thi trên SQL Server trong lần xuất bản này.
- Kiến trúc và mô hình nghiệp vụ là đề xuất để thảo luận, không phải quy tắc kế toán hay cam kết tuân thủ pháp luật. Các tham số retention, RPO/RTO và hạn mức là ví dụ, cần chủ sở hữu nghiệp vụ quyết định.
- Không có cấu hình “tối ưu nhất” cho mọi hệ thống. Mỗi thay đổi phải giữ đúng kết quả và được đo với dữ liệu, tải đồng thời và điều kiện vận hành đại diện.

## Lộ trình 8 tuần

| Tuần | Học | Đầu ra thực hành |
|---|---|---|
| 1 | Nền tảng, workload, mô hình dữ liệu | Workload inventory và ERD |
| 2 | Khóa, constraint, tiền, thời gian | Data dictionary và quy tắc bất biến |
| 3 | Ledger, payment, bảo hiểm | State machine và mapping bút toán |
| 4 | Transaction, concurrency, idempotency | Thử hai session và retry |
| 5 | Index, plan, statistics, SQL | Báo cáo tuning trước/sau |
| 6 | Partition, archive, báo cáo | Kế hoạch tăng trưởng dữ liệu |
| 7 | Bảo mật, backup, monitoring | Restore drill và runbook |
| 8 | Integration và capstone | Review thiết kế bằng checklist |

## Nguyên tắc xuyên suốt

1. Viết rõ điều gì tuyệt đối không được sai: không chi vượt số dư, không ghi nhận cùng giao dịch hai lần, không thất lạc bút toán.
2. Gắn invariant với nơi thực thi: constraint, transaction, procedure, quyền ghi hoặc quy trình đối soát.
3. Thiết kế từ workload thật; index phục vụ câu truy vấn cụ thể.
4. Dữ liệu lịch sử, quyền truy cập và khả năng restore là một phần của thiết kế ban đầu.
5. Ghi giả thuyết, số đo và rollback cho mỗi thay đổi hiệu năng.

## Tài nguyên

- [Mục lục và tuyến đọc nhanh](INDEX.md)
- [Từ điển thuật ngữ](GLOSSARY.md)
- [Nguồn chính thức và cách cập nhật](REFERENCES.md)
- [Mẫu review và báo cáo tuning](09-workshops/02-review-templates.md)
- [Lab và giới hạn kiểm chứng](10-labs/README.md)

Các tình huống, tên khách hàng và số tài khoản trong wiki đều là dữ liệu giả lập.
