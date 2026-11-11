# Prompt Engineering & Vibe Coding Wiki

Hướng dẫn tiếng Việt dùng ChatGPT và coding agent cho **Frontend, Backend, Database và Infrastructure**. Có thêm **Data Engineering (DE)** để hỗ trợ pipeline, event và đối soát.

**30 tình huống với prompt có thể sao chép**, chia theo coding, troubleshooting và phân tích log. Mỗi tình huống có lý do thiết kế prompt, ví dụ kết quả mong đợi, tiêu chí nghiệm thu và lỗi thường gặp. Prompt/contract/số liệu do wiki biên soạn để luyện tập; nguồn chính thức hỗ trợ cơ sở kỹ thuật, không phải chứng nhận hiệu quả của prompt.

[Mục lục đầy đủ](INDEX.md) · [Sổ nguồn](REFERENCES.md) · [Thuật ngữ](GLOSSARY.md) · [Phạm vi kiểm chứng](VALIDATION.md)

## Chọn đúng nhu cầu

| Chủ đề | Coding | Troubleshooting | Phân tích log |
|---|---|---|---|
| FE: React/Next.js | [Component và contract](01-frontend/01-coding.md) | [Hydration, Effect/race](01-frontend/02-troubleshooting.md) | [Console, release/HAR](01-frontend/03-log-analysis.md) |
| BE: C#/.NET | [API, idempotency](02-backend/01-coding.md) | [DbContext, latency](02-backend/02-troubleshooting.md) | [Timeout, exception](02-backend/03-log-analysis.md) |
| DB: SQL Server | [Schema, report query](03-database/01-coding.md) | [Query plan, deadlock](03-database/02-troubleshooting.md) | [Error, Query Store](03-database/03-log-analysis.md) |
| Infra | [Docker, Terraform](04-infrastructure/01-coding.md) | [Pod, NGINX/TLS](04-infrastructure/02-troubleshooting.md) | [Access log, journal](04-infrastructure/03-log-analysis.md) |
| DE mở rộng | [Pipeline, Kafka consumer](05-data-engineering/01-coding.md) | [Retry, Spark skew](05-data-engineering/02-troubleshooting.md) | [Offset, DAG attempt](05-data-engineering/03-log-analysis.md) |

## Bắt đầu trong 15 phút

1. Đọc [khung prompt](00-foundations/01-prompt-design.md) và [bảo vệ dữ liệu](00-foundations/04-security-and-data.md).
2. Chọn một case gần công việc, thay file/version và dùng dữ liệu giả lập hoặc được phép.
3. Ghi phạm vi quyền; với incident, bắt đầu chỉ đọc. Với coding, dùng workspace/lab.
4. Đối chiếu output với nghiệm thu, mở nguồn được dẫn và chạy kiểm tra có thể tái hiện.
5. Lưu phần đã/chưa chạy; dùng follow-up dựa trên output thực tế, không chỉ yêu cầu “làm tốt hơn”.

## Lộ trình gợi ý cho team

| Tuần | Nội dung | Sản phẩm |
|---|---|---|
| 1 | Nền tảng, context, evidence, dữ liệu | Task brief + prompt A/B |
| 2 | FE/BE coding và review | Một patch nhỏ + test hành vi |
| 3 | DB/Infra troubleshooting và log | Incident brief + evidence table |
| 4 | DE, architecture, eval và capstone | ADR + kết quả chấm + handoff |

Lộ trình và thời lượng là đề xuất của wiki. Xem [workshop](08-workshops/01-exercises.md), [capstone](08-workshops/02-capstone.md), [workflow vibe coding](06-workflows/01-vibe-coding.md) và [mẫu copy nhanh](07-templates/01-task-brief.md).

## Phạm vi và giới hạn

Mốc đối chiếu nguồn: **11/11/2026**. Không khóa model cụ thể; prompt cần được thử lại khi model/tools/phiên bản thay đổi. Các đoạn code, log và lệnh là minh họa, chưa phải ứng dụng đã build/chạy hoặc runbook được phê duyệt. Chat không có công cụ không thể tự chạy test hay đọc máy; tài liệu yêu cầu ghi đúng khả năng thực tế. Không có deployment, database migration, giao dịch thật hoặc thay đổi hạ tầng nào được thực hiện bởi việc xuất bản wiki.

Hướng dẫn nền tảng: [OpenAI Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) và [ChatGPT Learn — Prompting](https://learn.chatgpt.com/docs/prompting). Toàn bộ nguồn công nghệ được dẫn tại từng bài và [REFERENCES](REFERENCES.md).
