# Đối chiếu CCNA và MCSA networking

[Trang đầu](README.md) · [Mục lục](INDEX.md) · [Nguồn](REFERENCES.md)

**Mốc:** 11/11/2026. Đây là bản đồ học **fundamentals**, không phải sao chép toàn bộ blueprint hay cam kết phủ mọi câu hỏi thi.

## CCNA 200-301 v1.1

Sáu domain theo Cisco: Network Fundamentals 20%, Network Access 20%, IP Connectivity 25%, IP Services 10%, Security Fundamentals 15%, Automation and Programmability 10%. Mã mục dưới đây tra tại blueprint chính thức. [C01]

| Mã CCNA | Bài/lab của wiki | Mức độ hiện tại / phần cần học thêm |
|---|---|---|
| 1.1–1.4 | [Bài 01](01-foundations/01-network-and-devices.md), [Bài 03](01-foundations/03-media-ethernet-and-metrics.md) | Giải thích/đọc counter; cần quan sát thêm phần cứng thực |
| 1.5 | [Bài 04](01-foundations/04-tcp-udp-and-ports.md) | Giải thích + packet walk |
| 1.6–1.7 | [Bài 05](02-addressing/01-ipv4-cidr-and-arp.md), [Bài 06](02-addressing/02-subnetting-vlsm-worked-examples.md), [Lab 01](10-labs/01-ip-and-packet-walk.md) | Ví dụ tính subnet và lab IP |
| 1.8–1.9 | [Bài 07](02-addressing/03-ipv6-ndp-and-slaac.md), [Lab 03](10-labs/03-static-ospf-ipv6-and-nat.md) | IPv6, EUI-64, ND/SLAAC; static lab |
| 1.10 | [Bài 05](02-addressing/01-ipv4-cidr-and-arp.md), [Bài 25](09-troubleshooting/01-method-and-packet-capture.md) | Windows/Linux có lệnh; macOS cần tự thực hành thêm |
| 1.11 | [Bài 23](07-security-wireless/03-wlan-rf-and-controller.md) | RF/SSID/channel/security; cần site survey thực tế |
| 1.12 | [Bài 20](06-windows-server/05-performance-virtualization-and-sdn.md) | Nhận diện VM/container/VRF; chưa có lab riêng từng runtime |
| 1.13 | [Bài 03](01-foundations/03-media-ethernet-and-metrics.md) | Giải thích MAC learning/flooding; quan sát Lab01/02 |
| 2.1–2.2 | [Bài 08](03-switching/01-vlan-trunk-and-intervlan.md), [Lab 02](10-labs/02-vlan-routing-and-resilience.md) | Cấu hình access/trunk/inter-VLAN; voice VLAN mới ở mức giải thích |
| 2.3 | [Bài 10](03-switching/03-etherchannel-and-discovery.md) | Lệnh đọc CDP/LLDP và lab kiểm neighbor |
| 2.4 | [Bài 10](03-switching/03-etherchannel-and-discovery.md), [Lab 02](10-labs/02-vlan-routing-and-resilience.md) | L2 LACP có lab; L3 LACP mới có định hướng |
| 2.5 | [Bài 09](03-switching/02-stp-and-protection.md), [Lab 02](10-labs/02-vlan-routing-and-resilience.md) | Giải thích role/guard + ví dụ edge; chưa lab mọi guard |
| 2.6–2.9 | [Bài 23](07-security-wireless/03-wlan-rf-and-controller.md), [Bài 21](07-security-wireless/01-acl-firewall-and-device-access.md), [Lab 05](10-labs/05-policy-wireless-and-capture.md) | Kiến trúc/WLC GUI/management; tùy simulator |
| 3.1–3.3 | [Bài 11](04-routing/01-route-selection-and-static.md), [Lab 03](10-labs/03-static-ospf-ipv6-and-nat.md) | Routing decision + IPv4/IPv6 static; floating có ví dụ |
| 3.4 | [Bài 12](04-routing/02-single-area-ospf.md), [Lab 03](10-labs/03-static-ospf-ipv6-and-nat.md) | Single-area OSPFv2 P2P; broadcast DR/BDR ở mức giải thích |
| 3.5 | [Bài 11](04-routing/01-route-selection-and-static.md) | FHRP nhận diện mục đích; chưa có lab HSRP/VRRP |
| 4.1 | [Bài 14](05-services/02-nat-and-pat.md), [Lab 03](10-labs/03-static-ospf-ipv6-and-nat.md) | Static/pool có ví dụ; PAT là lab bổ sung |
| 4.2 | [Bài 15](05-services/03-operations-ntp-snmp-syslog-qos.md) | NTP client/server có lệnh mẫu; chưa lab đo sync |
| 4.3, 4.6 | [Bài 13](05-services/01-dns-and-dhcp-protocols.md), [Bài 17](06-windows-server/02-dhcp-ipam-and-failover.md), [Lab 04](10-labs/04-windows-dns-dhcp-and-ipam.md) | DNS/DHCP, relay, client; router DHCP client là bài mở rộng |
| 4.4–4.5, 4.7 | [Bài 15](05-services/03-operations-ntp-snmp-syslog-qos.md) | SNMP/syslog/QoS giải thích; chưa build collector |
| 4.8 | [Bài 21](07-security-wireless/01-acl-firewall-and-device-access.md), [Lab 05](10-labs/05-policy-wireless-and-capture.md) | SSH có ví dụ/cách xác nhận |
| 4.9 | [Bài 15](05-services/03-operations-ntp-snmp-syslog-qos.md) | TFTP/FTP nhận diện; không có lab file transfer |
| 5.1–5.4, 5.8 | [Bài 21](07-security-wireless/01-acl-firewall-and-device-access.md), [Bài 18](06-windows-server/03-ad-dns-nps-and-remote-access.md) | Khái niệm, local user/AAA; certificate/MFA ở mức nhận diện |
| 5.5 | [Bài 18](06-windows-server/03-ad-dns-nps-and-remote-access.md), [Bài 22](07-security-wireless/02-layer2-security-and-vpn.md) | VPN/IPsec giải thích; chưa có lab tunnel hoàn chỉnh |
| 5.6–5.7 | [Bài 21](07-security-wireless/01-acl-firewall-and-device-access.md), [Bài 22](07-security-wireless/02-layer2-security-and-vpn.md), [Lab 05](10-labs/05-policy-wireless-and-capture.md) | ACL/port security có mẫu; DAI phải kiểm capability/binding |
| 5.9–5.10 | [Bài 23](07-security-wireless/03-wlan-rf-and-controller.md), [Lab 05](10-labs/05-policy-wireless-and-capture.md) | WPA/WPA2/WPA3 và nhiệm vụ GUI WPA2 PSK |
| 6.1–6.7 | [Bài 20](06-windows-server/05-performance-virtualization-and-sdn.md), [Bài 24](08-automation/01-api-json-iac-and-ai.md) | Giải thích architecture/AI/API/JSON/Ansible/Terraform; chưa chạy automation |

