# 15. NTP, SNMP, syslog, QoS và truyền file

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 4.2, 4.4–4.5, 4.7, 4.9. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Chọn công cụ vận hành; hiểu queueing và chính sách thời gian.

## Đồng bộ thời gian

NTP đồng bộ clock giữa các thiết bị theo mô hình phân cấp. Stratum thể hiện quan hệ tầng tới nguồn thời gian, không phải điểm chất lượng tuyệt đối. Log lệch clock gây khó ghép sự kiện; kiểm tra trạng thái sync và nguồn đang được chọn, không chỉ thấy câu lệnh NTP trong config. [R17]

Ví dụ lab Cisco tự thiết kế: R1 dùng `ntp master 8` làm nguồn cục bộ để học; R2 dùng `ntp server 10.255.0.1`. Kiểm tra `show ntp associations` và `show ntp status`. Nguồn cục bộ lab không phải nguồn thời gian đáng tin cậy cho hệ thống thật. [C01][R17]

## Telemetry và log

SNMP cho phép đọc/quản lý đối tượng trên agent, thường thông qua polling và thông báo. Ưu tiên cấu hình SNMPv3 có authentication/privacy khi hệ thống hỗ trợ và chính sách yêu cầu; chỉ nói “v3” chưa xác nhận đã bật mã hóa. [R23]

Syslog có facility và severity. Severity từ 0 Emergency, 1 Alert, 2 Critical, 3 Error, 4 Warning, 5 Notice, 6 Informational đến 7 Debug. Số nhỏ hơn nghiêm trọng hơn. Cần ghi timezone, timestamp và thông tin thiết bị; log level quá rộng có thể tạo tải đáng kể. [R18]

## QoS lúc có tắc nghẽn

DSCP là dấu phân loại ở IP header, được dùng cùng chính sách để chọn cách xử lý từng chặng; không tự tạo bảo đảm end-to-end. Classification nhận diện traffic; marking gắn nhãn; queueing phục vụ hàng đợi. Policing thường drop/remark khi vượt mức; shaping đệm và điều tiết tốc độ, có thể tăng delay. [R19][C21]

Ví dụ suy luận: ưu tiên voice giúp khi uplink nghẽn, nhưng không làm cáp hỏng hết loss hay tăng băng thông vật lý. Đo queue drop/jitter trước và sau thay đổi, không gắn mọi traffic “ưu tiên cao”.

## TFTP, FTP và truy cập quản trị

TFTP là giao thức truyền file đơn giản, không có cơ chế đăng nhập/mã hóa như SSH; FTP cổ điển cũng không tự mã hóa. Dùng SFTP/SCP hoặc kênh được bảo vệ khi cần bí mật. Trong giáo trình, TFTP/FTP phục vụ nhận diện khả năng và hạn chế, không là lựa chọn mặc định cho credential. [R26][R27][C19]

## Tự kiểm tra

**Câu hỏi:** Thiết bị đã cấu hình NTP server thì có chắc clock đã đồng bộ chưa?

<details>
<summary>Xem gợi ý trả lời</summary>

Chưa. Cần kiểm tra peer được chọn, trạng thái sync và reachability; config chỉ nêu ý định.

</details>

## Nguồn của bài

- [R17] — RFC 5905 — NTPv4.
- [R18] — RFC 5424 — Syslog.
- [R19] — RFC 2474 — Differentiated Services.
- [R23] — RFC 3411 — SNMP architecture.
- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [T01] — IANA — Service names and port numbers.
- [C19] — Cisco — Configure SSH on Routers.
- [C21] — Cisco — Policing and Shaping Overview.
- [R26] — RFC 1350 — TFTP.
- [R27] — RFC 959 — FTP.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R17]: https://www.rfc-editor.org/rfc/rfc5905 "RFC 5905 — NTPv4"
[R18]: https://www.rfc-editor.org/rfc/rfc5424 "RFC 5424 — Syslog"
[R19]: https://www.rfc-editor.org/rfc/rfc2474 "RFC 2474 — Differentiated Services"
[R23]: https://www.rfc-editor.org/rfc/rfc3411 "RFC 3411 — SNMP architecture"
[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[T01]: https://www.iana.org/assignments/service-names-port-numbers/ "IANA — Service names and port numbers"
[C19]: https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html "Cisco — Configure SSH on Routers"
[C21]: https://www.cisco.com/c/en/us/td/docs/routers/ios-xe/quality-of-service/quality-of-service/m_qos-plcshp-oview-0.html "Cisco — Policing and Shaping Overview"
[R26]: https://www.rfc-editor.org/rfc/rfc1350 "RFC 1350 — TFTP"
[R27]: https://www.rfc-editor.org/rfc/rfc959 "RFC 959 — FTP"
