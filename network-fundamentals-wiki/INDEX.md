# Mục lục Network Fundamentals

[Trang đầu](README.md) · [Lộ trình](ROADMAP.md) · [Đối chiếu syllabus](SYLLABUS-MAPPING.md) · [Nguồn học](REFERENCES.md) · [Thuật ngữ](GLOSSARY.md)

## 01-foundations

- [01. Mạng máy tính và vai trò thiết bị](01-foundations/01-network-and-devices.md) — Vẽ đường đi của một request; phân biệt switch, router, firewall, AP và controller.
- [02. OSI, TCP/IP và hành trình gói tin](01-foundations/02-osi-tcpip-packet-walk.md) — Giải thích encapsulation; tách lỗi liên kết, IP, TCP và ứng dụng.
- [03. Cáp, Ethernet và chỉ số hiệu năng](01-foundations/03-media-ethernet-and-metrics.md) — Chọn loại liên kết; đọc MAC table, lỗi cổng và các chỉ số mạng.
- [04. TCP, UDP, port và kết nối ứng dụng](01-foundations/04-tcp-udp-and-ports.md) — Đọc handshake; hiểu vì sao ping được nhưng API vẫn không truy cập được.

## 02-addressing

- [05. IPv4, CIDR, gateway và ARP](02-addressing/01-ipv4-cidr-and-arp.md) — Xác định subnet của host và next hop; phân biệt IP route với ARP.
- [06. Subnetting, VLSM và kế hoạch địa chỉ](02-addressing/02-subnetting-vlsm-worked-examples.md) — Chia subnet theo nhu cầu; kiểm tra overlap và tính khả năng mở rộng.
- [07. IPv6, Neighbor Discovery và SLAAC](02-addressing/03-ipv6-ndp-and-slaac.md) — Đọc/rút gọn IPv6; hiểu link-local, RA và lý do không chặn toàn bộ ICMPv6.

## 03-switching

- [08. VLAN, trunk và inter-VLAN routing](03-switching/01-vlan-trunk-and-intervlan.md) — Tạo VLAN và trunk; giải thích vì sao trunk không tự định tuyến.
- [09. STP, Rapid PVST+ và bảo vệ vòng lặp](03-switching/02-stp-and-protection.md) — Đọc root/port role; phân biệt BPDU guard, root guard, loop guard và BPDU filter.
- [10. EtherChannel, LACP, CDP và LLDP](03-switching/03-etherchannel-and-discovery.md) — Kiểm tra link aggregation; dùng neighbor discovery để xác nhận dây nối.

## 04-routing

- [11. Routing table, static route và FHRP](04-routing/01-route-selection-and-static.md) — Chọn đúng route; phân biệt longest prefix, administrative distance và metric.
- [12. OSPFv2 một area](04-routing/02-single-area-ospf.md) — Lập neighbor area 0, đọc trạng thái và tìm lỗi adjacency.

## 05-services

- [13. DNS và DHCP: từ tên miền đến cấu hình IP](05-services/01-dns-and-dhcp-protocols.md) — Tách lỗi DNS và DHCP; giải thích relay và cache.
- [14. NAT, PAT và đường về](05-services/02-nat-and-pat.md) — Phân biệt static NAT, dynamic pool và PAT; kiểm tra translation có điều kiện.
- [15. NTP, SNMP, syslog, QoS và truyền file](05-services/03-operations-ntp-snmp-syslog-qos.md) — Chọn công cụ vận hành; hiểu queueing và chính sách thời gian.

## 06-windows-server

- [16. Windows DNS: zone, record và bảo vệ phân giải tên](06-windows-server/01-dns-zones-security-and-lab.md) — Chọn zone type, tạo record lab và hiểu cập nhật DNS an toàn.
- [17. Windows DHCP, IPAM và failover](06-windows-server/02-dhcp-ipam-and-failover.md) — Tạo scope/options trong lab; phân biệt lease HA với quản lý địa chỉ.
- [18. AD DS, NPS/RADIUS và truy cập từ xa](06-windows-server/03-ad-dns-nps-and-remote-access.md) — Hiểu phụ thuộc DNS của domain và chuỗi xác thực truy cập mạng.
- [19. Chi nhánh: DFS, BranchCache và BGP ở mức nhận diện](06-windows-server/04-branch-dfs-and-bgp-context.md) — Phân biệt namespace, replication và cache; biết vị trí BGP trong chương trình lịch sử.
- [20. Networking hiệu năng cao, Hyper-V và SDN](06-windows-server/05-performance-virtualization-and-sdn.md) — Phân biệt teaming, offload, VRF và overlay; chọn phép đo trước tối ưu.

## 07-security-wireless

- [21. ACL, firewall và quản trị thiết bị](07-security-wireless/01-acl-firewall-and-device-access.md) — Viết ACL từ yêu cầu; quản trị bằng SSH và hiểu AAA.
- [22. DHCP snooping, DAI, port security và VPN](07-security-wireless/02-layer2-security-and-vpn.md) — Hiểu chuỗi tin cậy L2; tránh tự chặn IP tĩnh khi bật DAI.
- [23. Wi-Fi, RF, WLC và bảo mật WLAN](07-security-wireless/03-wlan-rf-and-controller.md) — Phân biệt SSID/VLAN; đọc cấu hình WLAN và kiểm tra từ RF đến IP.

## 08-automation

- [24. REST API, JSON, automation và AI trong vận hành mạng](08-automation/01-api-json-iac-and-ai.md) — Đọc JSON và HTTP; biết vai trò Ansible/Terraform và giới hạn AI.

## 09-troubleshooting

- [25. Troubleshooting có bằng chứng và packet capture](09-troubleshooting/01-method-and-packet-capture.md) — Điều tra theo giả thuyết; đọc capture mà không kết luận quá mức.

## Lab và capstone

- [Lab 01 — IP, subnet và packet walk](10-labs/01-ip-and-packet-walk.md)
- [Lab 02 — VLAN, inter-VLAN, STP và LACP](10-labs/02-vlan-routing-and-resilience.md)
- [Lab 03 — Static route, OSPF, IPv6 và NAT](10-labs/03-static-ospf-ipv6-and-nat.md)
- [Lab 04 — Windows DNS/DHCP và bài mở rộng domain/IPAM](10-labs/04-windows-dns-dhcp-and-ipam.md)
- [Lab 05 — Chính sách, Wi-Fi và capture](10-labs/05-policy-wireless-and-capture.md)
- [Lab 06 — Capstone mạng cho hệ thống backend](10-labs/06-capstone-and-report.md)

## Tự đánh giá và duy trì

- [30 câu hỏi](11-assessment/01-review-questions.md)
- [Đáp án và phần cần ôn](11-assessment/02-answers.md)
- [Trạng thái kiểm chứng](VALIDATION.md)
- [Lịch sử nội dung](CHANGELOG.md)
