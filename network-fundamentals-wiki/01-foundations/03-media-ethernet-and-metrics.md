# 03. Cáp, Ethernet và chỉ số hiệu năng

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.3–1.4, 1.13. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Chọn loại liên kết; đọc MAC table, lỗi cổng và các chỉ số mạng.

## Chọn cáp theo cả hai đầu

Copper twisted-pair, multimode fiber và single-mode fiber có yêu cầu đầu nối, transceiver, bước sóng và khoảng cách khác nhau. Ví dụ 1000BASE-T trên module phù hợp có thể dùng cáp đồng tới 100 m; 1000BASE-SX và LX/LH có điều kiện quang khác. Không áp “cáp quang đi bao xa” thành một con số chung. Tra đúng model trong datasheet. [C03][C04]

## Ethernet và MAC learning

Switch học **MAC nguồn** cùng cổng/VLAN khi nhận frame; dùng MAC đích để quyết định forwarding. Unknown unicast được flood trong VLAN, trừ cổng nhận và các giới hạn cấu hình; broadcast cũng giới hạn bởi miền L2. MAC table có aging. Mỗi cổng full-duplex không dùng cơ chế collision như Ethernet half-duplex chia sẻ cũ. [C05]

Ví dụ tự thiết kế: PC-A lần đầu gửi PC-B khi switch chưa biết MAC-B. Switch flood; khi B trả lời, switch học B. Các frame sau có thể unicast ra cổng B.

## Đo đúng thứ đang chậm

| Chỉ số | Câu hỏi nó trả lời |
|---|---|
| Link speed / bandwidth | Liên kết có dung lượng danh định bao nhiêu? |
| Throughput / goodput | Truyền được bao nhiêu dữ liệu, bao nhiêu payload hữu ích? |
| RTT | Gửi rồi nhận trả lời mất bao lâu? |
| Jitter | Độ trễ biến thiên ra sao? |
| Loss / retransmission | Có mất hoặc phải truyền lại không? |
| Utilization / queue drop | Cổng/queue có đang bão hòa không? |

Các khái niệm dùng để đọc phép đo, không có ngưỡng tốt/xấu chung cho mọi workload. Wireshark có công cụ thống kê và phân tích TCP để quan sát thời gian, lưu lượng, retransmission. [T02]

Ví dụ tính tự thiết kế: file 100 MB, tốc độ payload 80 Mb/s thì lý tưởng cần `100 × 8 / 80 = 10 giây`, chưa tính setup và overhead. 1 byte = 8 bit; MB và MiB cần thống nhất khi đo.

## Cách kiểm tra

Trên Cisco dùng `show interfaces` và `show mac address-table`; quan sát thay đổi counter giữa hai thời điểm. CRC tăng gợi ý kiểm tra đường truyền nhưng chưa xác định chính xác bộ phận hỏng. Link up không chứng minh VLAN, duplex và chất lượng cáp đều đúng. [C03][C05]

## Tự kiểm tra

**Câu hỏi:** Gộp hai đường 1 Gb/s có chắc một file đi với tốc độ 2 Gb/s không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Cơ chế cân bằng theo flow thường giữ một flow trên một member. Xem thêm bài EtherChannel.

</details>

## Nguồn của bài

- [C03] — Cisco — Cable, Connector and AC Power Cord Guide.
- [C04] — Cisco — Gigabit Ethernet SFP data sheet.
- [C05] — Cisco — Configuring VLANs.
- [C10] — Cisco — EtherChannels.
- [T02] — Wireshark — User Guide.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C03]: https://www.cisco.com/c/en/us/support/docs/switches/catalyst-6000-series-switches/21268-132.html "Cisco — Cable, Connector and AC Power Cord Guide"
[C04]: https://www.cisco.com/c/en/us/products/collateral/interfaces-modules/gigabit-ethernet-gbic-sfp-modules/datasheet-c78-366584.html "Cisco — Gigabit Ethernet SFP data sheet"
[C05]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-2_1_e/configuration/guide/2960_scg/swvlan.html "Cisco — Configuring VLANs"
[C10]: https://www.cisco.com/c/en/us/td/docs/switches/lan/catalyst2960/software/release/15-0_2_se/configuration/guide/scg2960/swethchl.html "Cisco — EtherChannels"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
