# Bảo mật, release và chuyển đổi core

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Bảo vệ theo tài sản và đường đi

Threat model gồm chiếm tài khoản, chiếm quyền môi giới, sửa hạn mức, thay số tài khoản nhận tiền, đánh cắp credential gateway, giả bản tin, tấn công availability và sửa log. Kiểm soát phải gắn từng threat với identity, trust boundary, dữ liệu và khả năng phát hiện.

RBAC xác định vai trò; ABAC bổ sung phạm vi chi nhánh, desk, tài khoản, hạn mức và điều kiện. Chức năng lập/duyệt phải chống self-approval ở backend. Mã hóa đường truyền và lưu trữ cần quản lý khóa, rotation, revocation và quyền truy cập; chỉ bật HTTPS là chưa đủ.

## Secret và audit

Secret không nằm trong git, ảnh chụp màn hình hoặc ví dụ wiki. Dùng secret manager/vault phù hợp, quyền tối thiểu và rotation được diễn tập. Log che token, OTP, PII; dữ liệu test dùng synthetic hoặc masking đúng mục đích. Việc chuyển dữ liệu production sang UAT phải có quy trình và quyền phù hợp.

## Release hệ thống giao dịch

Chốt phạm vi → rule/config review → test unit/integration/conformance → rehearsal → kế hoạch rollback/forward-fix → người quyết định → triển khai theo cửa sổ được phép → đối soát. Một schema migration phá vỡ consumer không rollback đơn giản bằng đổi image về bản cũ.

## Chuyển đổi core

Duy trì mapping account/instrument/order ID; migrate số dư cùng hold, pending settlement, accrued interest, quyền đang chờ và restriction. So tổng tiền là chưa đủ: cần số lượng tài khoản, từng asset bucket, nghĩa vụ theo ngày, ngày đến hạn và các trạng thái trung gian.

Chạy rehearsal với dữ liệu đại diện, đo thời gian và định nghĩa điểm không thể quay lại sau khi tạo giao dịch bên ngoài. Shadow traffic có thể phục vụ so sánh read/calculation, nhưng không được để hệ thống shadow gửi lệnh thật hoặc thanh toán thật.

## Chọn vendor

Đánh giá khả năng xuất dữ liệu và journal, ownership đặc tả, hỗ trợ sự cố, conformance, DR, latency đo được, phương án thay thế, chi phí thay đổi và điều khoản dữ liệu. Một demo nhanh không chứng minh khả năng reconcile sau crash.

**Bài tập:** rollback app sau khi version mới đã phát một loại event mới. **Đáp án:** phải kiểm tra old consumer xử lý được và dữ liệu đã ghi; cần backward compatibility hoặc forward recovery, không chỉ rollback deployment.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
