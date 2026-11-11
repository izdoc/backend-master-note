# 13. DNS và DHCP: từ tên miền đến cấu hình IP

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 4.3, 4.6. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Tách lỗi DNS và DHCP; giải thích relay và cache.

## DNS giải quyết tên

Resolver hỏi hệ thống DNS; authoritative server trả dữ liệu cho zone mình chịu trách nhiệm, recursive resolver tìm câu trả lời thay client và cache theo TTL. Cache giúp giảm truy vấn, cũng khiến sửa record chưa xuất hiện ngay ở mọi client. NXDOMAIN khác timeout: một bên là phản hồi tên không tồn tại, bên kia chưa nhận được phản hồi cần thiết. [R13]

| Record | Ý nghĩa |
|---|---|
| A / AAAA | Tên tới IPv4 / IPv6 |
| CNAME | Alias tới một tên khác |
| MX | Mail exchanger |
| NS / SOA | Name server / thông tin authority của zone |
| PTR | Tra ngược địa chỉ theo namespace reverse |
| SRV | Vị trí dịch vụ, kèm port/priority/weight |

DNS dùng cả UDP và TCP 53; không chỉ TCP khi zone transfer, và TCP không nên bị chặn chỉ vì “DNS là UDP”. DNSSEC xác thực dữ liệu DNS theo chuỗi tin cậy, không mã hóa nội dung truy vấn. [R14][M05]

## DHCPv4 cấp lease

DORA là cách nhớ chu trình thường gặp: Discover, Offer, Request, ACK. Lease gồm IP có thời hạn và có thể kèm mask, router, DNS. Reservation gắn việc cấp IP với định danh client; exclusion ngăn cấp trong một dải; chúng là hai khái niệm khác nhau. Renewal không nhất thiết lặp toàn bộ broadcast như lần đầu. [R12][M09]

Broadcast DHCP không được router chuyển như lưu lượng IP thông thường. Relay trên gateway chuyển yêu cầu tới server khác subnet và cung cấp thông tin giúp chọn scope. [R12]

Ví dụ tự thiết kế cho gateway VLAN 10:

```text
interface GigabitEthernet0/0.10
 ip helper-address 10.10.20.10
```

Kiểm tra route và policy giữa relay/server; nhiều image Cisco helper mặc định chuyển thêm loại UDP khác, nên phải kiểm tra tài liệu/image khi áp thực tế. [C11]

## Quy trình kiểm tra

Client không có IP phù hợp: xem link/VLAN → DHCP packets → relay → scope/lease/options. Có IP nhưng không mở được tên: hỏi DNS cụ thể bằng `nslookup` hoặc `Resolve-DnsName`, so với kết quả dùng IP. Địa chỉ IPv4 link-local 169.254.x.x là dấu hiệu cần kiểm tra cấp IP, không phải kết luận server DHCP chắc chắn hỏng. [M09][M04]

## Tự kiểm tra

**Câu hỏi:** Client nhận đúng IP nhưng gateway option sai thì có thể vào server cùng subnet không?

<details>
<summary>Xem gợi ý trả lời</summary>

Có thể. Giao tiếp cùng subnet không cần default gateway; truy cập subnet khác có thể thất bại.

</details>

## Nguồn của bài

- [R12] — RFC 2131 — DHCPv4.
- [R13] — RFC 1034 — DNS concepts.
- [R14] — RFC 1035 — DNS implementation.
- [M04] — Microsoft — DNS overview.
- [M05] — Microsoft — DNS architecture.
- [M09] — Microsoft — DHCP overview.
- [C11] — Cisco — IP Routing Configuration Guide.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R12]: https://www.rfc-editor.org/rfc/rfc2131 "RFC 2131 — DHCPv4"
[R13]: https://www.rfc-editor.org/rfc/rfc1034 "RFC 1034 — DNS concepts"
[R14]: https://www.rfc-editor.org/rfc/rfc1035 "RFC 1035 — DNS implementation"
[M04]: https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top "Microsoft — DNS overview"
[M05]: https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-architecture "Microsoft — DNS architecture"
[M09]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top "Microsoft — DHCP overview"
[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
