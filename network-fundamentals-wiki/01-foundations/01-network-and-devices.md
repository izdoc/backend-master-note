# 01. Mạng máy tính và vai trò thiết bị

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.1–1.2. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Vẽ đường đi của một request; phân biệt switch, router, firewall, AP và controller.

## Mạng giải quyết việc gì?

Mạng cho phép các endpoint trao đổi dữ liệu qua liên kết và giao thức chung. LAN thường nằm trong phạm vi cơ sở; WAN nối các mạng ở xa. Internet là liên mạng; một mạng nội bộ không cần Internet để hai máy cùng LAN trao đổi. Client yêu cầu dịch vụ, server cung cấp dịch vụ; cùng một máy có thể giữ cả hai vai trò. [C02]

## Đặt thiết bị đúng chỗ

| Thành phần | Công việc chính | Ví dụ tự thiết kế |
|---|---|---|
| Switch L2 | Chuyển Ethernet frame theo MAC trong VLAN | Nối PC với máy in |
| Router / switch L3 | Chuyển IP packet giữa subnet | User VLAN sang Server VLAN |
| Firewall | Áp chính sách giữa vùng mạng | Cho HTTPS vào API |
| IPS | Phát hiện/chặn lưu lượng phù hợp dấu hiệu tấn công | Chặn mẫu exploit |
| AP | Cho client Wi-Fi truy cập LAN | Laptop vào mạng văn phòng |
| Controller | Điều khiển/cấu hình nhiều thiết bị | Quản lý nhiều AP |
| PoE switch/injector | Cấp điện qua Ethernet cho thiết bị tương thích | AP, IP phone |

Bảng tóm lược vai trò; một thiết bị thực tế có thể gộp nhiều chức năng. Kiểm tra công suất PoE và khả năng thiết bị thay vì chỉ kiểm tra có cổng mạng. [C01][C02]

## Kiến trúc cơ bản

Two-tier thường gộp distribution và core; three-tier tách access/distribution/core. Spine-leaf nối leaf lên các spine, phù hợp lưu lượng giữa các server. SOHO thường gộp router, switch, AP và NAT. On-premises và cloud đều cần thiết kế địa chỉ, route và chính sách truy cập. [C01][C02]

## Tình huống

PC `10.10.10.50/24` gọi API `10.10.20.20/24`: PC xác định đích ở subnet khác, chuyển frame tới gateway. Gateway định tuyến sang subnet server, chính sách có thể cho hoặc chặn. Không thể kết luận “API lỗi” chỉ vì thấy timeout.

**Lỗi dễ nhầm:** switch L2 không tự tạo kết nối giữa hai VLAN; có Internet không chứng minh DNS nội bộ đúng. Đây là suy luận từ vai trò thiết bị trong mô hình trên.

## Tự kiểm tra

**Câu hỏi:** Hai PC cùng VLAN và cùng subnet có cần router để trao đổi trực tiếp không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Chúng có thể trao đổi qua switch L2 sau khi phân giải địa chỉ liên kết. Router cần khi chuyển giữa các subnet.

</details>

## Nguồn của bài

- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [C02] — Cisco — What is computer networking?.
- [R02] — RFC 826 — ARP.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[C02]: https://www.cisco.com/site/us/en/learn/topics/networking/what-is-computer-networking.html "Cisco — What is computer networking?"
[R02]: https://www.rfc-editor.org/rfc/rfc826 "RFC 826 — ARP"
