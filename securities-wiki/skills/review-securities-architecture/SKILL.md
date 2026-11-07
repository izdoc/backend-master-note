---
name: review-securities-architecture
description: "Review kiến trúc OMS/RMS, ledger, tích hợp Sở/ngân hàng/VSDC và khả năng phục hồi; dùng khi đánh giá thiết kế, ADR hoặc phương án chuyển đổi."
---

# review-securities-architecture


1. Đọc [kiến trúc tham chiếu](../../docs/09-solution-architecture/reference-architecture.md) và [vòng đời lệnh](../../docs/03-trading-and-matching/order-lifecycle.md).
2. Xác định sản phẩm, actor, nguồn sự thật, boundary tài sản và ngoại tác. Thiếu dữ liệu thì ghi câu hỏi cùng ảnh hưởng quyết định, không tự gán topology của SSI/DNSE/TCBS.
3. Lần theo request → reserve → route → ack/fill → ledger → settlement → reconciliation. Kiểm tra crash trước/sau mỗi bước, duplicate, out-of-order, UNKNOWN và cancel/fill race.
4. Kiểm tra idempotency key/scope/hash, atomicity marker+effect, single-writer/fencing, price staleness, effective rules và quyền phê duyệt.
5. Đọc [DR runbook](../../docs/10-operations-and-security/incident-bcp-dr.md); yêu cầu bằng chứng external reconciliation sau restore.
6. Viết finding gồm mức độ, kịch bản gây lỗi, tác động kinh tế, vị trí trong thiết kế, đề xuất và cách kiểm chứng. Dùng [ADR](../../templates/adr.md) khi có lựa chọn cần quyết định.
7. Không khẳng định exactly-once xuyên nhiều hệ thống nếu chưa chứng minh. Không sửa/call production trong review.
