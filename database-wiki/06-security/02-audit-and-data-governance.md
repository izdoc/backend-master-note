# 18 · Audit, retention và chất lượng dữ liệu

[Mục lục](../INDEX.md)

## Ba loại lịch sử khác nhau

- **Business history:** ai duyệt, vì sao payment chuyển trạng thái, phiên bản rule nào được dùng.
- **Technical change history:** cột nào đổi từ giá trị gì sang gì, thời điểm ghi nhận.
- **Security audit:** ai đăng nhập, đọc/sửa object hoặc thay đổi quyền/cấu hình.

Một cột `UpdatedBy` không đáp ứng cả ba. Audit record nên có actor thực, actor type, correlation/request ID, operation, target, reason, outcome và thời gian chuẩn hóa. Với thay đổi nghiệp vụ quan trọng, ghi audit cùng transaction hoặc dùng outbox để chuyển tiếp bền vững; ghi log sau commit có thể mất khi process chết.

## Chống can thiệp và quyền quản trị

Không gọi bảng append-only là bất biến tuyệt đối nếu admin vẫn có thể sửa. Hạn chế writer, tách người quản trị, chuyển log sang nơi có chính sách bảo vệ riêng và kiểm tra mất log. Hash chain hỗ trợ phát hiện sửa khi có mốc kiểm chứng bên ngoài; nếu kẻ sửa có thể thay cả chuỗi và mốc thì bảo vệ không đầy đủ.

SQL Server Audit hỗ trợ ghi sự kiện engine, không tự chứa ý nghĩa nghiệp vụ như “phê duyệt ngoại lệ do hồ sơ bổ sung”. Kết hợp hai lớp và kiểm soát dữ liệu nhạy cảm trong audit.

## Retention là một ma trận

| Loại dữ liệu | Cần quyết định | Chủ sở hữu đề xuất |
|---|---|---|
| Entry/chứng từ | Thời hạn, legal hold, truy xuất | Kế toán/nghiệp vụ/compliance |
| Request payload | Mục đích, PII, thời gian tối thiểu cần giữ | Product/security |
| Query/technical log | Nhu cầu điều tra và chi phí | SRE/DBA/security |
| Backup | Retention, mã hóa, vị trí, quyền xóa | DBA/security |

Không áp cùng một số năm cho mọi tài liệu. Xóa trên OLTP còn cần xem replica, export, search index, archive và vòng đời backup. Legal hold phải ngăn purge được chỉ định mà không biến mọi dữ liệu thành lưu vô hạn.

## Chất lượng dữ liệu có số đo

Theo dõi duplicate reference, orphan, NULL ngoài dự kiến, currency sai, khoảng hiệu lực chồng lấn, journal mất cân bằng, projection lệch ledger và batch thiếu dòng. Định nghĩa ngưỡng, chủ xử lý và SLA riêng cho từng loại.

Đối soát tự động phải mở exception case có trạng thái và audit, không chỉ gửi email không ai theo. Phân biệt lỗi dữ liệu mới phát sinh với backlog; ghi tuổi của exception và số tiền ảnh hưởng theo currency.

**Bài tập:** một operator sửa trực tiếp balance để đóng ticket. Review cần tìm quyền đã cho phép việc đó, chứng cứ audit, ảnh hưởng ledger và quy trình adjustment thay thế; không chỉ thêm cảnh báo giao diện.

Nguồn kỹ thuật: [SQL Server Audit](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine?view=sql-server-ver16). Retention cụ thể phải lấy từ chính sách và yêu cầu hiện hành của tổ chức.
