# Lab SQL Server: posting, retry và tuning

[Mục lục wiki](../INDEX.md)

## Môi trường và giới hạn

Dùng **database mới, trống, tên `DatabaseWikiLab` trên SQL Server 2022**, compatibility 160, không dùng database thật. Script không tạo/xóa database; người học tạo bằng công cụ quản trị. Script schema chỉ chạy một lần và từ chối nếu schema đã có. Dữ liệu đều giả lập.

Mô hình ví cùng currency, không hold/fee/FX/overdraft. OpeningBalance lưu riêng để bài tập có nguồn vốn ban đầu; đối soát là `OpeningBalance + SUM(Entry.SignedAmount) = Balance`. Hệ thống thật nên mô hình hóa opening theo quy trình mở sổ đã phê duyệt. Lab dùng signed entries, không thay chart of accounts và bút toán kế toán đầy đủ.

**Trạng thái kiểm chứng:** đã review tĩnh, kiểm tra cấu trúc file/link; chưa thực thi bằng SQL Server, chưa benchmark, chưa thử đồng thời hoặc restore. Các kết quả dưới đây là **kỳ vọng nghiệm thu**, không phải log chạy thực tế.

## Thứ tự

1. Tạo database mới `DatabaseWikiLab`. Chạy bằng `sqlcmd -b -d DatabaseWikiLab` hoặc **bật SQLCMD Mode trong SSMS**. Mỗi file có `:ON ERROR EXIT` để dừng script nếu chọn database/tạo schema lỗi, không tiếp tục batch sau. Authentication được quản lý ngoài source. Chạy riêng từng file theo thứ tự.
2. Chạy [01-schema.sql](01-schema.sql): tạo schema, account, journal, entry, request và dữ liệu ban đầu.
3. Chạy [02-post-transfer.sql](02-post-transfer.sql): tạo procedure sở hữu transaction, không nhận ambient transaction; tạo role `LabPoster` chỉ có quyền cần thiết.
4. Chạy [03-smoke-tests.sql](03-smoke-tests.sql): chuyển 25 USD, retry, payload conflict, insufficient funds, currency/tenant mismatch và kiểm tra invariant. Các key cố định giúp chạy lại smoke test mà không posting thêm.
5. Chạy [04-query-tuning.sql](04-query-tuning.sql) riêng: tạo dataset 100.000 dòng, bật actual plan và so `STATISTICS IO/TIME`; script này có thể chạy lại nhưng không tự reset dữ liệu.
6. Dùng [05-diagnostics.sql](05-diagnostics.sql) để xem trạng thái; cần quyền xem DMV theo version. Không có `KILL`, sửa option hoặc xóa cache.

## Test đồng thời bằng hai cửa sổ

Sau bước 2, mở hai connection vào database lab. Với hai request khác key cùng chuyển từ account 5 (100 USD) sang 6:

```sql
-- Cửa sổ A: dùng key concurrent-a.
EXEC LabFinance.PostTransfer
    @TenantId=1, @FromAccountId=5, @ToAccountId=6,
    @Amount=80, @Currency='USD', @IdempotencyKey='concurrent-a';
-- Cửa sổ B: chạy gần cùng lúc, đổi key thành concurrent-b.
```

Kỳ vọng chỉ một transfer thành công, account 5 còn 20, account 6 là 180. Luồng kia không đủ tiền. Nếu chỉ chạy tuần tự thì chưa chứng minh contention path; có thể dùng harness nhiều connection và barrier bên ngoài, ghi số lần lặp và kết quả. Không thêm `WAITFOR` vào procedure sản xuất để thử.

Với cùng key/cùng payload trên hai connection, kỳ vọng một journal và cả hai nhận cùng JournalId nếu không có lỗi transient; nếu deadlock/network lỗi thì retry toàn call với key cũ. Test payload khác cùng key phải conflict. Thử ngược chiều cần account mới/reset lab riêng, vì kịch bản trên đã thay số dư.

## Kiểm tra quyền

Tạo user thử nghiệm theo cơ chế authentication của lab và cho vào `LabPoster`. Procedure phải chạy được, direct INSERT/UPDATE/DELETE vào schema phải bị từ chối. Tài khoản dbo/sysadmin dùng để setup không chứng minh quyền ứng dụng đã đúng. Không cấp DDL/ALTER procedure cho role runtime.

## Giới hạn cần đọc trước khi tái sử dụng

- Mọi writer phải theo procedure và cùng thứ tự khóa; đây không phải proof cho các đường ghi ngoài protocol.
- Idempotency trong lab có scope tenant + thao tác transfer; key được so theo collation nhị phân, không nhận space đầu/cuối. Không có purge key trong lab.
- Tham số decimal(19,4) có thể đã bị làm tròn khi bind từ giá trị scale cao hơn; API phải validate scale trước khi gọi.
- Procedure trả kết quả sau commit. Client mất response cần retry cùng key, không suy luận thất bại.
- Multi-currency, partial reversal, settlement ngân hàng, maker-checker và outbox là bài mở rộng; không được giả định đã có trong lab.
- Để reset, dùng một database lab mới hoặc tái tạo có kiểm soát bằng công cụ quản trị; wiki không cung cấp lệnh xóa database tự động.
