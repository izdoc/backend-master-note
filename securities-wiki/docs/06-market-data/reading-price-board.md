# Đọc bảng điện: giá, khối lượng và tín hiệu

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Một dòng bảng điện nói gì?

| Trường | Diễn giải | Sai lầm thường gặp |
|---|---|---|
| Mã, sàn, board | Danh tính công cụ và nơi giao dịch | Chỉ lưu symbol, bỏ venue/lô |
| Tham chiếu, trần, sàn | Mốc so sánh và giới hạn cho phiên/phạm vi | Tự lấy giá đóng cửa hôm qua cho mọi ngày |
| Dư mua / dư bán | Giá và lượng đang chờ được feed công bố | Hiểu là cam kết sẽ khớp mình |
| Giá/khối lượng khớp | Giao dịch đã xảy ra theo feed | Hiểu là giá có thể mua ngay |
| Tổng lượng/giá trị | Tích lũy theo phạm vi thống kê | Cộng cả lô/thỏa thuận không cùng định nghĩa |
| Cao/thấp/mở/đóng | Thống kê OHLC theo quy tắc | Trộn giá raw và adjusted |
| Nước ngoài | Mua/bán/room theo trường được công bố | Cho rằng room UI là phép cấp quyền đặt lệnh |

Màu phổ biến: xanh tăng, đỏ giảm, vàng tham chiếu, tím trần, xanh lam sàn. Màu là quy ước UI; phải có số, nhãn và trạng thái để người dùng phân biệt, kể cả người khó phân biệt màu. Đơn vị giá/khối lượng phải hiện rõ.

## Ví dụ sổ giá giả lập

Bid tốt nhất 25.000 × 1.000; ask tốt nhất 25.100 × 700; last 25.050. Spread = 100 đồng; midpoint = 25.050. Last bằng midpoint chỉ là trùng hợp. Đặt LO mua 25.000 không khớp ngay với ask 25.100. Đặt mua 1.000 ở 25.100 cũng không được đảm bảo khớp 1.000 vì top ask đang chỉ có 700 và có độ trễ.

Nếu tham chiếu 25.000 và last 25.100, mức tăng là 100 đồng = 0,4%. Giá trần/sàn cần lấy theo dữ liệu thị trường và quy tắc hợp lệ; không tính từ màu.

## Chỉ số, NAV và giá giao dịch

Chỉ số thị trường là kết quả một phương pháp tính theo rổ, trọng số, divisor và điều chỉnh; không lấy trung bình cộng giá mọi cổ phiếu. VN-Index, chỉ số nhóm và chỉ số ngành có mục đích khác nhau. Với ETF, market price có thể lệch NAV/iNAV. Một bảng giá giỏi phải phân biệt chỉ số, giá quỹ và giá cơ sở dùng định giá.

## Khi đóng cửa hoặc mất feed

Không đổi mọi giá thành 0; đó có thể được hiểu là tài sản mất hết giá trị. Giữ giá cuối kèm nhãn “dữ liệu lúc…”, trạng thái disconnected/stale và ngày giao dịch. Cột không có dữ liệu phải khác cột có số 0. Sắp xếp bảng theo giá cũ mà không báo độ trễ có thể gây hiểu nhầm.

**Bài tập:** giá chart ngày không khớp giá historical trên bảng. **Đáp án:** kiểm tra đơn vị, timezone, regular/odd lot, điều chỉnh quyền, nguồn, thời điểm snapshot và quy tắc OHLC trước khi kết luận mất dữ liệu.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
