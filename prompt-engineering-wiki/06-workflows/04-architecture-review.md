# Prompt cho solution architecture và ADR

[Trang chính](../README.md)

Trang này là phương pháp review do wiki biên soạn. Áp dụng nguyên tắc nêu goal/context/boundary của ChatGPT Learn; không coi output kiến trúc là bằng chứng đáp ứng SLO khi chưa đo. [OAI-C](https://learn.chatgpt.com/docs/prompting)

## Prompt ví dụ: luồng tiếp nhận kết quả NFC

```text
Đề xuất kiến trúc demo nhận kết quả NFC và kích hoạt tài khoản qua downstream.
Chưa có API thật; mọi tên hệ thống là minh họa. Stack C#/.NET + SQL Server.
Mục tiêu nghiệp vụ giả định: chỉ yêu cầu kích hoạt sau NFC được chấp nhận;
duplicate callback không tạo tác động lặp; downstream timeout giữ trạng thái chưa rõ để đối soát.
SLO/volume/retention chưa chốt: liệt kê quyết định còn thiếu, không tự gán thành yêu cầu.
So sánh tối đa 3 phương án: synchronous, durable job, outbox+worker.
Mỗi phương án có transaction boundary, failure modes, auth, observability,
chi phí vận hành và điều kiện phù hợp; không thêm broker chỉ vì “microservices”.
Tạo sequence diagram cho failure path quan trọng và ADR ngắn:
context, decision, alternatives, consequences, validation, open questions.
Nguồn cho cơ chế framework/protocol phải là docs chính thức đúng version.
Không tuyên bố exactly-once cho downstream chưa có hợp đồng idempotency.
```

## Vì sao viết như vậy?

Invariant xác định hành vi cần giữ. SLO chưa biết buộc kiến trúc ghi pending thay vì bịa capacity. So sánh ít phương án có tiêu chí rõ giúp người phụ trách chọn. Failure path cho thấy điểm không nằm trong transaction DB và kế hoạch đối soát. Đây là lập luận thiết kế, chưa phải kết quả thử nghiệm của prompt.

## Ví dụ kết quả mong đợi

ADR có thể chọn durable job nếu phù hợp SLA/đội vận hành, nhưng phải ghi điều kiện để quyết định. Khi downstream timeout, state machine có trạng thái chưa xác định; worker không mù quáng gọi lại nếu chưa có idempotency/status API. Kế hoạch kiểm chứng phải thử crash trước/sau DB commit, callback trùng, callback trái thứ tự và downstream trả kết quả muộn.

## Cách review output

Kiểm xem sơ đồ có thể hiện đúng boundary và ownership không. Yêu cầu dẫn source cho mọi claim về API/guarantee cụ thể; lập danh sách giả định nghiệp vụ riêng. Không dùng số throughput “ước lượng” để phê duyệt sizing. Muốn capacity cần workload model và benchmark phù hợp.

## Nguồn

- [OAI-C: ChatGPT Learn — Prompting](https://learn.chatgpt.com/docs/prompting) — Mục tiêu, ngữ cảnh, đầu ra, ranh giới; dùng cho Chat và Codex.
- [HTTP: IETF — RFC 9110, HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) — HTTP status và idempotent method; không quy định thiết kế Idempotency-Key của ví dụ.
- [KAFKA: Apache Kafka 4.1 — Design](https://kafka.apache.org/41/design/design/) — Delivery semantics và giới hạn exactly-once với sink ngoài Kafka.
