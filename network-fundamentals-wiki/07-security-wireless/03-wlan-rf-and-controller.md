# 23. Wi-Fi, RF, WLC và bảo mật WLAN

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.11, 2.6–2.9, 5.9–5.10. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Phân biệt SSID/VLAN; đọc cấu hình WLAN và kiểm tra từ RF đến IP.

## RF trước khi nói tốc độ

Wi-Fi dùng môi trường radio chia sẻ. SSID là tên mạng được quảng bá/cấu hình; BSSID nhận diện BSS theo giao diện radio tương ứng. Kênh và channel width ảnh hưởng overlap, dung lượng và nhiễu. Với kế hoạch 2.4 GHz 20 MHz thông dụng, 1/6/11 là các kênh không chồng lấn; kênh được phép còn tùy regulatory domain. Không áp cùng kế hoạch cho 5/6 GHz. [C15]

RSSI mạnh chưa bảo đảm chất lượng: cần nhìn noise/SNR, channel utilization, retry và site survey. Tăng công suất AP không chắc giúp client phát yếu gửi ngược về tốt hơn. [C15]

## Kiến trúc và đường dữ liệu

Autonomous AP quản lý cục bộ; lightweight AP làm việc với WLC; cloud-managed quản lý từ cloud theo sản phẩm. Cần phân biệt đường quản lý và đường data: cloud-managed không có nghĩa tất cả client traffic phải đi qua cloud. Local/FlexConnect có cách chuyển tiếp khác nhau theo thiết kế. [C17][C24]

Nhận diện AP modes local, FlexConnect, monitor và sniffer; không coi một AP ở mode quan sát là đang phục vụ client như bình thường. Các mode hỗ trợ phụ thuộc dòng AP/controller. [C25]

## Bảo mật

WPA/TKIP là công nghệ cũ; WPA2 với AES-CCMP và WPA3 thuộc các lựa chọn cần phân biệt. Personal dùng cơ chế chia sẻ secret thích hợp; Enterprise dùng 802.1X/EAP và hạ tầng AAA/certificate. Không suy “ẩn SSID” là mã hóa. [C16]

## Lab GUI theo khả năng controller

Lab tự thiết kế trên WLC mô phỏng hoặc thiết bị lab, menu có thể khác phiên bản:

1. Tạo WLAN profile, SSID `NET-LAB`, bật WLAN.
2. Chọn WPA2-Personal/AES và PSK riêng của lab.
3. Ánh xạ WLAN vào VLAN10 qua interface/policy profile phù hợp.
4. Kiểm tra AP được gán profile/tag và radio phục vụ đúng.
5. Kết nối laptop, kiểm tra association, IP DHCP, gateway, DNS và ứng dụng.

Chụp các màn hình General, Security, VLAN/policy và client state. Không ghi PSK vào báo cáo công khai. [C16]

**Bẫy:** đã associate chưa đồng nghĩa đã có IP; SSID khác nhau có thể cùng VLAN; sai trunk/policy có thể làm client nhận nhầm DHCP. Thực hành thêm QoS profile và đọc advanced settings theo giao diện, không dùng giá trị “tối ưu” chung cho mọi mạng. [C16]

## Tự kiểm tra

**Câu hỏi:** Laptop thấy SSID và kết nối được nhưng không nhận IP. Có thể chỉ kết luận sai mật khẩu không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Association thành công rồi cần kiểm tra ánh xạ VLAN, forwarding path, trunk/relay và DHCP.

</details>

## Nguồn của bài

- [C15] — Cisco — Wireless RF Reference Guide.
- [C16] — Cisco — Catalyst 9800 WLAN Security, IOS XE 17.9.
- [C17] — Cisco — AP connectivity and configuration.
- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [M09] — Microsoft — DHCP overview.
- [C24] — Cisco — Unified Wireless Network Solution Guide.
- [C25] — Cisco — Access Point Modes, IOS XE 17.13.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C15]: https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/technical-reference/wireless-rf-reference-guide.html "Cisco — Wireless RF Reference Guide"
[C16]: https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-9/config-guide/b_wl_17_9_cg/m_wlan_security_9800.html "Cisco — Catalyst 9800 WLAN Security, IOS XE 17.9"
[C17]: https://content.ciscodcloud.com/content/cisco-dcloud/us/en/home/support/help/using-dcloud/wireless_connect.html "Cisco — AP connectivity and configuration"
[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[M09]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top "Microsoft — DHCP overview"
[C24]: https://www.cisco.com/c/en/us/products/collateral/wireless/unified-wireless-network-sg.html "Cisco — Unified Wireless Network Solution Guide"
[C25]: https://www.cisco.com/c/en/us/td/docs/wireless/controller/9800/17-13/config-guide/b_wl_17_13_cg/m-sniffer-cg.html "Cisco — Access Point Modes, IOS XE 17.13"
