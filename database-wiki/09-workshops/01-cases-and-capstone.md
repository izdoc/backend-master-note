# 25 · Workshop, câu hỏi và capstone

[Mục lục](../INDEX.md) · [Mẫu đầu ra](02-review-templates.md)

## Sáu workshop

| Buổi | Nhiệm vụ | Tiêu chí đạt |
|---|---|---|
| 1 · Modeling | Vẽ payment/hold/journal/account | Grain, cardinality, unique scope và state rõ |
| 2 · Concurrency | Hai request cùng rút tiền | Không âm, không orphan, lỗi có giải thích |
| 3 · Retry | Gửi cùng key 20 lần, có payload khác | Một hiệu ứng; payload khác bị conflict |
| 4 · Tuning | Tra lịch sử theo account/ngày | Kết quả tương đương; có plan/IO trước sau |
| 5 · Reconciliation | Nạp sao kê trùng và late arrival | Không mất dòng; exception có owner |
| 6 · Recovery | Restore mốc chọn trước trên lab riêng | Đo đủ thời gian và kiểm tra nghiệp vụ |

## Capstone: ví thanh toán có đối soát

Thiết kế hệ thống nhiều tenant, account một currency, chuyển nội bộ, rút ra ngân hàng, phí và hold. Giả định để thảo luận: dữ liệu 24 tháng, tải đỉnh gấp 10 lần trung bình, vài account tổ chức chiếm phần lớn giao dịch. Người làm phải chọn các giá trị TPS/SLO và giải thích cách đo, không tự gọi giả định là kết quả benchmark.

Đầu ra gồm ERD, data dictionary, invariant matrix, state machine, index proposal, transaction protocol, outbox/inbox contract, archive policy, RPO/RTO, monitoring và migration plan. Có ít nhất một quyết định ADR với phương án đã loại và lý do.

### Các lỗi phải thử

1. Client mất response sau commit.
2. Callback đến hai lần và callback đến ngược thứ tự.
3. Hai transfer ngược chiều cùng account.
4. Worker outbox chết sau publish.
5. Sao kê thiếu dòng nhưng tổng tiền tình cờ không đổi.
6. Backfill chạy trong lúc writer đang cập nhật.
7. Replica chậm, client vừa ghi xong chuyển sang đọc replica.
8. Mất key mã hóa hoặc credential khi restore.

### Rubric 100 điểm

| Nhóm | Điểm | Bằng chứng |
|---|---:|---|
| Mô hình và invariant | 25 | Constraint + transaction + quyền ghi |
| Concurrency/idempotency | 25 | Kịch bản nhiều session và retry |
| Hiệu năng | 20 | Dataset, parameter, actual plan, IO/CPU |
| Vận hành/bảo mật | 20 | Restore drill, quyền, alert, runbook |
| Khả năng giải thích | 10 | ADR, nguồn, giới hạn và trade-off |

## Mười câu hỏi tự kiểm tra có đáp án

1. **Balance có thể là projection không?** Có, nhưng cần ledger nguồn và protocol cập nhật/rebuild nhất quán.
2. **Có PK thì khỏi unique reference?** Không; hai khóa giải quyết hai vấn đề.
3. **RCSI có ngăn hai writer chi vượt không?** Không tự động; vẫn cần write protocol.
4. **Timeout nghĩa là thất bại?** Có thể chưa biết; query/retry cùng key.
5. **Seek luôn nhanh hơn scan?** Không; phụ thuộc số page/dòng và lookup.
6. **Thêm index có miễn phí với ghi?** Không; tăng cập nhật, log và storage.
7. **Partition có thay index không?** Không; xem pruning và workload.
8. **Read replica thay backup không?** Không; sai dữ liệu có thể được replicate.
9. **CDC có thay domain event không?** Không tự động; row change thiếu ý nghĩa nghiệp vụ.
10. **Báo cáo tổng khớp là đủ?** Không; sai lệch ngược dấu có thể triệt tiêu nhau.

## Gợi ý giảng viên

Yêu cầu học viên giải thích một failure timeline và nơi bảo vệ invariant, không chỉ đọc định nghĩa. Nếu chưa có SQL Server, thực hiện review thiết kế và chuẩn bị script; đánh dấu concurrency/performance/restore là chưa kiểm chứng cho đến khi chạy trên engine thật.
