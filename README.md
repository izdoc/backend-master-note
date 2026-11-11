# Backend Master Note

Tài liệu học tập của dự án **From Dev To TA**, từ nền tảng lập trình đến thiết kế kiến trúc và vận hành hệ thống.

## Clean Architecture

[Đọc bộ 15 bài: Clean Architecture từ nền tảng đến thực chiến](clean-architecture/Clean_Architecture_Tu_Nen_Tang_Den_Thuc_Chien.md)

Bộ bài bằng tiếng Việt, dùng C#/.NET và ứng dụng quản lý mượn sách BookNest làm ví dụ xuyên suốt. Mỗi bài có giải thích, ví dụ, bài tập và gợi ý đáp án.

| Bài | Nội dung |
|---|---|
| 1–4 | Kiến trúc, bốn tầng, DIP/DI, Clean, Hexagonal, Onion và DDD |
| 5–8 | Use case, Domain, Application, API và database |
| 9–10 | Kiểm thử và CQRS |
| 11–13 | Transaction, concurrency, event, outbox, idempotency và vận hành |
| 14–15 | Refactor hệ thống cũ, ADR và đồ án tổng kết |

Mã trong tài liệu phục vụ minh họa, chưa phải ứng dụng hoàn chỉnh đã được biên dịch. Nguồn tham khảo và giới hạn được ghi trong tài liệu.

## Microservices: Up and Running

[Bản tiếng Việt và toàn bộ tài nguyên sách](microservicesupandrunning_vi_1.0/).

## Nghiệp vụ và kiến trúc hệ thống chứng khoán

[Đọc bộ Securities Wiki](securities-wiki/README.md) · [Mục lục 38 bài và trang tra cứu](securities-wiki/INDEX.md)

Bộ training tiếng Việt theo 14 chuyên mục: nền tảng chứng khoán, vận hành Sở, kết nối CTCK, phòng ban, bảng giá, khớp lệnh, margin, thanh toán/đối soát, quản trị rủi ro, kiến trúc và vận hành. Có lộ trình 8 tuần, 6 workshop, 30 câu hỏi có đáp án, capstone, lab Python offline và 4 thư mục skill để cập nhật nội dung.

Mốc rà soát nguồn: 07/11/2026. Tài liệu phân biệt quy định đã xác minh, thay đổi sắp có hiệu lực và kiến trúc minh họa; xem sổ nguồn và regulatory watch trước khi áp dụng.

## Thiết kế và tối ưu cơ sở dữ liệu

[Đọc Database Engineering Wiki](database-wiki/README.md) · [Mục lục 26 bài](database-wiki/INDEX.md)

Wiki tiếng Việt theo 11 category về thiết kế dữ liệu, ledger/số dư, ngân hàng/chứng khoán/bảo hiểm, transaction/concurrency, idempotency, SQL/index/plan/statistics, partition/archive, bảo mật, backup/restore, vận hành và tích hợp .NET. Có lộ trình 8 tuần, 6 workshop, capstone, mẫu review/tuning và 5 script lab SQL Server.

Trọng tâm SQL Server 2022, có bài đối chiếu PostgreSQL 18. Mốc rà soát: 11/11/2026. Script đã được review tĩnh, chưa thực thi trên SQL Server trong lần xuất bản này; xem hướng dẫn lab và nguồn trước khi áp dụng.

## Nền tảng mạng máy tính — CCNA và Windows Server networking

[Đọc Network Fundamentals Wiki](network-fundamentals-wiki/README.md) · [Mục lục 25 bài](network-fundamentals-wiki/INDEX.md) · [Nguồn học đáng tin cậy](network-fundamentals-wiki/REFERENCES.md)

Giáo trình tiếng Việt gồm IP/subnetting/IPv6, Ethernet/VLAN/STP/LACP, routing/OSPF/NAT, DNS/DHCP/IPAM/NPS, Windows Server, Wi-Fi, bảo mật, automation và troubleshooting. Có lộ trình 8 tuần, 6 lab/workshop, 30 câu hỏi có giải thích và 60 thuật ngữ.

Đối chiếu CCNA 200-301 v1.1 và phần networking của MCSA Windows Server 2016; MCSA là hệ chứng chỉ đã nghỉ. Nguồn RFC Editor, Cisco, Microsoft và tài liệu công cụ được dẫn trong từng bài. Mốc rà soát: 11/11/2026. Lab đã rà tĩnh, chưa thực thi trên simulator/Windows Server trong lần xuất bản này; xem [phạm vi kiểm chứng](network-fundamentals-wiki/VALIDATION.md).

## Prompt Engineering và Vibe Coding cho kỹ sư phần mềm

[Đọc Prompt Engineering Wiki](prompt-engineering-wiki/README.md) · [Mục lục](prompt-engineering-wiki/INDEX.md) · [Nguồn chính thức](prompt-engineering-wiki/REFERENCES.md)

Wiki tiếng Việt cho FE, BE, Database và Infrastructure, có phần mở rộng Data Engineering. Gồm 30 tình huống coding, troubleshooting và phân tích log; mỗi tình huống có prompt sao chép, lý do thiết kế, ví dụ kết quả, tiêu chí nghiệm thu và lỗi thường gặp. Ví dụ theo React/Next.js, C#/.NET, SQL Server, Docker/Kubernetes, Terraform và pipeline/event.

Có nền tảng prompt/context/evidence, workflow vibe coding và incident, review kiến trúc/ADR, 4 mẫu tái sử dụng, rubric đánh giá, 6 workshop và capstone. Mốc đối chiếu 32 nguồn: 11/11/2026. Prompt/code/log là minh họa, chưa chạy A/B với model hoặc thực thi ứng dụng/hạ tầng; xem [phạm vi kiểm chứng](prompt-engineering-wiki/VALIDATION.md).
