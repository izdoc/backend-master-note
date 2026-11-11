# 22. DHCP snooping, DAI, port security và VPN

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 5.5, 5.7–5.8. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Hiểu chuỗi tin cậy L2; tránh tự chặn IP tĩnh khi bật DAI.

## Ba lớp kiểm soát L2

DHCP snooping chặn DHCP server traffic không hợp lệ ở untrusted ports và học bindings từ trao đổi DHCP. Chỉ trust hướng tới server hợp lệ đã xác minh, không trust mọi uplink một cách máy móc. DAI kiểm tra ARP trên untrusted ports dựa vào bindings hoặc cơ chế ARP ACL phù hợp. [C14]

Port security giới hạn MAC được phép trên cổng theo cấu hình. Các violation mode protect/restrict/shutdown có hành vi khác nhau; sticky MAC học được có thể xuất hiện trong running config và cần hiểu cách lưu. Giới hạn một MAC có thể không phù hợp cổng IP phone cộng PC. Nó không xác thực người dùng như 802.1X. [C20]

## Ví dụ chỉ dùng trong lab

Giả sử Gi0/1 thực sự đi tới DHCP server hợp lệ, Fa0/1 là client động VLAN10:

```text
ip dhcp snooping
ip dhcp snooping vlan 10
interface GigabitEthernet0/1
 ip dhcp snooping trust
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10
 switchport port-security
 switchport port-security maximum 1
 switchport port-security violation restrict
end
show ip dhcp snooping binding
show port-security interface FastEthernet0/1
```

Sau khi client renew trong lab và binding hợp lệ đã có, mới khảo sát `ip arp inspection vlan 10` cùng trust/ARP ACL cho đúng đường đi. Máy IP tĩnh cần được xử lý trước; bật DAI khi thiếu binding có thể làm mất kết nối. Packet Tracer/image có thể không hỗ trợ đủ feature. [C14][C20]

Đây là cấu hình từng phần tự thiết kế; không áp trực tiếp vào hạ tầng đang dùng. Hoàn tác lab: gỡ port security ở Fa0/1, tắt snooping VLAN10; nếu đã bật DAI thì gỡ DAI VLAN10 và cấu hình trust liên quan mới thêm.

## VPN bảo vệ phạm vi nào?

IPsec định nghĩa bảo vệ ở tầng IP, có tunnel và transport mode theo thiết kế. Site-to-site bảo vệ giữa gateway, remote access bảo vệ kết nối client tới điểm VPN. Dữ liệu sau khi giải mã tại đầu cuối vẫn cần phân quyền, segmentation và bảo vệ ứng dụng. VPN không chứng minh mọi host sau gateway đều đáng tin. [R20]

Bài tập tự thiết kế: vẽ chi nhánh → gateway VPN → server và đánh dấu đoạn được tunnel bảo vệ, đoạn LAN và điểm xác thực người dùng. So sánh chứng chỉ, MFA và nhật ký với mô hình chỉ dùng mật khẩu dùng chung.

## Tự kiểm tra

**Câu hỏi:** DAI có thể làm máy cấu hình IP tĩnh mất mạng không?

<details>
<summary>Xem gợi ý trả lời</summary>

Có. Nếu không có ánh xạ được cho phép phù hợp trên untrusted path, ARP hợp lệ của máy vẫn có thể bị loại.

</details>

## Nguồn của bài

- [C14] — Cisco — Troubleshoot DAI and IPSG.
- [C20] — Cisco — Port security command reference.
- [R20] — RFC 4301 — IPsec architecture.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C14]: https://www.cisco.com/c/en/us/support/docs/switches/lan-switch-software/222274-troubleshoot-dynamic-arp-inspection-dai.html "Cisco — Troubleshoot DAI and IPSG"
[C20]: https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/security/s1/sec-s1-cr-book/sec-cr-s6.html "Cisco — Port security command reference"
[R20]: https://www.rfc-editor.org/rfc/rfc4301 "RFC 4301 — IPsec architecture"
