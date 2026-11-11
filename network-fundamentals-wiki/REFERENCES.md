# Nguồn học network đáng tin cậy

[Trang đầu](README.md) · [Mục lục](INDEX.md) · [Đối chiếu chương trình](SYLLABUS-MAPPING.md)

**Mốc rà soát nguồn:** 11/11/2026. Trang này là bản đồ nguồn học và sổ trích dẫn cho toàn wiki, đọc trực tiếp trên GitHub.

## Nên bắt đầu ở đâu?

| Mục tiêu | Nguồn chính | Cách dùng |
|---|---|---|
| Học mạng từ đầu | [Cisco Networking Academy][T04] | Chọn lộ trình networking và lab phù hợp; trang có thể cần tài khoản/JavaScript |
| Học theo CCNA | [Blueprint Cisco][C01] | Kiểm phạm vi và động từ explain/configure/verify trước khi chọn bài |
| Học Windows networking | [Microsoft Learn learning path][M03] | DNS, DHCP, IPAM, NPS và remote access theo phiên bản hỗ trợ |
| Hiểu giao thức chuẩn | [RFC Editor][R01] | Đọc abstract, phần liên quan, status, updates và errata; không cần đọc hết ngay |
| Đọc packet | [Wireshark User Guide][T02] | Làm capture nhỏ rồi đối chiếu field/filter |
| Học automation | [Cisco DevNet][T05], [Ansible][T06], [Terraform][T07] | Bắt đầu read-only/inventory, rồi quản lý thay đổi |

Các cổng học có nội dung/quyền truy cập thay đổi theo tài khoản. Không khẳng định mọi khóa hoặc lab tại đó đều miễn phí.

## Vì sao tin các nguồn này?

- **RFC Editor/IETF:** nguồn gốc mô tả giao thức; phân biệt Standards Track, Informational, Experimental và tài liệu đã bị thay thế. Một RFC không tự động là chuẩn còn mới nhất.
- **Cisco:** dùng để xác định phạm vi CCNA và hành vi/cú pháp thiết bị Cisco. Chú ý family, IOS/IOS XE, release và feature support.
- **Microsoft Learn:** dùng cho Windows networking và PowerShell. Chú ý Applies to, AD/domain prerequisites, edition và deprecation.
- **IANA:** registry chính thức của service/port, không phải bằng chứng rằng một port đang chạy đúng ứng dụng.
- **Wireshark/Ansible/HashiCorp:** tài liệu gốc cho công cụ tương ứng; không thay spec giao thức hay thiết kế bảo mật của tổ chức.

Đây là tiêu chí biên soạn của wiki. Blog/forum có thể hữu ích để tìm manh mối nhưng không dùng làm nguồn quyết định duy nhất cho hành vi chuẩn hoặc cấu hình.

## Cách đọc trích dẫn

Mã [R10], [C13], [M10] trong bài dẫn tới nguồn trực tiếp. Một đoạn có nhiều mã khi cần cả chuẩn giao thức và cách triển khai hãng. Bài tập, topology, phép tính và quy trình điều tra do wiki tự thiết kế được ghi rõ; nguồn hỗ trợ nguyên lý, không có nghĩa hãng đã chạy/duyệt ví dụ này.

Không tải/chép lại sách hoặc đề thi có bản quyền vào repository; không dùng exam dump làm nguồn học.

## Giới hạn kiểm tra truy cập

Nguồn được rà qua trang chính thức hoặc kết quả lập chỉ mục từ tên miền gốc. Đây **không phải** báo cáo HTTP kiểm đủ mọi URL ở mọi thời điểm. PDF M02 đọc được qua chỉ mục tìm kiếm nhưng công cụ mở trực tiếp gặp kiểu nội dung octet-stream; hai cổng T04/T05 chỉ trả vỏ JavaScript trong trình đọc tự động. M17 được dùng cho khuyến nghị Always On VPN khi triển khai mới; M26 là trang kiến trúc lịch sử. Nếu link đổi, tìm lại đúng tiêu đề trên tên miền hãng và cập nhật ngày rà soát.

## Cisco: blueprint, nền tảng và cấu hình

