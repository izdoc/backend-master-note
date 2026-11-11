# Phạm vi kiểm chứng lần xuất bản

[Trang chính](README.md)

Mốc: **11/11/2026**.

| Hạng mục | Trạng thái | Phạm vi |
|---|---|---|
| Nguồn chính thức | Đã mở/đối chiếu | 32 nguồn; xem REFERENCES và giới hạn phiên bản |
| Nội dung prompt | Đã rà soát tĩnh | 30 case, đủ 5 nhóm × 3 loại × 2 tình huống |
| Link Markdown nội bộ, code fence, ID, JSON ví dụ | Đã kiểm tự động | Kết quả được tạo từ validator khi xuất bản |
| Chạy prompt A/B với model | Chưa chạy | Không có số pass rate/hiệu quả thực nghiệm |
| Build/test các ứng dụng trong prompt | Chưa chạy | Chỉ có đoạn mã minh họa và yêu cầu tạo code |
| SQL, container, cluster, Terraform | Chưa thực thi | Không kết nối DB/cluster hoặc apply hạ tầng |
| UI/HAR, production logs, giao dịch | Không sử dụng | Mọi case/log/số liệu là giả lập |

Không xem “mong đợi” là kết quả đã chạy. Nguồn có thể hỗ trợ cơ chế công nghệ nhưng không chứng minh prompt tối ưu. Kiểm đúng version trong dự án, contract nghiệp vụ, quyền và dữ liệu trước khi áp dụng. Khi dùng công cụ thật, lưu lệnh/exit status/output và cập nhật trạng thái theo bằng chứng thực tế.

## Kết quả kiểm cấu trúc

35 file Markdown; 30 case ID duy nhất; 160 liên kết nội bộ hợp lệ; code fence cân bằng; 1 block JSON parse hợp lệ. Không có lỗi cấu trúc được phát hiện. Kiểm tra này không xác nhận tính đúng của code hoặc hiệu quả prompt.
