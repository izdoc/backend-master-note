# 25. Troubleshooting có bằng chứng và packet capture

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** Thực hành xuyên suốt CCNA/MCSA. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Điều tra theo giả thuyết; đọc capture mà không kết luận quá mức.

## Chốt phạm vi trước khi sửa

Quy trình dưới đây là phương pháp vận hành do giáo trình đề xuất:

1. Ghi source, destination, transport/port, thời gian và môi trường.
2. Xác định ảnh hưởng: một máy, một VLAN, một site hay tất cả.
3. Lấy trạng thái ban đầu: IP/route/DNS, cổng, log, thay đổi gần nhất.
4. Viết một giả thuyết kiểm chứng được, chọn phép đo có thể bác bỏ nó.
5. Đổi ít nhất có thể, đo lại cùng điều kiện, ghi hoàn tác.

Không “tắt firewall rồi thử” như bước đầu chung. Nếu cần phép thử policy, giới hạn vào đúng flow/thời gian lab và ghi kết quả.

## Các điểm kiểm tra

| Tầng | Windows / Linux / Cisco |
|---|---|
| NIC/IP | `Get-NetIPConfiguration` / `ip address` / `show ip interface brief` |
| Route/neighbor | `route print`, `arp -a` / `ip route`, `ip neigh` / `show ip route`, `show arp` |
| DNS | `Resolve-DnsName` / `getent hosts`, `dig` nếu có / kiểm DNS server |
| TCP port | `Test-NetConnection host -Port 443` / `nc -vz host 443` nếu có |
| Listening | `Get-NetTCPConnection -State Listen` / `ss -lntp` |
| Ứng dụng | `curl -v https://host` và log phía server |

Bảng là gợi ý công cụ theo OS, không phải mọi lệnh đều cài sẵn. Các output giúp kiểm tra giả thuyết; không thay thế kiến thức giao thức. [M27][M04][C11][R10]

## Capture filter khác display filter

Capture filter quyết định packet nào được thu vào; display filter chỉ giới hạn packet hiển thị sau capture. Display filter không khôi phục packet đã bị capture filter loại. Ví dụ hiển thị: [T02][T03]

```text
arp
dns
tcp.port == 443
ip.addr == 10.10.20.20
tcp.flags.syn == 1 && tcp.flags.ack == 0
tcp.analysis.retransmission
```

Đây là các filter độc lập. Capture đúng interface, timestamp và điểm quan sát. Trên switch, SPAN cần cấu hình riêng; một PC bình thường không nhìn được mọi unicast của cả VLAN. [T02]

## Ba case cho backend

**Timeout TCP:** xem SYN đã ra NIC chưa, có SYN/ACK không, route về, ACL và listener. **TLS fail:** xem trust chain, hostname/SNI và thời gian. **HTTP 502:** xem reverse proxy upstream, DNS/route/port/TLS tới backend; HTTP response đã có là bằng chứng khác với mất link. Đây là nhánh điều tra minh họa, không chẩn đoán tự động. [R10][R21][R25]

Capture có thể chứa thông tin nhạy cảm; chỉ thu trong phạm vi được phép và lọc dữ liệu trước chia sẻ. Ghi “không thấy trong capture tại X” thay cho “không hề được gửi”.

## Tự kiểm tra

**Câu hỏi:** Không thấy gói phản hồi ở máy client thì đã xác định server không gửi chưa?

<details>
<summary>Xem gợi ý trả lời</summary>

Chưa. Packet có thể bị loại trên đường hoặc capture sai điểm/interface; cần đối chiếu capture/log phía server và các hop liên quan.

</details>

## Nguồn của bài

- [T02] — Wireshark — User Guide.
- [T03] — Wireshark — Display filter expressions.
- [M27] — Microsoft — New-NetIPAddress.
- [M04] — Microsoft — DNS overview.
- [C11] — Cisco — IP Routing Configuration Guide.
- [R10] — RFC 9293 — TCP.
- [R21] — RFC 9110 — HTTP semantics.
- [R25] — RFC 8446 — TLS 1.3.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
[T03]: https://www.wireshark.org/docs/wsug_html_chunked/ChWorkBuildDisplayFilterSection.html "Wireshark — Display filter expressions"
[M27]: https://learn.microsoft.com/en-us/powershell/module/nettcpip/new-netipaddress "Microsoft — New-NetIPAddress"
[M04]: https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top "Microsoft — DNS overview"
[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
[R10]: https://www.rfc-editor.org/rfc/rfc9293 "RFC 9293 — TCP"
[R21]: https://www.rfc-editor.org/rfc/rfc9110 "RFC 9110 — HTTP semantics"
[R25]: https://www.rfc-editor.org/rfc/rfc8446 "RFC 8446 — TLS 1.3"
