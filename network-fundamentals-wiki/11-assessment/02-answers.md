# Đáp án và hướng ôn tập

[Câu hỏi](01-review-questions.md) · [Mục lục](../INDEX.md)

Các phép tính subnet là lời giải tự biên soạn; phần giải thích liên kết về bài học có nguồn chính thức.

## Câu 1

Switch L2 chuyển frame trong miền VLAN theo MAC; router chuyển IP packet giữa subnet. Một thiết bị có thể có cả hai chức năng.

Đọc lại [01. Mạng máy tính và vai trò thiết bị](../01-foundations/01-network-and-devices.md).

## Câu 2

Thường là MAC next hop/gateway trên Ethernet hiện tại, không phải MAC server ở xa.

Đọc lại [02. OSI, TCP/IP và hành trình gói tin](../01-foundations/02-osi-tcpip-packet-walk.md).

## Câu 3

Không. Throughput/goodput chịu ảnh hưởng overhead, RTT, loss, congestion và giới hạn máy/dịch vụ.

Đọc lại [03. Cáp, Ethernet và chỉ số hiệu năng](../01-foundations/03-media-ethernet-and-metrics.md).

## Câu 4

Không. Ứng dụng còn cần xử lý retry, transaction và chống xử lý trùng.

Đọc lại [04. TCP, UDP, port và kết nối ứng dụng](../01-foundations/04-tcp-udp-and-ports.md).

## Câu 5

10.0.0.0/8, 172.16.0.0/12 và 192.168.0.0/16.

Đọc lại [05. IPv4, CIDR, gateway và ARP](../02-addressing/01-ipv4-cidr-and-arp.md).

## Câu 6

192.168.7.64/28; broadcast .79, host thông thường .65–.78. Block size là 16.

Đọc lại [06. Subnetting, VLSM và kế hoạch địa chỉ](../02-addressing/02-subnetting-vlsm-worked-examples.md).

## Câu 7

Không. /28 có 14 host usable, nhưng yêu cầu ít nhất 15. Cần /27 nếu không có thay đổi khác.

Đọc lại [06. Subnetting, VLSM và kế hoạch địa chỉ](../02-addressing/02-subnetting-vlsm-worked-examples.md).

## Câu 8

Không có broadcast; Neighbor Discovery qua ICMPv6 đảm nhiệm chức năng phân giải neighbor cùng các chức năng khác.

Đọc lại [07. IPv6, Neighbor Discovery và SLAAC](../02-addressing/03-ipv6-ndp-and-slaac.md).

## Câu 9

Router Advertisement, không phải option default gateway trong DHCPv6.

Đọc lại [07. IPv6, Neighbor Discovery và SLAAC](../02-addressing/03-ipv6-ndp-and-slaac.md).

## Câu 10

Không. Trunk vận chuyển frame theo VLAN; inter-VLAN cần routing và policy cho phép.

Đọc lại [08. VLAN, trunk và inter-VLAN routing](../03-switching/01-vlan-trunk-and-intervlan.md).

## Câu 11

Frame untagged có thể được phân vào VLAN khác hai đầu; cần kiểm tra cấu hình đúng link và platform.

Đọc lại [08. VLAN, trunk và inter-VLAN routing](../03-switching/01-vlan-trunk-and-intervlan.md).

## Câu 12

Không. Nó cho edge port forwarding nhanh; các cơ chế STP/BPDU vẫn cần được hiểu.

Đọc lại [09. STP, Rapid PVST+ và bảo vệ vòng lặp](../03-switching/02-stp-and-protection.md).

## Câu 13

Root Guard ngăn superior BPDU làm đổi root qua cổng; BPDU Guard phản ứng khi nhận BPDU tại cổng không nên có BPDU.

Đọc lại [09. STP, Rapid PVST+ và bảo vệ vòng lặp](../03-switching/02-stp-and-protection.md).

## Câu 14

Không. Cần ít nhất một đầu active và member tương thích.

Đọc lại [10. EtherChannel, LACP, CDP và LLDP](../03-switching/03-etherchannel-and-discovery.md).

## Câu 15

