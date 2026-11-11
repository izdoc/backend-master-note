# 05 · Tiền, thời gian và dữ liệu lịch sử

[Mục lục](../INDEX.md)

## Tiền phải có đơn vị

Không lưu một con số rồi ngầm hiểu mọi khoản đều là VND. Cặp amount/currency là tối thiểu. Nếu dùng minor units kiểu integer, phải có bảng exponent theo currency và quy tắc xử lý tài sản không theo cùng quy ước.

Ví dụ thiết kế: tiền hạch toán `decimal(19,4)`, tỷ giá `decimal(19,8)`, quantity có scale riêng. Đây là lựa chọn cho lab, không phải mặc định cho mọi sản phẩm. Kiểm tra giá trị cực đại, kết quả nhân/chia, tổng cộng và việc thu hẹp precision/scale. `float` là số gần đúng, không phù hợp làm giá trị tiền cần so sánh chính xác.

Tách ba việc: độ chính xác khi tính, độ chính xác lưu kết quả, cách hiển thị. Lưu rate gốc và rate áp dụng, phiên bản công thức phí, quy tắc làm tròn và bên chịu phần chênh. Làm tròn từng dòng rồi cộng có thể khác cộng rồi làm tròn; phải thống nhất với nghiệp vụ và bút toán rounding.

## Thời gian có nhiều ý nghĩa

| Trường | Ý nghĩa |
|---|---|
| OccurredAt | Sự kiện xảy ra ở nguồn |
| ReceivedAt | Hệ thống nhận sự kiện |
| PostedAt | Hạch toán vào sổ |
| BusinessDate | Ngày nghiệp vụ theo lịch/cut-off |
| ValueDate | Ngày giá trị phục vụ nghiệp vụ liên quan |

Dùng UTC cho timestamp kỹ thuật và lưu zone/offset cần thiết cho chứng từ. `datetime2` không tự mang timezone. Không suy ra business date chỉ bằng `CAST(UTC AS date)` nếu ngày nghiệp vụ phụ thuộc giờ đóng sổ hoặc ngày nghỉ.

## Lịch sử và hồi tố

Tỷ lệ phí áp dụng từ ngày X cần `EffectiveFrom/EffectiveTo`. Khi sửa hồi tố, còn cần biết hệ thống ghi nhận thay đổi vào lúc nào. Đây là hai trục: thời gian hiệu lực nghiệp vụ và thời gian ghi nhận. Dùng khoảng nửa mở `[from, to)` để tránh một thời điểm thuộc hai phiên bản; ngăn khoảng chồng lấn trong transaction có kiểm soát.

Temporal table có thể hỗ trợ lịch sử thay đổi kỹ thuật nhưng không tự thay thế mọi yêu cầu hiệu lực nghiệp vụ hoặc chống can thiệp bởi quản trị viên.

`rowversion` của SQL Server là token nhị phân để phát hiện thay đổi, **không phải timestamp thời gian**. Giữ cột `UpdatedAt` riêng khi cần hiển thị thời điểm.

**Bài tập:** giao dịch xảy ra 23:59, callback nhận hôm sau, ngày đó đã chốt. Đáp án cần quy tắc late arrival và bút toán điều chỉnh; không sửa ngày cũ âm thầm.

Nguồn: [decimal/numeric](https://learn.microsoft.com/en-us/sql/t-sql/data-types/decimal-and-numeric-transact-sql?view=sql-server-ver16), [rowversion](https://learn.microsoft.com/en-us/sql/t-sql/data-types/rowversion-transact-sql?view=sql-server-ver16), [PostgreSQL numeric](https://www.postgresql.org/docs/18/datatype-numeric.html).
