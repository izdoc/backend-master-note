# Thiết kế prompt theo kết quả cần đạt

[Trang chính](../README.md)

ChatGPT Learn đề xuất nêu mục tiêu, ngữ cảnh, đầu ra và ranh giới khi những phần đó hữu ích. OpenAI API mô tả cách thêm ví dụ input/output và tài liệu liên quan. Đây là kỹ thuật định hướng, không bảo đảm đáp án đúng. [OAI-C](https://learn.chatgpt.com/docs/prompting) [OAI-P](https://developers.openai.com/api/docs/guides/prompt-engineering)

## Cách dùng trong kỹ thuật phần mềm

Wiki dùng khung biên soạn: **Mục tiêu → Ngữ cảnh → Bằng chứng → Giới hạn → Đầu ra → Nghiệm thu**. Khung này là quy ước của wiki, không phải tiêu chuẩn hay công thức chính thức của OpenAI. Không cần điền mọi ô cho câu hỏi ngắn.

| Phần | Ví dụ | Mục đích thiết kế |
|---|---|---|
| Mục tiêu | Sửa stale response khi tìm khách hàng | Chốt hành vi quan sát được |
| Ngữ cảnh | React, version từ lockfile, StrictMode dev | Tránh chọn nhầm API/giả định |
| Bằng chứng | Component, repro và request trả ngược | Cho phép kiểm tra giả thuyết |
| Giới hạn | Không tắt StrictMode; chưa gọi API thật | Giới hạn thay đổi |
| Đầu ra | Patch nhỏ và test race | Tạo kết quả review được |
| Nghiệm thu | AB luôn là kết quả cuối khi q=AB | Đo hành vi thay vì độ hay của câu trả lời |

## Prompt mơ hồ và prompt đủ dùng

Mơ hồ: “Bạn là senior dev, sửa React của tôi cho tốt nhất.”

```text
Sửa SearchBox để response của query cũ không ghi đè query mới.
File component, lockfile và mock API đã đính kèm. Repro: A trả sau AB.
Giữ contract props và UI hiện có, chưa thêm package.
Trả diff tối thiểu và test response trả ngược; báo phần chưa chạy.
```

Role giúp chọn góc nhìn nhưng không thay thế file, version hay bằng chứng. Đoạn trên là ví dụ tự biên soạn, chưa phải kết quả thực nghiệm.

## Kỹ thuật chọn theo nhu cầu

| Kỹ thuật | Khi dùng | Ví dụ trong wiki |
|---|---|---|
| Zero-shot | Hành vi đơn giản, contract rõ | Viết query có khoảng UTC |
| Few-shot | Phân loại cần nhãn/format ổn định | Cho 2 ví dụ log và nhãn evidence/unknown |
| Delimiter | Phân biệt yêu cầu với dữ liệu | Đặt log trong block riêng có line ID |
| Chia nhiệm vụ | Có nhiều quyết định hoặc tác động | Thu bằng chứng → patch → verify |
| Retrieval | API/version hoặc quy định cần nguồn | Mở tài liệu chính thức đúng version |
| Output contract | Kết quả cần kiểm/so sánh | facts, hypotheses, next_checks |

OpenAI hướng dẫn prompt reasoning trực tiếp, không cần yêu cầu chuỗi suy nghĩ nội bộ. Trong wiki, hãy yêu cầu kết luận kèm bằng chứng, giả định và kiểm tra có thể tái hiện. [OAI-R](https://developers.openai.com/api/docs/guides/reasoning-best-practices)

Ví dụ few-shot tự biên soạn:

```text
Phân loại nhận định: FACT / HYPOTHESIS / UNKNOWN.
Ví dụ: “L1 status=401” -> FACT.
Ví dụ: “Token đã hết hạn” khi chỉ có 401 -> HYPOTHESIS.
Ví dụ: “Thời điểm hết hạn token” khi không có metadata -> UNKNOWN.
Đầu vào: L2 ghi bank timeout. Nhận định: ngân hàng chưa chuyển tiền.
```

Kết quả mong đợi cho nhận định cuối: HYPOTHESIS; cần status query hoặc đối soát. Nếu schema đầu ra nghiêm ngặt, bổ sung ví dụ lỗi và kiểm tra bằng parser; một yêu cầu JSON trong chat không tự tạo bảo đảm schema.

## Nguồn

- [OAI-C: ChatGPT Learn — Prompting](https://learn.chatgpt.com/docs/prompting) — Mục tiêu, ngữ cảnh, đầu ra, ranh giới; dùng cho Chat và Codex.
- [OAI-P: OpenAI — Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) — Ngữ cảnh, ví dụ đầu vào/đầu ra và chỉ dẫn rõ ràng.
- [OAI-R: OpenAI — Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) — Prompt trực tiếp; không cần yêu cầu chuỗi suy nghĩ nội bộ.
