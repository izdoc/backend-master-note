# Bù trừ, thanh toán, DvP và CCP

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Từ giao dịch sang nghĩa vụ

**Clearing** xác định nghĩa vụ, đối chiếu và có thể bù trừ theo cơ chế thị trường. **Settlement** hoàn tất chuyển giao. **Custody** quản lý lưu ký và trạng thái tài sản. **DvP** gắn chuyển giao chứng khoán với thanh toán tiền để kiểm soát rủi ro giao một bên mà không nhận bên kia [S14].

Trong netting đa phương, một thành viên có thể nhận nghĩa vụ ròng; công ty vẫn phải giữ giao dịch và nghĩa vụ chi tiết cho từng khách. Ví dụ khách A mua 100 triệu, khách B bán 80 triệu: nghĩa vụ ròng cấp thành viên có thể 20 triệu trong mô hình đơn giản, nhưng không được biến nghĩa vụ từng khách thành 20 triệu chung.

## Chu kỳ theo nhóm sản phẩm

Trang dịch vụ VSDC [S19] tại ngày rà soát nêu:

| Nhóm | Chu kỳ thông thường được trang dịch vụ nêu |
|---|---|
| Cổ phiếu, chứng chỉ quỹ, CW | T+2 |
| Trái phiếu doanh nghiệp niêm yết | T+1 |
| Công cụ nợ | T+1, theo từng giao dịch |
| Trái phiếu riêng lẻ | T+0, theo từng giao dịch |
| Lãi/lỗ vị thế phái sinh, thực hiện HĐTL chỉ số | T+1 |
| Thực hiện HĐTL trái phiếu Chính phủ | E+3 theo ngày làm việc |

Cùng trang dẫn quy chế cơ sở số 39/QĐ-HĐTV ngày 29/04/2025. Chu kỳ không thay thế điều kiện đủ tiền/chứng khoán, cutoff hay quy trình ngoại lệ. Các thay đổi sau ngày chốt cần đối chiếu lại, đặc biệt mốc Thông tư 145.

## T+2 theo ngày làm việc

Mô hình thanh toán cổ phiếu T+2 được VSDC triển khai với phân bổ để giao dịch phiên chiều T+2 từ năm 2022 [S09]. T là ngày giao dịch; T+2 là ngày làm việc thanh toán thứ hai sau T, không phải cộng 48 giờ. Trạng thái hoàn tất phải dựa trên xác nhận, không chỉ timer.

Giả sử giao dịch thứ Sáu 06/11/2026 và không có ngày nghỉ đặc biệt: T+1 là thứ Hai 09/11; T+2 là thứ Ba 10/11. Nếu lịch nghỉ thanh toán khác, kết quả đổi. Lịch settlement và lịch thị trường phải có version, nguồn và phạm vi sản phẩm; không mặc định mọi trái phiếu/phái sinh theo T+2.

## Quy trình back office tham chiếu

Nhận kết quả → đối chiếu giao dịch → xác định nghĩa vụ → dự kiến funding → xác nhận thông tin/ngoại lệ → nhận hoàn tất → phân bổ vào subledger khách → đối soát tổng → báo cáo. Khi có lỗi, quản lý case theo hạn chót, loại sai lệch và người xử lý; không sửa file kết quả rồi xóa bản gốc.

## CCP là vai trò pháp lý và quản trị rủi ro

CCP đứng giữa các bên theo cơ chế pháp lý áp dụng, có quản lý nghĩa vụ, ký quỹ, default management và nguồn lực bảo vệ. Không gọi mọi netting engine là CCP. KRX vận hành không tự chứng minh mọi giao dịch cơ sở đã qua CCP. S11 ghi Thông tư 145/2026 gồm nội dung trước và khi triển khai CCP; phải xác minh thông báo triển khai riêng.

## Trường hợp thanh toán lỗi

Nghĩa vụ chưa hoàn thành cần hiển thị riêng với thiếu chứng khoán/thiếu tiền/lỗi kỹ thuật, nguồn xác nhận, deadline, action owner. Nếu phải huy động nguồn hỗ trợ hoặc xử lý theo cơ chế thị trường thì chỉ người có thẩm quyền thực hiện; phần mềm cần bảo toàn bằng chứng và thứ tự sự kiện.

**Bài tập:** đến 13:00 chưa nhận xác nhận hoàn tất. **Đáp án:** không tự mở quyền bán/rút chỉ vì thường ngày đã xong; kiểm tra nguồn, đối chiếu và kích hoạt quy trình ngoại lệ.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S09, S10, S11, S14, S19, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
