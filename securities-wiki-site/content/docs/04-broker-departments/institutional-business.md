# Khách tổ chức, tự doanh, IB và nghiên cứu

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Khách tổ chức cần nhiều vai trò

Portfolio manager quyết định đầu tư; trader thực hiện; custodian lưu ký; bộ phận middle/back office xác nhận và phân bổ. Tài khoản giao dịch, tài khoản lưu ký và tài khoản thanh toán có thể liên quan các tổ chức khác nhau. Thiết kế phải biểu diễn rõ executing broker, beneficial owner, custodian, allocation và người có quyền xác nhận.

Một lệnh khối có thể cần phân bổ theo workflow được phép. Không biến sửa allocation sau giao dịch thành cách sửa tùy ý chủ thể giao dịch. Mọi sửa sai phải theo quy trình, hạn chót, thẩm quyền và dấu vết.

## Non-prefunding cần kiểm soát tín dụng

VSDC mô tả sửa đổi quy chế năm 2024 phục vụ nhà đầu tư nước ngoài là tổ chức được mua cổ phiếu không yêu cầu đủ tiền khi đặt lệnh theo phạm vi điều chỉnh [S10]. Điều này không có nghĩa mọi nhà đầu tư được bỏ kiểm tra tiền. Thiết kế phải có eligibility, hạn mức, cam kết thanh toán, thời hạn funding, giám sát nghĩa vụ, kịch bản thiếu tiền và trách nhiệm của các bên. Chi tiết áp dụng tại ngày triển khai cần pháp chế đối chiếu văn bản hiện hành.

## Tự doanh

Công ty giao dịch bằng nguồn vốn của mình cần sổ vị thế và P&L riêng, giới hạn thị trường/tín dụng/thanh khoản và cơ chế phê duyệt. Không gộp tài sản khách hàng vào tài sản công ty. Giao dịch cùng mã giữa tự doanh và khách hàng làm tăng nhu cầu giám sát xung đột lợi ích và thứ tự xử lý.

## Ngân hàng đầu tư và tư vấn tài chính doanh nghiệp

Các hoạt động có thể gồm tư vấn phát hành, niêm yết, cấu trúc vốn và M&A trong phạm vi giấy phép. Dữ liệu deal có thể là thông tin chưa công bố. Cần restricted list, watch list, phân quyền hồ sơ, tường thông tin và quy trình duyệt báo cáo. Không đưa dữ liệu deal vào kho tìm kiếm nội bộ mở cho mọi nhân viên.

## Research và product distribution

Báo cáo phân tích cần quản lý phiên bản, người phê duyệt, thời điểm công bố và quyền truy cập. Phân phối sản phẩm cần giải thích đặc điểm, phí, rủi ro và điều kiện khách hàng; doanh thu phân phối không phải bảo đảm giá trị đầu tư.

**Bài tập:** tài khoản tổ chức không pre-fund bị ngân hàng chậm chuyển tiền trong ngày thanh toán. **Đáp án:** kích hoạt funding escalation, xác nhận nghĩa vụ và hạn chót, áp dụng quy trình đã ký; không xóa giao dịch đã khớp trong OMS để làm cân tiền.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S10, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
