# Sổ nguồn chính thức và cách sử dụng

[Trang chính](README.md)

Mốc đối chiếu: **11/11/2026**. Các trang dưới được mở và đối chiếu trong lần biên soạn này. Sổ nguồn không phải cam kết nội dung URL không đổi. Một số trang Microsoft có banner yêu cầu đăng nhập nhưng nội dung kỹ thuật vẫn đọc được; manual systemd dùng nguồn XML chính thức trên GitHub vì trang freedesktop timeout.

## Tiêu chí chọn

Ưu tiên tài liệu chính thức của dự án/nhà cung cấp và RFC. Mỗi bài dẫn source ngay cạnh cơ sở kỹ thuật; prompt và contract demo do wiki tự biên soạn. Không nguồn nào chứng minh các prompt này tối ưu cho mọi model hay bảo đảm code an toàn.

| ID | Tài liệu | Dùng để đối chiếu |
|---|---|---|
| OAI-P | [OpenAI — Prompt engineering](https://developers.openai.com/api/docs/guides/prompt-engineering) | Ngữ cảnh, ví dụ đầu vào/đầu ra và chỉ dẫn rõ ràng. |
| OAI-C | [ChatGPT Learn — Prompting](https://learn.chatgpt.com/docs/prompting) | Mục tiêu, ngữ cảnh, đầu ra, ranh giới; dùng cho Chat và Codex. |
| OAI-R | [OpenAI — Reasoning best practices](https://developers.openai.com/api/docs/guides/reasoning-best-practices) | Prompt trực tiếp; không cần yêu cầu chuỗi suy nghĩ nội bộ. |
| OAI-E | [OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) | Đánh giá theo nhiệm vụ, dữ liệu kiểm thử và kết hợp người review. |
| REACT-D | [React — You Might Not Need an Effect](https://react.dev/learn/you-might-not-need-an-effect) | Phân biệt dữ liệu tính từ state với đồng bộ hệ thống ngoài. |
| REACT-E | [React — Synchronizing with Effects](https://react.dev/learn/synchronizing-with-effects) | Dependency, cleanup và hành vi development. |
| NEXT-S | [Next.js — Server and Client Components](https://nextjs.org/docs/app/getting-started/server-and-client-components) | Ranh giới server/client trong App Router. |
| NEXT-H | [Next.js — Hydration error](https://nextjs.org/docs/messages/react-hydration-error) | Khác biệt HTML server và lần render client đầu tiên. |
| PW | [Playwright — Best Practices](https://playwright.dev/docs/best-practices) | Test hành vi và locator theo role/text. |
| EF-C | [Microsoft — DbContext configuration](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/) | Lifetime và giới hạn sử dụng DbContext đồng thời. |
| EF-Q | [Microsoft — Efficient Querying](https://learn.microsoft.com/en-us/ef/core/performance/efficient-querying) | Projection, index và các chi phí truy vấn. |
| NET-E | [Microsoft — ASP.NET Core error handling](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/error-handling?view=aspnetcore-10.0) | Xử lý lỗi theo môi trường và response lỗi. |
| SQL-U | [Microsoft — UNIQUE and CHECK constraints](https://learn.microsoft.com/en-us/sql/relational-databases/tables/unique-constraints-and-check-constraints?view=sql-server-ver16) | Constraint tại database; dùng cho ví dụ SQL Server 2022. |
| SQL-N | [Microsoft — decimal and numeric](https://learn.microsoft.com/en-us/sql/t-sql/data-types/decimal-and-numeric-transact-sql?view=sql-server-ver16) | Precision và scale; không tự chọn chính sách làm tròn nghiệp vụ. |
| SQL-Q | [Microsoft — Query Store](https://learn.microsoft.com/en-us/sql/relational-databases/performance/monitoring-performance-by-using-the-query-store?view=sql-server-ver17) | Lịch sử query, plan và runtime; kiểm tra tính năng ở phiên bản thực tế. |
| SQL-D | [Microsoft — Deadlocks guide](https://learn.microsoft.com/en-us/sql/relational-databases/sql-server-deadlocks-guide?view=sql-server-ver17) | Chu trình khóa và xml_deadlock_report. |
| PG-E | [PostgreSQL — Using EXPLAIN](https://www.postgresql.org/docs/current/using-explain.html) | Plan; EXPLAIN ANALYZE thực sự thực thi câu lệnh. |
| TF | [HashiCorp — terraform plan](https://developer.hashicorp.com/terraform/cli/commands/plan) | Xem trước thay đổi; saved plan có thể chứa bí mật. |
| DOCKER | [Docker — Running containers](https://docs.docker.com/engine/containers/run/) | Mount, port, resource và runtime options. |
| K8S | [Kubernetes — Debug Running Pods](https://kubernetes.io/docs/tasks/debug/debug-application/debug-running-pod/) | Pod status, logs và logs của container trước đó. |
| NG-L | [NGINX — HTTP log module](https://nginx.org/en/docs/http/ngx_http_log_module.html) | log_format, access_log và thời gian request. |
| NG-U | [NGINX — HTTP upstream module](https://nginx.org/en/docs/http/ngx_http_upstream_module.html) | Upstream status và biến đo thời gian. |
| SYSTEMD | [systemd — journalctl manual source](https://github.com/systemd/systemd/blob/main/man/journalctl.xml) | Nguồn manual chính thức; đối chiếu man trên máy với phiên bản cài đặt. |
| OTEL | [OpenTelemetry — Logs](https://opentelemetry.io/docs/concepts/signals/logs/) | Timestamp, TraceId, SpanId và metadata log. |
| OWASP-L | [OWASP — Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) | Dữ liệu nên loại khỏi log và bảo vệ log. |
| OWASP-I | [OWASP — LLM Prompt Injection Prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html) | Defense in depth và quyền công cụ; delimiter không phải cơ chế cách ly. |
| HTTP | [IETF — RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) | HTTP status và idempotent method; không quy định thiết kế Idempotency-Key của ví dụ. |
| SRE | [Google SRE — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) | Quan sát, giả thuyết và thử nghiệm để loại trừ nguyên nhân. |
| AIRFLOW | [Apache Airflow — Best Practices](https://airflow.apache.org/docs/apache-airflow/stable/best-practices.html) | Task retry, kết quả nhất quán và data interval. |
| KAFKA | [Apache Kafka 4.1 — Design](https://kafka.apache.org/41/design/design/) | Delivery semantics và giới hạn exactly-once với sink ngoài Kafka. |
| SPARK | [Apache Spark — SQL Performance Tuning](https://spark.apache.org/docs/latest/sql-performance-tuning.html) | Partition, statistics, join và adaptive execution. |

| SQL-ERR | [Microsoft — SQL Server error 2627](https://learn.microsoft.com/en-us/sql/relational-databases/replication/mssql-eng002627?view=sql-server-ver17) | Đối chiếu mã duplicate key/constraint, không suy nguyên nhân replication khi thiếu bằng chứng. |

## Phạm vi phiên bản

Ví dụ lấy C#/.NET theo csproj thực tế; SQL Server 2022 là target của bài DDL; React/Next theo lockfile và App Router khi ghi rõ. Link SQL view ver17 dùng cho cơ chế Query Store/deadlock, không khẳng định mọi tính năng ver17 có trên 2022. Kafka cố định docs 4.1; Spark/Airflow/PostgreSQL/NGINX/Kubernetes/Terraform dùng nguồn đang xuất bản, cần mở lại theo version cài đặt trước khi dùng syntax/config cụ thể. Không có tuyên bố “bản mới nhất” về sản phẩm/chứng chỉ/model.

## Cách thêm nhận định mới

Ghi claim, URL, section, version, ngày mở và bài sử dụng. Nếu nguồn bị đổi hoặc không mở được, đánh dấu pending và đừng dùng nó để khẳng định cơ chế chưa kiểm. Khi thay prompt, lưu case/output trước và sau; khi thay công nghệ, kiểm cả acceptance criteria và giới hạn guarantee.
