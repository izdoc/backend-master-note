# Lab 03 — Static route, OSPF, IPv6 và NAT

[Mục lục](../INDEX.md) · [Bảng đối chiếu](../SYLLABUS-MAPPING.md)

**Thời lượng gợi ý:** 2–3 giờ. **Môi trường:** hai router R1/R2, hai switch và hai PC trong Packet Tracer/CML tương thích. Đây là lab mới, độc lập Lab02. Chưa thực thi trong phiên này.

## Topology bằng bảng cổng

| Thiết bị | Gi0/0 nối LAN | Gi0/1 nối router còn lại |
|---|---|---|
| R1 | 10.1.10.1/24; 2001:db8:10::1/64 | 10.255.0.1/30; 2001:db8:ff::1/64 |
| R2 | 10.2.20.1/24; 2001:db8:20::1/64 | 10.255.0.2/30; 2001:db8:ff::2/64 |

PC-A: 10.1.10.10/24, gateway .1; IPv6 2001:db8:10::10/64, gateway 2001:db8:10::1.
PC-B: 10.2.20.20/24, gateway .1; IPv6 2001:db8:20::20/64, gateway 2001:db8:20::1.
Bật các interface bằng `no shutdown`. Đây là kế hoạch địa chỉ tự thiết kế.

## A. Static IPv4

R1: `ip route 10.2.20.0 255.255.255.0 10.255.0.2`.
R2: `ip route 10.1.10.0 255.255.255.0 10.255.0.1`.

Kiểm tra routing table và ping giữa PC. Xóa route ở R2 bằng lệnh `no ip route ...` tương ứng; giải thích vì sao thiếu chiều về gây thất bại. Khôi phục. [C11]

## B. OSPFv2

Gỡ **cả hai** static route ở phần A trước khi xác nhận học route OSPF. Trên R1:

```text
router ospf 1
 router-id 1.1.1.1
 passive-interface default
 no passive-interface GigabitEthernet0/1
interface GigabitEthernet0/0
 ip ospf 1 area 0
interface GigabitEthernet0/1
 ip ospf 1 area 0
 ip ospf network point-to-point
```

R2 cấu hình đối xứng, Router ID 2.2.2.2. Kiểm tra `show ip ospf neighbor` có Full và `show ip route ospf` có LAN ở xa. Trạng thái phải được đọc cùng topology. [C12][R15]

Tạo lỗi area trên đúng một interface transit, quan sát neighbor mất; khôi phục area0. Không dùng static route tồn tại sẵn để che lỗi.

## C. IPv6 static

Bật `ipv6 unicast-routing` trên cả hai router, gán địa chỉ theo bảng. R1 thêm `ipv6 route 2001:db8:20::/64 2001:db8:ff::2`; R2 thêm route về 2001:db8:10::/64 qua 2001:db8:ff::1. Kiểm tra neighbor, route và ping IPv6. OSPFv2 phần B chỉ phục vụ IPv4 trong lab này. [C11][R06]

## D. PAT như một phương án riêng

Lưu bản C. Giữ transit IPv4, tắt OSPF trên **cả hai router** (`no router ospf 1`) và xác nhận R2 không còn route tới LAN R1. Trên R1 đặt Gi0/0 inside, Gi0/1 outside:

```text
access-list 10 permit 10.1.10.0 0.0.0.255
ip nat inside source list 10 interface GigabitEthernet0/1 overload
ip route 10.2.20.0 255.255.255.0 10.255.0.2
```

Từ PC-A tạo traffic tới PC-B; quan sát translation và địa chỉ nguồn nhìn từ phía R2. PC-B gửi trả về 10.255.0.1 qua gateway R2, không cần biết LAN R1. PAT và route là hai cấu phần khác nhau. [C18][R16]

## Mở rộng và hoàn tác

Thử router làm DHCP client bằng `ip address dhcp` trên một interface **ở topology phụ có DHCP server**, kiểm tra IP/default route nhận được; không thay IP transit chính lúc đang làm A–D. So sánh static NAT và dynamic pool theo bài14.

Nộp 4 ảnh routing/NAT cùng dự đoán trước từng lỗi. Hoàn tác bằng file lab bản C hoặc xóa riêng cấu hình vừa thêm, khôi phục IP/OSPF theo bản lưu.

## Nguồn dùng cho lab

- [C11] — Cisco — IP Routing Configuration Guide.
- [C12] — Cisco — OSPFv2 on an interface basis.
- [C18] — Cisco — NAT troubleshooting FAQ.
- [R15] — RFC 2328 — OSPFv2.
- [R16] — RFC 3022 — Traditional NAT.
- [R06] — RFC 8200 — IPv6.

[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
[C12]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iro-mode-ospfv2.html "Cisco — OSPFv2 on an interface basis"
[C18]: https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/218012-troubleshoot-network-address-translation.html "Cisco — NAT troubleshooting FAQ"
[R15]: https://www.rfc-editor.org/rfc/rfc2328 "RFC 2328 — OSPFv2"
[R16]: https://www.rfc-editor.org/rfc/rfc3022 "RFC 3022 — Traditional NAT"
[R06]: https://www.rfc-editor.org/rfc/rfc8200 "RFC 8200 — IPv6"
