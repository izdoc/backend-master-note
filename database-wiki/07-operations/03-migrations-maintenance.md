# 21 · Migration và bảo trì không làm đứt dịch vụ

[Mục lục](../INDEX.md)

## Expand → migrate → contract

Ví dụ cần tách `FullName` thành cấu trúc mới:

1. **Expand:** thêm cột/bảng mới tương thích phiên bản ứng dụng cũ; xác nhận DDL lock và thời gian trên dữ liệu đại diện.
2. **Migrate:** deploy code hỗ trợ chuyển tiếp, backfill theo key range nhỏ, có checkpoint và đối soát.
3. **Cutover:** chuyển đường đọc/ghi, theo dõi và giữ đường quay lại trong thời gian đã chốt.
4. **Contract:** chỉ bỏ cột cũ khi mọi writer/reader/job/export đã chuyển và rollback window kết thúc.

Không mặc định “thêm cột là tức thì”. Default, nullability, index, engine/version và kích thước bảng ảnh hưởng cách thực thi. Transactional DDL cũng có thể giữ khóa lâu.

## Backfill có thể chạy lại

Batch theo PK ổn định, ghi checkpoint sau commit, xử lý khi batch chạy lại và kiểm soát tốc độ theo tải. `TOP` không có order không đảm bảo thứ tự mong muốn. Không dùng OFFSET tăng dần khi chính batch đang thay đổi tập lọc; có thể bỏ sót dòng.

Dual write có rủi ro lệch nếu hai nơi không cùng transaction. Nếu bắt buộc, ghi rõ nguồn ưu tiên, cơ chế sửa lệch và mốc dừng. Backfill chạy cùng writer cần version/condition để tránh ghi đè dữ liệu mới bằng bản cũ.

## Deploy gate

Review migration phải có: lượng dòng, thời gian dự kiến từ rehearsal, lock/log/tempdb headroom, ảnh hưởng replica, khả năng rollback và kiểm tra sau deploy. Backup trước deploy là cần trong một số quy trình nhưng không phải rollback tức thì; restore có thể mất dữ liệu mới và vượt RTO.

Ứng dụng nhiều instance không nên cùng tự chạy migration lớn lúc startup. Chọn một deployment identity và một tiến trình có kiểm soát. Script thay đổi schema phải được version control và liên kết release.

## Bảo trì dựa trên bằng chứng

- Integrity check có lịch và kế hoạch xử lý lỗi, không chỉ job báo xanh.
- Statistics được kiểm tra theo thay đổi dữ liệu/query; không mặc định FULLSCAN mọi bảng.
- Index maintenance xét page density, kích thước và workload, cùng chi phí log/replication.
- File growth dự báo và thử; không shrink định kỳ như một cách “tối ưu”.
- Thử restore sau thay đổi mã hóa/key và sau thay đổi hạ tầng quan trọng.

**Bài tập:** thêm unique key vào bảng callback có duplicate sẵn. Đáp án: thống kê và phân loại duplicate, sửa theo nghiệp vụ có audit, chặn duplicate mới, rồi triển khai constraint; không xóa tùy ý một dòng theo `ROW_NUMBER()` mà bỏ qua side effect đã phát sinh.
