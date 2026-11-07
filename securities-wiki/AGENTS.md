# Securities Wiki — hướng dẫn làm việc

## Phạm vi

- Viết tài liệu tiếng Việt rõ ràng cho BA, QA, developer, architect và lãnh đạo nghiệp vụ.
- Chỉ sửa chuyên mục được yêu cầu; bảo toàn nội dung khác trong repository.
- Đây là wiki đào tạo và lab giả lập, không phải engine chứng khoán production.
- Các thư mục `skills/` là source workflow đi kèm dự án; không giả định đã cài vào tài khoản ChatGPT/Codex của người dùng.

## Quy tắc nội dung

1. Đọc README, bài liên quan, `docs/13-reference/sources.md` và regulatory watch trước khi cập nhật rule.
2. Ưu tiên văn bản gốc VNX/HOSE/HNX/VSDC/UBCKNN/Bộ Tài chính. Ghi ngày đọc, ngày ban hành, ngày hiệu lực, phạm vi và điều khoản đã xác minh.
3. Phân biệt hiện hành, tương lai đã ban hành, dự thảo, lịch sử và chưa xác minh. Không gọi dự thảo là quy định đang áp dụng.
4. Không suy đoán IP/port, wire schema, SLA, topology hoặc công nghệ nội bộ SSI, DNSE, TCBS.
5. Dùng dữ liệu giả lập; không đưa credential, PII, dữ liệu khách thật hoặc tài liệu thành viên hạn chế vào repo công khai.
6. Mỗi bài mới có mục tiêu/ngữ cảnh, giải thích, ví dụ hoặc tình huống, câu hỏi và đáp án, nguồn/giới hạn.
7. Cập nhật bài tập và config cùng thay đổi nội dung; lưu ngữ cảnh lịch sử và source version.

## Kiểm tra trước commit

```bash
python3 scripts/build_index.py
python3 scripts/validate.py
python3 -m unittest discover -s labs -p 'test_*.py' -v
```

Thực hiện từ thư mục `securities-wiki`. Kiểm tra diff, không thêm output sinh tự động ngoài các file được chủ ý quản lý. Ghi CHANGELOG. Không force push. Khi cập nhật nhánh, kiểm tra remote HEAD và bảo toàn thay đổi người khác.
