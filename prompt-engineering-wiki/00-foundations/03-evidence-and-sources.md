# Bằng chứng, trích nguồn và điều chưa biết

[Trang chính](../README.md) · [Sổ nguồn](../REFERENCES.md)

Google SRE trình bày troubleshooting dựa trên quan sát, giả thuyết và thử nghiệm. Wiki áp dụng bằng bảng kiểm chứng để kết luận có thể đối chiếu. [SRE](https://sre.google/sre-book/effective-troubleshooting/)

## Ba loại thông tin trong wiki

| Loại | Ví dụ | Cách ghi |
|---|---|---|
| Kiến thức từ nguồn | DbContext không hỗ trợ thao tác song song cùng instance | Link Microsoft ngay cạnh nhận định |
| Quy ước biên soạn | Task brief gồm 6 phần | Ghi là quy ước của wiki |
| Dữ liệu giả lập | API p95=1400ms, log request=r1 | Ghi demo; không gọi là benchmark |

Một link có thật chưa chứng minh một câu đúng. Mở đúng trang, tìm đoạn hỗ trợ nhận định, kiểm tra phiên bản/phạm vi, rồi diễn giải ngắn. Nếu không truy cập được thì ghi chưa xác minh; không tạo link trông giống docs.

## Prompt bắt buộc đối chiếu

```text
Với mỗi đề xuất kỹ thuật, ghi:
- evidence: dòng log/file hoặc đoạn tài liệu hỗ trợ;
- scope: phiên bản và điều kiện áp dụng;
- uncertainty: điều chưa biết;
- verification: phép kiểm có thể bác bỏ giả thuyết.
Ưu tiên tài liệu nhà cung cấp, RFC hoặc dự án chính thức.
Nếu không có khả năng mở web, đừng nói đã xác minh tài liệu hôm nay.
```

Ví dụ tự biên soạn: log ghi HTTP 500 là fact; “DB down” là hypothesis; trạng thái DB chưa được đọc là unknown. Không dùng mức confidence do model tự chấm như xác suất đã được hiệu chuẩn.

## Khi các nguồn khác nhau

So sánh version, ngày cập nhật, kiểu triển khai và default bị override. Tài liệu latest có thể khác phiên bản trong lockfile. Với SQL Server, kiểm thêm engine/compatibility; với Next.js, phân biệt router; với infra, phân biệt provider/CLI và config thực tế. Xin đúng file trước khi đổi giải pháp.

## Cập nhật định kỳ theo nhu cầu

Khi đổi framework/model/tool, mở lại các nguồn có liên quan, ghi ngày đối chiếu và rerun case thất bại trước đó. Không tự động tuyên bố wiki luôn cập nhật chỉ vì URL là latest. [Quy trình đóng góp](../CONTRIBUTING.md) quy định bằng chứng cần lưu.

## Nguồn

- [SRE: Google SRE — Effective Troubleshooting](https://sre.google/sre-book/effective-troubleshooting/) — Quan sát, giả thuyết và thử nghiệm để loại trừ nguyên nhân.
