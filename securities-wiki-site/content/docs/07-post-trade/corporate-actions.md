# Lưu ký, thực hiện quyền và chuyển khoản chứng khoán

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Ba ngày dễ nhầm

Ngày giao dịch không hưởng quyền liên quan việc giao dịch có kèm quyền hay không; ngày đăng ký cuối cùng xác định danh sách theo cơ chế áp dụng; ngày thanh toán/thực hiện là khi lợi ích được phân bổ theo thông báo. Ngày được hưởng không đồng nghĩa tiền đã sẵn sàng rút hoặc cổ phiếu mới đã được giao dịch.

## Các loại sự kiện

Cổ tức tiền, cổ tức cổ phiếu, cổ phiếu thưởng, quyền mua, tách/gộp, chuyển đổi, sáp nhập, hủy niêm yết và thay đổi mã có tác động khác nhau. Event model cần `eventId`, instrument, dates, ratio/cash amount, rounding, election deadline, restriction, source, revision và trạng thái phê duyệt.

## Ví dụ quyền mua giả lập

Khách có 1.000 cổ phiếu đủ điều kiện; tỷ lệ 5:1 → có quyền mua 200 cổ phiếu. Giá đăng ký 10.000 → cần 2 triệu trước hạn theo quy trình. Các trạng thái: entitlement calculated → notified → subscribed → funds reserved/paid → allocated → tradable khi đủ điều kiện. Không ghi 200 cổ phiếu vào sellable ngay lúc khách đăng ký.

Khách có 1.003 cổ phiếu cần áp dụng quy tắc xử lý phần lẻ trong thông báo. Không tự chọn floor hay round theo tiện lợi. Sự kiện bị sửa tỷ lệ sau khi đã phân bổ cần delta/reversal có kiểm soát, không chạy lại batch và cộng thêm một lần.

## Điều chỉnh giá và chart

Giá tham chiếu điều chỉnh quyền và dữ liệu chart adjusted phục vụ mục đích khác nhau. Duy trì raw OHLC và factor lịch sử có version. Backtest dùng giá đã điều chỉnh nhưng không điều chỉnh lượng/tiền quyền tương ứng có thể tạo lợi nhuận giả.

## Chuyển khoản và phong tỏa

Chuyển chứng khoán giữa nơi lưu ký có trạng thái yêu cầu, kiểm tra khả dụng, giữ lượng, gửi điện, chờ xác nhận, hoàn tất hoặc từ chối. Một vị thế bị phong tỏa không được tính như tài sản bán tự do. Nếu timeout chưa xác nhận, giữ trạng thái chờ tra soát; không giải tỏa cả hai đầu.

## Kiểm soát batch

Khóa idempotency theo event + account + component + revision; kiểm tra control totals về tổng người hưởng, lượng, tiền và phần lẻ. Người lập và người duyệt kiểm tra nguồn, ngày, tập khách, kết quả thử trước khi ghi sổ. Quyền không chỉ là một job chạy lúc nửa đêm.

**Bài tập:** nhận cùng file cổ tức hai lần, tên file khác. **Đáp án:** dedup theo identity nghiệp vụ và nội dung/phiên bản, không chỉ filename. Tên khác có thể cùng sự kiện hoặc bản điều chỉnh cần xử lý riêng.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S11, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
