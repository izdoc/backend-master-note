# 21. ACL, firewall và quản trị thiết bị

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 5.1–5.6, 5.8; 2.8, 4.8. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Viết ACL từ yêu cầu; quản trị bằng SSH và hiểu AAA.

## Viết policy trước câu lệnh

Threat là mối đe dọa, vulnerability là điểm yếu, exploit là cách khai thác, mitigation là biện pháp giảm rủi ro. Bảo vệ mạng còn gồm nhận thức người dùng, kiểm soát vật lý, quản lý mật khẩu và phương án như MFA/certificate. Đây là các nhóm kiến thức security của CCNA. [C01]

ACL thông thường xử lý từ trên xuống, dừng ở entry khớp đầu tiên và có implicit deny cuối. Standard IPv4 ACL chủ yếu xét IP nguồn; extended có thể xét protocol, nguồn/đích và port. Wildcard `0.0.0.255` trong ví dụ nghĩa không xét 8 bit cuối, khác cách đọc subnet mask. ACL stateless không tương đương stateful firewall. [C13]

## Ví dụ tự thiết kế

Yêu cầu lab: user 10.10.10.0/24 được DNS tới .20.10 và HTTPS tới .20.20, không được các kết nối khác qua interface này.

```text
ip access-list extended USERS-IN
 permit udp 10.10.10.0 0.0.0.255 host 10.10.20.10 eq 53
 permit tcp 10.10.10.0 0.0.0.255 host 10.10.20.10 eq 53
 permit tcp 10.10.10.0 0.0.0.255 host 10.10.20.20 eq 443
interface GigabitEthernet0/0.10
 ip access-group USERS-IN in
end
show access-lists USERS-IN
```

Đây là policy cố ý hẹp để học implicit deny; ping, DHCP hoặc quản trị có thể bị chặn nếu đi qua điểm lọc này. Thêm dịch vụ cần thiết theo yêu cầu trước dùng ở topology khác. Cần kiểm tra chiều về và rule ở các hop khác. Hoàn tác lab bằng `no ip access-group USERS-IN in` trên đúng interface. [C13]

## Truy cập thiết bị

Ví dụ SSH cho router lab có IP reachable; nhập secret riêng tại console, không dùng secret mẫu chung:

```text
hostname R1
ip domain-name example.test
username netadmin privilege 15 secret <NHAP_SECRET_RIENG>
crypto key generate rsa modulus 2048
ip ssh version 2
line vty 0 4
 login local
 transport input ssh
```

Placeholder phải được thay, không dán nguyên vào thiết bị. Kiểm tra cú pháp/image và cả dải VTY còn lại; áp policy truy cập quản trị theo subnet quản lý. Telnet/HTTP không mã hóa phiên như SSH/HTTPS. [C19]

AAA tách authentication, authorization, accounting; RADIUS/TACACS+ dùng theo thiết kế sản phẩm. Tránh sửa AAA từ xa khi chưa có console/đường phục hồi được kiểm chứng. [M14][C19]

## Tự kiểm tra

**Câu hỏi:** Vì sao thêm permit ở cuối ACL vẫn không làm traffic được phép?

<details>
<summary>Xem gợi ý trả lời</summary>

Có thể một deny phía trên đã khớp trước. Cần xem thứ tự, hướng gắn và counter trên đúng ACL.

</details>

## Nguồn của bài

- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [C13] — Cisco — Configure IP Access Lists.
- [C19] — Cisco — Configure SSH on Routers.
- [M14] — Microsoft — Network Policy Server.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[C13]: https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html "Cisco — Configure IP Access Lists"
[C19]: https://www.cisco.com/c/en/us/support/docs/security-vpn/secure-shell-ssh/4145-ssh.html "Cisco — Configure SSH on Routers"
[M14]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/nps/nps-top "Microsoft — Network Policy Server"
