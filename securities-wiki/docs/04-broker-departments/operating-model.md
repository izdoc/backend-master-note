# Bản đồ phòng ban và trách nhiệm giao dịch

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Front, middle và back office

Front office tiếp xúc khách hàng và tạo doanh thu; middle office kiểm soát rủi ro, giám sát và hỗ trợ giao dịch; back office xác nhận, hạch toán, lưu ký, thanh toán và đối soát. Đây là cách chia chức năng, không phải sơ đồ tổ chức bắt buộc. Một CTCK có thể đặt tên hoặc gộp phòng ban khác nhau.

| Bộ phận | Công việc thường gặp | Đầu ra/bằng chứng | Điểm phối hợp |
|---|---|---|---|
| Môi giới/kinh doanh | Tìm khách, tư vấn trong phạm vi, chăm sóc, nhận lệnh được ủy quyền | Hồ sơ tương tác, chứng cứ lệnh | CS, Compliance, Trading |
| Dịch vụ khách hàng | Mở/đổi/đóng tài khoản, ủy quyền, xử lý yêu cầu | Hồ sơ đã kiểm tra, case ID | Identity, lưu ký, pháp chế |
| Trading operations | Theo dõi phiên, lệnh bất thường, kết nối, hỗ trợ lệnh | Nhật ký phiên, hàng đợi ngoại lệ | IT, Sở, môi giới |
| Risk/margin | Hạn mức, tài sản bảo đảm, cảnh báo, xử lý khoản vay | Policy version, quyết định hạn mức | Treasury, Finance, broker |
| Lưu ký/thực hiện quyền | Chuyển khoản CK, phong tỏa, phân bổ quyền | Đối chiếu vị thế, danh sách quyền | VSDC, Finance |
| Thanh toán/đối soát | Nghĩa vụ thị trường, funding, khớp sổ | Break register, xác nhận hoàn tất | Ngân hàng, VSDC |
| Kế toán/tài chính | Subledger/GL, phí, chi phí, báo cáo | Chứng từ và bút toán | Mọi dòng nghiệp vụ |
| Treasury | Thanh khoản, nguồn vốn, kế hoạch chi trả | Cash forecast, funding plan | Risk, settlement |
| Compliance/pháp chế | Quy định, điều kiện sản phẩm, giám sát hành vi | Ý kiến kiểm soát, báo cáo | HĐQT/điều hành |
| Tự doanh/IB/nghiên cứu | Đầu tư công ty, tư vấn tài chính DN, phân tích | Vị thế riêng, deal hồ sơ, báo cáo | Information barrier |
| IT/Security/SRE | Hệ thống, quyền, an toàn, khôi phục | Telemetry, release, incident log | Chủ nghiệp vụ |
| Kiểm toán nội bộ | Đánh giá độc lập kiểm soát | Phát hiện và theo dõi khắc phục | Ban quản trị |

## Tình huống nộp tiền chưa lên sức mua

CS nhận case, xác minh người yêu cầu và mã giao dịch. Cash operations kiểm tra sao kê/callback ngân hàng. IT kiểm tra ingest và idempotency. Finance xác nhận ledger. Nếu chưa có bằng chứng tiền đã đến, không sửa số dư thủ công theo ảnh chuyển khoản. Nếu có giao dịch chưa xác định tài khoản, đưa vào suspense và xử lý có người lập/người duyệt.

## RACI mẫu cho thay đổi hạn mức

Risk đề xuất và chịu trách nhiệm policy; người có thẩm quyền được công ty quy định phê duyệt; IT triển khai cấu hình; Operations kiểm tra hiệu lực; Finance/Treasury được tham vấn về nguồn vốn; CS được thông tin về cách giải thích khách hàng. Phải nêu một người/role chịu trách nhiệm cuối cùng, không để “cả team cùng chịu”.

## Ba tuyến bảo vệ

Tuyến kinh doanh/vận hành sở hữu rủi ro của mình; quản lý rủi ro và tuân thủ kiểm soát/giám sát; kiểm toán nội bộ đánh giá độc lập. Người triển khai kỹ thuật không tự phê duyệt thay đổi business limit chỉ vì có quyền database.

**Bài tập:** môi giới đề nghị bỏ kiểm tra margin cho khách VIP. **Đáp án:** chuyển luồng ngoại lệ có hạn mức, thời hạn và người phê duyệt được ủy quyền; không mở bypass kỹ thuật vô thời hạn.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