Không. Hash thường giữ một flow trên một member; tổng dung lượng hữu ích thể hiện trên nhiều flow.

Đọc lại [10. EtherChannel, LACP, CDP và LLDP](../03-switching/03-etherchannel-and-discovery.md).

## Câu 16

/24. Longest prefix match chọn forwarding từ bảng; AD so nguồn route cho cùng prefix khi chọn route.

Đọc lại [11. Routing table, static route và FHRP](../04-routing/01-route-selection-and-static.md).

## Câu 17

Chưa. Cần đường về, neighbor/link, policy và phản hồi của đích.

Đọc lại [11. Routing table, static route và FHRP](../04-routing/01-route-selection-and-static.md).

## Câu 18

Không. Process ID Cisco là cục bộ; cần kiểm tra area/timer/network type/authentication và các điều kiện khác.

Đọc lại [12. OSPFv2 một area](../04-routing/02-single-area-ospf.md).

## Câu 19

Không. Có thể bình thường trên broadcast network; xem adjacency với DR/BDR và topology.

Đọc lại [12. OSPFv2 một area](../04-routing/02-single-area-ospf.md).

## Câu 20

Không. DNS dùng TCP53 nữa; cần policy cho đúng các chức năng giao thức.

Đọc lại [13. DNS và DHCP: từ tên miền đến cấu hình IP](../05-services/01-dns-and-dhcp-protocols.md).

## Câu 21

Reservation cấp địa chỉ ổn định cho client định danh; exclusion loại địa chỉ/range khỏi cấp động.

Đọc lại [13. DNS và DHCP: từ tên miền đến cấu hình IP](../05-services/01-dns-and-dhcp-protocols.md).

## Câu 22

Không. Translation, policy, transport, TLS và xử lý ứng dụng là các phần cần kiểm tra riêng.

Đọc lại [14. NAT, PAT và đường về](../05-services/02-nat-and-pat.md).

## Câu 23

Không. 0 là Emergency, 7 là Debug; số nhỏ hơn nghiêm trọng hơn.

Đọc lại [15. NTP, SNMP, syslog, QoS và truyền file](../05-services/03-operations-ntp-snmp-syslog-qos.md).

## Câu 24

Không. Secondary thường là bản sao read-only nhận dữ liệu qua zone transfer.

Đọc lại [16. Windows DNS: zone, record và bảo vệ phân giải tên](../06-windows-server/01-dns-zones-security-and-lab.md).

## Câu 25

Không. Cơ chế failover được dạy ở đây phục vụ scope IPv4; không áp nguyên cách cho DHCPv6.

Đọc lại [17. Windows DHCP, IPAM và failover](../06-windows-server/02-dhcp-ipam-and-failover.md).

## Câu 26

Gateway/AP/controller gửi request tới NPS. Cần phân biệt với endpoint/người dùng đang xin truy cập.

Đọc lại [18. AD DS, NPS/RADIUS và truy cập từ xa](../06-windows-server/03-ad-dns-nps-and-remote-access.md).

## Câu 27

Không. Namespace quản lý đường dẫn/referral; cần cơ chế replication hoặc đồng bộ riêng.

Đọc lại [19. Chi nhánh: DFS, BranchCache và BGP ở mức nhận diện](../06-windows-server/04-branch-dfs-and-bgp-context.md).

## Câu 28

Có thể deny phía trên match trước, gắn sai hướng/interface, wildcard sai hoặc bị chặn tại thiết bị khác.

Đọc lại [21. ACL, firewall và quản trị thiết bị](../07-security-wireless/01-acl-firewall-and-device-access.md).

## Câu 29

Không. Phải kiểm tra tiếp DHCP, VLAN, route, DNS, TCP/TLS và ứng dụng.

Đọc lại [23. Wi-Fi, RF, WLC và bảo mật WLAN](../07-security-wireless/03-wlan-rf-and-controller.md).

## Câu 30

Không. Cần kiểm schema, nội dung response, trạng thái tác vụ nếu bất đồng bộ và xác nhận lại trạng thái thiết bị.

Đọc lại [24. REST API, JSON, automation và AI trong vận hành mạng](../08-automation/01-api-json-iac-and-ai.md).
