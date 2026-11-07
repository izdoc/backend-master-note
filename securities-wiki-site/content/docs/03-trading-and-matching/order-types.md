# Loại lệnh và điều kiện thực hiện

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Phân biệt phương thức với loại lệnh

Khớp liên tục, khớp định kỳ và thỏa thuận là phương thức. LO, ATO, ATC, MTL, MAK, MOK là loại lệnh/điều kiện thực hiện theo thị trường. “Mua”, “bán” là chiều. Lô chẵn/lẻ là nhóm khối lượng. “Lệnh điều kiện” do CTCK quản lý không mặc nhiên là một loại lệnh native của Sở.

| Lệnh | Ý nghĩa để học | Điểm thiết kế |
|---|---|---|
| LO | Mua không cao hơn/bán không thấp hơn giá giới hạn | Không đảm bảo sẽ khớp |
| ATO / ATC | Tham gia xác định giá mở/đóng cửa | Không có giá giới hạn do khách nhập; không đảm bảo khớp toàn bộ |
| MTL | Khớp theo cơ chế thị trường, dư chuyển LO theo quy tắc | Cần xử lý giá phần dư và biên giá |
| MAK | Khớp được bao nhiêu thực hiện bấy nhiêu, hủy dư | Không để phần dư nằm trên sổ như LO |
| MOK | Chỉ thực hiện khi đáp ứng điều kiện khớp toàn bộ | Tránh nhầm với lệnh khớp một phần |
| Sau giờ: lệnh giới hạn không có giá (tên PLO còn gặp ở UI) | Giao dịch theo cơ chế phiên sau giờ | Tên hiển thị của CTCK có thể khác mã giao thức |

Bảng mô tả khái niệm; khả dụng phải kiểm tra theo venue và phiên. SSI công bố HOSE thay MP bằng MTL trong chuyển đổi KRX [S06]. Không giữ enum MP cũ làm lựa chọn mặc định.

## ATO/ATC không có ưu tiên tuyệt đối

Hướng dẫn HOSE được UBCKNN đăng nêu ATO/ATC không vượt LO mua trần/bán sàn đã nhập trước [S07]. Cần phân biệt xác định giá khớp, xác định thứ tự phân bổ và cách hiển thị dư mua/bán. Chúng là ba bài toán khác nhau; không lấy giá hiển thị trên bảng điện làm giá giới hạn của ATO/ATC.

## Lệnh điều kiện do công ty quản lý

Ví dụ stop-loss: CTCK theo dõi điều kiện trigger; khi thỏa mãn thì sinh một lệnh con phù hợp với thị trường. Có ít nhất hai vòng đời: parent strategy và child exchange order. Trigger xảy ra không đảm bảo gửi thành công; gửi thành công không đảm bảo khớp; khớp không đảm bảo giá đúng mức trigger nếu thị trường biến động.

Thiết kế phải trả lời: dùng last trade hay bid/ask để trigger, dữ liệu có stale không, mất kết nối có trigger lại không, sau chuyển sàn có giữ strategy không, phiên nào được phép phát lệnh, kiểm tra sức mua ở lúc tạo hay lúc gửi. Cần cả lúc tạo và kiểm tra lại lúc gửi theo policy.

## Sửa và hủy

Request hủy chỉ là ý định. Chỉ giải tỏa sau xác nhận có thẩm quyền cho phần chưa khớp. SSI mô tả sửa giá/tăng khối lượng làm đổi ưu tiên thời gian, giảm khối lượng giữ ưu tiên; một yêu cầu sửa không đồng thời đổi cả giá và lượng trong hướng dẫn KRX đó [S06]. Production phải đối chiếu schema hiện hành và ý nghĩa total quantity/leaves quantity.

**Tình huống:** khách hủy 1.000 cổ phiếu, trong lúc chờ khớp thêm 200. **Đáp án:** nhận fill, cập nhật nghĩa vụ; xác nhận hủy chỉ áp dụng phần còn lại. Không “undo” fill vì người dùng đã bấm hủy trước khi app nhận kết quả.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S16, S17, S05, S06, S07, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
