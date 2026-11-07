# Sản phẩm: cổ phiếu, trái phiếu, quỹ, chứng quyền, phái sinh

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Sở hữu, cho vay và hợp đồng rủi ro

Cổ phiếu thể hiện quyền lợi của cổ đông. Trái phiếu tạo quan hệ chủ nợ với nghĩa vụ theo điều kiện phát hành. Chứng chỉ quỹ là phần vốn trong quỹ; ETF có cơ chế hoán đổi và giao dịch thứ cấp theo cấu trúc sản phẩm. Chứng quyền có bảo đảm có thời hạn, giá thực hiện, tỷ lệ chuyển đổi và rủi ro tổ chức phát hành. Hợp đồng tương lai là cam kết theo đặc tả hợp đồng, được quản lý vị thế và ký quỹ.

| Sản phẩm | Dữ liệu bắt buộc trong mô hình | Rủi ro dễ bỏ sót |
|---|---|---|
| Cổ phiếu | Mã, thị trường, đơn vị giá, trạng thái giao dịch, quyền | Pha loãng, hạn chế chuyển nhượng, thanh khoản |
| Trái phiếu | Mệnh giá, coupon, lịch trả, day-count, đáo hạn, điều kiện mua lại | Vỡ nợ, tái đầu tư, giá sạch/giá bẩn |
| ETF | NAV, iNAV nếu có, rổ hoán đổi, đơn vị tạo lập | Tracking error, premium/discount |
| Chứng quyền | Tài sản cơ sở, strike, ratio, expiry, phương thức thực hiện | Đòn bẩy, mất toàn bộ phí mua, phòng ngừa rủi ro |
| Hợp đồng tương lai | Underlying, multiplier, maturity, settlement method | Variation margin, expiry, thanh khoản vị thế |

## Ví dụ tính toán do wiki đặt ra

- Mua 100 cổ phiếu giá 25.000 đồng: giá trị trước phí = 2.500.000 đồng. Giá tăng 1.000 đồng tạo lãi chưa thực hiện 100.000 đồng; chưa tính phí, thuế, vốn vay.
- Một trái phiếu giả lập mệnh giá 100 triệu, coupon 8%/năm, trả một lần mỗi năm: coupon năm = 8 triệu. Lãi suất thị trường tăng thường làm giá trái phiếu lãi cố định giảm, nhưng cần lịch dòng tiền và spread để định giá cụ thể.
- Chứng quyền mua giả lập: giá thanh toán cơ sở 60.000, strike 50.000, ratio 5:1; giá trị thực hiện lý thuyết mỗi chứng quyền = max(60.000−50.000,0)/5 = 2.000. Lợi nhuận còn phải trừ giá mua và chi phí.
- Hợp đồng tương lai giả lập multiplier 100.000 đồng/điểm: long 2 hợp đồng, tăng 5 điểm tạo 1 triệu đồng trước chi phí. Multiplier này là giả định bài tập, không thay thế đặc tả hợp đồng đang niêm yết.

## Thiết kế sản phẩm

Đừng tạo bảng `Stock` rồi nhét mọi tài sản vào đó. Có `Instrument` với khóa nội bộ bất biến; thuộc tính chung gồm loại, tiền tệ, trạng thái, thị trường và ngày hiệu lực. Thuộc tính riêng đặt trong cấu trúc phù hợp. `symbol` có thể thay đổi; một lịch sử chuyển sàn không nên làm đứt lịch sử sở hữu.

Mỗi sản phẩm cần product approval: đối tượng khách hàng, điều kiện được giao dịch, risk model, booking, fee/tax, settlement, reporting, vận hành sự cố và khách hàng được cung cấp thông tin gì. Tách việc “hệ thống có thể biểu diễn” khỏi “công ty được phép cung cấp”.

**Câu hỏi:** cùng có mã giao dịch thì cổ phiếu và hợp đồng tương lai có dùng chung bảng số dư không? **Đáp án:** có thể dùng một lớp định danh chung, nhưng vị thế, nghĩa vụ, ký quỹ và vòng đời phải được mô hình riêng.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
