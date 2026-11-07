# Architect: ADR, NFR, trade-off và đánh giá giải pháp

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Một quyết định kiến trúc tốt phải kiểm chứng được

ADR ghi bối cảnh, invariant, lựa chọn, phương án khác, lý do, hệ quả, cách kiểm tra và điều kiện xem lại. “Dùng microservice vì scalable” không đủ. Nêu tải nào tăng, boundary nào cần độc lập và failure mode nào được cải thiện hoặc trở nên khó hơn.

## Ma trận NFR

| NFR | Câu hỏi cụ thể | Bằng chứng cần có |
|---|---|---|
| Correctness | Có thể vượt sức mua hoặc ghi fill hai lần không? | Concurrency/crash test và reconciliation |
| Latency | p95/p99 ở load và cửa sổ nào? | Histogram, trace, test data |
| Capacity | Peak, skew, burst, recovery load? | Load model và kết quả |
| Availability | Hỏng thành phần nào vẫn phục vụ gì? | Fault injection và runbook |
| Recoverability | Restore xong đối chiếu external effects ra sao? | DR rehearsal |
| Auditability | Tái dựng quyết định bằng ruleset nào? | Sample audit reconstruction |
| Changeability | Đổi rule hoặc venue mapping mất bao lâu? | Config versioning và regression |
| Security | Ai có thể sửa tiền/quyền/hạn mức? | Threat model và access review |

## Build hay buy

Build cho phép kiểm soát domain và integration nhưng đòi năng lực vận hành lâu dài. Buy rút ngắn một phần triển khai nhưng có rủi ro phụ thuộc và giới hạn truy xuất dữ liệu. Đánh giá cả exit cost, khả năng đọc journal, test harness, licensing market data và yêu cầu tùy biến. Không so chỉ giá license năm đầu.

## Kỹ thuật nợ và roadmap

Ưu tiên theo rủi ro kinh tế × xác suất × khả năng phát hiện, đồng thời xét phụ thuộc và cost of delay. Sửa thiếu idempotency trên thanh toán thường cấp thiết hơn đổi framework UI. Roadmap nên tách control hardening, capacity, product capability và modernization để người điều hành biết giá trị từng nhóm.

## Review liên chức năng

Architect, Business, Risk, Operations, Security và Finance cùng review các điểm thuộc thẩm quyền. Các câu hỏi bắt buộc: tiền và chứng khoán bị giữ ở đâu; recovery dựa trên nguồn nào; có thể gửi trùng không; ai xử lý ngoại lệ; báo cáo nào bị ảnh hưởng; cấu hình có ngày hiệu lực không; ai được dừng/mở lại.

**Bài tập:** đề nghị dùng event sourcing toàn hệ thống. **Đáp án:** xem domain nào hưởng lợi từ replay, quy định correction, schema evolution, storage và khả năng vận hành. Không áp dụng đồng loạt nếu chỉ cần audit và outbox cho phần lớn nghiệp vụ.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
