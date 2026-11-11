# Workflow vibe coding có review

[Trang chính](../README.md) · [Nghiệm thu](03-evaluation.md)

Trong wiki, “vibe coding” nghĩa là làm việc theo vòng lặp yêu cầu bằng ngôn ngữ tự nhiên → AI đề xuất/sửa code → người và công cụ kiểm tra. Đây là định nghĩa làm việc của wiki, không phải chứng nhận chất lượng. Tài liệu OpenAI khuyến nghị đánh giá theo nhiệm vụ và theo dõi khi thay đổi prompt/model. [OAI-E](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

## Một vòng làm việc đề xuất

1. **Chốt hành vi:** viết acceptance criteria, edge cases, version và giới hạn.
2. **Đọc hiện trạng:** xin tóm tắt call path/file liên quan, nêu thiếu dữ liệu.
3. **Thay đổi nhỏ:** một slice có thể review; giữ scope và contract đã chốt.
4. **Kiểm tra đúng rủi ro:** build/typecheck; test hành vi lỗi, quyền, concurrency nếu liên quan.
5. **Review diff:** tác động dữ liệu, dependency, log, secret, rollback và vận hành.
6. **Ghi kết quả:** lệnh/output đã chạy, chưa chạy, quyết định và việc còn lại.

Đây là workflow biên soạn. Không phải mọi thay đổi đều cần mọi loại test; chọn kiểm tra có thể phát hiện lỗi thực tế của thay đổi.

## Ví dụ chuỗi prompt: API tạo yêu cầu rút tiền

```text
Vòng 1: Đọc task brief và file liên quan. Chỉ ra invariant, transaction boundary,
scope idempotency và chỗ thiếu. Đề xuất một slice nhỏ; chưa gọi bank.
```

```text
Vòng 2: Thực hiện slice đã chọn trong sandbox, theo conventions của repo.
Tạo test hai request đồng thời cùng key và cùng key/khác payload.
Ghi migration là đề xuất review; chưa áp dụng DB thật.
```

```text
Vòng 3: Review diff từ góc nhìn lỗi giữa commit và response.
Chỉ nêu finding có file/evidence, impact và cách tái hiện.
Sửa finding trong phạm vi rồi chạy kiểm tra liên quan nếu có môi trường.
```

```text
Vòng 4: Viết handoff gồm hành vi sau sửa, file thay đổi, lệnh đã chạy,
kết quả, phần chưa chạy và quyết định triển khai còn chờ.
Không nói “production ready” khi chưa có kiểm chứng triển khai.
```

## Khi nào dừng và bổ sung context?

Nếu model tự tạo interface không có trong repo, quay lại file thật. Nếu sửa vòng lặp nhưng test không kiểm hành vi gốc, viết repro trước. Nếu kết quả cần DB/cluster mà môi trường không có, ghi blocked và chuẩn bị checklist chạy ở lab; không sửa report thành “passed”. Nếu thay đổi vượt contract, cần quyết định mới trước khi tiếp tục.

## Nguồn

- [OAI-E: OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — Đánh giá theo nhiệm vụ, dữ liệu kiểm thử và kết hợp người review.
