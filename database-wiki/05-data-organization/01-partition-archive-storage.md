# 15 · Schema, file, partition và archive

[Mục lục](../INDEX.md)

## Tổ chức logic trước vật lý

Schema theo trách nhiệm như `Customer`, `Payments`, `Ledger`, `Audit`, `Staging` giúp phân quyền và nhận diện ownership. Schema không tự cô lập CPU/I/O hoặc đảm bảo transaction giữa domain phù hợp. Tránh một schema cho mỗi ngày hoặc một bảng cho mỗi tháng nếu chỉ nhằm quản lý thời gian; truy vấn và migration sẽ khó hơn.

SQL Server data file, transaction log và tempdb có vai trò khác nhau. Tách logical volume chỉ có ích về I/O nếu lớp storage thật hỗ trợ; hai thư mục trên cùng thiết bị không tạo thêm throughput. Pre-size theo số đo, cấu hình growth theo dung lượng phù hợp và cảnh báo dung lượng trống. Autogrowth là lưới dự phòng, không phải capacity plan.

## Partition giải quyết việc gì?

Partition chia ngang bảng theo key. Nó hữu ích cho lifecycle và có thể giúp truy vấn khi engine loại được partition không liên quan. Query không lọc theo key hoặc vẫn đọc phần lớn dữ liệu có thể không nhanh hơn; index vẫn cần thiết.

Ví dụ ứng viên: ledger entry theo tháng `BusinessDate`, nếu retention và query đều theo ngày nghiệp vụ. Cần xem giao dịch đến muộn và truy vấn theo account xuyên nhiều năm. Không thêm partition date vào unique key rồi vô tình cho phép cùng `ExternalReference` xuất hiện ở hai tháng.

Trong SQL Server, unique index được partition-aligned phải chứa partitioning column trong key. Nếu cần uniqueness toàn cục theo reference, phải đánh giá unique index không aligned hoặc bảng registry riêng cùng transaction, cùng với các hạn chế switch và maintenance phát sinh.

## Sliding window và archive

1. Tạo trước partition tương lai; tránh split dữ liệu lớn ngay giờ cao điểm.
2. Xác định mốc đóng, kiểm tra late arrival và legal hold.
3. Chuẩn bị archive target tương thích và kiểm tra yêu cầu index/constraint cho switch.
4. Đối chiếu số dòng, amount theo currency, min/max và hash theo chiến lược phù hợp.
5. Thử truy xuất và restore archive trước khi loại khỏi online tier.

Archive không phải xóa dữ liệu. Ghi catalog: dữ liệu nằm đâu, ai đọc được, thời gian lấy lại và cách giải mã. Không xóa parent khi child còn cần audit. Nếu purge theo batch, chọn key ổn định và theo dõi log/lock; `DELETE` hàng trăm triệu dòng trong một transaction có thể gây gián đoạn.

## Compression và bảo trì

Compression đổi CPU lấy I/O/storage; benchmark cả đọc và ghi. Không shrink data file định kỳ rồi để nó tăng trở lại. Không rebuild mọi index chỉ vì đạt một tỷ lệ fragmentation cố định; xét kích thước, page density, query và chi phí log.

Nguồn engine: [SQL Server partitioned tables](https://learn.microsoft.com/en-us/sql/relational-databases/partitions/partitioned-tables-and-indexes?view=sql-server-ver16), [PostgreSQL partitioning](https://www.postgresql.org/docs/18/ddl-partitioning.html). Quy trình archive là đề xuất cần kiểm chứng theo hệ thống.
