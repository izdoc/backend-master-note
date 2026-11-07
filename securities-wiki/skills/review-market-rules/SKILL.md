---
name: review-market-rules
description: "Rà soát quy định thị trường chứng khoán Việt Nam và cập nhật mốc hiệu lực; dùng khi luật, quy chế Sở/VSDC, loại lệnh, phiên hoặc settlement thay đổi."
---

# review-market-rules


1. Đọc [regulatory watch](../../docs/13-reference/regulatory-watch.md), [sources](../../docs/13-reference/sources.md), [config nguồn](../../config/sources.json).
2. Tìm văn bản gốc chính thức. Kiểm tra cơ quan, số, năm, ngày ban hành, ngày hiệu lực, văn bản thay thế, điều khoản chuyển tiếp và phạm vi.
3. Đọc điều khoản/phụ lục cần dùng. Nếu PDF là scan, kiểm tra hình ảnh bảng hoặc đoạn quyết định; không dựa riêng OCR khi số/ký hiệu mơ hồ.
4. Phân loại active, future-effective, draft, historical, unresolved theo ngày người dùng yêu cầu. Khi listing mâu thuẫn điều khoản hiệu lực, ghi mâu thuẫn và ưu tiên văn bản có thẩm quyền.
5. Dùng [mẫu impact](../../templates/rule-change.md), lập delta cũ/mới và liệt kê bài, config, lab, báo cáo, UI, gateway bị ảnh hưởng.
6. Không bịa wire fields, IP, port, SLA hay eligibility chưa xác minh. Giữ tham số thiếu là chưa phê duyệt.
7. Cập nhật nguồn và bài cùng nhau; chạy validate/index/tests. Phân biệt cập nhật wiki với phê duyệt rule production của business/legal owner.

Ví dụ: “Hôm nay trước ngày hiệu lực nhưng thông tư đã ban hành” phải giữ trạng thái future-effective; không biến thành active chỉ vì đã có PDF.
