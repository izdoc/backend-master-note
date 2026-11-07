# Theo dõi quy định và mốc hiệu lực

**Ngày chốt nội dung: 07/11/2026.** Đây là danh sách công việc cập nhật, không phải một tác vụ tự động đã được lên lịch.

| Mốc | Sự kiện | Trạng thái tại ngày chốt | Việc team cần chuẩn bị |
|---|---|---|---|
| 16/03/2026 | Quy chế niêm yết/giao dịch số 22 | Metadata hiện hành đã đọc, kiểm tra điều khớp liên quan | Version hóa rule; không dùng riêng bản 2025 |
| 18/03/2026 | Quy chế UPCoM số 23 | Đã xác minh metadata; chưa review toàn văn | Owner đọc toàn văn trước phê duyệt cấu hình |
| 28/05/2026 | Quy chế kết nối CNTT số 39 | Xác minh metadata | Review hồ sơ kết nối, thay đổi và nghiệm thu |
| 16/11/2026 | Thông tư 145/2026 có hiệu lực | **Sắp có hiệu lực**; các quy chế trong thông báo lấy ý kiến vẫn là dự thảo | Tìm bản cuối ban hành, impact assessment, test và training delta |
| 23/12/2026 | Ngày cuối giao dịch cổ phiếu niêm yết HNX theo kế hoạch | **Tương lai đã công bố** | Chốt danh sách mã, pending instructions và reconciliation |
| 24–25/12/2026 | Tạm ngừng các cổ phiếu HNX thuộc phạm vi chuyển | **Tương lai đã công bố** | Trạng thái theo mã, chặn lệnh điều kiện phát sai |
| 28/12/2026 | Ngày đầu giao dịch tại HOSE của cổ phiếu chuyển | **Tương lai đã công bố** | Venue mapping, tick/lot/phase, giá, chart, room và thông báo khách |

Nguồn: [S02, S11, S12, S18 trong sổ nguồn](sources.md). Không suy ra các thị trường khác do HNX tổ chức cũng ngừng trong hai ngày chuyển giao.

## Quy trình cập nhật

1. Tìm văn bản gốc và xác minh cơ quan, số, ngày, hiệu lực, phạm vi và thay thế.
2. Ghi source/evidence, xác định active, future-effective, draft hoặc unresolved.
3. Tạo bảng delta: rule cũ/mới, sản phẩm/kênh bị ảnh hưởng, ngày cutover.
4. Cập nhật bài, config, bài tập và đáp án cùng nhau; không đổi lịch sử một quyết định đã được ghi nhận.
5. Nghiệp vụ/pháp chế kiểm tra rule; QA kiểm tra scenario; IT kiểm tra mapping và recovery; Operations kiểm tra readiness.
6. Chạy kiểm tra repo và tạo commit có lý do. Cập nhật CHANGELOG.

## Điều chưa được phép kết luận từ wiki

Chưa có đủ bằng chứng để coi mọi tham số trong hướng dẫn CTCK là cấu hình production tại mọi thời điểm; chưa có đặc tả thành viên để viết gateway thật; không khẳng định CCP cơ sở, T+0 hay bán khống đã được triển khai chỉ vì KRX hoạt động. Các tham số chưa xác minh phải giữ trạng thái chưa phê duyệt, không điền bằng suy đoán.

[Danh mục](README.md) · [Trang đầu](../../README.md)
