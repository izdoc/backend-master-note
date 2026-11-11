# Thuật ngữ mạng máy tính

[Mục lục](INDEX.md) · [Nguồn tham khảo](REFERENCES.md)

Đây là định nghĩa ngắn để tra cứu; đọc bài học và nguồn trước khi cấu hình. Một thuật ngữ như TTL có ý nghĩa khác theo ngữ cảnh.

| Thuật ngữ | Giải thích ngắn | Nguồn |
|---|---|---|
| ACL | Danh sách rule lọc theo điều kiện, có thứ tự khớp. | [C13] |
| AD DS | Directory/domain service của Windows Server. | [M18] |
| Administrative distance | Độ ưu tiên cục bộ giữa nguồn route cho cùng prefix. | [C11] |
| Anycast | Nhiều node dùng địa chỉ, routing chọn một đích phù hợp. | [R07] |
| AP | Điểm truy cập mạng không dây. | [C17] |
| ARP | Phân giải IP next hop thành địa chỉ liên kết trên Ethernet IPv4. | [R02] |
| ASN/BGP | Định danh hệ thống tự trị / giao thức trao đổi reachability theo policy. | [C11] |
| Broadcast domain | Miền frame broadcast L2 được chuyển trong đó. | [C05] |
| CIDR | Biểu diễn/cấp phát mạng bằng prefix length. | [R04] |
| Control plane | Phần điều khiển thông tin dùng cho forwarding/policy. | [M26] |
| Data plane | Phần thực hiện chuyển traffic theo trạng thái điều khiển. | [M26] |
| DAI | Kiểm tra ARP theo binding/chính sách được cấu hình. | [C14] |
| Default route | Route /0 dùng khi không có prefix dài hơn phù hợp. | [C11] |
| DHCP | Dịch vụ/giao thức cấp lease và tham số IP. | [R12] |
| DHCP relay | Thành phần chuyển trao đổi DHCP qua ranh giới subnet. | [R12] |
| DNS | Hệ thống tên phân tán, có authority, resolver và cache. | [R13] |
| DNSSEC | Cơ chế xác thực dữ liệu DNS theo chuỗi tin cậy. | [M04] |
| DSCP | Trường đánh dấu DiffServ dùng cho chính sách xử lý IP. | [R19] |
| Duplex | Cách liên kết gửi/nhận hai chiều; full và half có hành vi khác. | [C03] |
| EtherChannel | Nhóm liên kết logic từ các cổng tương thích. | [C10] |
| FHRP | Nhóm cơ chế dự phòng first-hop gateway. | [R24] |
| Flow | Nhận diện luồng thường dựa IP/port/transport. | [R10] |
| Gateway | Next-hop router theo route của host. | [R01] |
| Goodput | Tốc độ dữ liệu hữu ích của ứng dụng trong phép đo. | [T02] |
| IPAM | Quản lý không gian IP và thông tin DNS/DHCP tập trung. | [M13] |
| IPsec | Kiến trúc bảo vệ traffic ở lớp IP. | [R20] |
| Jitter | Độ biến thiên delay trong ngữ cảnh phép đo. | [C15] |
| LACP | Giao thức thương lượng link aggregation. | [C10] |
| Link-local | Địa chỉ IPv6 chỉ có phạm vi link. | [R07] |
| LLDP/CDP | Neighbor discovery; LLDP đa hãng, CDP của Cisco. | [C23] |
| Longest prefix match | Chọn prefix dài nhất khớp đích khi forwarding. | [R04] |
| MAC table | Ánh xạ MAC/VLAN sang cổng học được/cấu hình. | [C05] |
| MTU | Kích thước packet tối đa trên link theo ngữ cảnh giao thức. | [R06] |
| NAT/PAT | Dịch địa chỉ / dịch địa chỉ cùng port theo mô hình. | [R16] |
| NDP | Neighbor Discovery qua ICMPv6. | [R08] |
| NPS/RADIUS | Dịch vụ Windows triển khai AAA truy cập mạng theo RADIUS. | [M14] |
| NTP | Giao thức đồng bộ thời gian. | [R17] |
| OSPF | Giao thức routing link-state, dùng cost. | [R15] |
| Overlay/underlay | Mạng logic / mạng vận chuyển nền. | [M26] |
| PoE | Cấp điện qua Ethernet cho thiết bị tương thích. | [C02] |
| PortFast | Tối ưu chuyển trạng thái cho edge port. | [C07] |
| Prefix | Phần bit mạng được xác định bằng prefix length. | [R04] |
| QoS | Cơ chế phân loại/xử lý traffic theo chính sách. | [C21] |
| RA | Router Advertisement trong IPv6 ND. | [R08] |
| RST/FIN | TCP reset / kết thúc gửi theo cơ chế TCP. | [R10] |
| RTT | Thời gian khứ hồi của phép trao đổi được đo. | [T02] |
| SLAAC | IPv6 stateless address autoconfiguration. | [R09] |
| SNMP | Framework quản lý/giám sát đối tượng mạng. | [R23] |
| SSID | Tên mạng WLAN trong cấu hình/hiển thị client. | [C15] |
| STP | Cơ chế tạo topology forwarding L2 không loop. | [C07] |
| Subnet/VLSM | Mạng con / dùng subnet với độ dài prefix khác nhau. | [R04] |
| Syslog | Giao thức/log với facility và severity. | [R18] |
| TCP/UDP | Byte stream tin cậy có thứ tự / transport datagram. | [R10] [R11] |
| TLS | Giao thức bảo vệ kênh và xác thực theo cấu hình. | [R25] |
| Trunk/native VLAN | Link chở nhiều VLAN / VLAN cho traffic untagged theo cấu hình. | [C06] |
| TTL | Thời gian cache DNS hoặc hop limit IPv4, tùy header/ngữ cảnh. | [R13] |
| VRF | Miền bảng định tuyến riêng trên cùng thiết bị. | [C26] |
| WLC | Controller quản lý WLAN/AP theo kiến trúc. | [C24] |
| WPA2/WPA3 | Họ cơ chế bảo mật WLAN; kiểm mode/cipher/AKM cụ thể. | [C16] |
| Zone | Phần namespace DNS do server quản lý theo loại zone. | [M06] |
[C13]: https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html "Cisco — Configure IP Access Lists"
[M18]: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview "Microsoft — AD DS overview"
[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
[R07]: https://www.rfc-editor.org/rfc/rfc4291 "RFC 4291 — IPv6 addressing"
[C17]: https://content.ciscodcloud.com/content/cisco-dcloud/us/en/home/support/help/using-dcloud/wireless_connect.html "Cisco — AP connectivity and configuration"
[R02]: https://www.rfc-editor.org/rfc/rfc826 "RFC 826 — ARP"
[C05]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-2_1_e/configuration/guide/2960_scg/swvlan.html "Cisco — Configuring VLANs"
[R04]: https://www.rfc-editor.org/rfc/rfc4632 "RFC 4632 — CIDR"
[M26]: https://learn.microsoft.com/en-us/previous-versions/azure/azure-local/concepts/software-defined-networking "Microsoft — Software Defined Networking"
[C14]: https://www.cisco.com/c/en/us/support/docs/switches/lan-switch-software/222274-troubleshoot-dynamic-arp-inspection-dai.html "Cisco — Troubleshoot DAI and IPSG"
[R12]: https://www.rfc-editor.org/rfc/rfc2131 "RFC 2131 — DHCPv4"
[R13]: https://www.rfc-editor.org/rfc/rfc1034 "RFC 1034 — DNS concepts"
[M04]: https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top "Microsoft — DNS overview"
[R19]: https://www.rfc-editor.org/rfc/rfc2474 "RFC 2474 — Differentiated Services"
[C03]: https://www.cisco.com/c/en/us/support/docs/switches/catalyst-6000-series-switches/21268-132.html "Cisco — Cable, Connector and AC Power Cord Guide"
[C10]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-0_2_se/configuration/guide/scg2960/swethchl.html "Cisco — EtherChannels"
[R24]: https://www.rfc-editor.org/rfc/rfc9568 "RFC 9568 — VRRPv3"
[R10]: https://www.rfc-editor.org/rfc/rfc9293 "RFC 9293 — TCP"
[R01]: https://www.rfc-editor.org/rfc/rfc1122 "RFC 1122 — Internet host communication layers"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
[M13]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top "Microsoft — IPAM"
[R20]: https://www.rfc-editor.org/rfc/rfc4301 "RFC 4301 — IPsec architecture"
[C15]: https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/technical-reference/wireless-rf-reference-guide.html "Cisco — Wireless RF Reference Guide"
[C23]: https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/cdp-lldp-mac-udld/cdp-lldp-mac-udld-configuration-guide/c-configure-lldp.html "Cisco — Configure LLDP"
[R06]: https://www.rfc-editor.org/rfc/rfc8200 "RFC 8200 — IPv6"
[R16]: https://www.rfc-editor.org/rfc/rfc3022 "RFC 3022 — Traditional NAT"
[R08]: https://www.rfc-editor.org/rfc/rfc4861 "RFC 4861 — Neighbor Discovery"
[M14]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top "Microsoft — Network Policy Server"
[R17]: https://www.rfc-editor.org/rfc/rfc5905 "RFC 5905 — NTPv4"
[R15]: https://www.rfc-editor.org/rfc/rfc2328 "RFC 2328 — OSPFv2"
[C02]: https://www.cisco.com/site/us/en/learn/topics/networking/what-is-computer-networking.html "Cisco — What is computer networking?"
[C07]: https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10586-65.html "Cisco — PortFast and BPDU Guard"
[C21]: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/quality-of-service/quality-of-service/m_qos-plcshp-oview-0.html "Cisco — Policing and Shaping Overview"
[R09]: https://www.rfc-editor.org/rfc/rfc4862 "RFC 4862 — SLAAC"
[R23]: https://www.rfc-editor.org/rfc/rfc3411 "RFC 3411 — SNMP architecture"
[R18]: https://www.rfc-editor.org/rfc/rfc5424 "RFC 5424 — Syslog"
[R25]: https://www.rfc-editor.org/rfc/rfc8446 "RFC 8446 — TLS 1.3"
[C06]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960x/software/15-2_7_e/configuration_guide/b_1527e_consolidated_2960x_cg/m_vlan_trunk_cg_2960-x.html "Cisco — Configuring VLAN Trunks"
[C26]: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-routing/b-ip-routing/m_mp-multi-vrf-vrf-lite.html "Cisco — Multi-VRF Support"
[C24]: https://www.cisco.com/c/en/us/products/collateral/wireless/unified-wireless-network-sg.html "Cisco — Unified Wireless Network Solution Guide"
[C16]: https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-9/config-guide/b_wl_17_9_cg/m_wlan_security_9800.html "Cisco — Catalyst 9800 WLAN Security, IOS XE 17.9"
[M06]: https://learn.microsoft.com/en-us/windows-server/networking/dns/zone-types "Microsoft — DNS zones"
[R11]: https://www.rfc-editor.org/rfc/rfc768 "RFC 768 — UDP"
