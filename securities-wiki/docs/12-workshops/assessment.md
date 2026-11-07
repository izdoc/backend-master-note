# Bộ 30 câu hỏi vấn đáp và đáp án

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


| # | Câu hỏi | Đáp án cốt lõi |
|---:|---|---|
| 1 | Thị trường sơ cấp khác thứ cấp? | Sơ cấp huy động vốn qua phát hành; thứ cấp trao đổi tài sản đã phát hành. |
| 2 | Khớp lệnh đã có cổ phiếu bán ngay? | Chưa đủ kết luận; còn settlement, bucket và điều kiện sản phẩm. |
| 3 | VSDC có phải order matching engine? | Không đánh đồng chức năng lưu ký/bù trừ/thanh toán với khớp tại Sở. |
| 4 | KRX có nghĩa tự động được T+0? | Không; phải có quy định và thông báo triển khai sản phẩm. |
| 5 | LO có đảm bảo khớp? | Không; chỉ giới hạn mức giá chấp nhận. |
| 6 | ATO/ATC luôn ưu tiên mọi LO? | Không; xem quy tắc ưu tiên hiện hành và LO trần/sàn nhập trước. |
| 7 | MAK khác MOK? | MAK cho phép khớp phần rồi hủy dư; MOK yêu cầu toàn bộ theo điều kiện. |
| 8 | Last price có phải ask tốt nhất? | Không; một bên là giao dịch đã xảy ra, bên kia là cung chờ. |
| 9 | VWAP có phải tick hợp lệ? | Không nhất thiết. |
| 10 | Mất response có nên gửi order ID mới? | Không nếu chưa xác minh ý định cũ có được thực hiện không. |
| 11 | Cancel pending đã được giải tiền? | Chưa; cần xác nhận đủ cơ sở cho phần dư. |
| 12 | Seq number có thay execution ID? | Không; phạm vi và ý nghĩa khác nhau. |
| 13 | Vì sao cần payload hash cho idempotency? | Phát hiện cùng key nhưng nội dung khác. |
| 14 | Outbox đảm bảo mọi thứ exactly-once? | Không; vẫn có delivery trùng và external effects cần dedup. |
| 15 | Snapshot100 nhận delta103 thì sao? | Phát hiện gap, đánh dấu chưa đồng bộ và recovery theo contract. |
| 16 | Có nên giữ hàng đợi websocket vô hạn? | Không; bounded buffer, slow-consumer policy, resnapshot. |
| 17 | Sức mua và tiền được rút có giống nhau? | Không; sức mua có thể liên quan tín dụng hoặc khoản phải thu theo sản phẩm. |
| 18 | Giá trị tài sản lớn có chắc đủ thanh khoản? | Không; cần nguồn tiền đến đúng hạn và tài sản có khả năng chuyển thành tiền. |
| 19 | T+2 có phải 48 giờ? | Không; lịch ngày làm việc thanh toán. |
| 20 | Tổng tiền khớp đủ là đối soát đủ? | Không; phải khớp ID, lượng, giá trị và trạng thái. |
| 21 | Cổ tức cổ phiếu công bố là sellable? | Chưa; còn phân bổ, lưu ký và điều kiện giao dịch. |
| 22 | Backup restore xong là DR hoàn tất? | Không; phải reconcile external effects và phục hồi nghiệp vụ. |
| 23 | RPO bằng 0 có đủ chống double payment? | Không; idempotency và ownership vẫn cần. |
| 24 | TTL cache là business policy? | Không; cần rule về chất lượng dữ liệu và cách dùng khi stale. |
| 25 | Có được dùng dữ liệu khách thật trong wiki công khai? | Không; dùng synthetic, không lộ định danh/credential. |
| 26 | Ai phê duyệt tăng hạn mức? | Role có thẩm quyền theo policy; không phải ai có quyền SQL. |
| 27 | Rule cùng số văn bản có thể khác? | Có; cần cơ quan, số, năm, ngày và phiên bản. |
| 28 | Thông tư đã ban hành là active ngay? | Không; kiểm tra ngày hiệu lực và điều khoản chuyển tiếp. |
| 29 | Mọi CTCK phải dùng microservices? | Không; chọn theo invariant, tải, đội ngũ và yêu cầu vận hành. |
| 30 | Go/no-go nên dựa vào gì? | Bằng chứng dữ liệu/kết nối/control, rủi ro còn lại và người chịu trách nhiệm. |

Cách dùng: người học trả lời trước khi mở cột đáp án; yêu cầu thêm một ví dụ và một failure mode cho mỗi câu. Đây là bộ đánh giá đào tạo nội bộ, không phải ngân hàng câu hỏi chứng chỉ chính thức.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
