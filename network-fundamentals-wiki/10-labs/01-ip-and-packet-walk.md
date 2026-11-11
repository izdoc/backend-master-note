# Lab 01 — IP, subnet và packet walk

[Mục lục](../INDEX.md) · [Bảng đối chiếu](../SYLLABUS-MAPPING.md)

**Thời lượng gợi ý:** 60–90 phút. **Môi trường:** hai PC và một switch trong Packet Tracer, hoặc hai VM cùng virtual switch nội bộ. Bài tập do giáo trình tự thiết kế; chưa thực thi trong phiên xuất bản này.

## Nhiệm vụ A: tính tay

1. Với `172.16.5.139/27`, xác định network, broadcast, host range.
2. Xác định .150 và .170 có cùng subnet với host trên không.
3. Chia `10.40.0.0/24` cho nhu cầu 60, 25, 10 host và một transit hai đầu.
4. Nêu điều kiện để dùng /31 thay /30.

CIDR và /31 tra [R04][R05]. Không xem đáp án trước khi viết phép tính.

## Nhiệm vụ B: hai máy cùng link

Cấu hình A `10.10.10.10/24`, B `10.10.10.20/24`; không đặt default gateway. Ping B từ A. Quan sát ARP cache trước/sau; capture ARP trên VM hoặc Simulation mode trong Packet Tracer. ARP phân giải IP của next hop trong link. [R02]

Thay B thành `10.10.20.20/24`, giữ nguyên switch và không có router. Dự đoán kết quả trước khi ping. Khôi phục B về .10.20 và kiểm tra lại.

## Nhiệm vụ C: transport

Trên máy lab có dịch vụ TCP được bật sẵn, kiểm tra đúng port. Tìm SYN, SYN/ACK, ACK bằng display filter `tcp.flags.syn == 1`. Nếu không có dịch vụ, ghi rõ “chưa có listener”, không ghi thất bại là lỗi mạng. [R10][T03]

Trong VM, dùng Wireshark User Guide để chọn đúng interface. Trong Packet Tracer, dùng event list mô phỏng, không gọi đó là một pcap thực tế. [T02]

## Kỳ vọng và đáp án

- A1: network `172.16.5.128/27`, broadcast .159, usable .129–.158.
- A2: .150 cùng subnet, .170 khác subnet.
- A3: một phương án là .0/26, .64/27, .96/28, .112/30; usable lần lượt .1–.62, .65–.94, .97–.110, .113–.114. Phần còn lại dự trữ.
- A4: point-to-point, hai đầu hỗ trợ; không dùng như subnet broadcast nhiều host.
- B: cùng subnet có thể trao đổi không cần gateway. Khi đổi B sang subnet khác và không có route/router, trao đổi IP thông thường thất bại.

Các giá trị trên được tính từ đầu bài. Ping đầu tiên có thể chịu ảnh hưởng ARP; ghi nhiều lần và quan sát packet thay vì giả định mọi lần đều giống nhau.

## Nộp bài và hoàn tác

Nộp bảng phép tính, ảnh IP/route/ARP, hai packet mẫu và kết luận “đã chứng minh/chưa chứng minh”. Khôi phục IP B; tắt dịch vụ thử nghiệm nếu đã bật. Không giữ capture chứa dữ liệu không thuộc lab.

## Nguồn dùng cho lab

- [R02] — RFC 826 — ARP.
- [R04] — RFC 4632 — CIDR.
- [R05] — RFC 3021 — IPv4 /31.
- [R10] — RFC 9293 — TCP.
- [T02] — Wireshark — User Guide.
- [T03] — Wireshark — Display filter expressions.

[R02]: https://www.rfc-editor.org/rfc/rfc826 "RFC 826 — ARP"
[R04]: https://www.rfc-editor.org/rfc/rfc4632 "RFC 4632 — CIDR"
[R05]: https://www.rfc-editor.org/rfc/rfc3021 "RFC 3021 — IPv4 /31"
[R10]: https://www.rfc-editor.org/rfc/rfc9293 "RFC 9293 — TCP"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
[T03]: https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html "Wireshark — Display filter expressions"
