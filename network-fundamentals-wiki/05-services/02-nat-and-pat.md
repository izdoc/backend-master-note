# 14. NAT, PAT và đường về

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 4.1; PAT là phần bổ sung thực hành. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Phân biệt static NAT, dynamic pool và PAT; kiểm tra translation có điều kiện.

## Đổi địa chỉ và đổi cả port

Static NAT tạo ánh xạ địa chỉ cố định; dynamic NAT cấp ánh xạ từ pool; PAT/NAPT cho nhiều flow dùng chung địa chỉ qua ánh xạ port. NAT thay thông tin địa chỉ/transport theo kiểu triển khai; nó không tự tạo route và không thay chính sách firewall. [R16]

Inside local là địa chỉ host phía trong theo cách nhìn nội bộ; inside global là địa chỉ biểu diễn host đó phía ngoài trong mô hình NAT tương ứng. Always ghi rõ phía quan sát khi đọc log. [C18]

## Ví dụ lab tự thiết kế

R1 có inside Gi0/0 `10.10.10.1/24`, outside Gi0/1 `198.51.100.2/24`, peer ngoài `198.51.100.1`. Dải 198.51.100 chỉ dùng mô phỏng, không đưa ra Internet thật.

```text
interface GigabitEthernet0/0
 ip nat inside
interface GigabitEthernet0/1
 ip nat outside
access-list 10 permit 10.10.10.0 0.0.0.255
ip nat inside source list 10 interface GigabitEthernet0/1 overload
ip route 0.0.0.0 0.0.0.0 198.51.100.1
end
show ip nat translations
show ip nat statistics
```

`overload` minh họa PAT. ACL ở đây chọn traffic để NAT; nó chưa phải ACL bảo vệ interface. Có translation mới sau khi tạo traffic phù hợp; bảng rỗng khi chưa phát traffic chưa chứng minh sai cấu hình. [C18]

Hai ví dụ độc lập để học đúng trọng tâm blueprint:

```text
ip nat inside source static 10.10.10.20 198.51.100.20
ip nat pool LABPOOL 198.51.100.30 198.51.100.39 netmask 255.255.255.0
ip nat inside source list 10 pool LABPOOL
```

Không nhập chung các phương án mà chưa thiết kế sự tương tác. Peer ngoài phải có khả năng gửi packet về địa chỉ global; proxy ARP/routing phụ thuộc topology. [C18]

## Chẩn đoán

Kiểm tra source thực của packet, inside/outside, ACL match, route hai chiều và translation timeout. NAT thành công chưa chứng minh TCP/TLS/ứng dụng thành công. Inbound publish cần cả ánh xạ và chính sách cho phép đúng dịch vụ. [R16][C18]

## Tự kiểm tra

**Câu hỏi:** ACL dùng trong lệnh NAT permit 10.10.10.0/24 có tự chặn mọi traffic ngoài subnet đó không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Trong ngữ cảnh này nó chọn traffic để dịch địa chỉ. ACL lọc phải được áp vào điểm xử lý phù hợp như interface.

</details>

## Nguồn của bài

- [R16] — RFC 3022 — Traditional NAT.
- [C18] — Cisco — NAT troubleshooting FAQ.
- [C13] — Cisco — Configure IP Access Lists.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R16]: https://www.rfc-editor.org/rfc/rfc3022 "RFC 3022 — Traditional NAT"
[C18]: https://www.cisco.com/c/en/us/support/docs/ip/network-address-translation-nat/218012-troubleshoot-network-address-translation.html "Cisco — NAT troubleshooting FAQ"
[C13]: https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html "Cisco — Configure IP Access Lists"
