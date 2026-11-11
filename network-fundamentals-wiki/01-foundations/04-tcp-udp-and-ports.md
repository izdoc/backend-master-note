# 04. TCP, UDP, port và kết nối ứng dụng

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.5. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Đọc handshake; hiểu vì sao ping được nhưng API vẫn không truy cập được.

## Hai kiểu transport

TCP cung cấp byte stream có thứ tự và cơ chế truyền lại; dùng sequence/acknowledgment và flow control. Handshake mở kết nối thường là SYN → SYN/ACK → ACK. TCP không tự biết một request nghiệp vụ đã được commit, nên ứng dụng vẫn cần cơ chế chống xử lý trùng khi retry. [R10]

UDP mang datagram, không bảo đảm giao hàng, thứ tự hoặc chống trùng ở lớp UDP. Ứng dụng có thể bổ sung các cơ chế đó. “UDP luôn nhanh hơn” là kết luận thiếu điều kiện: kết quả phụ thuộc giao thức ứng dụng, loss và workload. [R11]

## Socket và port

Một flow thường được nhận diện bằng IP nguồn, port nguồn, IP đích, port đích và transport. Client thường dùng port tạm thời; server lắng nghe trên port dịch vụ. Port có thể đổi cấu hình; số port là manh mối, không chứng minh nội dung ứng dụng. [T01]

| Dịch vụ thường gặp | Transport/port mặc định để học |
|---|---|
| SSH | TCP 22 |
| DNS | UDP và TCP 53 |
| DHCPv4 server/client | UDP 67/68 |
| HTTP / HTTPS phổ biến | TCP 80/443; HTTP/3 có thể dùng UDP 443 |
| NTP | UDP 123 |
| SMB trực tiếp | TCP 445 |
| RADIUS authentication/accounting | UDP 1812/1813 |

Tra registry trước khi viết firewall rule; ứng dụng thực tế có thể dùng giá trị khác. [T01]

## Đọc triệu chứng

Ví dụ tự thiết kế: `Test-NetConnection 10.10.20.20 -Port 443` thành công nghĩa là kiểm tra TCP tới cổng đó thành công trong lần đo. Nó chưa kiểm tra được chứng chỉ, quyền đăng nhập hay phản hồi nghiệp vụ.

RST có thể đến từ host hoặc thiết bị trung gian chủ động từ chối; timeout có thể do drop, thiếu route hoặc máy không phản hồi. “Connection refused” và “timeout” cần nhánh điều tra khác nhau. [R10]

**Thực hành:** capture một kết nối HTTPS, tìm SYN/SYN-ACK/ACK; sau đó quan sát FIN hoặc RST. Không kỳ vọng đọc được HTTP payload khi TLS đang mã hóa. [T02]

## Tự kiểm tra

**Câu hỏi:** Ping thành công có xác nhận SQL Server hoặc HTTPS đang hoạt động không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Ping kiểm tra ICMP; cần kiểm tra đúng transport/port, rồi đến giao thức và nghiệp vụ ứng dụng.

</details>

## Nguồn của bài

- [R10] — RFC 9293 — TCP.
- [R11] — RFC 768 — UDP.
- [T01] — IANA — Service names and port numbers.
- [T02] — Wireshark — User Guide.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R10]: https://www.rfc-editor.org/rfc/rfc9293 "RFC 9293 — TCP"
[R11]: https://www.rfc-editor.org/rfc/rfc768 "RFC 768 — UDP"
[T01]: https://www.iana.org/assignments/service-names-port-numbers/ "IANA — Service names and port numbers"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
