# 17 · Quyền truy cập và bảo vệ dữ liệu nhạy cảm

[Mục lục](../INDEX.md)

## Thiết kế theo đường truy cập

Liệt kê ai có thể đọc/ghi dữ liệu qua API, job, reporting, hỗ trợ vận hành, backup và môi trường test. Không chỉ bảo vệ tài khoản ứng dụng rồi bỏ qua file export, query log hoặc bản backup trên máy cá nhân.

| Vai trò minh họa | Quyền cần có | Cách kiểm tra |
|---|---|---|
| App posting | Execute procedure posting | Direct UPDATE ledger phải bị từ chối |
| Reporting | SELECT view được giới hạn | Không đọc PII ngoài nhu cầu |
| Reconciliation worker | Ghi staging và thực thi workflow | Không sửa entry posted tùy ý |
| Migration identity | DDL trong thời gian deploy | Không dùng làm credential runtime |
| Operator | Diagnostics theo phạm vi | Hành động đặc quyền có audit |

Least privilege phải được thử bằng danh tính thật của application. Unit test gọi với sysadmin không chứng minh quyền đã cấu hình đúng. Dùng role và cấp quyền có chủ đích; hạn chế tài khoản dùng chung, quản lý secret ngoài source và xoay vòng theo quy trình.

## Các lớp mã hóa

TLS bảo vệ đường truyền khi cấu hình và xác thực certificate đúng. TDE bảo vệ data/log files ở trạng thái lưu trữ; không ngăn người đã được cấp SELECT đọc dữ liệu. Mã hóa cột hoặc ở application có thể giảm phạm vi plaintext nhưng ảnh hưởng search, index, rotation và recovery.

Lưu key/certificate backup tách khỏi dữ liệu, kiểm soát quyền và thử restore khi mất máy chủ gốc. Backup mã hóa mà mất khóa có thể không khôi phục được. Không ghi secret hoặc PII nguyên bản vào exception/SQL text nếu không cần.

## Tenant và dữ liệu định danh

Định nghĩa classification theo cột và mục đích sử dụng. Tách dữ liệu định danh khỏi dữ liệu giao dịch khi phù hợp, dùng internal ID cho join. Masking ở màn hình hữu ích nhưng không thay authorization. Hash email không salt/key vẫn có thể bị dò; tìm kiếm định danh bằng token/hash cần threat model, chuẩn hóa và chiến lược key rotation.

Nếu dùng row-level security, kiểm thử connection pooling và session context: tenant context cũ không được rò sang request sau. RLS cũng không thay mọi kiểm tra nghiệp vụ về quyền dùng account.

## Dữ liệu test

Ưu tiên dữ liệu tổng hợp. Khi bắt buộc dùng bản sao, loại/tokenize dữ liệu nhạy cảm theo quy trình được duyệt và kiểm soát export. Data masking phải giữ tính nhất quán khóa khi cần test join và vẫn giữ phân bố đủ để benchmark; thay mọi amount thành 1 làm sai đặc tính workload.

Nguồn: [Microsoft — TDE](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/transparent-data-encryption?view=sql-server-ver16). Ma trận quyền và các biện pháp bổ sung là hướng dẫn thiết kế, cần kiểm chứng theo threat model.
