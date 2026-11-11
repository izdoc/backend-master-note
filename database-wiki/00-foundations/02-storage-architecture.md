# 02 · Chọn kiến trúc lưu trữ theo trách nhiệm

[Mục lục](../INDEX.md)

## Lựa chọn khởi đầu

Với giao dịch tài chính có nhiều ràng buộc và cần commit nguyên tử, cơ sở dữ liệu quan hệ là lựa chọn khởi đầu hợp lý. Quyết định cuối cùng còn phụ thuộc vận hành, đội ngũ, tải và sản phẩm. Không đưa thêm một công nghệ chỉ vì dữ liệu tăng.

| Thành phần | Phù hợp | Trách nhiệm cần tránh giao nhầm |
|---|---|---|
| SQL Server/PostgreSQL | Transaction, khóa, constraint, báo cáo quan hệ | Không mặc định biến thành kho mọi file và mọi log |
| Redis | Cache, dữ liệu có thể tái tạo, rate limit | Cache balance không tự thành nguồn tiền chính xác |
| Document database | Aggregate tài liệu có cấu trúc linh hoạt | Cần kiểm tra phạm vi atomicity thực tế |
| Search engine | Tìm kiếm văn bản, xếp hạng | Kết quả search có thể trễ so nguồn |
| Object storage | Chứng từ, sao kê gốc, tài liệu lớn | Cần metadata, hash, quyền và lifecycle riêng |
| Warehouse | Phân tích lịch sử, tổng hợp lớn | Không quyết định available balance theo dữ liệu trễ |

## OLTP và OLAP

OLTP ưu tiên nhiều giao dịch ngắn, truy cập ít dòng và ghi có cạnh tranh. OLAP ưu tiên quét, join và tổng hợp nhiều dữ liệu. Một báo cáo có SQL đúng vẫn có thể làm chậm giao dịch vì tranh CPU, memory grant hoặc I/O.

Khởi đầu có thể dùng cùng engine nhưng tách workload bằng lịch chạy, giới hạn tài nguyên hoặc read model. Khi cần, chuyển báo cáo sang kho riêng qua pipeline có watermark và đối soát. Replica đọc không mặc định đọc được giao dịch vừa commit trên primary.

## Ranh giới dữ liệu

Một modular monolith có thể dùng nhiều schema và transaction nội bộ. Microservices có quyền sở hữu dữ liệu riêng; service khác gọi contract hoặc nhận event thay vì sửa trực tiếp bảng. Đổi sang database-per-service làm mất khả năng FK/transaction cục bộ xuyên service; phải thiết kế trạng thái trung gian và compensation.

Không dùng distributed transaction hoặc saga theo thói quen. Nếu một invariant cần commit nguyên tử và các đối tượng luôn đi cùng nhau, cân nhắc giữ chúng trong cùng ranh giới trước.

## Quyết định cần ghi lại

ADR phải nêu workload, consistency, RPO/RTO, chi phí giấy phép, backup, năng lực trực vận hành và cách chuyển đổi nếu giả định sai. Ví dụ: chưa shard ví vì một database vẫn đủ tải; tiêu chí xem lại là đã tối ưu query nhưng write/log throughput vẫn không đạt SLO qua benchmark.

**Bài tập:** phân loại customer profile, ledger, hợp đồng PDF và dữ liệu dashboard. Với mỗi loại, chọn nguồn dữ liệu chính và mô tả dữ liệu nào có thể tái tạo.
