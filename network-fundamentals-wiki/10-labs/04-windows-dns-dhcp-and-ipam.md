# Lab 04 — Windows DNS/DHCP và bài mở rộng domain/IPAM

[Mục lục](../INDEX.md) · [Bảng đối chiếu](../SYLLABUS-MAPPING.md)

**Thời lượng gợi ý:** 2–3 giờ cơ bản; bài mở rộng cần thêm phiên lab.
**Môi trường:** một Windows Server 2022/2025 và một Windows client có quyền quản trị, nối cùng virtual switch **Internal/Private**. Không nối DHCP lab ra mạng công ty. Tạo checkpoint trước khi bắt đầu.

Packet Tracer mô phỏng thiết bị, không tự nối các VM Windows bên ngoài vào topology. Muốn kết hợp Cisco thực/ảo với VM cần nền tảng/bridge được hỗ trợ; lab này dùng riêng virtual switch Windows. Chưa chạy các lệnh dưới đây trong phiên xuất bản.

## A. Chuẩn bị IP tĩnh

Server tên DNSDHCP1, NIC lab `Ethernet`, địa chỉ 10.10.20.10/24; client để DHCP. Không cần gateway cho hai máy cùng subnet và không truy cập bên ngoài. Kiểm tra `Get-NetAdapter` để thay alias cho đúng.

Trên VM mới chưa có IPv4 tĩnh xung đột:

```powershell
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 10.10.20.10 -PrefixLength 24
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses 10.10.20.10
Get-NetIPConfiguration
```

Không thêm IP trùng hoặc bỏ địa chỉ của NIC đang dùng remote management; thao tác tại console VM. [M27]

## B. DNS file-backed

```powershell
Install-WindowsFeature DNS -IncludeManagementTools
Add-DnsServerPrimaryZone -Name "example.test" -ZoneFile "example.test.dns"
Add-DnsServerResourceRecordA -ZoneName "example.test" -Name "api" -IPv4Address "10.10.20.20"
Resolve-DnsName api.example.test -Server 10.10.20.10
```

Kỳ vọng A record .20.20. Chưa có API ở địa chỉ đó cũng không ảnh hưởng việc DNS trả record. Không dùng `-ReplicationScope` trong lab standalone này; tham số đó thuộc cấu hình AD-integrated phù hợp. [M07][M08]

## C. DHCP cùng subnet

Tạo scope **20.0**, khác scope VLAN10 trong bài17:

```powershell
Install-WindowsFeature DHCP -IncludeManagementTools
Add-DhcpServerv4Scope -Name "SERVERLAN-LAB" -StartRange 10.10.20.50 -EndRange 10.10.20.100 -SubnetMask 255.255.255.0 -State Active
Set-DhcpServerv4OptionValue -ScopeId 10.10.20.0 -DnsServer 10.10.20.10 -DnsDomain "example.test"
Get-DhcpServerv4Scope
```

Standalone/workgroup lab không thực hiện AD authorization. Nếu VM đã join domain, dùng quy trình authorization của Microsoft với tài khoản có quyền; không bỏ qua trạng thái authorization. [M10][M11]

Trên client, thử `ipconfig /release`, `ipconfig /renew`, `ipconfig /all` tại console. Hai lệnh release/renew làm gián đoạn địa chỉ tạm thời; đây là client lab riêng. Kỳ vọng IP .50–.100, DNS .10, không có gateway do lab không cần ra ngoài.

Trên server xem `Get-DhcpServerv4Lease -ScopeId 10.10.20.0`; trên client thử `Resolve-DnsName api.example.test`. Ghi rõ kiểm tra dùng DNS nhận từ DHCP.

## D. Lỗi có chủ đích

Sửa DNS option trong scope sang địa chỉ không chạy DNS, renew client rồi quan sát: ping server bằng IP có thể vẫn được, phân giải tên thất bại. Khôi phục option .10, renew, xác nhận. Không bật forwarder Internet để che lỗi local DNS.

## E. Bài mở rộng tách riêng

- **AD DS:** dựng domain trong checkpoint/lab khác; kiểm tra SRV và `nltest /dsgetdc:<domain>`, so sánh secure dynamic update với file-backed zone. [M19][M20]
- **Failover:** thêm server thứ hai, tạo relationship cho scope IPv4, ghi partner state và lease trước/sau dừng một server trong lab. [M12]
- **IPAM:** dùng VM member server riêng, triển khai theo tài liệu IPAM, ghi discovery/provisioning/GPO và quyền cần thiết. Không cài chồng mọi role vào DC chỉ để giảm VM. [M13]

Ba mục này là nhiệm vụ học tiếp theo tài liệu hãng, không phải runbook đầy đủ đã kiểm chứng.

## Hoàn tác và nộp bài

Xóa scope mới `Remove-DhcpServerv4Scope -ScopeId 10.10.20.0 -Force`, xóa zone lab mới `Remove-DnsServerZone -Name "example.test" -Force`, hoặc phục hồi checkpoint. Không dùng lệnh đó nếu tên/scope đã tồn tại trước lab.

Nộp ảnh server role, IP client, lease, DNS answer, packet DORA nếu capture và nhật ký lỗi/khôi phục.

## Nguồn dùng cho lab

- [M07] — Microsoft — Install DNS Server.
- [M08] — Microsoft — Add-DnsServerPrimaryZone.
- [M10] — Microsoft — Install and configure DHCP Server.
- [M11] — Microsoft — Add-DhcpServerv4Scope.
- [M12] — Microsoft — DHCP failover.
- [M13] — Microsoft — IPAM.
- [M19] — Microsoft — DNS and AD DS.
- [M20] — Microsoft — Verify SRV records.
- [M27] — Microsoft — New-NetIPAddress.

[M07]: https://learn.microsoft.com/en-us/windows-server/networking/dns/quickstart-install-configure-dns-server "Microsoft — Install DNS Server"
[M08]: https://learn.microsoft.com/en-us/powershell/module/dnsserver/add-dnsserverprimaryzone "Microsoft — Add-DnsServerPrimaryZone"
[M10]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server "Microsoft — Install and configure DHCP Server"
[M11]: https://learn.microsoft.com/en-us/powershell/module/dhcpserver/add-dhcpserverv4scope "Microsoft — Add-DhcpServerv4Scope"
[M12]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-failover "Microsoft — DHCP failover"
[M13]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top "Microsoft — IPAM"
[M19]: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/dns-and-ad-ds "Microsoft — DNS and AD DS"
[M20]: https://learn.microsoft.com/en-us/troubleshoot/windows-server/networking/verify-srv-dns-records-have-been-created "Microsoft — Verify SRV records"
[M27]: https://learn.microsoft.com/en-us/powershell/module/nettcpip/new-netipaddress "Microsoft — New-NetIPAddress"
