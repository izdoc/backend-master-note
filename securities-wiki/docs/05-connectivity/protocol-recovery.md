# FIX, sequence, recovery và idempotency

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## FIX là kiến thức chung, không phải lời khẳng định về wire protocol KRX

FIX phân biệt session với application. Session xử lý kết nối và khả năng khôi phục trao đổi bản tin; application biểu diễn nghiệp vụ. Bộ chuẩn mô tả sequence, resend và xử lý khả năng bản tin lặp [S13]. Venue có dialect và quy định riêng. Chỉ triển khai theo đặc tả được cấp, không giả định chuẩn FIX chung là đủ chứng nhận.

## Kịch bản mất acknowledgement

Gateway ghi ý định gửi O123; gửi ra mạng; Sở chấp nhận; phản hồi bị mất; OMS timeout. Có hai thực tế hợp lệ: bên ngoài chưa nhận, hoặc đã nhận nhưng phản hồi không đến. Timeout không phân biệt được chúng. Gửi lại một lệnh mới có thể làm khách mua hai lần.

Thiết kế: durable outbound journal; trạng thái UNKNOWN; khôi phục session theo contract; xử lý response/truy vấn/đối chiếu bằng ID ổn định; chỉ phát lệnh kinh tế mới khi có cơ sở. Recovery protocol không phải generic HTTP retry với exponential backoff.

## Sequence không bằng execution ID

Sequence dùng để kiểm tra chuỗi trong một phiên/luồng. Execution ID nhận diện sự kiện kinh tế theo phạm vi mà đối tác quy định. `session+seq` có thể giúp chống lặp delivery nhưng không đủ chống ghi tiền hai lần nếu cùng execution xuất hiện qua đường replay hoặc báo cáo khác.

Thực hiện inbox với khóa dedup nghiệp vụ, payload hash và trạng thái áp dụng. Nếu cùng key mà payload khác, đưa vào conflict workflow. Nếu đúng bản lặp, ghi nhận delivery mà không áp dụng tiền/chứng khoán lần nữa. Giao dịch database phải bao trùm dedup marker và economic effect.

## Outbox và giới hạn “exactly once”

Transaction lưu order/reservation cùng outbox đảm bảo ý định phát không bị rơi giữa database và message bus. Publisher có thể phát trùng khi crash sau send trước mark-sent. Consumer vẫn cần idempotency. “Broker hỗ trợ exactly-once” không tự tạo đúng một tác động trên ngân hàng, Sở, SMS và SQL Server cùng lúc.

## Chuyển ngày

Business date, session epoch và UTC timestamp có mục đích khác nhau. Sequence có thể reset theo quy định phiên; execution ID cũng có thể chỉ duy nhất theo ngày. Dedup key phải đủ scope. Không xóa inbox lúc 00:00 chỉ vì đã sang ngày dân sự, trong khi bản tin cuối ngày hoặc replay còn đến.

**Bài tập:** crash sau cập nhật cash nhưng trước lưu processed-event. **Đáp án:** nếu hai thao tác không nguyên tử, replay sẽ ghi tiền lần nữa. Đưa vào cùng transaction hoặc dùng cơ chế equivalent được chứng minh qua crash test.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S13, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
