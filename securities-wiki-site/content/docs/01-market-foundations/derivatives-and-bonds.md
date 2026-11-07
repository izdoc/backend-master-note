# Phái sinh, trái phiếu và các dòng nghiệp vụ mở rộng

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Phái sinh: vị thế thay cho sở hữu cổ phiếu

Với hợp đồng tương lai, cần quản lý long/short, open/close, giá thanh toán, lãi lỗ hằng ngày, tài sản ký quỹ, nghĩa vụ bổ sung, giới hạn vị thế và đáo hạn. Không lấy logic “mua xong chờ cổ phiếu về” áp vào mọi hợp đồng. Từng hợp đồng có multiplier, bước giá, expiry calendar và phương thức settlement riêng.

Ví dụ giả lập long 3 hợp đồng ở 1.200, multiplier 100.000 đồng/điểm; giá dùng cho bài tập cuối ngày 1.190: lỗ = (1.190−1.200)×3×100.000 = 3 triệu. Nếu trước đó có 10 triệu tiền bảo đảm và không có yếu tố khác thì còn 7 triệu sau khoản lỗ này. Có bị yêu cầu bổ sung không phụ thuộc yêu cầu ký quỹ và các nghĩa vụ thực tế, không chỉ số dư dương.

Danh mục cần đánh giá intraday, không đợi batch cuối ngày. Khi force close, phải xét thanh khoản và trạng thái thị trường; một vị thế vượt giới hạn không tự biến mất vì hệ thống gửi lệnh đóng. Theo dõi closing order riêng với position remaining.

## Trái phiếu: lịch dòng tiền và đối tượng giao dịch

Bond master cần mệnh giá, số lượng, giá mua, coupon fixed/floating, reference rate/spread, day-count, lịch trả, maturity, quyền mua lại và điều kiện sản phẩm. Tách clean price khỏi accrued interest và dirty price. Ví dụ giả lập clean price 98 triệu + accrued 1 triệu = dirty 99 triệu; không được vừa dùng dirty rồi cộng accrued lần nữa.

Trái phiếu Chính phủ, doanh nghiệp niêm yết và doanh nghiệp riêng lẻ không có cùng điều kiện người mua, cơ chế giao dịch và settlement. Không dùng bộ rule cổ phiếu để cho phép giao dịch trái phiếu. Các điều kiện pháp lý chi tiết cần được owner sản phẩm/pháp chế xác nhận.

## Repo, vay chứng khoán và bán khống

Repo gồm bán và cam kết mua lại theo hợp đồng; cần cả hai chân, giá trị tài sản, haircut, lãi/repo rate, margin maintenance và xử lý vi phạm. Securities lending có lender, borrower, tài sản cho vay, phí, collateral, recall và return. Việc tồn tại cơ chế vay chứng khoán không đồng nghĩa mọi khách hàng được tự do bán khống trên mọi thị trường.

## Quỹ mở và ETF

Quỹ mở có dealing calendar, cutoff, NAV áp dụng, subscription/redemption, phí và thời gian thanh toán theo tài liệu sản phẩm. ETF có giao dịch thứ cấp và cơ chế creation/redemption theo lô/đối tượng phù hợp. Dịch vụ phân phối phải phân biệt “nhận yêu cầu” với “được áp NAV” và “hoàn tất phân bổ”.

## Thuế và phí

Cấu hình theo loại khách, cư trú/tư cách, sản phẩm, giao dịch, ngày hiệu lực, cơ sở tính, thời điểm ghi nhận và làm tròn. Bài tập wiki dùng phí giả lập; không coi đó là biểu thuế. Finance/Tax owner phải phê duyệt rate table và test; báo cáo gross, fee, tax và net phải đối chiếu được.

**Bài tập:** dùng `profit = currentPrice - costPrice` cho tất cả sản phẩm. **Đáp án:** thiếu số lượng, multiplier, accrued, coupon, FX, realized/unrealized, variation margin, phí và các yếu tố đặc thù.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
