# Lộ trình training 8 tuần

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Kết quả đầu ra

Sau khóa học, một thành viên phải giải thích được tiền và chứng khoán đang ở đâu tại từng thời điểm; một lệnh đã được nhận ở lớp nào; ai có quyền sửa sai; dữ liệu nào là bằng chứng; ai chịu trách nhiệm khi có chênh lệch. Kiến thức công nghệ được kiểm tra thông qua các câu hỏi đó.

| Tuần | Chủ đề | Sản phẩm thực hành | Người dẫn |
|---|---|---|---|
| 1 | Thị trường, sản phẩm, thuật ngữ, tài khoản | Vẽ hệ sinh thái và diễn giải một giao dịch | BA + nghiệp vụ |
| 2 | Phiên giao dịch, order book, khớp lệnh | Tính tay sổ lệnh, đấu giá, đọc bảng giá | Trading operations |
| 3 | Phòng ban, tiền, chứng khoán, margin | Vẽ swimlane, bảng trách nhiệm và số dư | Back office + Risk |
| 4 | Sở, gateway, session, market data | Đặc tả xử lý reconnect và mất gói | Integration lead |
| 5 | Clearing, settlement, quyền, đối soát | Đối soát một ngày giả lập | Settlement + Finance |
| 6 | OMS/RMS, ledger, dữ liệu, bảo mật | ADR và mô hình transaction | Architect |
| 7 | SRE, BCP/DR, sự cố, migration | Diễn tập mất kết nối và sai số dư | Operations + Security |
| 8 | Quản trị sản phẩm, rủi ro và capstone | Hội đồng go/no-go | Business director + CTO |

Mỗi tuần có hai buổi 90 phút: 30 phút kiến thức, 35 phút tình huống, 20 phút trình bày, 5 phút chốt bằng chứng. Ngoài giờ học, dành 60–90 phút cho bài tập. Đây là lịch gợi ý cho team, không phải cam kết thời lượng đạt chứng chỉ.

## Ba tuyến học

- **Người mới/Developer/QA:** học theo thứ tự chuyên mục 01–08; sau mỗi bài tự diễn giải bằng ví dụ trước khi viết code.
- **Senior Solution Architect:** học toàn bộ, tập trung 05–10; đầu ra là invariant, consistency boundary, capacity model, failure model, ADR và kế hoạch kiểm chứng.
- **Giám đốc nghiệp vụ:** đọc 01–04, 07–08, 11 và capstone; phải quyết định được quyền phê duyệt, hạn mức, mức chấp nhận rủi ro, cơ chế xử lý khách hàng và điều kiện dừng dịch vụ.

## Rubric thống nhất

Chấm mỗi năng lực 0–3: 0 chưa giải thích được; 1 biết khái niệm; 2 xử lý được tình huống thường; 3 xử lý được ngoại lệ và chứng minh bằng dữ liệu. Sáu năng lực: thị trường, vòng đời lệnh, tiền/chứng khoán, rủi ro, kiến trúc, vận hành. Mục tiêu đào tạo đề xuất: mỗi năng lực từ 2; architect phải đạt 3 ở kiến trúc và vận hành; giám đốc nghiệp vụ phải đạt 3 ở rủi ro và quy trình.

## Cách dùng wiki

Đọc ví dụ theo đúng giả định. Khi ví dụ ghi phí 0,15%, đó là số dùng để luyện tính, không phải biểu phí bắt buộc. Khi trang nói FIX, đó là kiến thức giao thức chung; mapping thực tế phải lấy từ bộ tài liệu thành viên được cấp. Đọc [mốc hiệu lực](../13-reference/regulatory-watch.md) trước buổi training có quy định thị trường.

## Câu hỏi kiểm tra

**Một người biết Kubernetes nhưng chưa phân biệt tiền chờ về và tiền được rút đã đủ thiết kế hệ thống chứng khoán chưa?** Chưa. Hạ tầng tốt không bù được mô hình nghiệp vụ sai; thiết kế sai số dư có thể tạo nghĩa vụ thanh toán mà công ty không đáp ứng được.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
