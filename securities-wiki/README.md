# Wiki nghiệp vụ và kiến trúc hệ thống chứng khoán Việt Nam

Bộ training tiếng Việt dành cho team BA, QA, developer, **Senior Solution Architect** và **giám đốc nghiệp vụ chứng khoán**. Đi từ thị trường và một lệnh mua/bán đến vận hành công ty, hạ tầng kết nối, kiểm soát tài sản, kiến trúc và quản trị.

**Phiên bản 1.0 — rà soát ngày 07/11/2026.** Ví dụ dữ liệu, phí, tải và SLO là giả lập. Kiến trúc là thiết kế tham chiếu, không phải mô tả nội bộ SSI, DNSE hay TCBS. Tài liệu công khai của các công ty chỉ dùng đúng phạm vi được công bố.

## Bắt đầu

- [Lộ trình training 8 tuần](docs/00-start-here/learning-path.md).
- [Mục lục từng bài](INDEX.md).
- [Sáu workshop có đáp án](docs/12-workshops/workshops.md), [30 câu vấn đáp](docs/12-workshops/assessment.md), [capstone](docs/12-workshops/capstone.md).
- [Từ điển Việt–Anh](docs/13-reference/glossary.md).
- [Sổ nguồn và mức xác minh](docs/13-reference/sources.md), [mốc hiệu lực cần theo dõi](docs/13-reference/regulatory-watch.md).

## Categories tương ứng folder

| Folder | Nội dung |
|---|---|
| [00-start-here](docs/00-start-here/README.md) | Lộ trình và đánh giá năng lực |
| [01-market-foundations](docs/01-market-foundations/README.md) | Hệ sinh thái, sản phẩm, tài khoản, số dư, phái sinh và trái phiếu |
| [02-exchange-operations](docs/02-exchange-operations/README.md) | Ngày vận hành Sở, phiên và ruleset |
| [03-trading-and-matching](docs/03-trading-and-matching/README.md) | Loại lệnh, khớp liên tục/định kỳ/thỏa thuận, vòng đời lệnh |
| [04-broker-departments](docs/04-broker-departments/README.md) | Phòng ban, khách hàng, tiền, margin, tổ chức, tự doanh và IB |
| [05-connectivity](docs/05-connectivity/README.md) | Kết nối Sở/VSDC/ngân hàng, protocol và recovery |
| [06-market-data](docs/06-market-data/README.md) | Bảng điện, price book, snapshot/delta, fan-out |
| [07-post-trade](docs/07-post-trade/README.md) | Clearing, settlement, quyền, ledger và đối soát |
| [08-risk-and-compliance](docs/08-risk-and-compliance/README.md) | RMS, hạn mức, tuân thủ và audit |
| [09-solution-architecture](docs/09-solution-architecture/README.md) | Domain, OMS/RMS, data/API/event, .NET/SQL |
| [10-operations-and-security](docs/10-operations-and-security/README.md) | SRE, capacity, BCP/DR, bảo mật, release/migration |
| [11-leadership-and-governance](docs/11-leadership-and-governance/README.md) | Product economics, RACI, NFR, ADR, buy/build |
| [12-workshops](docs/12-workshops/README.md) | Tình huống, đáp án, assessment, capstone |
| [13-reference](docs/13-reference/README.md) | Thuật ngữ, nguồn, theo dõi quy định |

## Source dự án

| Thư mục/file | Mục đích |
|---|---|
| `docs/` | Nguồn Markdown, đọc trực tiếp trên GitHub; Mermaid cho sơ đồ |
| `skills/<name>/SKILL.md` | 4 workflow cập nhật bài, rà rule, review kiến trúc, soạn training |
| `templates/` | Mẫu bài, ADR, impact thay đổi rule và sự cố |
| `config/` | Danh mục bài, nguồn và rule minh họa có nhãn phạm vi |
| `labs/` | Mã Python offline minh họa và kiểm thử |
| `scripts/` | Tạo mục lục và kiểm tra tính toàn vẹn |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Cách cập nhật và sử dụng skill source |
| [AGENTS.md](AGENTS.md) | Quy tắc để trợ lý làm việc đúng trong dự án |

## Chạy và kiểm tra

Chỉ cần Python 3.10+; không có dependency ngoài standard library. Từ thư mục này:

```bash
python3 scripts/build_index.py
python3 scripts/validate.py
python3 labs/trading_lab.py
python3 -m unittest discover -s labs -p 'test_*.py' -v
```

Windows có thể thay `python3` bằng `py -3`. Không cần chạy server để đọc wiki. Các snippet .NET/SQL trong bài là thiết kế/pseudocode; lab Python là phần chạy được đã tách riêng.

## Giới hạn và cập nhật

Các trang đã kiểm tra tập trung vào kiến thức training và điều khoản khớp lệnh liên quan. Danh mục nguồn nêu rõ phần đọc toàn văn, phần chỉ xác minh metadata và phần chưa đủ để cấu hình production. Đặc tả giao tiếp thành viên, SOP nội bộ, biểu phí/thuế thật và phê duyệt pháp chế không nằm trong bộ source công khai này.

Thông tư 145/2026 có ngày hiệu lực 16/11/2026 và kế hoạch chuyển cổ phiếu HNX sang HOSE cuối tháng 12/2026 phải được quản lý theo ngày hiệu lực; xem regulatory watch trước khi dùng tài liệu sau các mốc đó. Đây không phải cơ chế tự cập nhật hoặc chứng nhận tuân thủ.

[Changelog](CHANGELOG.md)
