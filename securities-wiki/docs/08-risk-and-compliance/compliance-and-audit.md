# Tuân thủ, giám sát thị trường và audit trail

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Biến quy định thành kiểm soát có thể chứng minh

Mỗi yêu cầu cần mapping: nguồn và hiệu lực → chủ sở hữu → quy trình → dữ liệu → kiểm soát phòng ngừa/phát hiện → bằng chứng → test → báo cáo. Một tài liệu “đã tuân thủ” không đủ nếu không chứng minh hệ thống áp dụng đúng phạm vi và đúng thời gian.

Các miền phải có người phụ trách: KYC/AML, điều kiện khách hàng/sản phẩm, xung đột lợi ích, công bố thông tin, giao dịch người nội bộ/người liên quan, quyền riêng tư, lưu trữ hồ sơ, giới hạn tài chính và báo cáo cơ quan quản lý. Ngưỡng, biểu mẫu và hạn nộp phải lấy từ rulebook hiệu lực; wiki không đặt số pháp định khi chưa xác minh.

## Hành vi thị trường cần hiểu

Giao dịch vòng tròn, tạo thanh khoản giả, lệnh gây hiểu nhầm cung cầu, lợi dụng thông tin chưa công bố và giao dịch vượt quyền là các nhóm rủi ro cần nghiên cứu. Dữ liệu cần gồm quan hệ tài khoản, lệnh hủy/sửa, fills, thời điểm, actor, thiết bị/kênh trong phạm vi được phép. Đừng chỉ chạy một ngưỡng số lệnh hủy rồi coi là phát hiện thao túng.

## Audit trail đủ dùng

Lưu ai làm, đại diện ai, làm gì, trên đối tượng nào, trước/sau, reason, approval, nguồn request, kết quả và timestamp. Dùng correlation xuyên dịch vụ nhưng tránh lộ bí mật. Audit log phải có kiểm soát truy cập, chống sửa/xóa trái phép và retention được phê duyệt. Developer debug log không thay được sổ audit.

## Quy trình ngoại lệ

Exception phải có phạm vi, giá trị tối đa, ngày hết hạn, người có thẩm quyền, compensating control và lịch rà soát. Dùng break-glass để xử lý sự cố phải lưu dấu và review sau; không tạo tài khoản admin dùng chung để “tiện ca trực”.

## Thay đổi quy định

Theo dõi ngày công bố, ngày hiệu lực và ngày triển khai hệ thống. S11 là ví dụ văn bản đã ban hành nhưng chưa có hiệu lực tại mốc 07/11/2026. Các dự thảo chưa được ban hành không được nâng thành active rule. Nếu web listing gắn nhãn “hiệu lực” khác nội dung văn bản, kiểm tra điều khoản hiệu lực và ghi mâu thuẫn.

**Bài tập:** lưu bản chụp báo cáo cuối ngày có đủ audit không? **Đáp án:** không. Cần truy ngược dữ liệu nguồn, phép biến đổi, ruleset, người duyệt và correction; báo cáo chỉ là một đầu ra.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S11, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
