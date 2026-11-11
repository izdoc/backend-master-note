# 02. OSI, TCP/IP và hành trình gói tin

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** Nền tảng bổ trợ CCNA. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Giải thích encapsulation; tách lỗi liên kết, IP, TCP và ứng dụng.

## Dùng mô hình để đặt câu hỏi

OSI là mô hình học 7 tầng: Physical, Data Link, Network, Transport, Session, Presentation, Application. TCP/IP thường được giảng theo 4 nhóm; cách ghép dưới đây là mô hình dạy học, không yêu cầu mọi phần mềm ánh xạ cứng vào một tầng. RFC 1122 mô tả các lớp communication của Internet. [R01]

| OSI | TCP/IP tương ứng khi học | Đối tượng quan sát |
|---|---|---|
| 1–2 | Link | Tín hiệu, Ethernet frame, MAC |
| 3 | Internet | IP packet, route |
| 4 | Transport | TCP segment, UDP datagram, port |
| 5–7 | Application | DNS, HTTP, mã hóa/phiên theo giao thức |

Dữ liệu ứng dụng được bọc trong transport, IP và frame để truyền qua liên kết. Nhận dữ liệu đi theo chiều tháo các lớp. Router thay lớp liên kết theo chặng kế tiếp; trong forwarding IP thông thường không có NAT, cặp IP nguồn/đích giữ nguyên nhưng TTL/Hop Limit giảm. [R01][R06]

## Request HTTPS: ví dụ tự thiết kế

1. Client hỏi DNS để lấy IP của `api.example.test`.
2. Client tra route; dùng ARP nếu cần MAC next hop trên Ethernet IPv4.
3. Với HTTPS qua TCP, client thiết lập TCP, rồi TLS, rồi gửi HTTP.
4. Server xử lý và gửi phản hồi theo đường quay về.

Đây là một trường hợp minh họa, không phải mọi HTTPS đều dùng TCP: HTTP/3 dùng QUIC trên UDP. Tên miền đã cache cũng có thể không tạo DNS query mới. [R02][R10][R21]

## Quan sát và suy luận

| Dấu hiệu | Câu hỏi tiếp theo |
|---|---|
| Không có link | Cáp, nguồn, NIC, trạng thái cổng? |
| ARP không trả lời | Đúng VLAN, IP và gateway? |
| SYN lặp lại | Route, ACL hay dịch vụ không phản hồi? |
| TCP đã nối nhưng TLS lỗi | Tên chứng chỉ, trust chain, thời gian? |
| HTTP 500 | Đã tới thành phần HTTP; kiểm tra ứng dụng/log |

Bảng là phương pháp phân tích do giáo trình đề xuất. Packet capture phải được đọc cùng cấu hình và log; thiếu một gói trong capture chưa chứng minh thiết bị không gửi. [T02]

## Tự kiểm tra

**Câu hỏi:** Qua ba router, MAC đích có luôn là MAC của server cuối không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. MAC thuộc liên kết hiện tại. Khi server ở xa, frame đầu tiên thường gửi tới MAC gateway; frame được thay cho các chặng Ethernet sau.

</details>

## Nguồn của bài

- [R01] — RFC 1122 — Internet host communication layers.
- [R02] — RFC 826 — ARP.
- [R06] — RFC 8200 — IPv6.
- [R10] — RFC 9293 — TCP.
- [R21] — RFC 9110 — HTTP semantics.
- [T02] — Wireshark — User Guide.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R01]: https://www.rfc-editor.org/rfc/rfc1122 "RFC 1122 — Internet host communication layers"
[R02]: https://www.rfc-editor.org/rfc/rfc826 "RFC 826 — ARP"
[R06]: https://www.rfc-editor.org/rfc/rfc8200 "RFC 8200 — IPv6"
[R10]: https://www.rfc-editor.org/rfc/rfc9293 "RFC 9293 — TCP"
[R21]: https://www.rfc-editor.org/rfc/rfc9110 "RFC 9110 — HTTP semantics"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
