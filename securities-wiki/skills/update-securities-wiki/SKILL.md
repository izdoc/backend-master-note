---
name: update-securities-wiki
description: "Cập nhật và mở rộng bài trong securities-wiki; dùng khi thêm kiến thức nghiệp vụ, sửa bài, bổ sung ví dụ hoặc cập nhật cấu trúc category."
---

# update-securities-wiki


1. Xác định root chứa `AGENTS.md`, `docs`, `config`, `labs`; đọc quy tắc dự án.
2. Đọc bài hiện tại và bài liên quan trước khi sửa. Chọn category theo nghiệp vụ, không tạo category theo tên công nghệ nếu đã có miền phù hợp.
3. Đọc [sổ nguồn](../../docs/13-reference/sources.md). Với dữ kiện có thể thay đổi, truy xuất nguồn gốc và ghi hiệu lực; chuyển sang workflow rà quy định nếu cần.
4. Dùng [mẫu bài](../../templates/lesson.md). Giải thích đơn giản, có ví dụ tính được, failure mode, câu hỏi và đáp án. Gắn nguồn đúng claim, gắn nhãn DESIGN cho kiến nghị.
5. Bảo toàn dữ liệu lịch sử và nội dung ngoài yêu cầu. Cập nhật bài tập/config liên quan, không để hai câu trả lời mâu thuẫn.
6. Chạy `python3 scripts/build_index.py`, `python3 scripts/validate.py`, và tests lab từ root dự án. Xem diff và cập nhật CHANGELOG.
7. Báo file đổi, kiến thức mới, xác minh và điểm còn thiếu. Chỉ push theo phạm vi người dùng yêu cầu; không tự triển khai production.

Ví dụ đầu vào: “Thêm bài sức mua cho tài khoản margin”; đầu ra phải có định nghĩa bucket, công thức được ghi là minh họa, race condition và test hoặc bài tập chứng minh.
