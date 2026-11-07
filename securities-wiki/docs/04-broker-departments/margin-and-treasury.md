# Margin, tài sản bảo đảm và thanh khoản công ty

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Margin là tín dụng có tài sản bảo đảm

Margin cổ phiếu và ký quỹ phái sinh không phải cùng một nghiệp vụ. Margin cổ phiếu thường liên quan khoản vay tài trợ mua; ký quỹ phái sinh là tài sản đảm bảo nghĩa vụ vị thế. Dùng chung tên `MarginBalance` mà không có ngữ nghĩa sẽ làm sai báo cáo.

## Mô hình giá trị tài sản bảo đảm

Công thức đào tạo: `eligibleValue = Σ(qty_i × min(marketPrice_i, valuationCap_i) × collateralRate_i)`. Đây chỉ là một mô hình tham chiếu. Công ty có thể có haircut, giới hạn tập trung, danh mục được nhận, giá định giá riêng và quy tắc xử lý quyền.

Giả lập: 1.000 cổ phiếu, giá 40.000, tỷ lệ nhận 50% → giá trị được tính 20 triệu. Giá giảm xuống 30.000 → còn 15 triệu. Khoản vay 18 triệu lúc này vượt giá trị ví dụ 3 triệu. Không kết luận tự động call margin 3 triệu nếu chưa biết công thức maintenance, lãi, phí, tiền và các tài sản khác.

## Quy trình khoản vay

Hợp đồng → đánh giá điều kiện → cấp hạn mức → giải ngân theo giao dịch → tính lãi → theo dõi tài sản → cảnh báo → bổ sung/giảm dư nợ → xử lý theo điều khoản khi vi phạm → tất toán. Cần theo dõi ngày giải ngân, ngày đến hạn, lãi suất theo kỳ, phương pháp tính ngày và thứ tự thu nợ.

**Call margin** là cảnh báo/yêu cầu khắc phục theo policy. **Force sell** là quyết định xử lý được phép theo hợp đồng/quy định. Chúng cần phân quyền, bằng chứng thông báo, hạn mức và xử lý trường hợp tài sản không thanh khoản. Không giả định force sell chắc chắn thu được đủ tiền.

## Rủi ro cấp công ty

Một khách hàng có đủ tài sản bảo đảm không có nghĩa công ty có đủ tiền thanh toán toàn thị trường. Treasury quản lý dòng tiền đến hạn, nguồn vay, room ngân hàng, nhu cầu settlement, rút tiền khách, kịch bản thị trường giảm và ngày nghỉ. Risk quản lý tập trung theo khách, nhóm liên quan, mã, ngành và nguồn vốn.

## Chính sách phải version hóa

Lưu eligibility và valuation policy dùng cho quyết định sức mua. Khi giảm tỷ lệ tài sản, đánh giá khách bị ảnh hưởng và thời điểm áp dụng; không retroactively làm biến mất lịch sử phê duyệt. Stale price hoặc limit service lỗi cần chế độ kiểm soát đã phê duyệt; “cho qua để giữ trải nghiệm” có thể phát sinh nghĩa vụ không đảm bảo.

**Bài tập:** dùng cache 5 phút cho số dư margin có an toàn không? **Đáp án:** có thể dùng cho màn hình có nhãn độ trễ; quyết định đặt lệnh cần trạng thái và reservation đủ nhất quán, cộng với chính sách giá stale rõ ràng.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
