# 20. Networking hiệu năng cao, Hyper-V và SDN

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.12, 6.2–6.3; 70-741: Advanced infrastructure. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Phân biệt teaming, offload, VRF và overlay; chọn phép đo trước tối ưu.

## Những tên dễ nhầm

NIC Teaming gộp adapter theo mô hình được hỗ trợ; SET tích hợp teaming với Hyper-V virtual switch. Không mặc định coi SET và LACP EtherChannel là cùng cơ chế cấu hình. Khả năng hỗ trợ phụ thuộc phiên bản Windows, NIC/driver và topology. [M24]

| Tính năng | Ý tưởng |
|---|---|
| RSS | Phân xử lý nhận qua nhiều CPU queue theo cơ chế hỗ trợ |
| vRSS / VMMQ | Mở rộng xử lý queue cho môi trường ảo theo platform |
| RDMA / SMB Direct | Giảm CPU và độ trễ truyền dữ liệu với phần cứng/phần mềm tương thích |
| SR-IOV | Chia chức năng NIC để VM có đường truy cập phần cứng phù hợp |
| DCB | Cơ chế Ethernet hỗ trợ phân lớp/điều khiển lưu lượng cho workload cần thiết |

Đây là bảng nhận diện, không phải mọi NIC đều hỗ trợ hay bật là nhanh hơn. Kiểm tra host, switch, driver và workload. [M25]

Ví dụ phép đo tự thiết kế: trước khi bật offload, ghi throughput, CPU, RTT, retransmission và cấu hình driver. Đổi một tham số mỗi lần; so sánh cùng workload. Lỗi checksum hiển thị ở capture tại host đôi khi liên quan offload, phải kiểm tra vị trí capture trước khi kết luận packet hỏng. [T02]

## Ảo hóa mạng

VM có virtual NIC nối virtual switch. Container dùng networking của runtime/host theo chế độ được chọn; container không mặc nhiên có một router vật lý riêng. VRF tách bảng định tuyến để nhiều miền logic tồn tại trên cùng thiết bị; route leaking cần được thiết kế nếu muốn giao tiếp. Đây là nhóm khái niệm được CCNA yêu cầu nhận diện; phần tách routing table tham khảo VRF Lite. [C01][C26]

Underlay là mạng vận chuyển nền; overlay là mạng logic đặt trên đó. Control plane quyết định thông tin forwarding/policy, data plane chuyển packet. Northbound API thường kết nối ứng dụng/automation tới controller; southbound kết nối controller với thành phần hạ tầng theo kiến trúc cụ thể. [C01][M26]

## Windows SDN

Mô hình Microsoft gồm Network Controller, Software Load Balancer và gateway, cùng Hyper-V virtual networking. HNV tách mạng tenant khỏi không gian vật lý. Controller không loại bỏ nhu cầu underlay, MTU, routing và khả năng phục hồi. Tài liệu M26 là nguồn kiến trúc lịch sử, không phải runbook triển khai mới. [M26]

**Bài tập:** vẽ hai tenant cùng dùng 10.0.0.0/24, chỉ rõ lớp nào phân biệt tenant và điểm nào được phép ra mạng vật lý. Giải thích vì sao NAT một mình không thay thế tenant isolation.

## Tự kiểm tra

**Câu hỏi:** Bật thêm nhiều offload có chắc giảm mọi loại độ trễ không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Phải đo với workload, NIC/driver và môi trường cụ thể; throughput cao hơn có thể đi cùng trade-off khác.

</details>

## Nguồn của bài

- [M24] — Microsoft — Software-only networking features.
- [M25] — Microsoft — Software/hardware integrated features.
- [M26] — Microsoft — Software Defined Networking.
- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [T02] — Wireshark — User Guide.
- [C26] — Cisco — Multi-VRF Support.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[M24]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/hpn/hpn-software-only-features "Microsoft — Software-only networking features"
[M25]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/hpn/hpn-software-hardware-features "Microsoft — Software/hardware integrated features"
[M26]: https://learn.microsoft.com/en-us/previous-versions/azure/azure-local/concepts/software-defined-networking "Microsoft — Software Defined Networking"
[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
[C26]: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/ip-routing/b-ip-routing/m_mp-multi-vrf-vrf-lite.html "Cisco — Multi-VRF Support"
