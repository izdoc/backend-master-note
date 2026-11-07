# Ma trận thị trường và cấu hình có ngày hiệu lực

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Đọc quy tắc theo phạm vi

Không tồn tại một bộ quy tắc “chứng khoán Việt Nam” dùng chung cho mọi tài sản. Khóa tra cứu nên chứa thị trường, nhóm sản phẩm, board/lô giao dịch, trạng thái chứng khoán, phiên và ngày hiệu lực. Ngày đầu giao dịch, ngày giao dịch trở lại, ngày không hưởng quyền và chứng khoán hạn chế có thể khác ngày bình thường.

Bảng dưới là bản học cho **cổ phiếu thông thường**, HOSE/HNX đã đối chiếu Phụ lục III quy chế VNX 22/2026 tại S17; UPCoM đối chiếu hướng dẫn S05 nhưng chưa review toàn văn quy chế 23/2026. Cần phê duyệt phạm vi và thông báo từng mã trước khi dùng làm cấu hình thật.

| Nội dung | HOSE | HNX niêm yết | UPCoM |
|---|---|---|---|
| Mở cửa | Định kỳ 09:00–09:15 | Liên tục từ 09:00 | Liên tục từ 09:00 |
| Liên tục sáng | 09:15–11:30 | 09:00–11:30 | 09:00–11:30 |
| Liên tục chiều | 13:00–14:30 | 13:00–14:30 | 13:00–15:00 |
| Đóng cửa định kỳ | 14:30–14:45 | 14:30–14:45 | Không có trong cấu hình này |
| Sau 14:45 | Thỏa thuận đến 15:00 | Có phiên khớp sau giờ | Tiếp tục đến 15:00 |

Mọi giờ là Asia/Ho_Chi_Minh. Đây không phải lịch cho trái phiếu, phái sinh hay mã hạn chế. Giao dịch thỏa thuận là luồng riêng; không suy ra từ bảng khớp lệnh.

## Biên giá, bước giá, lô

Ví dụ thường gặp để học: cổ phiếu HOSE biên độ ±7%, HNX ±10%, UPCoM ±15%; lô chẵn 100, lô lẻ 1–99. Theo S17, bước giá cổ phiếu HOSE lần lượt là 10 đồng dưới 10.000, 50 đồng từ 10.000 đến dưới 50.000 và 100 đồng từ 50.000; HNX/UPCoM cổ phiếu khớp lệnh thường dùng 100 đồng. Không áp dụng nguyên xi cho ETF, CW hoặc thỏa thuận. Các số này nằm trong hồ sơ **training baseline**, không được đánh dấu approved production khi chưa đối chiếu đầy đủ phụ lục hiện hành.

Đối với production, ưu tiên giá trần/sàn/tham chiếu nhận từ nguồn danh mục được phê duyệt; không chỉ lấy `reference * 1.07` vì còn bước giá, làm tròn và trường hợp đặc biệt. Nếu bảng giá dùng đơn vị nghìn đồng, 25,5 phải được chuẩn hóa thành 25.500 đồng trước khi tính tiền.

## Mô hình cấu hình

`RuleVersion = {market, instrumentClass, board, phase, effectiveFrom, effectiveTo, sourceId, status, approvers, checksum}`. Lưu cả phiên bản dùng để kiểm tra một lệnh. Hai phiên bản có cùng scope không được chồng hiệu lực. Giá trị `null` nghĩa là chưa xác minh, không phải không giới hạn.

## Thay đổi cần theo dõi

Quy chế niêm yết/giao dịch VNX số 22 ngày 16/03/2026 và quy chế UPCoM số 23 ngày 18/03/2026 được liệt kê tại S02. Không dùng số văn bản mà bỏ năm: cùng số 22 còn có bản năm 2025. Lịch chuyển cổ phiếu HNX sang HOSE cuối tháng 12/2026 được ghi riêng trong [regulatory watch](../13-reference/regulatory-watch.md).

**Bài tập:** đổi sàn của một mã có làm đổi mã định danh sở hữu không? **Đáp án:** giữ instrument ID nội bộ; version hóa venue mapping, tick table, session policy và điều kiện đặt lệnh theo ngày.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S02, S05, S12, S16, S17, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