“Có lab” nghĩa là đã có **hướng dẫn và tiêu chí**, chưa nghĩa là đã chạy lab trong phiên xuất bản. Các động từ configure/verify trong blueprint đòi hỏi người học thực hành trên công cụ hỗ trợ; các khoảng trống trên không nên bỏ qua nếu mục tiêu là thi.

## MCSA Windows Server 2016 — phạm vi được chọn

MCSA có nhiều track. Wiki chọn **Windows Server 2016**, chủ yếu 70-741; không bao gồm toàn bộ 70-740 (compute/storage) hay 70-742 (identity). Cấu trúc nhóm 70-741 theo tài liệu thay đổi objectives tháng 04/2017, trong đó DHCP và IPAM đã được gộp. Chứng chỉ/kỳ thi cũ đã nghỉ. [M02][M01]

| Nhóm lịch sử 70-741 | Bài/lab | Mức độ và hướng học tiếp |
|---|---|---|
| DNS | [Bài 13](05-services/01-dns-and-dhcp-protocols.md), [Bài 16](06-windows-server/01-dns-zones-security-and-lab.md), [Lab 04](10-labs/04-windows-dns-dhcp-and-ipam.md) | Zone/record/lab cơ bản; DNSSEC/policy/DANE/logging/scavenging mới nhận diện, cần lab chuyên sâu |
| DHCP và IPAM | [Bài 17](06-windows-server/02-dhcp-ipam-and-failover.md), [Lab 04](10-labs/04-windows-dns-dhcp-and-ipam.md) | DHCP scope/options có lệnh; failover/IPAM provisioning là bài mở rộng theo tài liệu hãng |
| Network connectivity | [Bài 11](04-routing/01-route-selection-and-static.md), [Bài 14](05-services/02-nat-and-pat.md), [Bài 18](06-windows-server/03-ad-dns-nps-and-remote-access.md), [Bài 22](07-security-wireless/02-layer2-security-and-vpn.md) | Routing/NAT, VPN/DirectAccess/NPS; chưa runbook chứng chỉ/VPN đầy đủ |
| Core/distributed networking | [Bài 05](02-addressing/01-ipv4-cidr-and-arp.md)–[Bài 07](02-addressing/03-ipv6-ndp-and-slaac.md), [Bài 19](06-windows-server/04-branch-dfs-and-bgp-context.md) | IP có bài thực hành; DFS/BranchCache/BGP mới giải thích/định hướng |
| Advanced infrastructure | [Bài 20](06-windows-server/05-performance-virtualization-and-sdn.md), [Bài 24](08-automation/01-api-json-iac-and-ai.md) | NIC/SET/RSS/RDMA/SR-IOV/DCB/SDN/HNV/Controller ở mức nhận diện |
| Bổ trợ identity từ 70-742 | [Bài 18](06-windows-server/03-ad-dns-nps-and-remote-access.md) | AD/DNS/SRV/AAA; không thay khóa AD DS, GPO, federation hay certificate services |

## Cách cập nhật

Khi blueprint thay đổi, ghi phiên bản/ngày ở README và CHANGELOG, so từng mục với nguồn gốc, cập nhật bảng này trước khi thêm bài. Không đổi nhãn thành phiên bản mới nếu chưa kiểm tra các phần thêm/bỏ. Với Windows, kiểm tra Applies to, edition và lifecycle của từng tính năng rồi mới sửa lệnh lab.

[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[M01]: https://learn.microsoft.com/en-us/credentials/certifications/posts/mcsa-mcsd-mcse-certifications-retire-with-continued-investment-to-role-based-certifications "Microsoft — MCSA/MCSD/MCSE retirement"
[M02]: https://download.microsoft.com/download/6/4/D/64DDF21C-C0C1-4FD0-9887-A27127A11A9A/OD_741_changes.pdf "Microsoft — 70-741 objective changes, April 2017"
