# 10 · Deadlock, retry và idempotency

[Mục lục](../INDEX.md) · [Lab transfer](../10-labs/README.md)

## Deadlock khác blocking

Blocking là session chờ tài nguyên session khác giữ. Deadlock là vòng chờ không thể tự tiến; engine chọn victim. Tăng timeout không phá nguyên nhân deadlock. Đọc deadlock graph để biết statement, index, loại lock và thứ tự tài nguyên.

Giảm xác suất bằng thứ tự khóa nhất quán, transaction ngắn, index giảm phạm vi đọc và batch nhỏ. Ví dụ chuyển A→B và B→A: cả hai luồng khóa account theo ID tăng dần thay vì luôn khóa bên gửi trước. Index update hoặc writer khác vẫn có thể tạo deadlock; phải có retry thích hợp.

## Ba loại thất bại khác nhau

| Tình huống | Có biết transaction commit chưa? | Xử lý |
|---|---|---|
| SQL Server deadlock victim 1205 | Transaction victim đã rollback | Retry toàn đơn vị công việc có giới hạn |
| Validation không đủ tiền | Biết thất bại nghiệp vụ | Trả lỗi, không retry tự động |
| Mất kết nối sau khi gửi commit | Có thể chưa biết | Query/retry cùng key, không tạo giao dịch mới |

Dùng backoff có jitter và giới hạn lần/thời gian, ghi correlation ID. Không retry cả luồng có HTTP side effect không idempotent như thể chỉ là database transaction.

## Idempotency bền vững

Một contract tốt có scope `(TenantId, Operation, IdempotencyKey)`, payload identity và kết quả đã commit. Cùng key/cùng payload trả lại kết quả cũ. Cùng key/khác payload phải báo conflict.

“SELECT chưa có rồi INSERT” không an toàn khi hai request cùng vào. Unique index là chốt bảo vệ. Có thể serialize theo key bằng key-range lock được index hỗ trợ, hoặc thử insert và xử lý duplicate đúng transaction. Dedupe chỉ bằng cache TTL không đủ cho callback đến muộn hay phục hồi sự cố.

Payload fingerprint phải có canonical form và bao gồm mọi trường có ý nghĩa nghiệp vụ; không hash JSON theo thứ tự thuộc tính tùy ý. Với lab nhỏ, lưu trực tiếp account, amount và currency để so sánh.

Nếu cần ghi trạng thái `InProgress` trước transaction chính, phải có lease/owner/expiry và cơ chế phục hồi worker chết. Lab chọn commit request record cùng posting nên không tồn tại request committed dở dang.

## Phạm vi “một lần”

Broker có thể gửi lại. Mục tiêu thiết kế là hiệu ứng nghiệp vụ chỉ một lần trong phạm vi được bảo vệ: inbox unique và cập nhật nghiệp vụ cùng commit. Outbox có thể publish trùng sau crash; consumer vẫn cần idempotency. Không gọi đây là exactly-once end-to-end nếu chưa chứng minh toàn chuỗi.

**Bài tập:** client timeout, gửi lại key cũ sau 10 phút. Đáp án: trả JournalId cũ nếu payload khớp; không hạch toán lại và không suy luận thất bại từ việc client chưa nhận response.
