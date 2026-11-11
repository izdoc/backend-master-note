# Lab 02 — VLAN, inter-VLAN, STP và LACP

[Mục lục](../INDEX.md) · [Bảng đối chiếu](../SYLLABUS-MAPPING.md)

**Thời lượng gợi ý:** 2–3 giờ. **Môi trường:** Packet Tracer với 2 switch 2960, 1 router có subinterface và 2 PC. Tên cổng dưới đây là hợp đồng của bài lab; nếu model khác, ghi bảng đổi cổng trước khi nhập. Chưa thực thi trong lần xuất bản này.

## Đường nối và địa chỉ

| Kết nối | Cổng |
|---|---|
| PC-A ↔ SW1 | PC FastEthernet ↔ SW1 Fa0/1 |
| PC-B ↔ SW2 | PC FastEthernet ↔ SW2 Fa0/1 |
| SW1 ↔ SW2, link 1 | Gi0/1 ↔ Gi0/1 |
| SW1 ↔ SW2, link 2 | Gi0/2 ↔ Gi0/2 |
| SW1 ↔ R1 | Fa0/24 ↔ Gi0/0 |

PC-A: `10.10.10.50/24`, gateway `10.10.10.1`. PC-B: `10.10.20.50/24`, gateway `10.10.20.1`. Chỉ cắm link 1 trước. Hai subnet khác nhau cần routing. [C11]

## Bước 1: tạo VLAN và trunk

Trên **cả hai switch**, tạo VLAN10 và VLAN20. SW1 Fa0/1 access VLAN10; SW2 Fa0/1 access VLAN20. Link Gi0/1 và SW1 Fa0/24 là trunk cho VLAN10,20. [C05][C06]

Ví dụ SW1:

```text
enable
configure terminal
vlan 10
 name USERS
vlan 20
 name SERVERS
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10
interface FastEthernet0/24
 switchport mode trunk
 switchport trunk allowed vlan 10,20
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
end
```

SW2 làm tương tự nhưng Fa0/1 thuộc VLAN20 và chưa có Fa0/24 đi router.

## Bước 2: cấu hình router

```text
enable
configure terminal
interface GigabitEthernet0/0
 no shutdown
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
end
show ip route
```

Kỳ vọng có connected routes khi interface up. Ping từng gateway, rồi PC-A → PC-B. [C11]

## Bước 3: quan sát STP rồi LACP

Khi link 1 ổn định, cấu hình Gi0/2 thành trunk giống Gi0/1 ở hai switch rồi nối link 2. Quan sát `show spanning-tree vlan 10`; một đường có thể ở trạng thái alternate/discarding tương ứng. Không bật BPDU filter để ép cả hai đường forwarding. [C07]

Sau đó ở hai switch, gộp Gi0/1–2:

```text
configure terminal
interface range GigabitEthernet0/1 - 2
 channel-group 1 mode active
interface Port-channel1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
end
show etherchannel summary
```

Kỳ vọng hai member được bundled, STP nhìn port-channel là liên kết logic. Rút một member và kiểm tra lại ping; hội tụ có thể làm mất một số gói. [C10]

## Bước 4: chủ động tạo lỗi

Trên SW2 **Port-channel1**, đổi allowed VLAN thành chỉ VLAN10. Ghi output trunk, trạng thái PC-B và lý do. Khôi phục allowed list 10,20; xác nhận lại. Không tạo nhiều lỗi một lúc.

Đọc `show cdp neighbors` và `show lldp neighbors` nếu được hỗ trợ; giải thích vì sao output khác khi LLDP chưa được bật. [C22][C23]

## Nộp bài và hoàn tác

Nộp bảng VLAN/trunk/port-channel/route, ảnh ping và nhật ký một lỗi. Lưu file lab riêng trước thay đổi. Hoàn tác bằng cách mở lại bản trước thử nghiệm hoặc gỡ channel-group/cấu hình lab trên thiết bị lab; không dùng xóa startup-config trên thiết bị thật.

## Nguồn dùng cho lab

- [C05] — Cisco — Configuring VLANs.
- [C06] — Cisco — Configuring VLAN Trunks.
- [C07] — Cisco — PortFast and BPDU Guard.
- [C10] — Cisco — EtherChannels.
- [C11] — Cisco — IP Routing Configuration Guide.
- [C22] — Cisco — Configure CDP.
- [C23] — Cisco — Configure LLDP.

[C05]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-2_1_e/configuration/guide/2960_scg/swvlan.html "Cisco — Configuring VLANs"
[C06]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960x/software/15-2_7_e/configuration_guide/b_1527e_consolidated_2960x_cg/m_vlan_trunk_cg_2960-x.html "Cisco — Configuring VLAN Trunks"
[C07]: https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10586-65.html "Cisco — PortFast and BPDU Guard"
[C10]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-0_2_se/configuration/guide/scg2960/swethchl.html "Cisco — EtherChannels"
[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
[C22]: https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/cdp-lldp-mac-udld/cdp-lldp-mac-udld-configuration-guide/c-configure-cdp.html "Cisco — Configure CDP"
[C23]: https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/cdp-lldp-mac-udld/cdp-lldp-mac-udld-configuration-guide/c-configure-lldp.html "Cisco — Configure LLDP"
