# 18. AD DS, NPS/RADIUS và truy cập từ xa

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** 70-741: Connectivity/NPS; bổ trợ 70-742. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Hiểu phụ thuộc DNS của domain và chuỗi xác thực truy cập mạng.

## AD DS không phải chỉ là một bảng user

AD DS lưu đối tượng directory và cung cấp khả năng xác thực/truy cập tài nguyên theo mô hình domain. Domain controller cung cấp dịch vụ domain; Group Policy triển khai thiết lập theo thiết kế quản trị. Đây là phần bổ trợ networking từ 70-742, không thay toàn bộ giáo trình identity. [M18]

Domain client cần DNS có khả năng tìm record của AD. SRV giúp xác định dịch vụ/domain controller. Đặt DNS công cộng làm DNS trực tiếp duy nhất cho máy domain có thể làm tìm DC thất bại dù duyệt web vẫn được. [M19][M20]

Ví dụ quan sát trong domain lab đã tồn tại:

```powershell
Resolve-DnsName -Type SRV _ldap._tcp.dc._msdcs.example.test
nltest /dsgetdc:example.test
w32tm /query /status
```

Nếu chưa dựng AD cho `example.test`, không kỳ vọng các record trên tồn tại. Đồng hồ và DNS đều là phụ thuộc cần kiểm tra khi đăng nhập domain gặp lỗi. [M19][M20][R17]

## NPS và AAA

NPS là triển khai RADIUS của Microsoft. Trong ngữ cảnh NPS, **RADIUS client** thường là AP/controller/VPN gateway gửi Access-Request, không phải laptop của người dùng. Authentication kiểm tra danh tính; authorization quyết định được phép gì; accounting ghi sự kiện sử dụng. [M14]

Chuỗi ví dụ tự thiết kế: laptop → AP → NPS → kho định danh. Với EAP dùng certificate, client cần xác minh đúng chứng chỉ server, tên server và trust chain theo policy; không tắt validation như một cách khắc phục mặc định. Connection request policy và network policy giữ vai trò khác nhau trong xử lý request. [M14]

## VPN và công nghệ kế thừa

Remote-access VPN nối một client vào mạng; site-to-site VPN nối các mạng qua gateway. RRAS cung cấp các chức năng routing/remote access trên Windows Server; routing, pool cấp IP và policy chiều về đều ảnh hưởng kết nối sau khi xác thực. [M15][R20]

DirectAccess thuộc kiến thức lịch sử 70-741; Microsoft khuyến nghị dùng Always On VPN thay cho DirectAccess khi triển khai mới. Đọc DirectAccess để hiểu hệ thống cũ và học Always On VPN cho hướng hiện hành. Kiểm tra tài liệu hỗ trợ phiên bản trước triển khai. [M17][M16]

**Thực hành đề xuất:** viết sơ đồ luồng RADIUS, ghi IP/port, chứng chỉ, danh tính và log cần xem ở mỗi điểm. Không cần phơi dịch vụ domain/VPN ra Internet để học phần cơ bản.

## Tự kiểm tra

**Câu hỏi:** Trong log NPS, RADIUS client là controller hay laptop Wi-Fi?

<details>
<summary>Xem gợi ý trả lời</summary>

Thông thường là AP/controller/gateway đã cấu hình làm RADIUS client. Laptop là thiết bị/người dùng đang yêu cầu truy cập.

</details>

## Nguồn của bài

- [M14] — Microsoft — Network Policy Server.
- [M15] — Microsoft — Remote Access.
- [M16] — Microsoft — Always On VPN.
- [M17] — Microsoft — DirectAccess.
- [M18] — Microsoft — AD DS overview.
- [M19] — Microsoft — DNS and AD DS.
- [M20] — Microsoft — Verify SRV records.
- [R17] — RFC 5905 — NTPv4.
- [R20] — RFC 4301 — IPsec architecture.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[M14]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top "Microsoft — Network Policy Server"
[M15]: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/remote-access "Microsoft — Remote Access"
[M16]: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/overview-always-on-vpn "Microsoft — Always On VPN"
[M17]: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/directaccess/directaccess "Microsoft — DirectAccess"
[M18]: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/get-started/virtual-dc/active-directory-domain-services-overview "Microsoft — AD DS overview"
[M19]: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds "Microsoft — DNS and AD DS"
[M20]: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created "Microsoft — Verify SRV records"
[R17]: https://www.rfc-editor.org/rfc/rfc5905 "RFC 5905 — NTPv4"
[R20]: https://www.rfc-editor.org/rfc/rfc4301 "RFC 4301 — IPsec architecture"
