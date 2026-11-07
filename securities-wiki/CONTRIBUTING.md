# Cập nhật bộ wiki

Nội dung đọc trực tiếp trên GitHub bằng Markdown; sơ đồ dùng Mermaid. Không cần cài framework để học. `docs/<category>/` là nguồn chính; README chuyên mục và INDEX được tạo lại bằng script.

## Thêm bài

1. Chọn chuyên mục theo nghiệp vụ, đặt tên file ASCII bằng dấu gạch ngang.
2. Dùng [mẫu bài](templates/lesson.md); viết nội dung thật và ví dụ đủ đầu vào/đáp án.
3. Với quy tắc thị trường, thêm source vào [sources.json](config/sources.json), cập nhật [sổ nguồn](docs/13-reference/sources.md) và trạng thái hiệu lực.
4. Chạy build index, validate, lab tests như README.
5. Review nội dung, kiểm tra bằng tay phép tính và cập nhật CHANGELOG trước commit.

## Sử dụng các file skill

Mở file tương ứng trong `skills/` và yêu cầu trợ lý tuân theo quy trình đó khi sửa dự án:

- [Cập nhật bài wiki](skills/update-securities-wiki/SKILL.md).
- [Rà soát quy định](skills/review-market-rules/SKILL.md).
- [Review kiến trúc](skills/review-securities-architecture/SKILL.md).
- [Soạn buổi training](skills/create-securities-workshop/SKILL.md).

Đây là các skill source theo repository, chưa tự cài vào danh mục skill cá nhân. Khi copy riêng một skill, cần giữ các tài nguyên được liên kết hoặc cập nhật đường dẫn. Các workflow dùng root của dự án làm nơi chứa nguồn chuẩn để tránh sao chép rule nhiều nơi.

## Quyền phê duyệt

Author chuẩn bị thay đổi. Business/Legal owner xác nhận rule pháp lý, Risk xác nhận chính sách rủi ro, QA xác nhận scenario, Architect/Integration xác nhận mapping hệ thống. Việc push tài liệu được người dùng yêu cầu không đồng nghĩa phê duyệt triển khai rule vào production.

Các hạn chế về nguồn nằm trong regulatory watch. Không lấp thông tin chưa rõ bằng giả định rồi ghi là quy định Sở.
