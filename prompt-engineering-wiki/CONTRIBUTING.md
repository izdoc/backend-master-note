# Đóng góp và cập nhật

[Trang chính](README.md) · [Nguồn](REFERENCES.md)

Viết tiếng Việt rõ, dùng một tình huống cụ thể. Mỗi bài gồm cơ sở kỹ thuật có nguồn, đầu vào cần có, prompt, lý do thiết kế, ví dụ kết quả, nghiệm thu và lỗi thường gặp. Phân biệt nhận định từ nguồn với thiết kế của tác giả; mọi số liệu demo ghi giả lập.

Prompt mới cần ID theo nhóm, phiên bản liên quan, giới hạn hành động và cách xử lý thiếu bằng chứng. Không dùng hệ thống/credential/PII thật trong fixture. Không yêu cầu xuất suy nghĩ nội bộ; yêu cầu kết luận và evidence kiểm được.

Trước khi gửi thay đổi: đọc bài hiện hành, mở nguồn đúng version, kiểm link nội bộ/code fence/ID; chạy case phù hợp nếu có môi trường. Ghi rõ test đã chạy và chưa chạy. Khi đổi file, cập nhật INDEX/README nếu cấu trúc thay đổi. Không thêm workflow tự động thực thi lệnh trong prompt.

Lưu kết quả eval theo mẫu trong [Evaluation](06-workflows/03-evaluation.md). Nêu version model/tools nếu biết, không bịa khi giao diện không cung cấp. Người review quyết định merge/deploy theo quyền của repo và tổ chức.
