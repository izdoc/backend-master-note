# 06. Subnetting, VLSM và kế hoạch địa chỉ

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** CCNA 1.6. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Chia subnet theo nhu cầu; kiểm tra overlap và tính khả năng mở rộng.

## Cách tính

Với subnet IPv4 broadcast thông thường `/p`, số địa chỉ là `2^(32-p)`; host usable thường là số đó trừ 2. `/31` là ngoại lệ cho point-to-point theo RFC 3021; `/32` biểu diễn một địa chỉ/host route. Không áp công thức trừ 2 máy móc cho cả hai. [R04][R05]

| Prefix | Mask | Địa chỉ | Host thông thường |
|---|---|---:|---:|
| /24 | 255.255.255.0 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 14 |
| /30 | 255.255.255.252 | 4 | 2 |

Bảng là kết quả tính từ prefix. VLSM cho phép dùng các độ dài prefix khác nhau trong cùng kế hoạch địa chỉ. [R04]

## Bài giải tự thiết kế

Có `10.20.0.0/24`; cần 100 user, 50 server, 20 thiết bị quản trị và 2 địa chỉ transit. Đếm cả gateway và thiết bị dự phòng trước khi chọn prefix. Cấp khối lớn trước:

| Mục đích | Subnet | Usable | Broadcast |
|---|---|---|---|
| User | 10.20.0.0/25 | .1–.126 | .127 |
| Server | 10.20.0.128/26 | .129–.190 | .191 |
| Management | 10.20.0.192/27 | .193–.222 | .223 |
| Transit | 10.20.0.224/30 | .225–.226 | .227 |
| Dự trữ | .228–.255 | Chưa cấp | Chưa phải một subnet duy nhất |

Transit dùng /30 để dễ mô phỏng; chỉ chuyển /31 khi hai đầu hỗ trợ và liên kết thực sự point-to-point. [R05]

## Summary và overlap

Có thể gộp các prefix liền nhau **và đúng alignment**. Hai /24 `10.30.0.0/24` và `10.30.1.0/24` gộp thành `10.30.0.0/23`. Hai mạng `10.30.1.0/24` và `10.30.2.0/24` không gộp chính xác thành một /23. Summary quảng bá cả không gian trong nó; thiết kế phải xử lý phần chưa dùng. [R04]

**Checklist do giáo trình đề xuất:** không overlap giữa site/VPN/cloud, có block dự trữ, ghi owner/VLAN/gateway/DHCP range, tránh cấp động đè IP tĩnh. Không để nhớ bằng đầu thay cho IP plan.

## Tự kiểm tra

**Câu hỏi:** Cần 30 PC và một gateway thì /27 đã đủ chưa?

<details>
<summary>Xem gợi ý trả lời</summary>

Chưa. /27 có 30 host usable, trong khi cần ít nhất 31 địa chỉ. Chọn /26 nếu yêu cầu không thay đổi.

</details>

## Nguồn của bài

- [R04] — RFC 4632 — CIDR.
- [R05] — RFC 3021 — IPv4 /31.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[R04]: https://www.rfc-editor.org/rfc/rfc4632 "RFC 4632 — CIDR"
[R05]: https://www.rfc-editor.org/rfc/rfc3021 "RFC 3021 — IPv4 /31"
