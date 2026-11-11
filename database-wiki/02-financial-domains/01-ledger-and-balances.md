# 06 · Ledger, bút toán và số dư

[Mục lục](../INDEX.md) · [Lab posting](../10-labs/README.md)

## Phân biệt nguồn và bản tổng hợp

Ledger ghi lịch sử biến động đã hạch toán. Balance là projection phục vụ đọc nhanh. Chỉ lưu một cột balance mà không có lịch sử đầy đủ sẽ khó giải thích tiền đến từ đâu, retry gây gì và sửa sai bằng cách nào.

Một mô hình có `Journal` là chứng từ, `Entry` là từng dòng tài khoản, `Account` là tài khoản sổ cái hoặc sổ phụ. Hạch toán kép yêu cầu tổng Nợ bằng tổng Có trên đơn vị cân bằng đã quy định. Bản entry có signed amount trong lab chỉ minh họa chuyển giữa hai ví cùng currency; đó không phải toàn bộ chart of accounts hay mô hình kế toán pháp định.

## Các invariant cần thực thi

1. Journal đã posted không được có dưới hai entry trong mô hình lab.
2. Tổng signed amount bằng 0 theo currency của journal.
3. Entry chỉ vào account hợp lệ, cùng tenant/currency.
4. Posting, balance projection và idempotency cùng commit.
5. Không sửa/xóa lịch sử posted qua quyền ứng dụng thông thường.

`CHECK` từng dòng không kiểm tra được tổng các entry. Giải pháp thiết kế: chỉ cấp quyền execute procedure posting, thu hồi direct DML, validate toàn bộ tập entry trong transaction trước khi chuyển trạng thái. Invariant vẫn phải được đối soát định kỳ và kiểm thử với nhiều writer. Admin quyền cao là một trust boundary khác, cần audit độc lập.

## Số dư không chỉ một loại

| Loại | Mục đích |
|---|---|
| Book balance | Giá trị đã hạch toán |
| Hold/reserved | Tiền bị giữ cho nghĩa vụ chưa kết thúc |
| Available | Khả năng sử dụng theo sản phẩm |
| Pending | Giao dịch chưa đạt trạng thái chốt |

Công thức lab đơn giản: available = book − active holds. Margin, thấu chi, hạn mức, nghĩa vụ chưa thanh toán và quy tắc FX có thể thay đổi công thức; cần phiên bản hóa rule. Không lấy công thức ví điện tử áp dụng nguyên xi cho tài khoản chứng khoán margin.

## Reversal và rebuild

Sửa giao dịch bằng journal đảo có `ReversesJournalId`, sau đó journal mới nếu cần. Cần kiểm soát chỉ đảo một lần hoặc giới hạn tổng partial reversal không vượt gốc. Gắn lý do, người phê duyệt và liên kết gốc. Tách quyền yêu cầu/phê duyệt nếu nghiệp vụ cần maker-checker.

Balance rebuild phải đọc ledger tại một mốc nhất quán. Nếu rebuild trong lúc writer đang chạy, cần snapshot/cutover protocol; không ghi đè projection bằng tổng cũ. Khi có opening balance, coi đó là bút toán mở sổ hoặc thành phần được ghi nguồn rõ.

**Tình huống review:** balance là 100 nhưng entry chỉ giải thích được 90. Không “UPDATE thêm 10 cho khớp”. Xác định mốc, giao dịch thiếu, opening balance, rounding và writer ngoài procedure trước khi lập adjustment có phê duyệt.
