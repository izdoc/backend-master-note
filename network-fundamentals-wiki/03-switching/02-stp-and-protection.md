# 09. STP, Rapid PVST+ và bảo vệ vòng lặp

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 2.5. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Đọc root/port role; phân biệt BPDU guard, root guard, loop guard và BPDU filter.

## Vì sao cần STP?

Liên kết L2 dự phòng có thể tạo loop, gây frame lặp và MAC table không ổn định. STP tạo topology forwarding không vòng lặp. Rapid PVST+ chạy một instance theo VLAN trên Cisco. Root bridge được chọn theo bridge ID thấp nhất; bridge ID gồm priority và thông tin định danh, không chỉ MAC. [C07][C09]

| Khái niệm | Cách hiểu khi đọc output |
|---|---|
| Root bridge | Mốc tính cây của instance |
| Root port | Đường tốt nhất của non-root bridge về root |
| Designated port | Cổng được chọn forwarding trên segment |
| Alternate port | Đường thay thế về root |
| RSTP states | Discarding, learning, forwarding |

Cost/bridge ID/port ID tham gia chọn vai trò theo trường hợp. Không học mẹo “cổng có số nhỏ nhất luôn thắng”. [C07][C09]

## Các tính năng bảo vệ khác nhau

| Tính năng | Tác dụng chính |
|---|---|
| PortFast | Cho edge port vào forwarding nhanh; STP vẫn tồn tại |
| BPDU Guard | Phát hiện BPDU ở nơi không nên có; thường đưa cổng err-disabled |
| Root Guard | Chặn superior BPDU làm đổi root qua cổng đó |
| Loop Guard | Giữ một số cổng khỏi forwarding sai khi mất BPDU mong đợi |
| BPDU Filter | Lọc BPDU; có thể làm mất bảo vệ loop nếu dùng sai |

BPDU Filter ở mức interface và chế độ global kết hợp PortFast có hành vi khác nhau; đọc tài liệu đúng platform. Root Guard không tương đương BPDU Guard. [C07][C08][C09]

## Ví dụ lab tự thiết kế

Chỉ áp dụng vào cổng PC lab đã xác nhận là edge:

```text
interface FastEthernet0/1
 spanning-tree portfast
 spanning-tree bpduguard enable
end
show spanning-tree vlan 10
show interfaces status err-disabled
```

Không bật PortFast/BPDU filter bừa trên liên kết giữa switch. Trước khi phục hồi err-disable, tìm nguyên nhân BPDU/loop; chỉ bounce cổng sẽ không sửa nguyên nhân. [C07]

**Quan sát:** chọn SW1 làm root VLAN 10, nối ba switch thành tam giác trong lab, ghi cổng alternate; rút một uplink và theo dõi hội tụ. Thời gian phụ thuộc platform/topology, không hứa một con số cố định.

## Tự kiểm tra

**Câu hỏi:** PortFast có tắt STP không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Nó tối ưu chuyển trạng thái cho edge port. Cổng vẫn xử lý BPDU theo tính năng được cấu hình.

</details>

## Nguồn của bài

- [C07] — Cisco — PortFast and BPDU Guard.
- [C08] — Cisco — Root Guard.
- [C09] — Cisco — Loop Guard and UDLD.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C07]: https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10586-65.html "Cisco — PortFast and BPDU Guard"
[C08]: https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol/10588-74.html "Cisco — Root Guard"
[C09]: https://www.cisco.com/c/en/us/support/docs/lan-switching/spanning-tree-protocol-stp-8021d/218321-configure-stp-with-loop-guard-and-bpdu-s.html "Cisco — Loop Guard and UDLD"
