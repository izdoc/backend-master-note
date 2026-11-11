# 10. EtherChannel, LACP, CDP và LLDP

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 2.3–2.4. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Kiểm tra link aggregation; dùng neighbor discovery để xác nhận dây nối.

## EtherChannel là một liên kết logic

EtherChannel gộp các member thành port-channel. LACP hỗ trợ thương lượng: active chủ động gửi; passive chờ đối tác. Active/active và active/passive có thể lập nhóm; passive/passive không chủ động khởi tạo. Cấu hình mode `on` là tĩnh, không dùng LACP. [C10]

Member cần tương thích speed/duplex, loại L2/L3 và các thuộc tính trunk/VLAN liên quan. Thuật toán hash thường phân flow vào member, nên một TCP flow không mặc nhiên đạt tổng tốc độ mọi member. Hai link 1 Gb/s tạo khả năng tổng hợp cho nhiều flow, không phải cam kết 2 Gb/s cho một download. [C10]

## Lab L2

Hai switch có Gi0/1 và Gi0/2 nối tương ứng. Chưa cắm song song cho tới khi cấu hình nhất quán hai đầu hoặc kiểm soát STP. Ví dụ tự thiết kế:

```text
interface range GigabitEthernet0/1 - 2
 switchport mode trunk
 switchport trunk allowed vlan 10,20
 channel-group 1 mode active
interface Port-channel1
 switchport mode trunk
 switchport trunk allowed vlan 10,20
end
show etherchannel summary
show interfaces port-channel 1
```

Kỳ vọng port-channel đang được sử dụng và member được bundled; ký hiệu cụ thể đọc ở legend của output. Rút một member rồi kiểm tra liên tục ping và member còn lại. Đây là quy trình lab, chưa có kết quả thực thi sẵn. [C10]

L3 EtherChannel dùng routed port với `no switchport` nếu model hỗ trợ; đặt IP trên port-channel logic thay vì gán các IP độc lập cho từng member. [C10]

## Neighbor discovery

CDP là giao thức của Cisco; LLDP là giao thức discovery đa hãng. Output neighbor giúp tìm thiết bị/cổng kết nối trực tiếp, IP quản trị hoặc capability khi được quảng bá. Nó không thay thế routing table hay bản vẽ end-to-end. Đây là nội dung cần biết của CCNA 2.3; hành vi/cú pháp tra tài liệu discovery. [C22][C23]

Quan sát bằng `show cdp neighbors detail` và `show lldp neighbors detail`; LLDP có thể cần bật trên image. Chỉ quảng bá discovery ở các liên kết phù hợp chính sách quản trị.

**Lỗi thường gặp:** cấu hình một member khác native VLAN, nhầm dây giữa hai switch độc lập không hỗ trợ multichassis, tưởng port-channel up nghĩa mọi member đều hoạt động.

## Tự kiểm tra

**Câu hỏi:** LACP passive ở cả hai đầu có tự lập EtherChannel không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Cần ít nhất một đầu active để chủ động thương lượng; kiểm tra cả cấu hình tương thích của member.

</details>

## Nguồn của bài

- [C10] — Cisco — EtherChannels.
- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [C22] — Cisco — Configure CDP.
- [C23] — Cisco — Configure LLDP.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C10]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-0_2_se/configuration/guide/scg2960/swethchl.html "Cisco — EtherChannels"
[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[C22]: https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/cdp-lldp-mac-udld/cdp-lldp-mac-udld-configuration-guide/c-configure-cdp.html "Cisco — Configure CDP"
[C23]: https://www.cisco.com/c/en/us/td/docs/switches/lan/c9000/lyr2-fwd/cdp-lldp-mac-udld/cdp-lldp-mac-udld-configuration-guide/c-configure-lldp.html "Cisco — Configure LLDP"
