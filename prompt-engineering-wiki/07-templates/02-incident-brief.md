# Mẫu incident brief

[Trang chính](../README.md) · [Cơ sở phương pháp](../06-workflows/02-incident-and-logs.md)

```text
Sự cố: <expected/actual và impact biết được>.
Môi trường: <lab/SIT/UAT/PROD, version, release, scope quyền>.
Cửa sổ: <start/end/timezone; clock sync có biết không>.
Thay đổi gần nhất: <commit/config/deploy hoặc chưa biết>.
Bằng chứng: <file có line ID, stack, trace/plan đã bỏ secret>.
Thiếu dữ liệu: <sampling, truncate, logs không truy cập được>.
Hãy tạo facts/hypotheses/unknowns; mỗi hypothesis có evidence và phép kiểm.
Ưu tiên kiểm chỉ đọc; nêu lệnh, context, quyền, rủi ro và output cần che.
Chưa restart/KILL/apply/retry giao dịch thật.
Đề xuất mitigation và permanent fix riêng, kèm cách xác minh và rollback limits.
Không khẳng định root cause trước khi có evidence đủ; nguồn phải chính thức.
```

Mẫu là quy ước của wiki. Ví dụ có dữ liệu: [BE-T02](../02-backend/02-troubleshooting.md) và [INF-T01](../04-infrastructure/02-troubleshooting.md).
