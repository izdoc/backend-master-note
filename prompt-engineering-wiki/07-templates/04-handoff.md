# Mẫu handoff và review diff

[Trang chính](../README.md)

```text
Tóm tắt công việc để người khác tiếp tục:
- Mục tiêu và acceptance criteria hiện hành.
- Repo/ref/commit, file đã thay đổi, quyết định và lý do ngắn.
- Facts đã kiểm được; assumptions chưa xác nhận; nguồn và ngày mở.
- Lệnh đã chạy + exit status + output; kiểm tra chưa chạy + lý do.
- Finding còn mở, rủi ro, bước tiếp theo và giới hạn quyền.
- Không đưa secret hoặc thông tin cá nhân vào bản tóm tắt.
Nếu tóm tắt khác file hiện hành, đọc file hiện hành trước khi sửa tiếp.
```

Prompt review:

```text
Review diff hiện tại theo mục tiêu và contract trong brief.
Chỉ nêu finding có thể chỉ ra file/line, trigger và impact.
Ưu tiên correctness, authorization/tenant, concurrency, transaction, dữ liệu và compatibility.
Không tạo finding chỉ để đủ số lượng. Nếu chưa có evidence thì ghi câu hỏi/giả thuyết.
Nêu test có thể phát hiện mỗi bug; không tự nhận test đã chạy.
```

Hai mẫu tự biên soạn, dùng cùng [rubric](../06-workflows/03-evaluation.md).
