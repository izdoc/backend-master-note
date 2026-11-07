# Khớp định kỳ, sau giờ và thỏa thuận

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Vì sao khớp định kỳ?

Khớp liên tục xử lý lệnh đến từng thời điểm. Khớp định kỳ gom ý định mua/bán trong một khoảng rồi xác định giá thực hiện ở thời điểm quy định. Nó có thể tập trung thanh khoản, nhưng tạo rủi ro thay đổi nhanh sát thời điểm xác định giá. Giá dự kiến trong phiên không phải cam kết giá cuối cùng.

Với tập lệnh LO, tại mỗi giá ứng viên p:

- `Demand(p)` = tổng mua có giá giới hạn ≥ p.
- `Supply(p)` = tổng bán có giá giới hạn ≤ p.
- `Executable(p) = min(Demand(p), Supply(p))`.

Chọn mức thỏa tiêu chí khối lượng; nếu hòa phải dùng đúng chuỗi tiêu chí của thị trường. Lab chỉ đưa ra tập giá tối đa và báo cần tie-break; không tự nhận là thuật toán HOSE đầy đủ.

## Đối chiếu quy tắc định kỳ VNX 2026

Điều 22 tại S16 yêu cầu không chỉ cực đại khối lượng: các lệnh mua cao hơn và bán thấp hơn giá chọn phải được thực hiện hết. Nếu nhiều mức đáp ứng, xét tiếp điều kiện các lệnh một bên được thực hiện hết, bên đối ứng thực hiện hết hoặc một phần; rồi xét giá trùng/gần giá thực hiện gần nhất. Điều khoản có nhánh riêng khi không có mức thỏa điều kiện trung gian. Khi implement cần chép thành decision table được nghiệp vụ kiểm tra, gồm cả trường hợp chưa có giá khớp trước đó; lab tối giản không triển khai đầy đủ chuỗi này.

## Ví dụ có nghiệm duy nhất

Mua: 200 @ 100; 300 @ 101; 100 @ 102. Bán: 100 @ 100; 300 @ 101; 200 @ 102. Đơn vị giá giả lập.

| Giá | Tổng mua có thể khớp | Tổng bán có thể khớp | Lượng khớp |
|---:|---:|---:|---:|
| 100 | 600 | 100 | 100 |
| 101 | 400 | 400 | 400 |
| 102 | 100 | 600 | 100 |

Giá 101 tối đa hóa khối lượng; giao dịch thực hiện tại một giá trong mô hình này. Phân bổ lệnh ở mức giá biên vẫn cần quy tắc ưu tiên. Nếu thêm ATO/ATC, không được gán giá 0 rồi sort như LO; phải biểu diễn loại lệnh và áp dụng quy tắc tương ứng.

## Phiên sau giờ

Phụ lục III quy chế VNX 22/2026 ghi HNX có phiên sau giờ 14:45–14:55 định kỳ và 14:55–15:00 liên tục, với lệnh giới hạn không có giá [S17]. Các hướng dẫn CTCK không hoàn toàn thống nhất cách gọi PLO/LO. Vì vậy data model nên có `phase=AFTER_HOURS`, `orderTypeCode` theo mapping chứng nhận và `displayLabel` riêng. Không đưa chữ PLO vào schema production chỉ vì giao diện quen dùng chữ đó. Quy tắc phân bổ sau giờ phải đối chiếu điều khoản riêng, không suy từ khớp liên tục thông thường.

## Giao dịch thỏa thuận

Hai bên thỏa thuận điều kiện rồi thực hiện báo cáo/xác nhận trên hệ thống theo quy trình. Đây không phải đi xuyên order book. Workflow tham chiếu gồm đề nghị, kiểm tra điều kiện, nhập, bên đối ứng xác nhận, kết quả, đối soát. Cần kiểm soát người nhập/người duyệt, giá/khối lượng, tư cách đối tác, hiệu lực, hủy/sửa theo thẩm quyền và nghĩa vụ tiền/chứng khoán.

Không kết luận thỏa thuận được bỏ qua sức mua, hạn chế chứng khoán hoặc thanh toán. Một giao dịch negotiated vẫn tạo nghĩa vụ; ký email ngoài hệ thống không thay thế mọi bước xác nhận chính thức.

**Bài tập:** hai giá đều có cùng khối lượng khớp cực đại. **Đáp án:** thiếu tie-break specification thì phải dừng xác định giá; kết quả “chọn giá gần tham chiếu” là chưa đủ nếu chưa biết toàn bộ thứ tự tiêu chí của venue.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: S16, S17, S05, S02, DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
