# Lộ trình 8 tuần và checklist học

[Trang đầu](README.md) · [Mục lục](INDEX.md) · [Nguồn học](REFERENCES.md)

Lịch dưới đây là đề xuất của giáo trình, khoảng 6–8 giờ/tuần. Tăng/giảm theo kiến thức hiện tại; thời gian này không phải cam kết đủ để đậu chứng chỉ. Đối chiếu blueprint ở [SYLLABUS-MAPPING.md](SYLLABUS-MAPPING.md).

| Tuần | Bài | Thực hành | Điều phải tự giải thích được |
|---|---|---|---|
| 1 | 01–04 | Capture handshake, đọc NIC/route | Request qua các lớp nào; switch khác router |
| 2 | 05–07 | Lab01, tính ít nhất 10 subnet | CIDR/VLSM, ARP next hop, IPv6 ND |
| 3 | 08–10 | Lab02 | VLAN/trunk, root/port role, LACP |
| 4 | 11–12 | Lab03 A–C | Longest prefix, route chiều về, OSPF |
| 5 | 13–15 | Lab03 D và DNS/DHCP packet walk | DNS/lease/relay, NAT, log/time/QoS |
| 6 | 16–20 | Lab04, chọn một bài mở rộng | DNS zone, DHCP options, IPAM/NPS/DFS |
| 7 | 21–24 | Lab05 | Policy, SSH, L2 security, WLAN, API/JSON |
| 8 | 25 + ôn | Lab06 + 30 câu tự kiểm tra | Điều tra một lỗi có chứng cứ và rollback |

## Checklist tiến độ cá nhân

Mỗi mục chỉ đánh dấu khi đã giải thích lại không cần nhìn bài.

- [ ] [01. Mạng máy tính và vai trò thiết bị](01-foundations/01-network-and-devices.md)
- [ ] [02. OSI, TCP/IP và hành trình gói tin](01-foundations/02-osi-tcpip-packet-walk.md)
- [ ] [03. Cáp, Ethernet và chỉ số hiệu năng](01-foundations/03-media-ethernet-and-metrics.md)
- [ ] [04. TCP, UDP, port và kết nối ứng dụng](01-foundations/04-tcp-udp-and-ports.md)
- [ ] [05. IPv4, CIDR, gateway và ARP](02-addressing/01-ipv4-cidr-and-arp.md)
- [ ] [06. Subnetting, VLSM và kế hoạch địa chỉ](02-addressing/02-subnetting-vlsm-worked-examples.md)
- [ ] [07. IPv6, Neighbor Discovery và SLAAC](02-addressing/03-ipv6-ndp-and-slaac.md)
- [ ] [08. VLAN, trunk và inter-VLAN routing](03-switching/01-vlan-trunk-and-intervlan.md)
- [ ] [09. STP, Rapid PVST+ và bảo vệ vòng lặp](03-switching/02-stp-and-protection.md)
- [ ] [10. EtherChannel, LACP, CDP và LLDP](03-switching/03-etherchannel-and-discovery.md)
- [ ] [11. Routing table, static route và FHRP](04-routing/01-route-selection-and-static.md)
- [ ] [12. OSPFv2 một area](04-routing/02-single-area-ospf.md)
- [ ] [13. DNS và DHCP: từ tên miền đến cấu hình IP](05-services/01-dns-and-dhcp-protocols.md)
- [ ] [14. NAT, PAT và đường về](05-services/02-nat-and-pat.md)
- [ ] [15. NTP, SNMP, syslog, QoS và truyền file](05-services/03-operations-ntp-snmp-syslog-qos.md)
- [ ] [16. Windows DNS: zone, record và bảo vệ phân giải tên](06-windows-server/01-dns-zones-security-and-lab.md)
- [ ] [17. Windows DHCP, IPAM và failover](06-windows-server/02-dhcp-ipam-and-failover.md)
- [ ] [18. AD DS, NPS/RADIUS và truy cập từ xa](06-windows-server/03-ad-dns-nps-and-remote-access.md)
- [ ] [19. Chi nhánh: DFS, BranchCache và BGP ở mức nhận diện](06-windows-server/04-branch-dfs-and-bgp-context.md)
- [ ] [20. Networking hiệu năng cao, Hyper-V và SDN](06-windows-server/05-performance-virtualization-and-sdn.md)
- [ ] [21. ACL, firewall và quản trị thiết bị](07-security-wireless/01-acl-firewall-and-device-access.md)
- [ ] [22. DHCP snooping, DAI, port security và VPN](07-security-wireless/02-layer2-security-and-vpn.md)
- [ ] [23. Wi-Fi, RF, WLC và bảo mật WLAN](07-security-wireless/03-wlan-rf-and-controller.md)
- [ ] [24. REST API, JSON, automation và AI trong vận hành mạng](08-automation/01-api-json-iac-and-ai.md)
- [ ] [25. Troubleshooting có bằng chứng và packet capture](09-troubleshooting/01-method-and-packet-capture.md)

## Nhật ký lỗi và lịch ôn tự quản lý

| Ngày | Chủ đề | Sai ở đâu? | Bằng chứng / bài đọc lại | Ngày ôn dự kiến | Đã giải thích lại? |
|---|---|---|---|---|---|
| Điền khi học | Ví dụ: subnet | Quên đếm gateway | Bài06, phép tính của mình | Sau 2–3 ngày | Chưa |

Lịch ôn 2–3 ngày, một tuần và cuối lộ trình là gợi ý tự học, không phải tính năng reminder tự động.

## Cách học tiếp

Theo nhánh Cisco: lab đủ các động từ configure/verify trong blueprint, làm thêm GUI WLAN và các tình huống L3 EtherChannel. Theo nhánh Windows: thực hành AD-integrated DNS, failover, IPAM và NPS/certificate ở domain lab riêng theo tài liệu Microsoft. Ghi phiên bản và kết quả, không dùng việc đọc xong làm bằng chứng đã cấu hình được.
