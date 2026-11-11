# 08 · Mô hình theo ngành: ngân hàng, chứng khoán, bảo hiểm

[Mục lục](../INDEX.md)

Các mô hình dưới đây phục vụ thiết kế phần mềm. Công thức sản phẩm, tài khoản kế toán, thời hạn thanh toán và yêu cầu lưu trữ phải được BA/kế toán/compliance xác nhận riêng.

## Ngân hàng và tín dụng

Tách `Facility` (hạn mức), `LoanContract` (hợp đồng vay), `Disbursement` (giải ngân), `RepaymentSchedule` và `Accrual` (dự thu/dự chi theo thiết kế nghiệp vụ). Lịch trả nợ là kế hoạch, không phải bằng chứng đã nhận tiền. Ghi nhận receipt và phân bổ vào gốc/lãi/phí bằng bảng allocation có nguồn.

Lãi suất cần kỳ hiệu lực, day-count convention, lịch ngày nghỉ, basis, rule làm tròn và version. Tái tính một kỳ phải có input/version rõ. Nếu đã hạch toán thì điều chỉnh bằng bút toán, không ghi đè lịch sử để che khác biệt.

## Chứng khoán

Phân biệt order, execution/trade, settlement obligation, cash movement và position. Một order có nhiều lần khớp; hủy phần còn lại không xóa trade đã khớp. Lưu sequence nguồn để xử lý duplicate hoặc out-of-order; một timestamp không đủ làm thứ tự duy nhất.

Position cần chiều account, instrument, trạng thái tài sản và ngày liên quan. Số lượng đã khớp, chờ về, được bán, phong tỏa và khả dụng không phải luôn là một số. Corporate action tạo biến động riêng có nguồn, ngày chốt quyền và rule; không sửa quantity thủ công hàng loạt.

Không hard-code chu kỳ settlement vào tên cột như `T2Amount`. Lưu settlement date được tính từ lịch và phiên bản rule; đối chiếu quy định hiện hành trước triển khai.

## Bảo hiểm

| Thực thể | Lưu gì | Điểm dễ sai |
|---|---|---|
| Policy | Hợp đồng và các version/endorsement | Sửa hợp đồng làm mất điều khoản cũ |
| Coverage | Phạm vi, limit, deductible có hiệu lực | Dùng limit hiện tại cho tổn thất quá khứ |
| PremiumSchedule | Kế hoạch thu phí | Coi scheduled = collected |
| PremiumReceipt/Allocation | Tiền đã thu, phân bổ kỳ phí | Một receipt có thể trả nhiều kỳ |
| Claim | Hồ sơ tổn thất, ngày xảy ra/khai báo | Nhầm ngày tổn thất với ngày nhận hồ sơ |
| ClaimReserve/Payment | Dự phòng và chi trả theo version | Cộng reserve và payment như hai khoản chi |

Claim có nhiều coverage/beneficiary/payment; tránh bảng claim phình thành hàng trăm cột. Khi đánh giá quyền lợi, dùng coverage có hiệu lực đúng thời điểm và điều kiện hợp đồng liên quan, không join bản policy mới nhất.

## Kinh nghiệm dùng chung

Tách trạng thái vận hành khỏi tác động tiền. Lưu reference của hệ thống ngoài nhưng dùng khóa nội bộ ổn định. Mọi phép tái tính cần input có thể giải thích. Định nghĩa rõ “as of business date” và “as known at system time” cho báo cáo hồi tố.

**Bài tập:** lập ERD claim có hai người thụ hưởng và ba đợt chi. Đáp án cần bảng liên kết và allocation; unique theo claim không được chặn nhiều payment hợp lệ.
