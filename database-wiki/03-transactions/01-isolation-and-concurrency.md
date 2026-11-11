# 09 · Transaction, isolation và cập nhật đồng thời

[Mục lục](../INDEX.md)

## Read-check-write là một vùng nguy hiểm

Hai request cùng đọc balance 100, cùng thấy đủ để trừ 80, rồi đều ghi. Kiểm tra ở C# trước `UPDATE` không bảo vệ được invariant nếu không có concurrency protocol.

Với một ví không cho âm và không có hold, conditional update là ví dụ đơn giản:

```sql
UPDATE Finance.Account
SET Balance = Balance - @Amount
WHERE AccountId = @AccountId
  AND @Amount > 0
  AND Balance >= @Amount;

IF @@ROWCOUNT <> 1
    THROW 51000, N'Không đủ điều kiện ghi nợ', 1;
```

Đây chỉ là một bước; khi chuyển tiền phải cập nhật hai ví, journal và idempotency trong cùng transaction. Nếu có hold/limit ở bảng khác, phép kiểm tra một dòng trên không đủ.

## Chọn isolation theo yêu cầu đọc

| Chế độ SQL Server | Đặc tính cần hiểu | Hệ quả thiết kế |
|---|---|---|
| READ COMMITTED kiểu khóa | Không đọc dirty data, lần đọc sau có thể khác | Không bảo vệ cả chuỗi read-check-write |
| READ COMMITTED với RCSI | Snapshot ở cấp statement | Hai SELECT trong transaction có thể thấy hai mốc |
| SNAPSHOT | Snapshot cấp transaction; có thể xung đột update | Có retry; write skew vẫn cần xử lý invariant |
| SERIALIZABLE | Bảo vệ phạm vi truy cập bằng cơ chế khóa phù hợp | Giảm concurrency, cần index và transaction ngắn |

`NOLOCK`/READ UNCOMMITTED có thể đọc dữ liệu chưa commit và kết quả không ổn định. Không dùng để tính tiền, tồn kho khả dụng hoặc đối soát. RCSI giảm một số tranh chấp đọc/ghi nhưng writer vẫn có thể chặn writer; nó không tự ngăn chi vượt số dư.

## Optimistic và pessimistic

Optimistic: đọc `rowversion`, update với `WHERE Version = @ExpectedVersion`, báo conflict nếu 0 dòng. Phù hợp chỉnh profile/record ít tranh chấp; không tự retry mù với dữ liệu người dùng đã cũ.

Pessimistic: giữ khóa trước khi ra quyết định trong transaction. `UPDLOCK, HOLDLOCK` có thể dùng cho pattern cụ thể; phải có index hỗ trợ phạm vi và cùng quy tắc cho mọi writer. Hint không thay thế thiết kế transaction.

## Transaction boundary

Giữ transaction ngắn; không chờ HTTP, email hoặc thao tác người dùng bên trong. Dùng `SET XACT_ABORT ON`, `TRY/CATCH`, rollback khi `XACT_STATE() <> 0`, rồi `THROW`. Xác định rõ procedure sở hữu transaction hay tham gia transaction caller; lab chọn sở hữu và từ chối ambient transaction.

**Bài tập:** hai session cùng trừ 80 từ 100. Kết quả nghiệm thu: chỉ một giao dịch được commit, balance 20, một journal; thất bại không để lại entry mồ côi.

Nguồn: [Microsoft — locking and row versioning](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-transaction-locking-and-row-versioning-guide?view=sql-server-ver16). Bảng là tóm tắt; hành vi cụ thể còn phụ thuộc isolation, statement và engine configuration.
