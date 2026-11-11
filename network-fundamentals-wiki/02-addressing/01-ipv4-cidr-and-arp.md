# 05. IPv4, CIDR, gateway và ARP

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.6–1.7, 1.10. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Xác định subnet của host và next hop; phân biệt IP route với ARP.

## Prefix là phần mạng

IPv4 có 32 bit. `/24` nghĩa là 24 bit đầu thuộc prefix; mask tương ứng `255.255.255.0`. CIDR dùng prefix length, không suy mạng hiện đại chỉ từ nhãn class A/B/C. Với subnet thông thường, network address đặt phần host bằng 0 và broadcast đặt phần host bằng 1. [R04]

Private IPv4 gồm `10.0.0.0/8`, `172.16.0.0/12` và `192.168.0.0/16`. Chúng không phải địa chỉ global để định tuyến trên Internet công cộng. Private không đồng nghĩa với được mã hóa hay được firewall bảo vệ. [R03]

## Phép tính tự thiết kế

Host `192.168.10.70/26`:

| Kết quả | Giá trị |
|---|---|
| Mask | 255.255.255.192 |
| Kích thước block | 64 địa chỉ |
| Subnet | 192.168.10.64/26 |
| Broadcast | 192.168.10.127 |
| Host thông thường | .65 đến .126 |

Lấy `70 AND 192 = 64` ở octet cuối. Đích .90 ở cùng subnet; đích .130 ở subnet khác. Đây là kết quả số học từ prefix, không phải cấu hình bắt buộc của một nhà cung cấp.

## ARP phân giải cái gì?

Trên Ethernet IPv4, ARP tìm MAC ứng với IP **next hop** trên liên kết. Nếu đích ở xa, PC thường ARP cho gateway, không ARP cho server ở xa. ARP request thường broadcast; ARP reply trả thông tin ánh xạ. ARP table khác MAC table của switch và khác routing table. [R02]

Gateway dùng địa chỉ host hợp lệ trong subnet theo thiết kế; không bắt buộc luôn là .1. Có nhiều route thì host tra routing table, không chỉ xem một ô “default gateway”. [R01][R04]

**Thực hành:** Windows: `ipconfig /all`, `route print`, `arp -a`; Linux: `ip address`, `ip route`, `ip neigh`. Ghi IP, prefix, next hop trước khi ping. Lệnh chỉ là công cụ quan sát; kiểm tra output trên OS của mình. [M27][R02]

**Lỗi dễ gặp:** hai máy cùng dải nhìn bằng mắt nhưng khác mask; trùng IP; gateway sai VLAN; ARP cache cũ sau thay thiết bị.

## Tự kiểm tra

**Câu hỏi:** Host 192.168.10.70/26 gửi tới 192.168.10.130: ARP cho .130 hay gateway?

<details>
<summary>Xem gợi ý trả lời</summary>

Theo route mặc định thông thường, ARP cho gateway cùng subnet. .130 không thuộc 192.168.10.64/26.

</details>

## Nguồn của bài

- [R01] — RFC 1122 — Internet host communication layers.
- [R02] — RFC 826 — ARP.
- [R03] — RFC 1918 — Private IPv4.
- [R04] — RFC 4632 — CIDR.
- [M27] — Microsoft — New-NetIPAddress.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R01]: https://www.rfc-editor.org/rfc/rfc1122 "RFC 1122 — Internet host communication layers"
[R02]: https://www.rfc-editor.org/rfc/rfc826 "RFC 826 — ARP"
[R03]: https://www.rfc-editor.org/rfc/rfc1918 "RFC 1918 — Private IPv4"
[R04]: https://www.rfc-editor.org/rfc/rfc4632 "RFC 4632 — CIDR"
[M27]: https://learn.microsoft.com/en-us/powershell/module/nettcpip/new-netipaddress "Microsoft — New-NetIPAddress"
