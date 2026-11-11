# 04 · Khóa, constraint và phạm vi duy nhất

[Mục lục](../INDEX.md)

## Khóa kỹ thuật và khóa nghiệp vụ

`AccountId bigint` thuận tiện làm PK; `AccountNo` vẫn cần unique đúng phạm vi. Có PK tự tăng không ngăn được hai dòng cùng số tài khoản. GUID hữu ích khi tạo ID phân tán nhưng khóa rộng và cách sinh ảnh hưởng index; đo trước khi chọn clustered key.

Trong hệ thống đa tenant, filter `TenantId` ở application là chưa đủ. FK ghép có thể ngăn liên kết account tenant A với customer tenant B:

```sql
-- Minh họa: parent phải có UNIQUE(TenantId, CustomerId).
ALTER TABLE Banking.Account
ADD CONSTRAINT FK_Account_Customer
    FOREIGN KEY (TenantId, CustomerId)
    REFERENCES Banking.Customer (TenantId, CustomerId);
```

Quyền truy cập từng dòng vẫn phải xử lý riêng; FK không phải cơ chế authorization.

## Constraint là tuyến phòng thủ dữ liệu

| Ràng buộc | Ví dụ | Giới hạn |
|---|---|---|
| `NOT NULL` | Currency bắt buộc | Chuỗi rỗng vẫn có thể lọt |
| `CHECK` | Amount > 0 | Không tự kiểm tra tổng nhiều entry |
| `UNIQUE` | Provider + ExternalEventId | Chọn sai scope sẽ bỏ lọt hoặc chặn nhầm |
| Foreign key | Payment thuộc account tồn tại | Không chứng minh account được phép thanh toán |
| Transaction + quyền ghi | Journal và balance cùng commit | Cần chặn đường ghi vòng ngoài |

`CHECK` trong SQL Server chấp nhận biểu thức UNKNOWN do NULL, vì vậy phải dùng `NOT NULL` khi bắt buộc có giá trị. Sau bulk load hoặc migration, kiểm tra constraint còn enabled/trusted; dữ liệu sai tồn tại sẵn không tự biến mất khi bật lại logic ứng dụng.

## Một số quyết định dễ bỏ sót

- Chuẩn hóa email, mã tham chiếu và quy tắc chữ hoa/thường trước khi đặt unique; collation ảnh hưởng so sánh.
- SQL Server không tự tạo index trên cột foreign key. Chỉ tạo khi workload join/delete/check parent thực sự hưởng lợi.
- Không dùng số CCCD, số điện thoại hoặc email làm PK xuyên hệ thống: chúng có thể thay đổi, cần bảo vệ và có trường hợp không sẵn có.
- `ON DELETE CASCADE` có thể lan ra nhiều bảng; dữ liệu tài chính thường cần quy trình đóng/ngừng hoạt động thay vì xóa dây chuyền.
- Với unique chỉ áp dụng dòng active, xem xét filtered unique index; phải định nghĩa chuyện tái sử dụng mã và giữ lịch sử.

**Bài tập:** webhook có `EventId` chỉ duy nhất trong từng provider. Đáp án: unique `(TenantId, Provider, EventId)` nếu tenant là phạm vi contract; unique chỉ `EventId` có thể loại bỏ sự kiện hợp lệ từ provider khác.

Nguồn kỹ thuật: [Microsoft — index design](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver16). Phạm vi khóa và ví dụ tenant là thiết kế minh họa của wiki.
