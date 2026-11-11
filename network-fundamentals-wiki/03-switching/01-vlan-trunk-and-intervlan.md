# 08. VLAN, trunk và inter-VLAN routing

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 2.1–2.2. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Tạo VLAN và trunk; giải thích vì sao trunk không tự định tuyến.

## Tách miền L2

VLAN chia switch thành các broadcast domain logic. Access port thường mang một data VLAN; voice VLAN có thể bổ sung riêng cho IP phone. Trunk 802.1Q vận chuyển nhiều VLAN qua một liên kết. Trên Cisco, VLAN 1 thường là default VLAN; native VLAN trên trunk thường nhận/gửi frame untagged theo cấu hình. Phải khớp native VLAN hai đầu. [C05][C06]

VLAN không tự là chính sách chặn truy cập: khi bật routing giữa VLAN, cần ACL/firewall để giới hạn dịch vụ theo yêu cầu. Inter-VLAN có thể dùng router subinterface hoặc SVI trên switch L3. [C11][C13]

## Ví dụ cấu hình độc lập

Giả sử switch lab có Fa0/1 nối PC User và Gi0/1 nối router. Đổi tên interface theo model. Hai phía trunk cần cấu hình tương ứng.

```text
configure terminal
vlan 10
 name USERS
vlan 20
 name SERVERS
interface FastEthernet0/1
 switchport mode access
 switchport access vlan 10
interface GigabitEthernet0/1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
end
show vlan brief
show interfaces trunk
```

Đây là ví dụ rút gọn tự thiết kế dựa trên cú pháp Cisco; không phải cấu hình đầy đủ cho sản xuất. `switchport trunk allowed vlan 10,20` thay danh sách hiện có; khi bổ sung vào hệ thống đang chạy phải hiểu khác biệt với `add`. [C05][C06]

Router lab:

```text
interface GigabitEthernet0/0
 no shutdown
interface GigabitEthernet0/0.10
 encapsulation dot1Q 10
 ip address 10.10.10.1 255.255.255.0
interface GigabitEthernet0/0.20
 encapsulation dot1Q 20
 ip address 10.10.20.1 255.255.255.0
```

PC dùng gateway theo subnet. Có hai connected route rồi vẫn phải kiểm tra ACL và chiều về. [C11]

## Bẫy khi vận hành

SVI có thể không up nếu VLAN chưa có cổng hoạt động phù hợp. VLAN đã tồn tại không có nghĩa được cho qua mọi trunk. Cùng VLAN ID ở hai site không có nghĩa đã nối cùng miền L2. [C05][C06]

**Bài tập thực hành:** bỏ VLAN 20 khỏi allowed list trong lab; ghi triệu chứng ở PC và output trunk trước/sau, rồi khôi phục.

## Tự kiểm tra

**Câu hỏi:** Hai PC ở VLAN 10 và VLAN 20 có ping được chỉ nhờ tạo trunk không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Cần routing giữa hai subnet và chính sách cho phép; trunk chỉ vận chuyển frame của các VLAN.

</details>

## Nguồn của bài

- [C05] — Cisco — Configuring VLANs.
- [C06] — Cisco — Configuring VLAN Trunks.
- [C11] — Cisco — IP Routing Configuration Guide.
- [C13] — Cisco — Configure IP Access Lists.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C05]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-2_1_e/configuration/guide/2960_scg/swvlan.html "Cisco — Configuring VLANs"
[C06]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960x/software/15-2_7_e/configuration_guide/b_1527e_consolidated_2960x_cg/m_vlan_trunk_cg_2960-x.html "Cisco — Configuring VLAN Trunks"
[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
[C13]: https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html "Cisco — Configure IP Access Lists"
