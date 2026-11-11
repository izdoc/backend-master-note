# Lab 06 — Capstone mạng cho hệ thống backend

[Mục lục](../INDEX.md) · [Bảng đối chiếu](../SYLLABUS-MAPPING.md)

**Thời lượng gợi ý:** 4–6 giờ. Đây là bài thiết kế độc lập do giáo trình đề xuất, không phải kiến trúc nội bộ của tổ chức nào.

## Bối cảnh

Một team có user office, server API, database và mạng quản trị. Chi nhánh cần truy cập API; khách Wi-Fi chỉ được ra vùng dịch vụ công cộng trong mô hình lab. Team cần phân biệt lỗi DNS, route, TLS và ứng dụng.

## Đầu ra bắt buộc

1. IP plan: block tổng, subnet/VLAN, gateway, IP tĩnh, DHCP range, phần dự trữ.
2. Topology: thiết bị/cổng, uplink, trunk, port-channel, vị trí routing/firewall.
3. Policy matrix có nguồn/đích/protocol/port/lý do.
4. DNS/DHCP plan: zone/record, options, relay nếu khác subnet, đường về.
5. Kế hoạch quản trị/log/time: subnet quản lý, SSH, NTP, syslog và backup config.
6. Biên bản kiểm tra với ít nhất 8 phép thử, một fault injection và rollback.

Nhóm kiến thức đối chiếu CCNA/Windows Server ở [C01][M03]. Các ngưỡng và địa chỉ cụ thể là quyết định của người làm bài.

## Policy minh họa để bắt đầu

| Nguồn | Đích | Dịch vụ | Kỳ vọng |
|---|---|---|---|
| User | API | HTTPS 443 | Cho phép |
| User | Database | TCP port DB đã chọn | Chặn |
| API | Database | TCP port DB đã chọn | Cho phép |
| Management | Router/switch | SSH 22 | Cho phép có kiểm soát |
| Guest | Management/DB | Mọi traffic thử nghiệm | Chặn |
| Client nội bộ | DNS đã chọn | UDP/TCP 53 | Cho phép |

Cần bổ sung DHCP, NTP và policy chiều về đúng topology. Không mở “any any” để đạt ping.

## Hai mức triển khai

**Mức mô phỏng:** Packet Tracer cho VLAN/routing/OSPF/NAT/ACL/WLAN; dùng server mô phỏng. Nộp file topology và output. Không ghi đã kiểm Windows Server/NPS nếu chưa chạy VM.

**Mức VM:** dựng DNS/DHCP thật theo Lab04, client và backend thử nghiệm; router/firewall ảo có hỗ trợ nối virtual networks. Không yêu cầu trả phí license hoặc phơi lab công khai để hoàn thành mức mô phỏng.

## Ma trận phép thử tối thiểu

| Phép thử | Chứng cứ |
|---|---|
| Client nhận đúng IP/options | IP config + DHCP lease |
| Tên API đúng IP | DNS answer từ server chỉ định |
| VLAN khác nhau cần router | Route + gateway |
| User truy cập API | TCP/HTTP theo khả năng lab |
| User không vào DB | ACL/firewall counter và phép thử cổng |
| API vào DB | Listener + phép thử dịch vụ phù hợp |
| Mất một uplink | Port-channel/STP trước và sau |
| DNS option sai rồi khôi phục | Triệu chứng + log thay đổi |

Thay bài test DB bằng một TCP listener thử nghiệm được quản lý nếu chưa có database. Ghi rõ phạm vi phép thử.

## Rubric do giáo trình đề xuất

- Địa chỉ và không overlap: 20 điểm.
- L2/L3 và khả năng giải thích đường đi: 25 điểm.
- Dịch vụ và chính sách: 25 điểm.
- Chứng cứ, xử lý lỗi và rollback: 20 điểm.
- Tài liệu và nguồn: 10 điểm.

Mốc 80/100 chỉ là tiêu chí nội bộ của wiki, không chuyển đổi sang điểm đậu Cisco/Microsoft.

## Mẫu báo cáo

```markdown
# Báo cáo capstone
- Ngày, người thực hiện, simulator/OS/image:
- Mục tiêu và giới hạn:
- IP plan và topology:
- Nguồn đã dùng (URL, phiên bản):
- Bảng trước/sau của từng phép thử:
- Lỗi chủ động, giả thuyết, bằng chứng:
- Thay đổi đã áp và cách hoàn tác:
- Điều đã xác minh / chưa xác minh:
```

Capture và screenshot chỉ lấy dữ liệu lab; lưu đủ timestamp và điểm đo để người khác đánh giá lại. [T02]

## Nguồn dùng cho lab

- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [M03] — Microsoft Learn — Windows Server networking learning path.
- [T02] — Wireshark — User Guide.

[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[M03]: https://learn.microsoft.com/en-us/training/paths/implement-operate-premises-hybrid/ "Microsoft Learn — Windows Server networking learning path"
[T02]: https://www.wireshark.org/docs/wsug_html/ "Wireshark — User Guide"
