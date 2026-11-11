# Workflow troubleshooting và phân tích log

[Trang chính](../README.md) · [Incident brief](../07-templates/02-incident-brief.md)

Phương pháp Google SRE dùng giả thuyết và kiểm tra để tìm nguyên nhân. Trong wiki, mỗi giả thuyết phải có phép kiểm và điều kiện loại trừ. [SRE](https://sre.google/sre-book/effective-troubleshooting/)

## Thứ tự làm việc đề xuất

| Bước | Việc cần làm | Ví dụ |
|---|---|---|
| Xác định phạm vi | Expected/actual, impact, bắt đầu/kết thúc | Một endpoint, release demo-42 |
| Bảo toàn evidence | Window, timezone, raw line ID, phần bị cắt | 08:00–08:10 UTC, L1–L200 |
| Lập timeline | Nối bằng request/trace và clock assumptions | API timeout → retry |
| Phân loại | Fact/hypothesis/unknown | 500 là fact; DB down chưa biết |
| Kiểm tra nhỏ | Ưu tiên đọc, nêu output sẽ quyết định gì | Lấy SQL plan, previous container logs |
| Chuẩn bị sửa | Patch, impact, rollback, test | Sửa cleanup hoặc lock order |
| Xác minh | So hành vi và metrics cùng điều kiện | Không lặp business write sau replay |

Các bước là quy ước vận hành của bài tập. Trong incident thật, hành động phục hồi còn phụ thuộc người điều phối, quyền và quy trình tổ chức.

## Ví dụ output tốt

| Evidence | Fact | Hypothesis | Next check |
|---|---|---|---|
| L2 bank timeout | Caller không nhận kết quả trong budget | Bank chậm hoặc response thất lạc | Status query/đối soát qua reference |
| L3 retry=1 | Có ghi nhận retry attempt | Có thể phát sinh gọi lặp | Kiểm idempotency và bank request log |

Không ghi phần trăm tin cậy tùy ý. Khi log lấy mẫu, hãy ghi “trong mẫu N event” và nêu thiếu denominator. Khi clock không đồng bộ, không suy thứ tự chính xác chỉ từ timestamp giữa host.

## Prompt follow-up từ giả thuyết đến kiểm chứng

```text
Giả thuyết H1 là connection pool exhaustion, chưa xác nhận.
Đây là pool metrics và trace cùng cửa sổ [đính kèm].
Chỉ ra evidence ủng hộ/phản bác H1, điều còn thiếu và tối đa hai phép kiểm tiếp theo.
Không tăng pool hoặc timeout trước khi đánh giá tải và dependency budget.
```

## Nguồn

- [SRE: Google SRE — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) — Quan sát, giả thuyết và thử nghiệm để loại trừ nguyên nhân.
- [OTEL: OpenTelemetry — Logs](https://opentelemetry.io/docs/concepts/signals/logs/) — Timestamp, TraceId, SpanId và metadata log.
