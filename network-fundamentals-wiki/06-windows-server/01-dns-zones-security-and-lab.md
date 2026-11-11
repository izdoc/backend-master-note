# 16. Windows DNS: zone, record và bảo vệ phân giải tên

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** 70-741: DNS; CCNA 4.3. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Chọn zone type, tạo record lab và hiểu cập nhật DNS an toàn.

## Không phải mọi DNS zone đều giống nhau

Primary zone có bản ghi có thể quản lý trực tiếp. Secondary giữ bản sao read-only qua zone transfer. Stub giữ thông tin giúp tìm authoritative servers, không phải toàn bộ record như secondary. AD-integrated zone lưu trong AD DS, dùng replication của AD và có thể cho secure dynamic update. File-backed primary trên standalone server không có đầy đủ đặc tính đó. [M06]

Forwarder gửi câu hỏi tới resolver khác; conditional forwarder chỉ áp cho namespace đã chỉ định. Delegation chuyển trách nhiệm một nhánh namespace; root hints giúp tìm root servers khi thực hiện phân giải đệ quy. Không dùng các từ này thay thế nhau. [M05]

## Các mục bảo vệ cần hiểu

Theo khung 70-741, cần nhận diện DNSSEC, cache locking, socket pool, Response Rate Limiting, DNS policies và logging. DNSSEC giúp kiểm tra tính xác thực/toàn vẹn dữ liệu, không mã hóa query. Secure dynamic updates cần thiết kế quyền và định danh; scavenging xóa record stale dựa trên aging, không được bật mà chưa hiểu bản ghi nào sẽ chịu ảnh hưởng. [M02][M04]

## Lab độc lập trên member/standalone server

Yêu cầu: Windows Server 2022/2025 lab, Administrator, NIC nội bộ IP tĩnh `10.10.20.10/24`; không có DNS zone `example.test` sẵn. Cú pháp dưới đây tạo **file-backed zone**, không dựng domain hay AD-integrated zone. [M07][M08]

```powershell
Install-WindowsFeature DNS -IncludeManagementTools
Add-DnsServerPrimaryZone -Name "example.test" -ZoneFile "example.test.dns"
Add-DnsServerResourceRecordA -ZoneName "example.test" -Name "api" -IPv4Address "10.10.20.20"
Resolve-DnsName api.example.test -Server 10.10.20.10
```

Địa chỉ và tên là ví dụ tự thiết kế; lệnh chưa được thực thi trong lần xuất bản này. Kỳ vọng câu trả lời A là `10.10.20.20`. Kết quả này chỉ xác nhận phân giải, chưa xác nhận API đang listen.

**Hoàn tác lab:** sau khi xác nhận đúng zone vừa tạo, dùng `Remove-DnsServerZone -Name "example.test" -Force`. Chỉ xóa zone mới của lab; không chạy vào zone đang dùng.

## Bài thực hành bổ sung

Tạo reverse zone và PTR phù hợp, giảm TTL trong lab rồi so sánh cache trước/sau sửa record. Với domain lab riêng, so sánh AD-integrated zone và secure updates; không ghép command tạo domain vào lab standalone này. [M05][M06]

## Tự kiểm tra

**Câu hỏi:** Có secondary DNS thì đã bảo đảm record trên primary cập nhật ngay lập tức ở mọi client chưa?

<details>
<summary>Xem gợi ý trả lời</summary>

Chưa. Cần xét zone transfer/refresh và cache TTL của resolver/client; secondary availability khác tính tức thời của mọi bản sao.

</details>

## Nguồn của bài

- [M02] — Microsoft — 70-741 objective changes, April 2017.
- [M04] — Microsoft — DNS overview.
- [M05] — Microsoft — DNS architecture.
- [M06] — Microsoft — DNS zones.
- [M07] — Microsoft — Install DNS Server.
- [M08] — Microsoft — Add-DnsServerPrimaryZone.
- [R13] — RFC 1034 — DNS concepts.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[M02]: https://download.microsoft.com/download/6/4/D/64DDF21C-C0C1-4FD0-9887-A27127A11A9A/OD_741_changes.pdf "Microsoft — 70-741 objective changes, April 2017"
[M04]: https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-top "Microsoft — DNS overview"
[M05]: https://learn.microsoft.com/en-us/windows-server/networking/dns/dns-architecture "Microsoft — DNS architecture"
[M06]: https://learn.microsoft.com/en-us/windows-server/networking/dns/zone-types "Microsoft — DNS zones"
[M07]: https://learn.microsoft.com/en-us/windows-server/networking/dns/quickstart-install-configure-dns-server "Microsoft — Install DNS Server"
[M08]: https://learn.microsoft.com/en-us/powershell/module/dnsserver/add-dnsserverprimaryzone "Microsoft — Add-DnsServerPrimaryZone"
[R13]: https://www.rfc-editor.org/rfc/rfc1034 "RFC 1034 — DNS concepts"