| Mã | Nguồn gốc | Dùng để học / giới hạn |
|---|---|---|
| C01 | [Cisco — CCNA 200-301 v1.1 exam topics](https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf) | Blueprint chính; đối chiếu phạm vi, không phải sách giải thích giao thức. |
| C02 | [Cisco — What is computer networking?](https://www.cisco.com/site/us/en/learn/topics/networking/what-is-computer-networking.html) | Tổng quan mạng, thiết bị và kiến trúc. |
| C03 | [Cisco — Cable, Connector and AC Power Cord Guide](https://www.cisco.com/c/en/us/support/docs/switches/catalyst-6000-series-switches/21268-132.html) | Cáp/đầu nối; ví dụ phần cứng cũ, phải kiểm tra model thực tế. |
| C04 | [Cisco — Gigabit Ethernet SFP data sheet](https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/datasheet-c78-366584.html) | Chuẩn quang/đồng, giới hạn khoảng cách theo transceiver. |
| C05 | [Cisco — Configuring VLANs](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-2_1_e/configuration/guide/2960_scg/swvlan.html) | VLAN/access port trên Catalyst 2960; nền tảng cho lab mô phỏng. |
| C06 | [Cisco — Configuring VLAN Trunks](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960x/software/15-2_7_e/configuration_guide/b_1527e_consolidated_2960x_cg/m_vlan_trunk_cg_2960-x.html) | 802.1Q, native VLAN và allowed VLAN. |
| C07 | [Cisco — PortFast and BPDU Guard](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10586-65.html) | PortFast/BPDU Guard và nguy cơ loop. |
| C08 | [Cisco — Root Guard](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10588-74.html) | Bảo vệ vị trí root bridge. |
| C09 | [Cisco — Loop Guard and UDLD](https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol-stp-8021d/218321-configure-stp-with-loop-guard-and-bpdu-s.html) | Loop guard, BPDU filter và sự cố liên kết. |
| C10 | [Cisco — EtherChannels](https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-0_2_se/configuration/guide/scg2960/swethchl.html) | LACP, điều kiện tương thích và cân bằng tải. |
| C11 | [Cisco — IP Routing Configuration Guide](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html) | Routing/static/OSPF; tra chương tương ứng với image. |
| C12 | [Cisco — OSPFv2 on an interface basis](https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iro-mode-ospfv2.html) | Cú pháp bật OSPF trên interface. |
| C13 | [Cisco — Configure IP Access Lists](https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html) | ACL standard/extended, thứ tự xử lý và hướng gắn. |
| C14 | [Cisco — Troubleshoot DAI and IPSG](https://www.cisco.com/c/en/us/support/docs/switches/lan-switch-software/222274-troubleshoot-dynamic-arp-inspection-dai.html) | DHCP snooping, bindings, DAI và thiết bị IP tĩnh. |
| C15 | [Cisco — Wireless RF Reference Guide](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/technical-reference/wireless-rf-reference-guide.html) | RF/channel/site survey; quy định kênh tùy quốc gia. |
| C16 | [Cisco — Catalyst 9800 WLAN Security, IOS XE 17.9](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-9/config-guide/b_wl_17_9_cg/m_wlan_security_9800.html) | WLAN security; tên màn hình khác giữa các controller. |
| C17 | [Cisco — AP connectivity and configuration](https://content.ciscodcloud.com/content/cisco-dcloud/us/en/home/support/help/using-dcloud/wireless_connect.html) | Autonomous/lightweight AP; tài liệu kiến trúc cũ. |
| C18 | [Cisco — NAT troubleshooting FAQ](https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/218012-troubleshoot-network-address-translation.html) | Inside/outside, translation và troubleshooting. |
| C19 | [Cisco — Configure SSH on Routers](https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html) | SSH keys, local authentication và VTY. |
| C20 | [Cisco — Port security command reference](https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s6.html) | Maximum, sticky và violation mode. |
| C21 | [Cisco — Policing and Shaping Overview](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/quality-of-service/quality-of-service/m_qos-plcshp-oview-0.html) | Phân biệt policing và shaping. |
| C22 | [Cisco — Configure CDP](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/cdp-lldp-mac-udld/cdp-lldp-mac-udld-configuration-guide/c-configure-cdp.html) | Discovery trực tiếp trên Cisco. |
| C23 | [Cisco — Configure LLDP](https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/cdp-lldp-mac-udld/cdp-lldp-mac-udld-configuration-guide/c-configure-lldp.html) | Discovery đa hãng. |
| C24 | [Cisco — Unified Wireless Network Solution Guide](https://www.cisco.com/c/en/us/products/collateral/wireless/unified-wireless-network-sg.html) | Controller/FlexConnect và kiến trúc WLAN. |
| C25 | [Cisco — Access Point Modes, IOS XE 17.13](https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-13/config-guide/b_wl_17_13_cg/m-sniffer-cg.html) | Local, monitor, sniffer và các mode hỗ trợ. |
| C26 | [Cisco — Multi-VRF Support](https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-routing/b-ip-routing/m_mp-multi-vrf-vrf-lite.html) | Bảng routing riêng và VRF Lite. |

## Microsoft: MCSA lịch sử và Windows Server

| Mã | Nguồn gốc | Dùng để học / giới hạn |
|---|---|---|
| M01 | [Microsoft — MCSA/MCSD/MCSE retirement](https://learn.microsoft.com/en-us/credentials/certifications/posts/mcsa-mcsd-mcse-certifications-retire-with-continued-investment-to-role-based-certifications) | Dùng bản UPDATE ngày 26/03/2020: nghỉ thi 31/01/2021. |
| M02 | [Microsoft — 70-741 objective changes, April 2017](https://download.microsoft.com/download/6/4/D/64DDF21C-C0C1-4FD0-9887-A27127A11A9A/OD_741_changes.pdf) | PDF lịch sử; search index đọc được, tải trực tiếp trả octet-stream trong công cụ kiểm tra. |
| M03 | [Microsoft Learn — Windows Server networking learning path](https://learn.microsoft.com/en-us/training/paths/implement-operate-premises-hybrid/) | Đọc tiếp theo hướng Windows Server/hybrid. |
| M04 | [Microsoft — DNS overview](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top) | Vai trò DNS trong Windows và AD DS. |
| M05 | [Microsoft — DNS architecture](https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-architecture) | Record, zone và mô hình phân giải. |
| M06 | [Microsoft — DNS zones](https://learn.microsoft.com/en-us/windows-server/networking/dns/zone-types) | Primary/secondary/stub và AD integration. |
| M07 | [Microsoft — Install DNS Server](https://learn.microsoft.com/en-us/windows-server/networking/dns/quickstart-install-configure-dns-server) | Cài role DNS, quản trị bằng PowerShell/GUI. |
| M08 | [Microsoft — Add-DnsServerPrimaryZone](https://learn.microsoft.com/en-us/powershell/module/dnsserver/add-dnsserverprimaryzone) | Phân biệt parameter set file-backed/AD-integrated. |
| M09 | [Microsoft — DHCP overview](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top) | Dịch vụ lease IPv4 và các tùy chọn. |
| M10 | [Microsoft — Install and configure DHCP Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server) | Role, scope, authorization và options. |
| M11 | [Microsoft — Add-DhcpServerv4Scope](https://learn.microsoft.com/en-us/powershell/module/dhcpserver/add-dhcpserverv4scope) | Tham số tạo scope. |
| M12 | [Microsoft — DHCP failover](https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-failover) | Quan hệ hai DHCP server cho scope IPv4. |
| M13 | [Microsoft — IPAM](https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top) | Quản lý IP/DNS/DHCP tập trung. |
| M14 | [Microsoft — Network Policy Server](https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top) | RADIUS, policy và AAA. |
| M15 | [Microsoft — Remote Access](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/remote-access) | RRAS/VPN; xem giới hạn triển khai trên Azure VM. |
| M16 | [Microsoft — Always On VPN](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/overview-always-on-vpn) | Hướng học remote access hiện hành. |
| M17 | [Microsoft — DirectAccess](https://learn.microsoft.com/en-us/windows-server/remote/remote-access/directaccess/directaccess) | Kiến thức kế thừa; hãng khuyến nghị Always On VPN cho triển khai mới. |
| M18 | [Microsoft — AD DS overview](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview) | Directory/domain/controller; bổ trợ 70-742. |
| M19 | [Microsoft — DNS and AD DS](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds) | Phụ thuộc DNS của domain. |
| M20 | [Microsoft — Verify SRV records](https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created) | Chẩn đoán tìm domain controller. |
| M21 | [Microsoft — DFS Namespaces](https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview) | Namespace và folder targets. |
| M22 | [Microsoft — DFS Replication](https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/dfsr-overview) | Đồng bộ dữ liệu; không thay backup. |
| M23 | [Microsoft — BranchCache](https://learn.microsoft.com/en-us/windows-server/networking/branchcache/branchcache) | Distributed/hosted cache; kiểm tra edition hỗ trợ. |
| M24 | [Microsoft — Software-only networking features](https://learn.microsoft.com/en-us/windows-server/networking/technologies/hpn/hpn-software-only-features) | NIC Teaming và SET. |
| M25 | [Microsoft — Software/hardware integrated features](https://learn.microsoft.com/en-us/windows-server/networking/technologies/hpn/hpn-software-hardware-features) | RSS, RDMA, SR-IOV, DCB. |
| M26 | [Microsoft — Software Defined Networking](https://learn.microsoft.com/en-us/previous-versions/azure/azure-local/concepts/software-defined-networking) | Trang lịch sử, mô hình Network Controller/SLB/gateway. |
| M27 | [Microsoft — New-NetIPAddress](https://learn.microsoft.com/en-us/powershell/module/nettcpip/new-netipaddress) | IP tĩnh, prefix và gateway. |

## RFC Editor: giao thức và tiêu chuẩn

| Mã | Nguồn gốc | Dùng để học / giới hạn |
|---|---|---|
| R01 | [RFC 1122 — Internet host communication layers](https://www.rfc-editor.org/rfc/rfc1122) | Kiến trúc Internet; đọc thêm updates/errata trên RFC Editor. |
| R02 | [RFC 826 — ARP](https://www.rfc-editor.org/rfc/rfc826) | IPv4-to-Ethernet address resolution. |
| R03 | [RFC 1918 — Private IPv4](https://www.rfc-editor.org/rfc/rfc1918) | Ba dải IPv4 private. |
| R04 | [RFC 4632 — CIDR](https://www.rfc-editor.org/rfc/rfc4632) | Prefix và aggregation. |
| R05 | [RFC 3021 — IPv4 /31](https://www.rfc-editor.org/rfc/rfc3021) | Ngoại lệ /31 trên point-to-point. |
| R06 | [RFC 8200 — IPv6](https://www.rfc-editor.org/rfc/rfc8200) | IPv6 base header và forwarding. |
| R07 | [RFC 4291 — IPv6 addressing](https://www.rfc-editor.org/rfc/rfc4291) | Loại địa chỉ IPv6 và EUI-64. |
| R08 | [RFC 4861 — Neighbor Discovery](https://www.rfc-editor.org/rfc/rfc4861) | RS/RA/NS/NA và default router. |
| R09 | [RFC 4862 — SLAAC](https://www.rfc-editor.org/rfc/rfc4862) | Tự cấu hình và duplicate address detection. |
| R10 | [RFC 9293 — TCP](https://www.rfc-editor.org/rfc/rfc9293) | Đặc tả TCP thay cho RFC 793 làm điểm bắt đầu. |
| R11 | [RFC 768 — UDP](https://www.rfc-editor.org/rfc/rfc768) | Datagram và giới hạn bảo đảm của UDP. |
| R12 | [RFC 2131 — DHCPv4](https://www.rfc-editor.org/rfc/rfc2131) | Cấp lease, renewal và relay. |
| R13 | [RFC 1034 — DNS concepts](https://www.rfc-editor.org/rfc/rfc1034) | Resolver, authority, cache. |
| R14 | [RFC 1035 — DNS implementation](https://www.rfc-editor.org/rfc/rfc1035) | Record và DNS transport; xem các RFC cập nhật. |
| R15 | [RFC 2328 — OSPFv2](https://www.rfc-editor.org/rfc/rfc2328) | Neighbor, link-state và DR/BDR. |
| R16 | [RFC 3022 — Traditional NAT](https://www.rfc-editor.org/rfc/rfc3022) | NAT/NAPT; không phải đặc tả firewall. |
| R17 | [RFC 5905 — NTPv4](https://www.rfc-editor.org/rfc/rfc5905) | Đồng bộ thời gian. |
| R18 | [RFC 5424 — Syslog](https://www.rfc-editor.org/rfc/rfc5424) | Facility, severity và message. |
| R19 | [RFC 2474 — Differentiated Services](https://www.rfc-editor.org/rfc/rfc2474) | DS field, DSCP và per-hop behavior. |
| R20 | [RFC 4301 — IPsec architecture](https://www.rfc-editor.org/rfc/rfc4301) | IP-layer security, tunnel/transport. |
| R21 | [RFC 9110 — HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110) | Method, status và ý nghĩa HTTP. |
| R22 | [RFC 8259 — JSON](https://www.rfc-editor.org/rfc/rfc8259) | Object, array, number, string và boolean/null. |
| R23 | [RFC 3411 — SNMP architecture](https://www.rfc-editor.org/rfc/rfc3411) | Management framework; tra mô hình bảo mật SNMPv3. |
| R24 | [RFC 9568 — VRRPv3](https://www.rfc-editor.org/rfc/rfc9568) | Virtual router redundancy cho IPv4/IPv6. |
| R25 | [RFC 8446 — TLS 1.3](https://www.rfc-editor.org/rfc/rfc8446) | TLS handshake và xác thực bằng certificate. |
| R26 | [RFC 1350 — TFTP](https://www.rfc-editor.org/rfc/rfc1350) | Truyền file đơn giản. |
| R27 | [RFC 959 — FTP](https://www.rfc-editor.org/rfc/rfc959) | FTP control/data; giao thức cơ bản không cung cấp mã hóa. |

## Công cụ và cổng học chính thức

| Mã | Nguồn gốc | Dùng để học / giới hạn |
|---|---|---|
| T01 | [IANA — Service names and port numbers](https://www.iana.org/assignments/service-names-port-numbers/) | Tra cặp transport/port; không suy ra ứng dụng chỉ từ port. |
| T02 | [Wireshark — User Guide](https://www.wireshark.org/docs/wsug_html/) | Capture, phân tích và diễn giải packet. |
| T03 | [Wireshark — Display filter expressions](https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html) | Cú pháp filter và toán tử. |
| T04 | [Cisco Networking Academy](https://www.netacad.com/) | Cổng khóa học/lab; cần JavaScript, có thể cần tài khoản. |
| T05 | [Cisco DevNet Learning Labs](https://developer.cisco.com/learning/) | Lab automation; cần JavaScript, có thể cần tài khoản. |
| T06 | [Ansible — Network Getting Started](https://docs.ansible.com/projects/ansible/latest/network/getting_started/index.html) | Automation trên nhiều nền tảng mạng. |
| T07 | [HashiCorp — Terraform intro](https://developer.hashicorp.com/terraform/intro) | Infrastructure as code, provider/state/plan. |


## Quy trình duy trì sổ nguồn

Khi sửa một thông tin kỹ thuật: mở nguồn gốc → kiểm phiên bản/status → sửa đoạn và citation gần đó → cập nhật syllabus mapping nếu đổi phạm vi → chạy kiểm link nội bộ → ghi thay đổi. Khi nguồn hãng và simulator khác nhau, ghi rõ khác biệt, không giả định simulator chứng minh mọi hành vi thiết bị thật.

[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[M03]: https://learn.microsoft.com/en-us/training/paths/implement-operate-premises-hybrid/ "Microsoft Learn — Windows Server networking learning path"
[R01]: https://www.rfc-editor.org/rfc/rfc1122 "RFC 1122 — Internet host communication layers"
[R10]: https://www.rfc-editor.org/rfc/rfc9293 "RFC 9293 — TCP"
[C13]: https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html "Cisco — Configure IP Access Lists"
[M10]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server "Microsoft — Install and configure DHCP Server"
[T01]: https://www.iana.org/assignments/service-names-port-numbers/ "IANA — Service names and port numbers"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
[T04]: https://www.netacad.com/ "Cisco Networking Academy"
[T05]: https://developer.cisco.com/learning/ "Cisco DevNet Learning Labs"
[T06]: https://docs.ansible.com/projects/ansible/latest/network/getting_started/index.html "Ansible — Network Getting Started"
[T07]: https://developer.hashicorp.com/terraform/intro "HashiCorp — Terraform intro"
