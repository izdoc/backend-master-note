# Lab 05 — Chính sách, Wi-Fi và capture

[Mục lục](../INDEX.md) · [Bảng đối chiếu](../SYLLABUS-MAPPING.md)

**Thời lượng gợi ý:** 2 giờ. Dùng bản sao Lab02 để thử ACL và cổng bảo mật. Với WLAN cần WLC/AP/client trong simulator hoặc thiết bị lab hỗ trợ; không phải mọi simulator có đủ feature. Chưa thực thi trong lần xuất bản này.

## A. ACL có kiểm chứng

Trên topology Lab02, thêm server mô phỏng 10.10.20.20/24, gateway .1 vào access VLAN20, bật HTTPS nếu simulator hỗ trợ. PC-A ở 10.10.10.50.

Viết bảng policy trước: HTTPS tới server được phép; ICMP để phép thử chẩn đoán nếu yêu cầu; các traffic còn lại bị chặn. Tạo named extended ACL và áp inbound trên subinterface VLAN10:

```text
ip access-list extended LAB-USERS
 permit tcp 10.10.10.0 0.0.0.255 host 10.10.20.20 eq 443
 permit icmp 10.10.10.0 0.0.0.255 host 10.10.20.20
interface GigabitEthernet0/0.10
 ip access-group LAB-USERS in
end
show access-lists LAB-USERS
```

Ví dụ tự thiết kế; nếu ứng dụng dùng DNS/DHCP cần thêm policy đúng flow, không suy ACL này là mẫu đủ dùng chung. Server phải có listener để phép thử TCP có ý nghĩa. [C13]

Đặt một deny khớp HTTPS trước permit trong lab, dự đoán rồi kiểm counter. Khôi phục thứ tự. Counter tăng hỗ trợ giả thuyết rule đã khớp, không tự chứng minh response nghiệp vụ thành công.

## B. L2 security

Trên một access port chỉ nối PC, thử port security maximum1/restrict theo bài22, rồi đổi PC/MAC mô phỏng. Quan sát violation counter. Xác nhận topology trước dùng sticky hoặc shutdown. [C20]

Nếu platform có DHCP snooping/DAI: dựng DHCP thật trong simulator, xác nhận lease/binding rồi mới bật DAI; thêm một máy IP tĩnh và lập kế hoạch ánh xạ cho phép. Không ghi “đã test DAI” nếu simulator chỉ chấp nhận lệnh nhưng không mô phỏng đầy đủ hành vi. [C14]

## C. SSH

Làm bài21 trên router lab: local user/secret riêng, RSA key, SSHv2 và VTY chỉ SSH; test từ subnet quản lý. Kiểm tra tài khoản sai bị từ chối và console còn khả dụng. Gỡ user/key lab chỉ khi đã xác nhận còn đường quản trị. [C19]

## D. WLAN GUI

Theo bài23: tạo NET-LAB, WPA2-Personal/AES, map VLAN10, chọn AP/profile phù hợp. Chụp phần WLAN security và VLAN mapping, che PSK. Test theo chuỗi association → DHCP → gateway → DNS → HTTPS. Ghi một thay đổi VLAN sai và triệu chứng rồi khôi phục. [C16]

## E. Capture có giới hạn

Trên phần VM hoặc thiết bị hỗ trợ capture, thu đúng flow 443; dùng display filter `tcp.port == 443`, `tcp.analysis.retransmission`. Nếu capture là TLS, giải thích vì sao không thấy HTTP plaintext. Với Packet Tracer chỉ dùng event mô phỏng, không nộp như pcap thật. [T02][T03]

## Tiêu chí đạt và hoàn tác

Đạt khi policy matrix khớp phép thử và mỗi thay đổi đều có chứng cứ trước/sau. Gỡ ACL khỏi interface trước xóa ACL; khôi phục port security/trust theo bản sao lab; xóa WLAN mới và xác nhận không còn profile lab được áp nhầm.

## Nguồn dùng cho lab

- [C13] — Cisco — Configure IP Access Lists.
- [C14] — Cisco — Troubleshoot DAI and IPSG.
- [C16] — Cisco — Catalyst 9800 WLAN Security, IOS XE 17.9.
- [C19] — Cisco — Configure SSH on Routers.
- [C20] — Cisco — Port security command reference.
- [T02] — Wireshark — User Guide.
- [T03] — Wireshark — Display filter expressions.

[C13]: https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html "Cisco — Configure IP Access Lists"
[C14]: https://www.cisco.com/c/en/us/support/docs/switches/lan-switch-software/222274-troubleshoot-dynamic-arp-inspection-dai.html "Cisco — Troubleshoot DAI and IPSG"
[C16]: https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-9/config-guide/b_wl_17_9_cg/m_wlan_security_9800.html "Cisco — Catalyst 9800 WLAN Security, IOS XE 17.9"
[C19]: https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html "Cisco — Configure SSH on Routers"
[C20]: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s6.html "Cisco — Port security command reference"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
[T03]: https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html "Wireshark — Display filter expressions"
