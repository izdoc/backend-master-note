# Giám đốc nghiệp vụ: mô hình kinh doanh và quyền quyết định

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Bản đồ lợi ích và rủi ro

Nguồn doanh thu có thể đến từ phí môi giới, dịch vụ tài chính, tư vấn, phân phối và hoạt động đầu tư theo giấy phép. Chi phí gồm vốn, công nghệ, nhân sự, market data, tuân thủ, vận hành và tổn thất. Tăng giao dịch không tự tạo lợi nhuận nếu phí giảm nhưng chi phí nguồn vốn và rủi ro tăng.

| Quyết định | Thông tin tối thiểu | Cơ chế kiểm soát |
|---|---|---|
| Ra sản phẩm | Khách mục tiêu, giấy phép/điều kiện, unit economics | Product approval và readiness |
| Cấp tín dụng | Nguồn vốn, risk appetite, concentration | Limits, collateral, escalation |
| Mở kênh API | Khách được cấp quyền, tải, hành vi tự động | Quota, auth, surveillance |
| Mở lại sau sự cố | Phạm vi lỗi, nghĩa vụ chưa rõ, bằng chứng phục hồi | Go/no-go có owner |
| Giảm phí | Doanh thu thực, cost-to-serve, churn | Đánh giá theo cohort |

## KPI cân bằng

Theo dõi active funded accounts, conversion từ onboarding tới giao dịch, retention, revenue per customer, cost-to-serve, utilization nguồn vốn, margin concentration, complaint turnaround, reconciliation breaks và operational loss. Cặp KPI rất quan trọng: tăng doanh số phải đi cùng chất lượng tín dụng; tăng tốc mở tài khoản đi cùng kiểm soát hồ sơ; uptime đi cùng đúng tài sản.

## Họp vận hành hằng ngày

Trước phiên: trạng thái hệ thống, lịch thị trường, thay đổi mã/quyền, funding và sự cố còn mở. Sau phiên: giao dịch bất thường, lệnh UNKNOWN, settlement due, break trọng yếu, khiếu nại và công việc ngày kế tiếp. Quyết định phải có owner và deadline; “IT đang xử lý” không phải trạng thái nghiệp vụ đủ rõ.

## Thẩm quyền ngoại lệ

Thiết kế ma trận quyền theo loại rủi ro, giá trị, thời gian và tác động khách hàng. Một người có thẩm quyền kinh doanh không mặc nhiên có quyền thay cơ chế kỹ thuật của Sở. IT không được dùng privilege hạ tầng để quyết định miễn phí, cấp tín dụng hay xóa nghĩa vụ.

## Đưa sản phẩm vào vận hành

Product dossier cần customer journey, eligibility, legal basis, pricing, ledger entries, cash/position impacts, settlement, reporting, abuse scenarios, support script, control owner, metrics và exit plan. Người duyệt phải hiểu tình huống xấu nhất có thể mất bao nhiêu, trong bao lâu và ai trả tiền.

**Bài tập:** ra margin campaign trước khi có funding stress test. **Đáp án:** cần lượng hóa cash outflow và concentration trước quyết định; hạn mức doanh số không thay thế thanh khoản.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
