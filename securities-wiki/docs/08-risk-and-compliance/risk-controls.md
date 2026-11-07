# RMS và kiểm soát trước, trong, sau giao dịch

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## RMS quyết định có nhận rủi ro hay không

Pre-trade risk không chỉ kiểm tra số dư. Cần xác thực người đặt, tài khoản được hoạt động, sản phẩm được cấp quyền, mã được giao dịch, phiên hợp lệ, giá/lượng hợp lệ, room/hạn mức, tiền/chứng khoán khả dụng và giới hạn toàn công ty. Một quyết định phải có reason code đủ để giải thích, policy version và đầu vào quan trọng.

## Phân loại kiểm soát

| Lớp | Ví dụ | Khi không có dữ liệu |
|---|---|---|
| Quyền | Người dùng có được đặt trên tiểu khoản? | Từ chối nếu không chứng minh được quyền |
| Thị trường | Mã, phiên, lot, price band | Không dùng dữ liệu ngày cũ như dữ liệu mới |
| Tài sản | Tiền/chứng khoán và reservation | Cần nhất quán ở điểm quyết định |
| Tín dụng | Margin, concentration, exposure | Chính sách fail-safe có phê duyệt |
| Hành vi | Lệnh bất thường, tốc độ, giá trị | Escalation theo mức độ, không tự kết tội |
| Hệ thống | Kill switch, throttle, degraded mode | Quyền dừng phải độc lập với UI khách |

## Reservation phải nguyên tử

`check()` rồi `reserve()` ở hai dịch vụ không có cơ chế đồng bộ có thể vượt hạn mức. Chọn consistency boundary theo tài khoản hoặc nhóm hạn mức. Nếu cần limit cấp công ty và limit cấp khách, phải có chiến lược quota/escrow hoặc coordinator được chứng minh; không hứa distributed transaction miễn phí.

## Room nước ngoài

Tư cách nhà đầu tư, tỷ lệ sở hữu và room là các thông tin khác nhau. Số hiển thị trên bảng giá có độ trễ và không phải bảo đảm được mua. Cần mapping investor classification, tài khoản lưu ký, dữ liệu room và phản hồi chính thức của thị trường. Mọi race tại thị trường vẫn phải xử lý reject an toàn.

## Kiểm soát sau giao dịch

Tính lại exposure khi có fill, giá biến động, quyền và thay đổi collateral. Theo dõi bất thường trên nhiều tài khoản có liên quan theo quyền truy cập và phạm vi chính sách. Một alert là tín hiệu cần điều tra, không phải kết luận vi phạm. Quản lý evidence, case, người xử lý và quyết định đóng/mở.

**Bài tập:** cache RMS bị lỗi và hệ thống tự trả `approved=true`. **Đáp án:** fail-open đó cần được đánh giá như phát tín dụng không kiểm soát; mặc định chặn hoặc hạn chế theo policy được phê duyệt, không dùng fallback boolean tùy ý.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
