# 12. OSPFv2 một area

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 3.4. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Lập neighbor area 0, đọc trạng thái và tìm lỗi adjacency.

## Ý tưởng link-state

OSPF router trao đổi thông tin link-state trong phạm vi thiết kế, xây cơ sở dữ liệu topology và tính đường theo cost. Router ID là định danh 32 bit; process ID Cisco là cục bộ, không cần giống nhau trên hai router. Area phải phù hợp trên liên kết tham gia cùng area. [R15][C12]

Neighbor đi qua các trạng thái như Down, Init, 2-Way, ExStart, Exchange, Loading và Full. Trong mạng broadcast có DR/BDR; hai DROther có thể dừng ở 2-Way với nhau và vẫn bình thường. Trên point-to-point không bầu DR/BDR. [R15]

## Lab hai router

Giả sử R1 và R2 đã có transit `10.255.0.0/30`, mỗi router có một LAN riêng. Ví dụ R1 tự thiết kế:

```text
router ospf 1
 router-id 1.1.1.1
 passive-interface default
 no passive-interface GigabitEthernet0/1
interface GigabitEthernet0/0
 ip ospf 1 area 0
interface GigabitEthernet0/1
 ip ospf 1 area 0
 ip ospf network point-to-point
end
show ip ospf neighbor
show ip ospf interface brief
show ip route ospf
```

R2 dùng Router ID `2.2.2.2`, bật area 0 trên hai interface tương ứng và cùng network type point-to-point ở transit. Passive trên LAN ngừng gửi Hello ở LAN nhưng prefix vẫn có thể được quảng bá khi interface đã được đưa vào OSPF. [C12]

Đây là cấu hình minh họa; tên cổng/image phải khớp lab. Thay Router ID trên thiết bị đang hoạt động có thể ảnh hưởng adjacency tùy release, không dùng thao tác reset process như bước sửa lỗi mặc định. [C12]

## Điều tra neighbor không lên

Checklist giáo trình: kiểm tra link/IP/subnet → area → Hello/Dead timer → network type → authentication → MTU → Router ID trùng → ACL chặn OSPF. Dùng output để thu hẹp, không đổi mọi tham số cùng lúc. Neighbor lên Full chưa chứng minh mọi LAN đã được đưa vào routing. [R15][C12]

DR/BDR được chọn theo priority rồi Router ID trong trường hợp phù hợp; không suy DR là router có cost thấp nhất. Bầu chọn không đơn giản là luôn thay DR hiện tại khi router “tốt hơn” mới xuất hiện. [R15]

## Tự kiểm tra

**Câu hỏi:** R1 dùng process OSPF 1, R2 dùng 100. Đây có tự gây lỗi neighbor không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Process ID có ý nghĩa cục bộ trên Cisco. Cần khớp các điều kiện giao thức trên liên kết, như area và timer.

</details>

## Nguồn của bài

- [R15] — RFC 2328 — OSPFv2.
- [C12] — Cisco — OSPFv2 on an interface basis.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R15]: https://www.rfc-editor.org/rfc/rfc2328 "RFC 2328 — OSPFv2"
[C12]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing/m_iro-mode-ospfv2.html "Cisco — OSPFv2 on an interface basis"
