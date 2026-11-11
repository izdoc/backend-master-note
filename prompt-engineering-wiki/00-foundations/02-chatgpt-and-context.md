# Dùng ChatGPT và coding agent với đúng ngữ cảnh

[Trang chính](../README.md)

Tài liệu ChatGPT Learn mô tả Chat cho trao đổi và Codex cho công việc với code/công cụ. Năng lực thực tế còn phụ thuộc giao diện, công cụ, quyền và tài khoản đang có; câu “hãy chạy test” không tự cấp shell hay quyền truy cập repo. [OAI-C](https://learn.chatgpt.com/docs/prompting)

## Chọn cách làm

| Tình huống | Dữ liệu cần đưa | Đầu ra nên yêu cầu |
|---|---|---|
| Hỏi/thiết kế trong chat | File hoặc đoạn code nhỏ, yêu cầu và version | Giải thích, patch đề xuất, test cần chạy |
| Agent có workspace | Repo/path/ref, hướng dẫn dự án, repro | Đọc file, sửa, chạy kiểm tra được cấp quyền |
| Chẩn đoán từ log | Log đã làm sạch và metadata | Evidence table; không bịa trạng thái máy |
| Tích hợp qua API | Prompt version, model snapshot nếu hỗ trợ, eval dataset | Output có schema/validation do ứng dụng kiểm |

API role là khái niệm của tích hợp API; gõ chữ “system:” vào chat không tương đương đổi system message. Tham khảo role và ví dụ message trong hướng dẫn API. [OAI-P](https://developers.openai.com/api/docs/guides/prompt-engineering)

## Gói context do wiki đề xuất

1. Business brief và invariant: điều gì phải đúng dù code thay đổi?
2. Phiên bản: csproj/package.json/lockfile/provider version, OS và engine.
3. File tối thiểu: caller, hàm lỗi, contract và config liên quan đã bỏ secret.
4. Bằng chứng: repro, expected/actual, timestamp và line IDs.
5. Quyền: chỉ đọc, sửa workspace hay được chạy lab; deployment là quyết định riêng.

Không tải cả repo chỉ để sửa một hàm. Bắt đầu với tập file đủ dùng, bổ sung khi câu hỏi mới cần file khác. Đây là lựa chọn workflow của wiki; đo lại chi phí và kết quả trong nhóm.

## Follow-up để cải thiện câu trả lời

```text
Giữ nguyên mục tiêu và contract ở task brief.
Patch vừa đề xuất chưa xử lý request AB trả trước A.
Đây là test thất bại và output thực tế [đính kèm].
Sửa đúng hành vi đó, giải thích file nào đổi và chạy lại test liên quan nếu có công cụ.
Không viết lại toàn bộ module. Phân biệt test đã chạy với test chỉ đề xuất.
```

Nếu câu trả lời dùng API không có trong version hiện tại, đưa exact error và yêu cầu đối chiếu docs/package đã khóa. Nếu hội thoại quá dài, dùng [handoff](../07-templates/04-handoff.md) ghi lại facts/decisions/open items; không tin bản tóm tắt tự sinh thay cho file hiện hành.

## Nguồn

- [OAI-C: ChatGPT Learn — Prompting](https://learn.chatgpt.com/docs/prompting) — Mục tiêu, ngữ cảnh, đầu ra, ranh giới; dùng cho Chat và Codex.
- [OAI-P: OpenAI — Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) — Ngữ cảnh, ví dụ đầu vào/đầu ra và chỉ dẫn rõ ràng.
