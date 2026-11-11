# 11 · Đo trước, đọc plan, rồi mới sửa

[Mục lục](../INDEX.md) · [Lab tuning](../10-labs/04-query-tuning.sql)

## Quy trình sáu bước

1. Chốt SQL, parameter, thời điểm, số dòng trả về, tải đồng thời và SLO bị vi phạm.
2. Xác định chậm ở database, network, connection pool hay xử lý application.
3. Thu actual execution plan trong môi trường kiểm soát, Query Store lịch sử và `STATISTICS IO/TIME`.
4. Đặt giả thuyết cụ thể: lookup quá nhiều, estimate sai, spill, blocking hoặc đọc vượt nhu cầu.
5. Thay một yếu tố, kiểm tra kết quả rồi đo lại nhiều nhóm tham số.
6. Đánh giá chi phí ghi/dung lượng và cách rollback; theo dõi sau rollout.

```sql
SET STATISTICS IO ON;
SET STATISTICS TIME ON;
-- Chạy SELECT với tham số đại diện, bật actual plan trong SSMS.
-- Không chạy câu DML chỉ để lấy actual plan trên dữ liệu thật.
SET STATISTICS TIME OFF;
SET STATISTICS IO OFF;
```

Không dùng `DBCC DROPCLEANBUFFERS` hoặc xóa toàn plan cache trên server dùng chung để tạo benchmark. Lab cold cache và warm cache phải được mô tả riêng; latency của một lần chạy không đủ kết luận.

## Đọc plan theo luồng dữ liệu

Tìm operator xử lý nhiều dòng, so estimated với actual rows và số lần thực thi. Đọc predicate, residual predicate, key lookup, sort, hash, memory grant, spill và implicit conversion. Phần trăm cost trên plan chủ yếu là ước lượng, không phải đồng hồ đo thời gian từng operator.

Seek vẫn có thể đọc nhiều page nếu khoảng tìm quá rộng; scan có thể hợp lý khi cần phần lớn bảng. Nested loops tốt khi outer nhỏ, nhưng inner lookup lặp hàng triệu lần có thể đắt. Hash join không mặc định xấu; kiểm tra dữ liệu đầu vào và spill.

## Bảng kết quả cần ghi

| Dữ liệu | Trước | Sau | Điều kiện |
|---|---|---|---|
| Logical reads | Điền đo thực tế | Điền đo thực tế | Cùng tham số và dataset |
| CPU/elapsed | Điền | Điền | Nêu concurrency và cache |
| Rows/hash kết quả | Điền | Điền | Kết quả phải tương đương |
| p95/p99 | Điền | Điền | Tính từ request-level samples |
| Insert/update throughput | Điền | Điền | Kiểm tra chi phí index mới |

Không có số benchmark sẵn trong wiki; không diễn giải câu SQL minh họa thành cam kết nhanh hơn X lần.

## Kinh nghiệm xử lý

Ưu tiên query theo tổng tài nguyên và ảnh hưởng nghiệp vụ: query 5 ms chạy một triệu lần có thể đáng tối ưu hơn báo cáo 10 giây chạy mỗi tuần. Nếu elapsed cao nhưng CPU thấp, tìm wait trước khi thêm index. Chụp bằng chứng trước khi restart làm mất dữ liệu chẩn đoán.

Nguồn: [Query Store best practices](https://learn.microsoft.com/en-us/sql/relational-databases/performance/best-practice-with-the-query-store?view=sql-server-ver16). Quy trình benchmark và mẫu báo cáo là đề xuất của wiki.
