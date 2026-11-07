# Sổ cái và đối soát nhiều lớp

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Một số dư phải giải thích được

Ledger lưu các giao dịch và bút toán có quan hệ cân đối, còn balance là kết quả tổng hợp. Chỉnh trực tiếp số dư để “cho khớp” làm mất giải thích lịch sử. Bút toán lỗi cần reversal hoặc adjustment liên kết với lý do và người duyệt.

Ví dụ kế toán khái niệm khi nhận tiền khách: tăng tài sản tiền ngân hàng và tăng khoản phải trả khách. Đây không phải hướng dẫn chọn số hiệu tài khoản kế toán pháp định; kế toán trưởng phê duyệt chart of accounts và booking rules. Tiền hold có thể được quản lý như reservation riêng; không tạo thu nhập vì khách đặt lệnh.

## Các cấp đối soát

| Đối chiếu | Khóa và phạm vi | Chênh lệch cần tìm |
|---|---|---|
| OMS ↔ kết quả giao dịch | Ngày, thị trường, execution ID | Thiếu/trùng/sai giá-lượng |
| Cash ledger ↔ ngân hàng | Tài khoản, currency, reference, value date | Tiền chưa xác định, phí, reversal |
| Position ledger ↔ lưu ký | Custody account, instrument, bucket | Chuyển khoản/phong tỏa chưa cập nhật |
| Subledger ↔ GL | Business date, book, posting type | Ghi sổ trễ, mapping sai |
| Thành viên ↔ từng khách | Tổng nghĩa vụ cùng phạm vi | Netting hoặc rounding sai |

Không chỉ so tổng tiền: thiếu giao dịch +100 và trùng −100 có thể làm tổng đúng nhưng dữ liệu sai. Đối soát cần cả cardinality, ID, lượng, giá trị và trạng thái.

## Quy trình break management

Phát hiện → phân loại → định lượng ảnh hưởng → giao owner → thu thập bằng chứng → sửa có thẩm quyền → chạy lại đối soát → đóng case. Theo dõi tuổi break, mức trọng yếu, deadline và khách bị ảnh hưởng. “Đã giải thích” chưa đồng nghĩa “đã sửa”.

## Ví dụ

Nguồn Sở có E1:100@20.000, E2:50@20.100; OMS có E1 hai lần và thiếu E2. Giá trị bên ngoài 3.005.000; ingest thô OMS 4.000.000. Dedup E1 giúp còn 2 triệu nhưng vẫn thiếu E2. Lab đối soát báo riêng duplicate và missing để team không nghĩ dedup đã giải quyết mọi thứ.

## Thời gian và làm tròn

Duy trì trade date, settlement date, value date, postedAt và businessDate. Phí có thể tính theo từng fill, lệnh hoặc ngày tùy hợp đồng; làm tròn ở đâu phải rõ. Dùng decimal hoặc integer minor unit, không float nhị phân cho tiền sổ cái. Nếu currency không có cùng số lẻ, metadata phải quyết định scale.

**Bài tập:** khôi phục DB về 10:00 nhưng ngân hàng đã hoàn thành rút tiền lúc 10:01. **Đáp án:** cần reconcile external effects sau restore, không phát lại mù tất cả outbox “chưa gửi” của bản backup.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
