# 16 · Báo cáo, warehouse và dự báo tăng trưởng

[Mục lục](../INDEX.md)

## Chốt grain trước SUM

Grain là một dòng đại diện điều gì: một payment, một entry, một account mỗi ngày hay một coverage mỗi kỳ. Join sai grain có thể nhân tổng tiền mà SQL vẫn chạy thành công.

Trong star schema, fact ghi đại lượng theo grain, dimension mô tả customer, product, branch và calendar. Dimension cần lịch sử loại SCD2 khi muốn báo cáo theo thuộc tính tại thời điểm cũ; join bằng hiệu lực và tránh khoảng chồng lấn. Dimension “hiện tại” và “tại thời điểm giao dịch” phục vụ hai câu hỏi khác nhau.

Balance là đại lượng tại một thời điểm, không cộng qua nhiều ngày như doanh số. Daily snapshot cuối ngày hữu ích, nhưng phải ghi timezone, cut-off và trạng thái chốt. Không cộng VND với USD vào một tổng tiền không có tỷ giá và ngày quy đổi.

## Pipeline báo cáo có contract

Ghi source position/watermark, batch ID, schema version, số dòng nguồn/đích và tổng kiểm soát theo currency. Cần xử lý update, delete, replay và sự kiện đến muộn. “Pipeline không lỗi” không chứng minh “dữ liệu đủ”. Dashboard phải hiển thị mốc dữ liệu và tình trạng freshness.

Replica đọc giảm tải một số trường hợp nhưng có lag và vẫn có chi phí tài nguyên. Columnstore có thể phù hợp quét/tổng hợp lớn; thử trên workload riêng và đo tác động ghi nếu dùng chung bảng OLTP. Đừng đưa mọi reporting query sang replica rồi bỏ qua tính nhất quán giữa nhiều lần đọc.

## Tính dung lượng theo thành phần

```text
Tăng trưởng dữ liệu ước tính = dòng/ngày × số byte trung bình/dòng
Storage tổng dự trù = data + indexes + log peak + temp/work space
                   + backup retention + replica/archive + headroom
```

Các biểu thức là mô hình sizing, không phải số đo engine. Ví dụ giả định 10 triệu dòng/ngày × 200 byte = khoảng 2 GB/ngày theo đơn vị thập phân, trước overhead/index/compression. Lấy size thực từ mẫu production đã làm sạch để hiệu chỉnh; không nhân hệ số index tùy ý rồi coi là chính xác.

Theo dõi thêm log generation, tốc độ backup/restore, IOPS/latency và memory working set. Database vừa ổ đĩa nhưng restore mất quá RTO vẫn chưa đạt yêu cầu.

## Khi nào shard?

Trước shard, tối ưu query/index, giảm dữ liệu nóng, tách reporting và thử scale-up theo giới hạn sản phẩm. Nếu write vẫn không đáp ứng, chọn shard key theo invariant và phân bố tải. Account-based shard dễ route ví nhưng transfer cross-shard mất transaction cục bộ; cần thiết kế reserve/settle và recovery, không chỉ thêm router.

**Bài tập:** báo cáo doanh số theo chi nhánh hiện tại và chi nhánh khi phát sinh. Đáp án: định nghĩa hai report/measure riêng; sử dụng lịch sử dimension khi cần, không sửa dữ liệu cũ theo chi nhánh mới mà không nêu ngữ nghĩa.
