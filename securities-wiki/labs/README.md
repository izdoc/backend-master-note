# Lab offline

Yêu cầu: Python 3.10+; chỉ dùng standard library, không cần API key hay tài khoản chứng khoán.

Từ thư mục `securities-wiki`:

```bash
python3 labs/trading_lab.py
python3 -m unittest discover -s labs -p 'test_*.py' -v
```

Trên Windows có thể thay `python3` bằng `py -3`.

| Bài | Hàm/class | Phạm vi |
|---|---|---|
| Khớp liên tục | `Book` | LO, integer price, price-time; không có tick/lot/room/phase thực tế |
| Định kỳ | `auction_candidates` | Chỉ cực đại khối lượng; không đầy đủ điều 22, không ATO/ATC/tie-break venue |
| Giữ sức mua | `ReservationWallet` | Đồng thời trong một process và retry; không persistence hay thanh toán |
| T+2 | `settlement_date` | Tính ngày theo lịch truyền vào; không xác nhận settlement |
| Đối soát | `reconcile` | Khóa đã được scope theo ngày/venue; tìm thiếu/thừa/trùng/sai |

Demo kỳ vọng: 3 fills, tổng tiền 11.265.000; ứng viên giá 101 với lượng 400; T+2 giả lập 10/11/2026; báo thiếu E2 và trùng E1.

Wallet lưu kết quả của ý định ban đầu. Retry một key đã giải tỏa trả kết quả nhận yêu cầu cũ và không giữ tiền lại; đây không phải API truy vấn trạng thái hiện tại. Sản phẩm thật phải trả resource/status rõ ràng và có journal bền vững. Lệnh hủy/timeout không được tự gọi `release_confirmed` khi chưa có bằng chứng.

Không kết nối mạng, không đặt lệnh thật. Kết quả test chứng minh hành vi của mô hình bài học, không phải chứng nhận hệ thống giao dịch production.

[Workshop](../docs/12-workshops/workshops.md) · [Trang đầu](../README.md)
