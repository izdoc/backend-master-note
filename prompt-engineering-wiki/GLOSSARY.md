# Thuật ngữ

[Trang chính](README.md)

Giải thích ngắn theo cách dùng của wiki; không thay thế định nghĩa đầy đủ trong nguồn.

| Thuật ngữ | Cách hiểu |
|---|---|
| Prompt | Yêu cầu/ngữ cảnh đưa cho model. |
| Context | Thông tin giúp xử lý đúng nhiệm vụ; cần kiểm nguồn và phiên bản. |
| Constraint | Điều kiện/giới hạn phải giữ. |
| Acceptance criteria | Điều kiện quan sát được để nghiệm thu. |
| Zero-shot | Yêu cầu không kèm cặp ví dụ input/output. |
| Few-shot | Yêu cầu có một số ví dụ input/output. |
| Delimiter | Dấu phân tách dữ liệu; không phải ranh giới bảo mật tuyệt đối. |
| Hallucination | Nội dung sai/bịa nhưng được trình bày có vẻ đúng. |
| Grounding | Gắn câu trả lời với bằng chứng/tài liệu được cung cấp. |
| Eval | Bài đánh giá theo nhiệm vụ và tiêu chí. |
| Fixture | Dữ liệu cố định phục vụ kiểm tra. |
| Repro | Các bước/đoạn mã tái hiện hiện tượng. |
| Fact | Điều đã quan sát/đối chiếu trong phạm vi bằng chứng. |
| Hypothesis | Giả thuyết cần kiểm. |
| Unknown | Thông tin chưa biết. |
| RCA | Phân tích nguyên nhân gốc; có thể tạm thời hoặc đã xác nhận. |
| Trace ID | Định danh nối ngữ cảnh trace khi hệ thống có truyền nó. |
| Span | Một đơn vị thao tác trong trace; có thể lồng nhau. |
| Denominator | Mẫu số cần có khi tính tỷ lệ. |
| Idempotency | Lặp thao tác vẫn giữ hiệu ứng theo hợp đồng đã xác định. |
| Invariant | Điều kiện nghiệp vụ/dữ liệu cần luôn đúng trong phạm vi định nghĩa. |
| Transaction boundary | Ranh giới các thao tác được bảo vệ bởi transaction cụ thể. |
| Replay | Xử lý lại input/event đã có. |
| Watermark | Mốc tiến độ theo nghĩa pipeline quy định; cần ghi semantics. |
| Blast radius | Phạm vi có thể bị tác động bởi thay đổi. |
| Rollback | Cách quay lại trạng thái phù hợp; không mặc nhiên phục hồi dữ liệu đã mất. |
| ADR | Bản ghi quyết định kiến trúc cùng bối cảnh/hệ quả. |
| Prompt injection | Dữ liệu không tin cậy cố lái model/công cụ sang nhiệm vụ khác. |
| Vibe coding | Trong wiki: vòng yêu cầu tự nhiên, AI tạo/sửa và kiểm tra có review. |
| Handoff | Bản bàn giao mục tiêu, evidence, quyết định và việc còn lại. |

Đối chiếu [OpenAI prompting](https://developers.openai.com/api/docs/guides/prompt-engineering), [OpenTelemetry Logs](https://opentelemetry.io/docs/concepts/signals/logs/), [RFC 9110](https://www.rfc-editor.org/rfc/rfc9110.html), [Kafka Design](https://kafka.apache.org/41/design/design/), [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).
