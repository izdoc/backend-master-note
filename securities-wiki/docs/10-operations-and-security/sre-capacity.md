# SRE, SLO và capacity planning

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Đo theo hành trình nghiệp vụ

API availability không bằng trading availability. Đo tỷ lệ lệnh hợp lệ được nhận và xử lý trong thời hạn, độ trễ từ nhận tới gateway/ack, tuổi lệnh UNKNOWN, thời gian cập nhật fill, độ trễ bảng giá và thời gian hoàn tất đối soát. Tách reject nghiệp vụ dự kiến khỏi lỗi kỹ thuật nhưng vẫn theo dõi tăng bất thường của cả hai.

## Ví dụ ngân sách độ trễ

SLO nội bộ minh họa cho bước nhận lệnh: p99 ≤200 ms tại tải thiết kế, không bao gồm thời gian phản hồi Sở. Dự toán: auth 20 ms, risk/reservation 70 ms, persistence/outbox 40 ms, network và dư địa 70 ms. Đây là mục tiêu giả lập để luyện, không phải số đo của SSI/DNSE/TCBS hoặc cam kết Sở.

Không cộng p99 của từng thành phần và coi luôn là p99 end-to-end; phân phối và tương quan ảnh hưởng kết quả. Đo distributed trace, histogram và tail latency thực tế.

## Capacity model

Giả lập peak 10.000 request/s, trung bình hệ thống giữ request 0,08 s → khoảng 800 request đồng thời theo quan hệ throughput × thời gian trong trạng thái ổn định. Nếu downstream chậm thành 2 s thì nhu cầu đang xử lý có thể lên 20.000 trước khi xét backlog. Vì vậy cần queue bound, timeout semantics, admission control và degradation policy.

Phân biệt order entry, cancel storm, execution burst, market data ticks và websocket fan-out. 100.000 người online không có nghĩa 100.000 lệnh/giây; một tick có thể nhân thành nhiều lượt gửi.

## Dashboard ca trực

Theo dõi session health, last sequence, last ack age, queue depth/oldest age, UNKNOWN count, reject rate theo mã lỗi, ledger lag, reconciliation breaks, price staleness, DB log latency và chứng thư sắp hết hạn. Mọi alert cần owner, mức độ, runbook và điều kiện đóng; không báo từng retry đơn lẻ như sự cố toàn hệ thống.

## Test tải có ý nghĩa

Mô phỏng mở cửa/đóng cửa, một số mã và tài khoản rất nóng, burst hủy/sửa, mất upstream, slow consumer, replay, disk chậm, hết connection pool và backlog recovery. Sau test, kiểm tra invariant tài sản và đối soát; throughput đẹp nhưng duplicate fill là thất bại.

**Bài tập:** 99,99% uptime nhưng downtime đúng 5 phút ATC. **Đáp án:** số uptime tháng che rủi ro theo phiên; cần SLO trọng yếu theo cửa sổ kinh doanh và đánh giá ảnh hưởng khách hàng.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
