# Thiết kế .NET và SQL Server cho đường ghi tài sản

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Một transaction nhận lệnh

Pseudocode sau là thiết kế tham chiếu, chưa phải dịch vụ production hay bộ mã .NET đã biên dịch:

```text
begin transaction
  insert idempotency(scope, key, payload_hash)   -- unique constraint
  lock account reservation boundary
  read current limits and rule version
  validate and calculate required reservation
  if unavailable: persist rejection, commit, return
  insert reservation
  insert order(state=ReadyToRoute)
  insert outbox(OrderReadyToRoute)
commit
return received order id
```

Unique constraint xử lý hai request trùng chạy đồng thời; transaction boundary xử lý hai lệnh khác key cùng tranh tiền. Không giữ transaction SQL trong lúc chờ network acknowledgement từ Sở.

## Lựa chọn concurrency

- Pessimistic locking giúp serialize quyết định trên account nhưng có nguy cơ hot key và deadlock.
- Optimistic concurrency dùng version/rowversion và retry transaction khi conflict; retry phải giữ cùng ý định, không lặp external effect.
- Single-writer partition theo account thuận lợi cho ordering nhưng phải xử lý failover, fencing và account cực nóng.

Không có một lựa chọn tốt cho mọi tải. Benchmark bằng phân bố tài khoản thực tế và burst mở/đóng cửa, không chỉ random đều.

## Những lỗi .NET quen gặp

Không chia sẻ một DbContext cho nhiều thao tác đồng thời [S20]. Scope của background worker phải rõ. Dùng decimal cho tiền, kiểm soát precision/scale ở cả DTO, domain và database. Cancellation của HTTP client không đồng nghĩa transaction hoặc lệnh bên ngoài đã hủy. Retry policy phải phân biệt read idempotent, command có key và hành động bên ngoài chưa rõ kết quả.

## SQL Server và hiệu năng

Thiết kế index cho account+state, execution dedup key, outbox pending và business date. Đọc dashboard từ projection/reporting path để tránh tranh lock với lệnh. Partitioning phục vụ quản lý dữ liệu và truy vấn có điều kiện phù hợp; không tự làm mọi truy vấn nhanh hơn. Theo dõi wait, log write latency, transaction duration, deadlock và kế hoạch thực thi.

`NOLOCK` không phải cách sửa số dư chậm [S21]: đọc bẩn hoặc không nhất quán có thể làm quyết định rủi ro sai. Chọn isolation theo invariant và test concurrency thật.

## Failover và restore

HA replica giúp tính sẵn sàng nhưng cần biết chế độ đồng bộ, commit semantics và khả năng mất dữ liệu. Restore database không đảo ngược tiền đã trả ngân hàng hay lệnh đã khớp. Runbook phải recovery journal, outbox/inbox, session và reconcile trước khi mở ghi.

**Bài tập:** retry transaction do deadlock sau khi đã gọi API ngân hàng trong transaction. **Đáp án:** ranh giới sai; external effect có thể lặp. Ghi payment intent/outbox trước, dùng idempotency và reconciliation ở adapter.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S20, S21, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
