# 13 · Các mẫu SQL ảnh hưởng lớn đến hiệu năng

[Mục lục](../INDEX.md)

## SARGability: để engine tìm trong index

```sql
-- Thường khó tận dụng trực tiếp index thời gian:
WHERE YEAR(CreatedAt) = @Year

-- Viết rõ khoảng thời gian, @From/@To cùng kiểu với cột:
WHERE CreatedAt >= @From AND CreatedAt < @To
```

Khoảng nửa mở tránh phải đoán thời điểm cuối ngày của `datetime`/`datetime2`. Không cam kết mọi biểu thức có hàm đều scan: optimizer có các phép biến đổi; xác nhận bằng plan và reads.

Tránh implicit conversion trên cột do parameter sai kiểu/độ dài hoặc join mã số dạng string với integer. `LIKE '%abc%'` thường không tìm được theo prefix B-tree; cân nhắc full-text/search theo yêu cầu, có đánh giá ngữ nghĩa tìm kiếm.

## Join đúng cardinality

Nếu cần biết customer có payment hay không, dùng `EXISTS` thay vì join rồi `DISTINCT` để xóa trùng. Nếu join payment với cả attempts và fee lines đều một-nhiều, số dòng có thể nhân chéo; aggregate từng nhánh về đúng grain trước khi join.

`UNION ALL` tránh bước loại trùng khi nghiệp vụ chấp nhận toàn bộ dòng. `UNION` đúng khi cần tập duy nhất, không thay chỉ vì muốn nhanh. `NOT EXISTS` thường diễn đạt anti-join rõ; `NOT IN` có NULL trong tập con có thể cho kết quả khác mong đợi.

## Phân trang

```sql
-- Trang tiếp, sắp xếp DESC; cursor lấy từ dòng cuối trang trước.
WHERE TenantId = @TenantId
  AND AccountId = @AccountId
  AND (CreatedAt < @LastTime
       OR (CreatedAt = @LastTime AND PaymentId < @LastId))
ORDER BY CreatedAt DESC, PaymentId DESC;
```

Kết hợp `TOP (@PageSize)` và index phù hợp. Keyset tránh phải bỏ qua rất nhiều dòng như trang OFFSET sâu, nhưng không tự tạo snapshot lịch sử bất biến nếu dữ liệu bị sửa hoặc insert hồi tố. Khi export cần tập ổn định, xác định snapshot/watermark và tie-breaker riêng.

## Batch và temporary table

Xử lý set-based thường giảm round-trip so với vòng lặp từng dòng. Batch vẫn cần giới hạn log, lock và thời gian transaction. CTE không mặc định materialize; query phức tạp dùng lại tập trung gian có thể hưởng lợi từ temp table có index/statistics, đổi lại tốn tempdb.

Đừng ép một SELECT khổng lồ bằng mọi giá. Chia bước khi giúp estimate và kiểm soát tập dữ liệu, sau đó đo toàn bộ pipeline, kể cả tạo temp table. Table variable không đồng nghĩa “chỉ ở RAM”; hành vi estimate khác theo version/compatibility.

**Bài tập:** tổng payment bị gấp ba khi thêm join attempt. Đáp án: sửa grain hoặc aggregate attempt trước; `SUM(DISTINCT Amount)` có thể làm mất hai payment hợp lệ cùng số tiền.
