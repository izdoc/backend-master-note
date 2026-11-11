# 23 · EF Core, Dapper và database contract

[Mục lục](../INDEX.md)

## SQL được sinh ra vẫn cần review

```csharp
// Minh họa; cần entity/DbContext thực tế và provider phù hợp.
var rows = await db.Payments
    .AsNoTracking()
    .Where(p => p.TenantId == tenantId && p.AccountId == accountId)
    .OrderByDescending(p => p.CreatedAt)
    .ThenByDescending(p => p.PaymentId)
    .Select(p => new { p.PaymentId, p.CreatedAt, p.Amount, p.Currency })
    .Take(50)
    .ToListAsync(cancellationToken);
```

Projection và giới hạn dòng làm rõ contract trả về. Không gọi `ToList` trước filter rồi tải cả bảng về RAM. Theo dõi số query, số dòng và SQL thực tế; N+1 có thể gây nhiều round-trip dù mỗi query riêng rất nhanh.

`Include` nhiều collection có thể nhân dữ liệu; cân nhắc projection hoặc split query. Split query thêm round-trip và cần xem consistency giữa các SELECT nếu dữ liệu đổi. Streaming giảm buffering của một số luồng nhưng giữ connection lâu; phải đo với pool và tốc độ consumer.

## Transaction và retry

Một `SaveChanges` có transaction theo khả năng provider, nhưng nhiều lần `SaveChanges` cộng Dapper/HTTP không tự thành một đơn vị nguyên tử. Khi EF Core và Dapper cùng thao tác nguyên tử, phải dùng cùng connection/transaction và quản lý lifecycle rõ. `DbContext` không dùng đồng thời từ nhiều task.

Execution strategy có retry phải bao trọn đơn vị transaction theo hướng dẫn provider. Không bọc lệnh gọi ngân hàng bên ngoài vào retry database một cách tùy tiện. Dùng idempotency key bền vững để giải quyết trường hợp client không biết commit thành công hay chưa.

## Parameter và loại dữ liệu

Với Dapper hoặc ADO.NET, parameter phải khớp kiểu/scale/length database. Parameter hóa giá trị, whitelist tên cột/chiều sắp xếp. Không ghép raw input vào `ORDER BY` hoặc `OPENQUERY` rồi cho rằng đã an toàn nhờ dùng Dapper.

Mapping .NET `decimal`, ngày giờ, nullable và concurrency token cần explicit contract. Trong EF, cấu hình precision/scale và `rowversion` theo provider; không coi `DateTime.Kind` là bằng chứng timezone đã lưu đúng ở database.

## Pool và observability

Đóng/dispose connection và reader đúng lúc; không chia sẻ connection global giữa request. Ghi correlation ID, command duration và query shape, tránh ghi PII/secret. Command timeout, cancellation và transient retry là các cơ chế khác nhau; cancellation không đủ chứng minh transaction chưa commit.

**Bài tập:** endpoint dùng `Task.WhenAll` trên cùng DbContext để chạy ba query. Đáp án: dùng tuần tự hoặc context riêng cho công việc độc lập, đồng thời xác định consistency mong muốn; không chỉ tăng pool size.

Nguồn: [EF efficient querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying), [EF transactions](https://learn.microsoft.com/en-us/ef/core/saving/transactions). Snippet chưa được biên dịch thành ứng dụng trong wiki.
