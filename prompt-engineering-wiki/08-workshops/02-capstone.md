# Capstone: sự cố chuyển tiền từ UI tới DB và hạ tầng

[Trang chính](../README.md)

Đây là case thiết kế tự biên soạn, không đại diện hệ thống ngân hàng thật. Không cần gọi dịch vụ bên ngoài.

## Đầu bài

Ứng dụng demo gồm React UI, C# API, SQL Server và NGINX. UI có thể bấm gửi lặp; API gọi dependency giả lập với timeout 2s; dependency có lúc trả kết quả sau 3s. Worker đọc event và ghi báo cáo. Mục tiêu: phân biệt request thất bại với kết quả nghiệp vụ chưa rõ, giữ một business effect cho một yêu cầu trong phạm vi hợp đồng demo.

## Bằng chứng giả lập

```text
L1 08:00:00Z ui request=r1 key=k1 click=submit
L2 08:00:01Z api request=r1 key=k1 dependency_attempt=1 started
L3 08:00:03Z api request=r1 key=k1 dependency_timeout
L4 08:00:03Z proxy request=r1 status=500
L5 08:00:04Z ui request=r2 key=k1 click=submit
L6 08:00:04Z api request=r2 key=k1 received
```

Không có dependency result, DB transaction log hay worker checkpoint. Không kết luận có hai lần chuyển tiền chỉ từ hai click.

## Năm sản phẩm cần nộp

1. Incident brief với facts/hypotheses/unknowns, scope và timeline.
2. Prompt FE sửa double-click và hiển thị trạng thái chưa rõ; không biến client thành nguồn bảo đảm chống trùng.
3. Prompt BE/DB đặc tả scope key, payload conflict, durable state và concurrency test; chưa gọi bank.
4. Prompt Infra nối proxy/app/dependency log theo request ID; chỉ đọc và giữ log thiếu là thiếu.
5. ADR và eval: boundary, status/reconciliation, crash tests, replay và tiêu chí dữ liệu đúng.

## Gợi ý chấm

Đạt khi không bịa bank outcome; có test request lặp/concurrent, crash sau commit trước response và worker replay; có phân biệt state chưa rõ. Nếu đề xuất outbox/inbox phải nêu mục đích và phạm vi transaction. Không chấm theo độ dài sơ đồ hoặc số công nghệ thêm vào.

Dùng [rubric](../06-workflows/03-evaluation.md) và [prompt kiến trúc](../06-workflows/04-architecture-review.md); đối chiếu [RFC HTTP](https://www.rfc-editor.org/rfc/rfc9110.html) và [Kafka delivery semantics](https://kafka.apache.org/41/design/design/) cho claim cụ thể, không xem các nguồn là bảo đảm nghiệp vụ xuyên mọi hệ thống.
