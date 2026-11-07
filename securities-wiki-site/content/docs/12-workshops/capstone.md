# Capstone: thiết kế nền tảng chứng khoán tham chiếu

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Bài toán giả lập

Thiết kế CTCK Alpha: 200.000 tài khoản, 40.000 online giờ cao điểm, peak 2.000 lệnh/s và 20.000 update market data/s ở đầu vào. Có cổ phiếu, tiền mặt, margin và khách tổ chức; web/mobile/broker portal/API. Các số là yêu cầu luyện tập, không đại diện tải công ty được nêu trong đề bài.

Đối tác ngoài: Sở, VSDC, hai ngân hàng. SLO nhận yêu cầu hợp lệ nội bộ p99≤200 ms tại tải thiết kế, không gồm exchange round trip; yêu cầu không tạo tác động kinh tế trùng. RTO/RPO và ngưỡng mất dữ liệu phải được nhóm đề xuất theo nghiệp vụ, không tự dùng một số cho toàn bộ hệ thống.

## Hồ sơ phải nộp

1. Context diagram và domain map; owner và nguồn sự thật từng dữ liệu.
2. Luồng đặt/sửa/hủy có partial fill, timeout, reconnect, duplicate và cuối ngày.
3. Cash/position buckets, reservation, ledger và invariant kiểm thử được.
4. Ma trận rule có ngày hiệu lực và quy trình phê duyệt.
5. Contract API/event, idempotency scope, privacy và audit model.
6. Capacity model cho lệnh và fan-out, SLO, dashboard và degradation policy.
7. BCP/DR, migration, reconciliation, fault-injection và readiness checklist.
8. RACI, product economics, risk appetite, complaint workflow và go/no-go.

## Tình huống hội đồng sẽ đưa thêm

- Cùng một tài khoản đặt từ ba kênh, tổng yêu cầu vượt tiền.
- Sở chấp nhận nhưng acknowledgement mất; khách bấm lại.
- Thay đổi fee schedule giữa ngày, execution đến chậm.
- Margin price feed stale khi thị trường giảm mạnh.
- Một mã chuyển sàn; lệnh điều kiện đang chờ và dữ liệu chart dài hạn.
- Quyền cổ tức được điều chỉnh sau lần phân bổ đầu.
- Restore database sau khi ngân hàng đã trả tiền.
- Treasury thiếu nguồn funding dù tổng tài sản khách lớn.

## Rubric 100 điểm

| Nhóm | Điểm | Điều kiện đạt |
|---|---:|---|
| Đúng nghiệp vụ và tài sản | 25 | Đi hết vòng đời, không double spend/post |
| Rule/source/effective date | 15 | Không dùng dự thảo như active |
| Integration và recovery | 20 | UNKNOWN, sequence, dedup, external reconciliation |
| Vận hành và bảo mật | 15 | Owner, evidence, drill, controls |
| Kiến trúc và trade-off | 15 | ADR có phương án, giới hạn, kiểm chứng |
| Điều hành và economics | 10 | Funding, cost, risk, customer impact |

Mốc đề xuất đạt: 75/100, không có lỗi nghiêm trọng như giải tỏa tiền khi chưa biết lệnh có khớp hay không hoặc phát lại thanh toán không idempotent. Lỗi critical phải sửa dù tổng điểm cao.

## Hướng giải mẫu

Bắt đầu modular trading core giữ order/reservation trong transaction đủ nhất quán; tách market data read path; adapter bền vững theo từng đối tác; ledger/inbox/outbox có khóa nghiệp vụ; reporting qua projection; reconciliation từ đầu. Có thể tách service dần sau khi chứng minh ownership, capacity và vận hành. Hội đồng chấp nhận phương án khác nếu chứng minh được invariant và rủi ro.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
