# Mục lục

[Trang chính](README.md)

## Nền tảng

- [Thiết kế prompt theo kết quả cần đạt](00-foundations/01-prompt-design.md)
- [Dùng ChatGPT và coding agent với đúng ngữ cảnh](00-foundations/02-chatgpt-and-context.md)
- [Bằng chứng, trích nguồn và điều chưa biết](00-foundations/03-evidence-and-sources.md)
- [Dữ liệu nhạy cảm và ranh giới công cụ](00-foundations/04-security-and-data.md)

## Frontend

- [FE • Coding: từ yêu cầu đến component](01-frontend/01-coding.md): FE-C01 Form tạo lệnh chuyển tiền, FE-C02 Trang danh sách trong Next.js
- [FE • Troubleshooting: hydration và Effect](01-frontend/02-troubleshooting.md): FE-T01 Hydration sai do ngày giờ, FE-T02 Fetch hai lần và response cũ đè mới
- [FE • Phân tích console, HAR và lỗi runtime](01-frontend/03-log-analysis.md): FE-L01 Phân biệt HTTP lỗi và lỗi UI, FE-L02 Tóm tắt lỗi theo release

## Backend

- [BE • Coding API, validation và idempotency](02-backend/01-coding.md): BE-C01 API tạo yêu cầu rút tiền chống trùng, BE-C02 Refactor endpoint và response lỗi
- [BE • Troubleshooting EF Core và API chậm](02-backend/02-troubleshooting.md): BE-T01 DbContext bị dùng đồng thời, BE-T02 API p95 tăng sau release
- [BE • Phân tích structured log và trace](02-backend/03-log-analysis.md): BE-L01 Timeout và retry không rõ kết quả, BE-L02 Gom nhóm exception không mất chi tiết

## Database

- [DB • Coding schema, migration và truy vấn](03-database/01-coding.md): DB-C01 Schema lưu kết quả NFC minh họa, DB-C02 Truy vấn báo cáo theo ngày
- [DB • Troubleshooting query chậm và deadlock](03-database/02-troubleshooting.md): DB-T01 Tuning có baseline, DB-T02 Deadlock hai transaction
- [DB • Phân tích error log, deadlock XML và thống kê](03-database/03-log-analysis.md): DB-L01 Error number và giới hạn kết luận, DB-L02 So sánh thống kê query theo cửa sổ

## Infrastructure

- [Infra • Coding Docker và Terraform](04-infrastructure/01-coding.md): INF-C01 Container hóa API trong sandbox, INF-C02 Review Terraform trước apply
- [Infra • Troubleshooting container và reverse proxy](04-infrastructure/02-troubleshooting.md): INF-T01 Pod khởi động lại liên tục, INF-T02 NGINX 502 sau đổi backend
- [Infra • Phân tích NGINX, systemd và sự cố nhiều lớp](04-infrastructure/03-log-analysis.md): INF-L01 Phân tích access log có timing, INF-L02 Đọc journal theo unit và thời gian

## Data Engineering mở rộng

- [DE mở rộng • Coding pipeline và consumer](05-data-engineering/01-coding.md): DE-C01 Pipeline đối soát chạy lại an toàn, DE-C02 Kafka consumer ghi DB
- [DE mở rộng • Troubleshooting chất lượng và hiệu năng](05-data-engineering/02-troubleshooting.md): DE-T01 Số tiền tăng sau retry, DE-T02 Spark job chậm do một task
- [DE mở rộng • Phân tích DAG, offset và lag](05-data-engineering/03-log-analysis.md): DE-L01 Offset commit không chứng minh mọi side effect, DE-L02 Gom DAG log theo attempt

## Workflow và kiến trúc

- [Workflow vibe coding có review](06-workflows/01-vibe-coding.md)
- [Workflow troubleshooting và phân tích log](06-workflows/02-incident-and-logs.md)
- [Đánh giá prompt và kết quả code](06-workflows/03-evaluation.md)
- [Prompt cho solution architecture và ADR](06-workflows/04-architecture-review.md)

## Mẫu tái sử dụng

- [Mẫu task brief cho coding](07-templates/01-task-brief.md)
- [Mẫu incident brief](07-templates/02-incident-brief.md)
- [Mẫu contract phân tích log](07-templates/03-log-contract.md)
- [Mẫu handoff và review diff](07-templates/04-handoff.md)

## Thực hành

- [Workshop: luyện prompt với dữ liệu giả lập](08-workshops/01-exercises.md)
- [Capstone: sự cố chuyển tiền từ UI tới DB và hạ tầng](08-workshops/02-capstone.md)

## Tra cứu và bảo trì

- [Nguồn](REFERENCES.md)
- [Thuật ngữ](GLOSSARY.md)
- [Đóng góp](CONTRIBUTING.md)
- [Kiểm chứng](VALIDATION.md)
