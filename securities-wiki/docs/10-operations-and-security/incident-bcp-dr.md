# Runbook sự cố, BCP và disaster recovery

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Ba mục tiêu khác nhau

HA giảm gián đoạn khi một thành phần hỏng. DR khôi phục khi mất site/hệ thống lớn. BCP giữ hoạt động kinh doanh ở mức chấp nhận được, bao gồm con người, nơi làm việc, liên lạc và quy trình. Backup không thay cho cả ba.

RTO là mục tiêu thời gian khôi phục; RPO là mức mất dữ liệu mục tiêu. Mỗi nghiệp vụ có mục tiêu riêng. Cần phân biệt RPO database và mất external effect: bản tin đã khớp tại Sở có thể vẫn tồn tại ngoài công ty dù database được restore về trước đó.

## Runbook: gateway mất kết nối sau gửi lệnh

1. Incident commander xác định scope và mốc thời gian; giữ log/journal.
2. Trading operations chuyển kênh bị ảnh hưởng sang trạng thái có kiểm soát; tránh nhận thêm vượt khả năng xử lý.
3. Đánh dấu các lệnh không rõ kết quả, giữ reservation liên quan.
4. Integration xác minh session/sequence và phối hợp khôi phục theo contract.
5. Replay/đối chiếu kết quả, áp dụng dedup; reconcile order, execution và hold.
6. Risk/Operations xác nhận điều kiện mở lại; CS thông tin đúng phạm vi và bằng chứng.
7. Lập postmortem, hành động phòng ngừa, owner và ngày hoàn tất.

Không restart liên tục làm mất bằng chứng; không force reset sequence để che gap; không gửi lại mọi pending order bằng ID mới.

## Runbook: bảng giá mất sequence

Đánh dấu stale ở phạm vi feed/board ảnh hưởng; dừng trigger phụ thuộc giá không tin cậy theo policy; lấy snapshot/recovery; kiểm tra continuity; publish trạng thái đồng bộ trở lại. Order entry có thể còn hoạt động, nhưng điều kiện mở/chặn phải được business và risk quy định trước.

## Diễn tập DR

Dừng/fence writer cũ; xác minh không split-brain; phục hồi dữ liệu và secret/session state; đối chiếu với bên ngoài; kiểm tra thanh khoản, market status, control totals; mở theo từng nhóm; theo dõi. Failback cần kế hoạch riêng, không chỉ đảo DNS.

| Điều kiện mở lại | Bằng chứng |
|---|---|
| Một writer có thẩm quyền | Fencing/lease và ownership |
| Không bỏ sót giao dịch | Reconciliation đã xử lý break trọng yếu |
| Số dư giải thích được | Ledger/hold/position checks |
| Kênh đã đồng bộ | Session + market data quality |
| Người chịu trách nhiệm chấp nhận | Quyết định go/no-go có timestamp |

**Bài tập:** RTO đạt 10 phút nhưng 20 lệnh UNKNOWN chưa xử lý. **Đáp án:** không thể coi phục hồi nghiệp vụ hoàn tất chỉ vì app lên; cần quyết định phạm vi dịch vụ được mở và cách cô lập các tài khoản/lệnh bị ảnh hưởng.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
