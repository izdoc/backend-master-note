# Tài khoản, tiểu khoản và các loại số dư

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Tách con người, quan hệ hợp đồng và số dư

`Customer` là hồ sơ khách hàng. `TradingAccount` là quan hệ tài khoản giao dịch. `SubAccount` phân tách sản phẩm/nguồn tiền theo mô hình công ty. `CustodyAccount` liên quan hoạt động lưu ký. `UserIdentity` phục vụ đăng nhập. Một người dùng có thể đại diện tổ chức hoặc được ủy quyền; không suy ra quyền giao dịch chỉ từ việc biết mã tài khoản.

## Tiền không chỉ có một con số

| Khái niệm | Ý nghĩa trong thiết kế |
|---|---|
| Booked/settled cash | Tiền đã ghi nhận theo trạng thái hoàn tất được xác định |
| Order reservation | Tiền dành cho lệnh chưa hoàn tất |
| Pending receivable/payable | Khoản sẽ nhận/trả từ giao dịch đã khớp |
| Withdrawable | Tiền được rút sau các điều kiện và nghĩa vụ |
| Buying power | Sức mua tính theo tiền và chính sách tín dụng |
| Restricted cash | Tiền bị phong tỏa vì lý do riêng |

Công thức đào tạo cho tài khoản tiền mặt đơn giản: `available = settled - open_order_hold - matched_unsettled_obligation - other_blocks`. Các bucket phải không trùng nhau. Nếu tiền khớp đã được trừ khỏi settled thì không trừ nghĩa vụ lần nữa. Sức mua có thể bao gồm hạn mức và tiền bán được phép sử dụng theo sản phẩm; đây không phải công thức chung cho mọi CTCK.

## Đi một lệnh từ đầu đến cuối

Giả lập tài khoản có 10.000.000 đồng; đặt mua 100 cổ phiếu giá 20.000, dự trù phí 0,15%: giữ 2.003.000, khả dụng còn 7.997.000. Khớp 60 ở giá 19.900: nghĩa vụ 1.195.791 gồm 1.194.000 và phí 1.791. Phần chưa khớp 40 giữ 801.200. Giữ và nghĩa vụ cộng lại 1.996.991; có thể giải phóng 6.009 nếu chính sách cho phép.

Khi hủy thành công phần còn lại, giải phóng 801.200; nghĩa vụ 1.195.791 vẫn tồn tại. Khi thanh toán, chuyển nghĩa vụ sang ghi nợ đã hoàn tất; không tiếp tục giữ cả hai bucket. Ví dụ không có thuế mua, phí khác hay cách làm tròn theo hợp đồng; production cần cấu hình đầy đủ.

## Chứng khoán cũng chia bucket

Có số lượng đã thanh toán, chờ nhận, chờ giao, giữ cho lệnh bán, cầm cố, hạn chế chuyển nhượng, và quyền chưa phân bổ. Quy tắc “có tổng tài sản 1.000 cổ phiếu nên bán được 1.000” có thể sai. Giả lập settled=1.000, blocked=200, pending_sell=300 thì bán khả dụng=500, với điều kiện pending_sell chưa bị trừ khỏi settled.

## Invariant và kiểm tra

- Không giải phóng hold chỉ vì request timeout.
- Mỗi hold có chủ sở hữu nghiệp vụ, lý do và sự kiện kết thúc.
- Tổng số dư các tiểu khoản phải đối chiếu được với sổ tổng và nguồn bên ngoài trong cùng phạm vi.
- Mọi thay đổi có transaction ID, business date, thời gian ghi nhận, actor, nguồn và liên kết reversal nếu có.

**Bài tập:** app và broker terminal đồng thời đặt mỗi lệnh cần 6 triệu khi tài khoản có 10 triệu. **Đáp án:** check và reserve phải nguyên tử trong cùng consistency boundary; hai lần đọc 10 triệu rồi trừ riêng là sai.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
