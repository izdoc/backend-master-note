# 17. Windows DHCP, IPAM và failover

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** 70-741: DHCP và IPAM. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Tạo scope/options trong lab; phân biệt lease HA với quản lý địa chỉ.

## Ba phần cần tách

DHCP cấp lease. IPAM quản lý không gian IP cùng thông tin DHCP/DNS tập trung, hỗ trợ discovery, provisioning và phân quyền. IPAM không thay DHCP để trả Offer cho client. RBAC, quyền truy cập server và GPO provisioning phải được chuẩn bị, không phải cài feature xong là tự quản lý toàn bộ mạng. [M09][M13]

DHCP failover cho hai Windows DHCP server chia sẻ trạng thái phục vụ scope IPv4. Có load balance và hot standby. Scope thay đổi có thể cần replicate cấu hình; không mặc định mọi thay đổi được đồng bộ như lease. DHCPv6 không dùng cơ chế failover IPv4 này. [M12]

## Lab scope tự thiết kế

Yêu cầu: Windows Server lab có IP tĩnh `10.10.20.10`, role chưa có scope VLAN10, client ở VLAN10, router có relay tới server. DHCP chỉ được nối trong mạng lab kín. [M10][M11]

```powershell
Install-WindowsFeature DHCP -IncludeManagementTools
Add-DhcpServerv4Scope -Name "VLAN10-LAB" -StartRange 10.10.10.50 -EndRange 10.10.10.150 -SubnetMask 255.255.255.0 -State Active
Set-DhcpServerv4OptionValue -ScopeId 10.10.10.0 -Router 10.10.10.1 -DnsServer 10.10.20.10 -DnsDomain "example.test"
Get-DhcpServerv4Scope
Get-DhcpServerv4Lease -ScopeId 10.10.10.0
```

Trong AD domain, thực hiện authorization bằng tài khoản có quyền và FQDN/IP đúng, ví dụ `Add-DhcpServerInDC -DnsName DHCP1.example.test -IPAddress 10.10.20.10`. Dòng này chỉ áp cho **domain lab đã tồn tại**, không áp máy standalone chưa có domain. [M10]

Kỳ vọng client nhận .50–.150, mask /24, gateway .1 và DNS 10.10.20.10. Kiểm tra lease và capture DORA, không chỉ nhìn biểu tượng mạng. Các lệnh chưa được thực thi trong lần xuất bản này.

**Hoàn tác:** xác nhận scope vừa tạo rồi `Remove-DhcpServerv4Scope -ScopeId 10.10.10.0 -Force`. Nếu đã authorize server mới của lab, bỏ authorization tương ứng; không xóa server đang phục vụ mạng thật.

## Mở rộng

Trên hai VM DHCP riêng, tạo failover cho một scope; quan sát lease khi một server dừng trong lab và khi phục hồi. Trên VM IPAM riêng, discovery server và ghi quyền/GPO cần thiết. Các bước này là bài thực hành theo tài liệu hãng, không phải cấu hình tự động đã hoàn tất. [M12][M13]

## Tự kiểm tra

**Câu hỏi:** IPAM hoạt động nhưng DHCP server đều dừng thì client mới có được IP nhờ IPAM không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. IPAM quản lý; DHCP server mới trực tiếp cấp lease. Cần thiết kế khả năng sẵn sàng của dịch vụ DHCP.

</details>

## Nguồn của bài

- [M09] — Microsoft — DHCP overview.
- [M10] — Microsoft — Install and configure DHCP Server.
- [M11] — Microsoft — Add-DhcpServerv4Scope.
- [M12] — Microsoft — DHCP failover.
- [M13] — Microsoft — IPAM.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[M09]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-top "Microsoft — DHCP overview"
[M10]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server "Microsoft — Install and configure DHCP Server"
[M11]: https://learn.microsoft.com/en-us/powershell/module/dhcpserver/add-dhcpserverv4scope "Microsoft — Add-DhcpServerv4Scope"
[M12]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/dhcp-failover "Microsoft — DHCP failover"
[M13]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/ipam/ipam-top "Microsoft — IPAM"
