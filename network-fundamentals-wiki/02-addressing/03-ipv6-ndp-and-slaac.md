# 07. IPv6, Neighbor Discovery và SLAAC

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.8–1.9. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Đọc/rút gọn IPv6; hiểu link-local, RA và lý do không chặn toàn bộ ICMPv6.

## Đọc địa chỉ

IPv6 có 128 bit, viết bằng 8 nhóm hex. Bỏ zero đầu mỗi nhóm; `::` thay một chuỗi nhóm zero và chỉ dùng một lần trong một địa chỉ. Ví dụ tự thiết kế `2001:0db8:0010:0000:0000:0000:0000:0020` rút thành `2001:db8:10::20`. [R06][R07]

| Loại | Ví dụ / phạm vi | Ý nghĩa |
|---|---|---|
| Global unicast | Thường gặp trong 2000::/3 | Địa chỉ unicast có phạm vi global |
| Link-local | fe80::/10 | Chỉ trên link; cần interface scope khi mơ hồ |
| Unique local | fc00::/7; thường dùng fd... | Dùng nội bộ theo mô hình ULA |
| Multicast | ff00::/8 | Một nhóm interface |
| Loopback / unspecified | ::1 / :: | Loopback / chưa có địa chỉ |
| Anycast | Dùng địa chỉ dạng unicast | Nhiều node cùng địa chỉ, tới node theo routing |

IPv6 không có broadcast. Anycast “gần” theo định tuyến, không nhất thiết gần địa lý. [R07]

## NDP và tự cấu hình

IPv6 dùng Neighbor Discovery qua ICMPv6: NS/NA cho neighbor resolution; RS/RA để host tìm router và thông tin link. Host nhận default router qua RA; DHCPv6 không thay RA để cấp default gateway. SLAAC dùng prefix từ RA và tạo interface identifier; DAD kiểm tra trùng địa chỉ. [R08][R09]

Modified EUI-64 chèn `ff:fe` vào giữa MAC 48 bit và đảo bit U/L. Ví dụ MAC `00:11:22:33:44:55` cho IID `0211:22ff:fe33:4455`. Không phải mọi host hiện đại đều dùng EUI-64; có thể dùng cơ chế khác. [R07][R09]

## Thực hành đọc output

Cisco: `show ipv6 interface brief`, `show ipv6 neighbors`, `show ipv6 route`. Windows: `Get-NetIPAddress -AddressFamily IPv6`; Linux: `ip -6 address`, `ip -6 route`.

Ví dụ interface router:

```text
ipv6 unicast-routing
interface GigabitEthernet0/0
 ipv6 address 2001:db8:10::1/64
 no shutdown
```

Địa chỉ 2001:db8 dùng cho tài liệu/lab. Kiểm tra image hỗ trợ và RA trước khi kỳ vọng client tự cấu hình. [C11][R08]

**Lỗi dễ nhầm:** chặn toàn bộ ICMPv6 có thể làm hỏng ND và thông báo MTU; có IPv6 link-local chưa chứng minh có route ra ngoài link. [R06][R08]

## Tự kiểm tra

**Câu hỏi:** Hai interface cùng dùng fe80::1 trên hai link khác nhau có luôn là trùng IP không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Link-local chỉ có ý nghĩa trong link; hệ điều hành dùng interface scope để phân biệt.

</details>

## Nguồn của bài

- [R06] — RFC 8200 — IPv6.
- [R07] — RFC 4291 — IPv6 addressing.
- [R08] — RFC 4861 — Neighbor Discovery.
- [R09] — RFC 4862 — SLAAC.
- [C11] — Cisco — IP Routing Configuration Guide.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R06]: https://www.rfc-editor.org/rfc/rfc8200 "RFC 8200 — IPv6"
[R07]: https://www.rfc-editor.org/rfc/rfc4291 "RFC 4291 — IPv6 addressing"
[R08]: https://www.rfc-editor.org/rfc/rfc4861 "RFC 4861 — Neighbor Discovery"
[R09]: https://www.rfc-editor.org/rfc/rfc4862 "RFC 4862 — SLAAC"
[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
