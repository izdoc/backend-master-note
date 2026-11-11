# 14 · Statistics, plan cache và dữ liệu lệch

[Mục lục](../INDEX.md)

## Estimate quyết định nhiều lựa chọn

Optimizer cần ước lượng số dòng để chọn join, access path và memory grant. Sau một đợt nạp dữ liệu lớn hoặc khi status phân bố lệch mạnh, estimate có thể không phản ánh workload. Statistics không phải bản đếm chính xác mọi tổ hợp giá trị.

Trong SQL Server, histogram thuộc cột đầu của statistics object. Vì vậy index ghép không có nghĩa có histogram đầy đủ cho mọi cột hoặc mọi tương quan. Tạo/update statistics cần dựa trên query và dữ liệu, không mặc định FULLSCAN toàn database mỗi đêm.

## Parameter sniffing

Procedure tra lịch sử một account ít giao dịch có thể được compile thành plan phù hợp tập nhỏ. Account tổ chức có hàng triệu dòng dùng lại plan đó có thể chậm. Parameter sniffing giúp tái sử dụng plan, không tự thân là lỗi; vấn đề xuất hiện khi một plan không hợp nhiều phân bố.

Trước khi sửa, ghi parameter compile/runtime, actual/estimated rows, plan history và thời điểm statistics thay đổi. Một truy vấn chậm cũng có thể do blocking hoặc cache lạnh, không phải mọi biến động đều là sniffing.

| Phương án | Khi cân nhắc | Chi phí/giới hạn |
|---|---|---|
| Update statistics có mục tiêu | Estimate sai vì dữ liệu đổi | I/O/CPU, recompile |
| Rewrite/split nhánh | Nhiều shape lọc khác nhau | Tăng code cần maintain |
| `OPTION (RECOMPILE)` tại statement | Query ít chạy, tham số rất lệch | Compile mỗi lần |
| Parameterized dynamic SQL | Nhiều bộ filter tùy chọn | Quản lý shape và whitelist identifier |
| Query Store plan forcing | Cần giảm regression đã xác minh | Có thể kém với parameter khác |
| PSP | Query đủ điều kiện trên engine hỗ trợ | Phụ thuộc version/compatibility |

Không nối giá trị người dùng vào SQL động. Dùng `sp_executesql` và tham số đúng kiểu; cột sắp xếp động phải chọn từ whitelist.

SQL Server 2022 có Parameter Sensitive Plan optimization với compatibility level 160 cho các truy vấn đủ điều kiện; không có nghĩa mọi pattern optional filter đều được giải quyết. Không đổi compatibility production chỉ để thử tính năng mà chưa regression test.

## Quản lý Query Store

Thiết lập dung lượng, retention, capture policy và kiểm tra có bị read-only hay không. Khi force plan/hint, ghi người phụ trách và điều kiện gỡ bỏ. Dữ liệu query có thể chứa giá trị nhạy cảm nếu application không parameterize; kiểm soát quyền truy cập và retention.

**Bài tập:** query tùy chọn `(@Status IS NULL OR Status=@Status)` có ba workload rất khác. Đáp án: đo từng workload; xem rewrite theo shape, recompile có mục tiêu hoặc khả năng engine; không tắt sniffing toàn server theo phản xạ.

Nguồn: [Statistics](https://learn.microsoft.com/en-us/sql/relational-databases/statistics/statistics?view=sql-server-ver16), [PSP](https://learn.microsoft.com/en-us/sql/relational-databases/performance/parameter-sensitive-plan-optimization?view=sql-server-ver16), [Query Store hints](https://learn.microsoft.com/en-us/sql/relational-databases/performance/query-store-hints-best-practices?view=sql-server-ver16).
