# Data model, API contract và sự kiện

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Mô hình dữ liệu tối thiểu

| Aggregate/bảng | Trường quan trọng | Ràng buộc |
|---|---|---|
| Order | ID, account, instrument, side, type, quantity, price, ruleset, revision | Không dùng float cho giá |
| Execution | Venue, businessDate, executionID, orderID, quantity, price, correctionOf | Unique theo scope đối tác |
| Reservation | ID, ownerType/ID, asset, amount, state | Một lý do không giải tỏa hai lần |
| JournalTransaction/Entry | TransactionID, book, currency, debit/credit, source | Cân bằng trong phạm vi book/currency |
| InstrumentVersion | StableID, symbol, venue, dates, units | Không chồng ngày hiệu lực |
| Inbox/Outbox | ID, schemaVersion, payloadHash, status, attempts | Marker và effect cùng transaction |

## API đặt lệnh

Request gồm account, instrument, side, quantity, orderType, limitPrice khi cần và idempotency key. Server lấy user/tenant từ identity đã xác thực, không tin `userId` do client gửi. Response trả internal order ID và trạng thái có nghĩa; đưa reason codes ổn định như `INSUFFICIENT_AVAILABLE_CASH`, kèm mô tả bản địa hóa ở lớp UI.

Idempotency key cần scope theo người/tài khoản/operation, canonical payload hash, thời hạn lưu và chính sách sau hết hạn. Cùng key khác payload trả conflict. Retry không có key không được tự coi là cùng ý định chỉ vì giá/lượng giống nhau.

## Event envelope đề xuất

```json
{
  "eventId": "evt-demo-001",
  "eventType": "OrderPartiallyFilled",
  "schemaVersion": 1,
  "aggregateId": "ord-demo-001",
  "aggregateVersion": 4,
  "businessDate": "2026-11-06",
  "occurredAt": "2026-11-06T02:30:00Z",
  "recordedAt": "2026-11-06T02:30:00.020Z",
  "correlationId": "req-demo-001",
  "data": {"executionId": "exec-demo-001", "quantity": 100, "priceVnd": 25000}
}
```

Đây là schema nội bộ minh họa, không phải bản tin Sở. Có `occurredAt` và `recordedAt` để không nhầm event time với processing time. Version là phục vụ thứ tự aggregate, không thay sequence của feed.

## Dữ liệu lịch sử

Thay đổi tên khách, room, venue, fee schedule, collateral và nhân sự cần giữ bối cảnh quá khứ. Reporting “as of” phải dùng đúng thời điểm. Với sửa sai, lưu business effective time và system recorded time khi yêu cầu truy vết cần hai trục thời gian.

## Contract evolution

Thêm trường optional có thể tương thích nhưng đổi ý nghĩa trường cũ thì không. `quantity` từ tổng lượng sang lượng còn lại là breaking change dù kiểu dữ liệu không đổi. Tạo schema mới, dual-read/dual-write có thời hạn và kiểm tra consumer trước chuyển.

**Bài tập:** truyền tiền dạng `25.000` trong JSON string. **Đáp án:** dấu chấm có thể là nhóm nghìn hay thập phân. Dùng integer đơn vị rõ ràng hoặc decimal canonical cùng currency/scale, không dùng format locale trên wire.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
