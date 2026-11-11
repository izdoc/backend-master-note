# Network Fundamentals Wiki — CCNA và Windows Server networking

Giáo trình tiếng Việt cho người bắt đầu học mạng, developer/backend engineer và team cần nền tảng vận hành. Đi từ đường đi của request tới IP, switching, routing, dịch vụ Windows Server, bảo mật và troubleshooting.

**Bắt đầu:** [Mục lục 25 bài](INDEX.md) · [Lộ trình 8 tuần](ROADMAP.md) · [Nguồn học đáng tin cậy](REFERENCES.md)

## Khung nội dung và phiên bản

- **CCNA:** đối chiếu 200-301 **v1.1**, theo blueprint Cisco được rà ngày **11/11/2026**; trước khi đăng ký thi phải kiểm tra lại blueprint tại Cisco. [C01]
- **MCSA:** dùng phần networking của **MCSA Windows Server 2016**, trọng tâm **70-741** và một phần phụ thuộc identity của 70-742. MCSA đã ngừng cấp theo hệ thi cũ từ **31/01/2021**; đây là học kiến thức kế thừa, không phải đường thi MCSA hiện hành. [M01][M02]
- **Thực hành Windows:** hướng tới lab Windows Server 2022/2025 cho các vai trò còn phù hợp, đối chiếu trang Applies to của từng feature. DirectAccess và một số tài liệu cũ được gắn nhãn lịch sử; không tự áp nguyên mọi tính năng Server2016 sang Server mới. [M03][M17]

Wiki tập trung **fundamentals**. [Bảng đối chiếu](SYLLABUS-MAPPING.md) ghi rõ mức giải thích, cấu hình mẫu hay bài mở rộng. Các mục BGP, DNS policy/DANE, IPAM provisioning, SDN/Network Controller và high-performance networking mới được giới thiệu/định hướng; không tuyên bố thay thế toàn bộ khóa luyện thi hoặc manual sản phẩm.

## Có gì trong bộ tài liệu?

| Phần | Nội dung |
|---|---|
| 25 bài học | Khái niệm → ví dụ → lỗi dễ gặp → tự kiểm tra có đáp án |
| 6 lab/workshop | IP/packet, VLAN/LACP, routing/OSPF/IPv6/NAT, Windows DNS/DHCP, policy/WLAN và capstone |
| Tự đánh giá | 30 câu hỏi có giải thích và liên kết bài ôn |
| Tra cứu | 60 thuật ngữ và sổ nguồn theo chủ đề |
| Duy trì | Checklist học, ma trận syllabus và trạng thái kiểm chứng |

Các ví dụ địa chỉ, topology, rubric và câu hỏi **tự biên soạn**, không sao chép đề thi. Mã nguồn tài liệu ở dạng Markdown dễ đọc/sửa; trang reference cũng đọc trực tiếp trên GitHub.

## Cách học

1. Đọc bài theo mục lục, tự vẽ đường đi của một packet.
2. Làm phép tính subnet và dự đoán kết quả trước khi chạy lệnh.
3. Thực hành bằng simulator hoặc VM theo yêu cầu từng lab.
4. Chụp output, giải thích kết quả rồi chủ động tạo một lỗi để điều tra.
5. Làm [30 câu hỏi](11-assessment/01-review-questions.md), đối chiếu [đáp án](11-assessment/02-answers.md), ôn lại phần chưa giải thích được.

## Đọc nguồn như thế nào?

Các mã như [R10], [C13], [M10] là liên kết tới RFC Editor, Cisco và Microsoft, đặt gần đoạn/bảng được hỗ trợ. [REFERENCES.md](REFERENCES.md) giải thích nguồn dùng cho phần nào, giới hạn phiên bản và thứ tự đọc. RFC có thể có updates/errata; cấu hình hãng phụ thuộc platform/image, không phải tiêu chuẩn chung của mọi thiết bị.

## Trạng thái lab

Đã rà tĩnh cấu trúc, phép tính và liên kết nội bộ. **Chưa chạy lab trên Packet Tracer/CML hoặc Windows Server trong lần xuất bản này.** Các dòng kỳ vọng là tiêu chí để người học kiểm tra, không phải kết quả đã đo. Xem [VALIDATION.md](VALIDATION.md) để biết phạm vi kiểm tra và cách ghi kết quả.

[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[M01]: https://learn.microsoft.com/en-us/credentials/certifications/posts/mcsa-mcsd-mcse-certifications-retire-with-continued-investment-to-role-based-certifications "Microsoft — MCSA/MCSD/MCSE retirement"
[M02]: https://download.microsoft.com/download/6/4/D/64DDF21C-C0C1-4FD0-9887-A27127A11A9A/OD_741_changes.pdf "Microsoft — 70-741 objective changes, April 2017"
[M03]: https://learn.microsoft.com/en-us/training/paths/implement-operate-premises-hybrid/ "Microsoft Learn — Windows Server networking learning path"
[M17]: https://learn.microsoft.com/en-us/windows-server/remote/remote-access/directaccess/directaccess "Microsoft — DirectAccess"
[R10]: https://www.rfc-editor.org/rfc/rfc9293 "RFC 9293 — TCP"
[C13]: https://www.cisco.com/c/en/us/support/docs/security/ios-firewall/23602-confaccesslists.html "Cisco — Configure IP Access Lists"
[M10]: https://learn.microsoft.com/en-us/windows-server/networking/technologies/dhcp/quickstart-install-configure-dhcp-server "Microsoft — Install and configure DHCP Server"
