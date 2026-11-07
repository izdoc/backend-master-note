# Khớp liên tục: giá, thời gian và nhiều mức giá

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Mô hình tối giản

Order book gồm hàng mua và hàng bán. Giá mua cao hơn đứng trước; giá bán thấp hơn đứng trước. Trong cùng mức giá, dùng quy tắc thời gian/thứ tự của venue. Bài này mô phỏng sổ LO lô chẵn, không xét lô lẻ, room ngoại, tự khớp, tạm dừng hoặc trường hợp đặc biệt.

| Lệnh bán đang chờ | Giá VND | Khối lượng | Thứ tự |
|---|---:|---:|---:|
| S1 | 25.000 | 100 | 1 |
| S2 | 25.000 | 200 | 2 |
| S3 | 25.100 | 300 | 3 |

Lệnh mua B1: 450, giá giới hạn 25.100. Trong mô hình price-time với giá lệnh đang chờ, B1 khớp S1 100 ở 25.000; S2 200 ở 25.000; S3 150 ở 25.100. S3 còn 150. Tổng tiền = 11.265.000; VWAP = 11.265.000 / 450 = 25.033,333… đồng.

VWAP là giá bình quân tính toán, không nhất thiết là mức giá đặt lệnh hợp lệ theo tick. Nếu UI làm tròn VWAP để tính lại tiền sẽ tạo sai số. Lưu từng fill và giá trị tiền chính xác; lấy tổng tiền chia tổng lượng để hiển thị bình quân.

## Tại sao “đúng giá” vẫn chưa khớp?

Một người nhìn thấy giá khớp 25.000 không biết toàn bộ hàng chờ trước mình. Giao dịch có thể thuộc lô/board khác; số dư hiển thị có độ trễ; lệnh mới chưa được sở chấp nhận. Phải tra exchange order ID, board, trạng thái, thời điểm và queue priority. Không thể chứng minh thứ tự khớp từ ảnh chụp bảng điện.

## Trường hợp lệnh không đi xuyên sổ

Nếu B2 mua 500 ở 24.900 khi giá bán tốt nhất 25.000, lệnh nằm chờ. Nếu chỉ có 100 bán ở 25.000 và B3 mua 300 LO cùng giá, khớp 100 rồi giữ 200. Với điều kiện khác như MAK, phần dư không được xử lý giống LO. Khi mã bị tạm ngừng, cơ chế xử lý lệnh chờ phải theo quy tắc venue.

## Điểm architect cần bảo vệ

Khóa sổ theo instrument/board/partition thích hợp; không cho nhiều writer tự quyết thứ tự của cùng một sổ. Ghi journal trước khi tuyên bố kết quả bền vững; tạo execution ID duy nhất trong scope đã định nghĩa. Replay cùng đầu vào và ruleset phải tái tạo được cùng trạng thái. Đây là nguyên tắc mô phỏng/thiết kế; không xác nhận engine thực tế của Sở dùng công nghệ nào.

**Bài tập:** thêm S4 bán 100 ở 24.950 sau S2 nhưng trước B1. Kết quả? **Đáp án:** giá tốt hơn ưu tiên trước thời gian giữa các mức: khớp S4 100, S1 100, S2 200, S3 50. Tổng tiền 11.250.000; VWAP 25.000. Xem lab để thử thêm các kịch bản.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S05, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
