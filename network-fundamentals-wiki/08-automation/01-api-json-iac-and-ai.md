# 24. REST API, JSON, automation và AI trong vận hành mạng

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 6.1–6.7. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Đọc JSON và HTTP; biết vai trò Ansible/Terraform và giới hạn AI.

## Từ CLI thủ công đến automation

Automation giúp làm lặp lại cấu hình và kiểm tra theo quy trình. Controller-based networking tập trung một phần điều khiển/policy qua controller; không đồng nghĩa mọi quyết định forwarding đều chạy trong controller. Underlay/overlay và northbound/southbound API cần được phân biệt như bài 20. [C01][M26]

REST-based API thường dùng HTTP và resource; GET đọc, POST xử lý/tạo theo API, PUT thay biểu diễn, PATCH sửa một phần theo định nghĩa API, DELETE xóa. Không suy mọi endpoint đều đúng CRUD chỉ dựa tên URL. Kiểm tra status, schema, pagination và cơ chế authentication. HTTPS bảo vệ kênh, còn quyền vẫn do hệ thống kiểm soát. [R21]

## JSON dễ đọc, vẫn phải đúng schema

Ví dụ inventory tự thiết kế, **không phải payload của Cisco API cụ thể**:

```json
{
  "hostname": "R1",
  "managementIp": "10.10.99.1",
  "enabled": true,
  "vlans": [10, 20],
  "description": null
}
```

Object dùng cặp key/value; array giữ danh sách; `true` là boolean khác chuỗi `"true"`. JSON chuẩn không cho comment hay trailing comma. Chuỗi IP không tự được xác minh là IP chỉ vì nó nằm trong JSON. [R22]

## Công cụ có vai trò khác nhau

Ansible dùng inventory/playbook/module để tự động hóa tác vụ trên thiết bị qua transport phù hợp. Idempotency phụ thuộc module và tác vụ, không phải cứ dùng YAML là tự an toàn. [T06]

Terraform dùng cấu hình khai báo và provider, có state và bước plan để xem thay đổi dự kiến. State có thể chứa dữ liệu nhạy cảm; không commit state/secret lên repository công khai. Một plan phải được xem trong ngữ cảnh hiện trạng và provider, không là bằng chứng thay đổi sẽ không gây gián đoạn. [T07]

## AI: biết dùng và biết kiểm chứng

Theo khung v1.1, cần phân biệt generative AI, predictive AI và machine learning trong vận hành. Generative AI có thể gợi ý giải thích/config; predictive model có thể dự báo bất thường từ dữ liệu. Đây là ví dụ ứng dụng, không phải bảo đảm chất lượng. [C01]

Quy trình do giáo trình đề xuất: lấy trạng thái read-only → tạo candidate diff → kiểm schema/cú pháp → lab → review → áp có rollback → đo sau đổi. Không đưa secret hoặc capture khách hàng vào công cụ chưa được phép. Đọc thêm lab chính thức DevNet theo API/image mình dùng. [T05]

## Tự kiểm tra

**Câu hỏi:** JSON đúng cú pháp có đồng nghĩa API sẽ chấp nhận cấu hình không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Cần đúng schema, kiểu dữ liệu, quyền, trạng thái thiết bị và ràng buộc nghiệp vụ của API.

</details>

## Nguồn của bài

- [C01] — Cisco — CCNA 200-301 v1.1 exam topics.
- [M26] — Microsoft — Software Defined Networking.
- [R21] — RFC 9110 — HTTP semantics.
- [R22] — RFC 8259 — JSON.
- [T05] — Cisco DevNet Learning Labs.
- [T06] — Ansible — Network Getting Started.
- [T07] — HashiCorp — Terraform intro.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[C01]: https://learningcontent.cisco.com/documents/marketing/exam-topics/200-301-CCNA-v1.1.pdf "Cisco — CCNA 200-301 v1.1 exam topics"
[M26]: https://learn.microsoft.com/en-us/previous-versions/azure/azure-local/concepts/software-defined-networking "Microsoft — Software Defined Networking"
[R21]: https://www.rfc-editor.org/rfc/rfc9110 "RFC 9110 — HTTP semantics"
[R22]: https://www.rfc-editor.org/rfc/rfc8259 "RFC 8259 — JSON"
[T05]: https://developer.cisco.com/learning/ "Cisco DevNet Learning Labs"
[T06]: https://docs.ansible.com/projects/ansible/latest/network/getting_started/index.html "Ansible — Network Getting Started"
[T07]: https://developer.hashicorp.com/terraform/intro "HashiCorp — Terraform intro"
