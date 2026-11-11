# 12 · Thiết kế index theo câu hỏi cần trả lời

[Mục lục](../INDEX.md)

## Ví dụ từ truy vấn

```sql
-- Các tên bảng/cột dưới đây là ví dụ thiết kế, không thuộc schema lab.
SELECT TOP (@PageSize) PaymentId, CreatedAt, Amount, Currency
FROM Payments.Payment
WHERE TenantId = @TenantId
  AND AccountId = @AccountId
  AND CreatedAt >= @From
  AND CreatedAt < @To
ORDER BY CreatedAt DESC, PaymentId DESC;

CREATE INDEX IX_Payment_Account_History
ON Payments.Payment
    (TenantId, AccountId, CreatedAt DESC, PaymentId DESC)
INCLUDE (Amount, Currency);
```

Đây là **ứng viên**: prefix tenant/account phục vụ equality, time phục vụ range và thứ tự trang. `PaymentId` làm tie-breaker. Cần đo actual plan và write overhead. Index này không mặc nhiên tốt cho báo cáo toàn tenant theo ngày vì account nằm trước time.

## Quyết định từng thành phần

Key quyết định cách tìm và sắp xếp. `INCLUDE` giúp có dữ liệu trả về mà không mở rộng key tìm kiếm; nó vẫn tốn storage và chi phí update. Đừng include mọi cột để đạt “covering” trên giấy.

Trong SQL Server rowstore, clustered key tham gia định vị dòng ở nonclustered index; key rộng có thể làm các index phụ lớn hơn. Chọn key ngắn, ổn định và phù hợp tải ghi. Key tăng dần giảm một số page split nhưng có thể gây tranh chấp trang cuối ở tải ghi cao; phải đo latch contention.

Filtered index hữu ích khi chỉ một phần dữ liệu thường được truy cập, ví dụ payment pending. Query phải có predicate mà optimizer chứng minh phù hợp filter; tham số hóa có thể ảnh hưởng khả năng sử dụng. Cột status thay đổi nhiều cũng làm index cập nhật nhiều.

## Những quy tắc không nên học thuộc cứng

- Không phải lúc nào cũng đặt cột có độ chọn lọc cao nhất lên đầu; xét prefix được dùng, range, ordering và các query khác.
- Không tạo index cho từng cột rồi kỳ vọng engine ghép thành index hoàn hảo.
- Missing-index recommendation thiếu bối cảnh write, overlap và các query khác; tổng hợp rồi thử.
- Usage counter có thể reset sau restart/failover; một kỳ quan sát thiếu EOD không đủ để xóa index.
- Index không thay thế constraint; unique phải xuất phát từ invariant, không chỉ hiệu năng.

## Review trước khi thêm

Liệt kê câu query mục tiêu, index đang có, estimated size, ảnh hưởng log/backup, thời gian build và rollback. Online/resumable không có nghĩa không khóa hoặc không tốn tài nguyên; kiểm tra edition/version và cửa sổ triển khai.

**Bài tập:** báo cáo lọc chỉ tenant và ngày, không account. Đáp án: đánh giá index theo `(TenantId, CreatedAt)` hoặc read model riêng; không kết luận index lịch sử account đã đáp ứng tốt.

Nguồn cấu trúc engine: [Microsoft index architecture](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-index-design-guide?view=sql-server-ver16). Ví dụ index là đề xuất riêng, cần benchmark.
