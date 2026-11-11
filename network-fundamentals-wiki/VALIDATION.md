# Phạm vi kiểm chứng

[Trang đầu](README.md) · [Mục lục](INDEX.md)

**Ngày:** 11/11/2026. Đây là báo cáo biên soạn, không phải kết quả nghiệm thu hạ tầng mạng.

## Đã kiểm tra

- Đủ 25 bài học và 6 lab, có mục tiêu, câu hỏi/đáp án hoặc tiêu chí thực hành.
- Các citation ID của bài/lab đều có nguồn URL HTTPS tương ứng.
- Đường dẫn Markdown tương đối trỏ tới file tồn tại trong bộ mới hoặc repository hiện có.
- Code fence cân bằng, có heading; JSON mẫu đúng cú pháp.
- Kiểm lại bằng phép tính IPv4: /26, /27, /28, VLSM và network/broadcast trong câu hỏi.
- Tách rõ MCSA lịch sử, Windows Server hiện hành và mức độ phủ syllabus.
- Rà tĩnh địa chỉ/cổng hai đầu, route chiều về, điều kiện AD authorization và zone parameter set.

## Chưa kiểm tra bằng thực thi

| Thành phần | Trạng thái |
|---|---|
| Packet Tracer/CML/Cisco IOS/IOS XE | Chưa chạy lab; không có file .pkt/.yaml đã nghiệm thu |
| Windows Server/AD DS/DNS/DHCP/IPAM/NPS | Chưa chạy VM hoặc cmdlet trên máy Windows |
| WLAN GUI và radio thực | Chưa kiểm thiết bị hoặc site survey |
| SDN/Ansible/Terraform | Chưa có triển khai automation; bài nhận diện nguyên lý |
| Toàn bộ URL bên ngoài | Có rà nguồn qua trang/chỉ mục chính thức; chưa HTTP-test toàn bộ 87 URL |

Môi trường soạn thảo không có simulator/VM Windows đang sẵn sàng để kiểm các lab trên. Không biến kết quả kiểm Markdown thành tuyên bố cấu hình đã chạy thành công.

## Khi chạy lab thực tế

Ghi ngày, phiên bản tool/image/OS, tên interface, topology, output trước/sau, phép thử có/không đạt, khác biệt cú pháp và cách hoàn tác. Nếu tính năng không được simulator hỗ trợ, đánh dấu **chưa kiểm chứng**, không đánh dấu đạt vì lệnh không báo lỗi.

## Duy trì chất lượng

Khi đổi bài hoặc nguồn, kiểm lại link nội bộ, phép tính bị ảnh hưởng và ma trận syllabus. Chỉ ghi “đã chạy” cho đúng platform/test case có bằng chứng. Không suy ra các image khác hoặc môi trường sản xuất đã được bảo đảm.
