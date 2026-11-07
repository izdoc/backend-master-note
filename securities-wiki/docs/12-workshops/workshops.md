# Sáu workshop có đầu vào và đáp án

> Bản đào tạo 1.0 • Rà soát: 07/11/2026 • Mức độ: Nền tảng → nâng cao  
> Phạm vi: kiến thức và thiết kế tham chiếu; ví dụ số liệu là giả lập. Quy tắc có ngày hiệu lực được quản lý riêng.


## Workshop 1 — Đọc bảng giá và đặt lệnh

**Đầu vào:** tham chiếu 25.000; bid 25.000×500; ask 25.100×200; last 25.050; khách có 10 triệu. Hỏi mức tăng, spread, đặt mua 300 LO 25.100 có chắc khớp hết không, tiền dự trù với phí giả lập 0,15% là bao nhiêu.

**Đáp án:** tăng 50/25.000=0,2%; spread 100; không chắc khớp hết vì lượng/giá có thể thay đổi và top ask chỉ 200; dự trù 300×25.100×1,0015=7.541.295. Không lấy last 25.050 làm giá giữ tiền của LO.

## Workshop 2 — Tính sổ khớp

**Đầu vào:** S1 bán 100@25.000 trước S2 bán 200@25.000; S3 bán 300@25.100. B1 mua 450@25.100.

**Đáp án:** 100+200+150; tổng tiền 11.265.000; S3 dư 150. Gọi lab `python3 labs/trading_lab.py`. Yêu cầu học viên đổi thứ tự S1/S2 để quan sát queue priority, đổi limit để quan sát lệnh không vượt mức giá.

## Workshop 3 — Tiền và fill trùng

**Đầu vào:** cash 10 triệu; giữ 2.003.000 cho mua 100@20.000; fill E1 60@19.900 gửi hai lần; hủy thành công 40 còn lại.

**Đáp án:** chỉ một nghĩa vụ 1.195.791 gồm phí giả lập; giải tỏa phần không dùng; số tiền chưa ràng buộc là 8.804.209 nếu không có nghĩa vụ khác. Sau settlement, cash đã ghi nợ và nghĩa vụ pending giảm tương ứng, không trừ lần hai. Nhóm phải chỉ rõ dedup marker và ledger effect nằm trong transaction nào.

## Workshop 4 — Khôi phục market data

**Đầu vào:** snapshot seq=100; delta đến theo thứ tự 101,103,102,103. Feed contract bài tập yêu cầu xử lý theo thứ tự, duplicate cùng nội dung được bỏ qua.

**Đáp án:** apply101; phát hiện gap khi 103, buffer và đánh dấu chưa đồng bộ; khi 102 đến apply102 rồi 103; duplicate103 không áp dụng lại. Nếu 103 trùng ID nhưng payload khác, báo conflict. Không đồng nhất logic này với mọi feed thật.

## Workshop 5 — Settlement và đối soát

**Đầu vào:** E1 mua 100@20.000, E2 mua 50@20.100. File nội bộ có E1 hai dòng, không có E2. Ngày T là 06/11/2026; giả sử không có ngày nghỉ đặc biệt.

**Đáp án:** báo duplicate E1 và missing E2; tổng nguồn chuẩn 3.005.000. T+2 là 10/11/2026. Không đánh dấu settled chỉ vì đã tới ngày. Lab đối soát đưa ra missing/extra/mismatched/duplicates thay vì chỉ true/false.

## Workshop 6 — Go/no-go sau DR

**Đầu vào:** web đã lên, database healthy, 30 lệnh UNKNOWN, gateway chưa khôi phục sequence, ngân hàng có 2 khoản rút đã thành công nhưng local chưa ghi.

**Đáp án:** chưa đủ điều kiện mở toàn bộ write. Fencing writer cũ, khôi phục session, reconcile external effects, giữ tiền/lệnh liên quan, xác định phạm vi dịch vụ có thể mở an toàn, người có thẩm quyền quyết định. RTO kỹ thuật đạt không đủ chứng minh RTO nghiệp vụ.

## Cách tổ chức

Mỗi nhóm 3–5 người gồm BA/dev/QA/operations. Chọn một người làm khách hàng, một người điều hành sự cố, một người kiểm tra bằng chứng. Nộp bảng số dư theo từng bước, sequence diagram, decision log và danh sách thông tin còn thiếu. Chấm tính đúng 40%, ngoại lệ 25%, bằng chứng 20%, truyền đạt 15%.


## Nguồn và phạm vi xác minh

Mã nguồn tham chiếu: DESIGN. Xem [sổ nguồn](../13-reference/sources.md). `DESIGN` là phân tích, bài tập hoặc thiết kế do bộ wiki đề xuất; không phải mô tả hạ tầng nội bộ một công ty hay đặc tả giao tiếp của Sở.

[Danh mục chuyên mục](README.md) · [Trang đầu](../../README.md)
