# 19. Chi nhánh: DFS, BranchCache và BGP ở mức nhận diện

[Mục lục](../INDEX.md) · [Lộ trình](../ROADMAP.md) · [Nguồn học](../REFERENCES.md)

**Đối chiếu:** 70-741: Core and distributed network solutions. **Mốc rà soát:** 11/11/2026.

**Sau bài này:** Phân biệt namespace, replication và cache; biết vị trí BGP trong chương trình lịch sử.

## Ba nhu cầu khác nhau

| Nhu cầu | Công nghệ để tìm hiểu | Giới hạn cần nhớ |
|---|---|---|
| Một đường dẫn logic tới nhiều share | DFS Namespaces | Không tự nhân bản nội dung |
| Đồng bộ folder giữa server | DFS Replication | Không thay backup/version phục hồi độc lập |
| Giảm tải WAN khi đọc lại nội dung | BranchCache | Không thay file server nguồn |

DFS namespace có folder target để client được referral tới vị trí dữ liệu. Nhiều target chỉ hữu ích nếu dữ liệu và quyền được tổ chức nhất quán. [M21]

DFSR là cơ chế replication folder; topology, lịch, backlog và xung đột cần được quản lý. Một thay đổi/xóa ngoài ý muốn có thể lan sang bản sao; replication không cung cấp đầy đủ mục tiêu khôi phục như một chiến lược backup. Không dùng nó như cơ chế sao chép tùy ý cho database file đang mở. [M22]

BranchCache lưu nội dung được hỗ trợ tại chi nhánh, theo distributed cache trên client hoặc hosted cache. Quyền truy cập nội dung vẫn phải được thỏa mãn; không hiểu cache là cho phép vượt quyền. Kiểm tra edition/OS và loại content server được hỗ trợ. [M23]

## Tình huống tự thiết kế

Chi nhánh có 30 người cùng tải bộ tài liệu đào tạo qua WAN. Namespace giúp tên share ổn định, replication có thể đặt dữ liệu ở file server chi nhánh, BranchCache có thể giảm tải nội dung lặp. Chọn theo yêu cầu consistency, vận hành và đường truyền; không bật tất cả chỉ vì thấy tên trong syllabus.

Workshop: vẽ hai file server và một client; tạo namespace trỏ một target, thêm target thứ hai rồi kiểm tra referral; sau đó mới thêm replication và kiểm tra file. Ghi rõ từng bước thay đổi điều gì.

## BGP trong phạm vi lịch sử

70-741 có nội dung routing IPv4/IPv6 và BGP trong nhóm core/distributed networking. BGP trao đổi reachability theo policy giữa các hệ thống định tuyến; khác mục tiêu thực hành OSPF single-area của CCNA. Ở fundamental, nhận diện ASN, peer và route advertisement; cấu hình BGP production cần giáo trình riêng về policy, filtering và bảo vệ route. [M02][C11]

Bài này chỉ nhận diện, không tuyên bố đã phủ kỹ năng cấu hình BGP hoặc toàn bộ DFSR của kỳ thi cũ. Xem ma trận phạm vi để biết phần cần học tiếp.

## Tự kiểm tra

**Câu hỏi:** Hai folder target trong DFS Namespace có tự có dữ liệu giống nhau không?

<details>
<summary>Xem gợi ý trả lời</summary>

Không. Namespace cung cấp đường dẫn và referral; cần replication hoặc phương pháp đồng bộ được thiết kế riêng.

</details>

## Nguồn của bài

- [M21] — Microsoft — DFS Namespaces.
- [M22] — Microsoft — DFS Replication.
- [M23] — Microsoft — BranchCache.
- [M02] — Microsoft — 70-741 objective changes, April 2017.
- [C11] — Cisco — IP Routing Configuration Guide.

Các đoạn cấu hình/ví dụ và bài tập do giáo trình tự biên soạn; chưa thực thi trên Cisco/Windows trong lần xuất bản này. Xem [trạng thái kiểm chứng](../VALIDATION.md) trước thực hành.

[M21]: https://learn.microsoft.com/en-us/windows-server/storage/dfs-namespaces/dfs-overview "Microsoft — DFS Namespaces"
[M22]: https://learn.microsoft.com/en-us/windows-server/storage/dfs-replication/dfsr-overview "Microsoft — DFS Replication"
[M23]: https://learn.microsoft.com/en-us/windows-server/networking/branchcache/branchcache "Microsoft — BranchCache"
[M02]: https://download.microsoft.com/download/6/4/D/64DDF21C-C0C1-4FD0-9887-A27127A11A9A/OD_741_changes.pdf "Microsoft — 70-741 objective changes, April 2017"
[C11]: https://www.cisco.com/c/en/us/td/docs/routers/ios/config/17-x/ip-routing/b-ip-routing.html "Cisco — IP Routing Configuration Guide"
