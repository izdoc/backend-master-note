# 11. Routing table, static route và FHRP

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 3.1–3.3, 3.5. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Chọn đúng route; phân biệt longest prefix, administrative distance và metric.

## Router quyết định ở hai bước

Khi xây routing table, router so sánh các nguồn route cho **cùng prefix** bằng administrative distance (AD), sau đó metric trong cơ chế thích hợp của giao thức. Khi forwarding, router chọn route khớp đích có prefix dài nhất trong bảng đã được cài. Không so AD của /24 với /16 để bỏ qua longest prefix match. AD là giá trị tin cậy cục bộ theo thiết bị, không phải phép đo tốc độ đường truyền. [C11]

Ví dụ tự thiết kế: bảng đã có default /0, `10.0.0.0/8` và `10.10.20.0/24`. Đích `10.10.20.20` dùng /24. Với hai ứng viên cùng /24, AD mới giúp quyết định nguồn route được ưu tiên. [R04][C11]

## Đọc một dòng

`O 10.20.0.0/24 [110/20] via 10.255.0.2`: O biểu thị OSPF, prefix /24, AD 110 và metric 20 theo cách hiển thị Cisco. Next hop phải reachable; có route đi chưa đủ, phía đích cũng cần route quay về. Default `0.0.0.0/0` là lựa chọn khi không có prefix cụ thể hơn. [C11]

## Ví dụ cú pháp

Giả sử next hop đã reachable:

```text
ip route 10.20.0.0 255.255.255.0 10.255.0.2
ip route 0.0.0.0 0.0.0.0 10.255.0.2
ip route 10.20.0.20 255.255.255.255 10.255.0.2
ip route 10.20.0.0 255.255.255.0 10.255.1.2 200
ipv6 route 2001:db8:20::/64 2001:db8:ff::2
ipv6 route ::/0 2001:db8:ff::2
```

Đây là các ví dụ độc lập: network, default, host và floating static route, không yêu cầu nhập tất cả. Floating static AD cao hơn route chính cùng prefix; nó chỉ biến mất/xuất hiện theo khả năng cài route, không tự phát hiện mọi lỗi upstream khi next hop vẫn reachable. [C11]

## First Hop Redundancy

FHRP cho host dùng virtual gateway và chuyển vai trò khi router gặp lỗi. Nó giải quyết dự phòng gateway, không thay routing giữa các router hay dự phòng ứng dụng. Mức CCNA cần hiểu mục đích/chức năng; HSRP/VRRP là ví dụ, không bắt buộc học sâu cấu hình trong giáo trình fundamental. [R24]

**Kiểm tra:** `show ip route`, `show ipv6 route`, `show ip interface brief`, ping có source phù hợp và traceroute hai chiều.

## Tự kiểm tra

**Câu hỏi:** Route /16 có AD 1 và route /24 đã được cài có AD 110: đích khớp cả hai chọn route nào?

<details>
<summary>Xem gợi ý trả lời</summary>

/24, vì forwarding dùng longest prefix match trên các route đã được cài.

</details>

## Nguồn của bài

- [C11] — Cisco — IP Routing Configuration Guide.
- [R04] — RFC 4632 — CIDR.
- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [R24] — RFC 9568 — VRRPv3.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
[R04]: https://www.rfc-editor.org/rfc/rfc4632 "RFC 4632 — CIDR"
[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[R24]: https://www.rfc-editor.org/rfc/rfc9568 "RFC 9568 — VRRPv3"
