# Onboarding, ủy quyền và quản lý tiền

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Onboarding là workflow có nhiều điều kiện

Thu thập hồ sơ → xác minh danh tính/tư cách → kiểm tra trùng lặp và danh sách kiểm soát theo chính sách → ký thỏa thuận → tạo cấu trúc tài khoản → liên kết nghiệp vụ lưu ký → cấp quyền dịch vụ → thông báo. Các bước có thể đồng bộ hoặc bất đồng bộ, nhưng trạng thái “được phép giao dịch” chỉ bật khi đầy đủ điều kiện tương ứng.

Tách trạng thái hồ sơ, hợp đồng, tài khoản, tài khoản ngân hàng và từng sản phẩm. Một khách hàng đã mở tài khoản không mặc nhiên đủ điều kiện margin, phái sinh hay mua mọi loại trái phiếu. Nhận diện tổ chức cần mô hình người đại diện, chủ sở hữu hưởng lợi, phạm vi ủy quyền và ngày hết hạn theo quy trình được phê duyệt.

## Nộp tiền

Luồng tham chiếu: ngân hàng phát giao dịch → xác minh nguồn bản tin → ghi inbox → chống trùng bằng bank reference trong đúng scope → xác định khách hàng → ghi ledger nguyên tử → cập nhật read model → thông báo. Callback và sao kê có thể cùng mô tả một giao dịch; tránh cộng hai lần. Một bank reference có thể không duy nhất toàn cầu, nên khóa có thể cần ngân hàng, tài khoản nhận, ngày và loại giao dịch.

## Rút tiền

Kiểm tra đăng nhập và quyền → kiểm tra người thụ hưởng → tính withdrawable → giữ tiền nguyên tử → tạo payment instruction → ngân hàng xử lý → nhận/truy vấn trạng thái → hạch toán kết quả → đối soát. Nếu timeout ngân hàng, trạng thái UNKNOWN; không tự giải tỏa hold rồi cho khách rút lần nữa.

Nếu bị từ chối chắc chắn, giải tỏa hold qua sự kiện nghiệp vụ. Nếu ngân hàng hoàn trả sau thành công, ghi giao dịch hoàn trả liên kết, không sửa bản ghi cũ thành chưa từng thành công.

## Hai loại chuyển nội bộ

Chuyển tiền giữa tiểu khoản cùng khách phải bảo toàn tổng tiền và kiểm tra ảnh hưởng margin. Chuyển giữa khách hàng khác là nghiệp vụ khác, có điều kiện và kiểm soát riêng; không tạo API chung chỉ đổi destination ID.

## Kiểm soát mất tài khoản

Đổi số điện thoại, thiết bị tin cậy, phương thức xác thực và tài khoản ngân hàng là hành động nhạy cảm. Thiết kế step-up authentication, kiểm tra phiên/quyền, cảnh báo bất thường và theo dõi sau thay đổi phù hợp chính sách. Không log OTP, giấy tờ đầy đủ hoặc token vào trace.

**Bài tập:** callback ngân hàng báo thành công, truy vấn tức thời báo pending. **Đáp án:** áp dụng state precedence và contract đã thống nhất; giữ cả hai bằng chứng, tra soát khi mâu thuẫn. Không luôn lấy bản tin đến sau làm sự thật.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
