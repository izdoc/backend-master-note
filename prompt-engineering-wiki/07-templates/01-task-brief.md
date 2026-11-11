# Mẫu task brief cho coding

[Trang chính](../README.md) · [Cơ sở thiết kế](../00-foundations/01-prompt-design.md)

Mẫu tự biên soạn. Thay mọi `<...>` trước khi gửi; xóa trường không cần.

```text
Mục tiêu: <hành vi quan sát được>.
Ngữ cảnh: <business flow, framework/version, OS/DB, repo/ref>.
Tài liệu: <file/contract/nguồn chính thức được phép dùng>.
Hiện trạng và expected: <repro, input/output mẫu đã làm sạch>.
Invariant: <quyền, dữ liệu, tiền, thời gian, compatibility>.
Phạm vi: <path cho sửa; công cụ/lệnh được phép; không deploy>.
Đầu ra: <patch nhỏ, giải thích quyết định, test và giới hạn>.
Nghiệm thu: <case và điều kiện pass>.
Nếu thiếu dữ kiện ảnh hưởng hành vi, hỏi đúng phần thiếu; ghi rõ giả định.
Không bịa file/API/test. Dẫn docs chính thức cho nhận định kỹ thuật.
Tách “đã chạy”, “chỉ review tĩnh”, “chưa chạy/blocked”.
```

Ví dụ điền hoàn chỉnh: [FE-C01](../01-frontend/01-coding.md), [BE-C01](../02-backend/01-coding.md), [DB-C01](../03-database/01-coding.md), [INF-C01](../04-infrastructure/01-coding.md).
