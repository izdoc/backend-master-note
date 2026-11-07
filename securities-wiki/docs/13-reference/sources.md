# Sổ nguồn và giới hạn xác minh

Mốc rà soát: **07/11/2026**, giờ Việt Nam. Nội dung pháp lý phải xét ngày hiệu lực, phạm vi và văn bản thay thế. Không có cam kết bộ wiki đã rà mọi sửa đổi tới từng mã/sản phẩm.

`DESIGN`: lời giải, mô hình, tình huống và kiến nghị kiến trúc do wiki xây dựng. Không gán cho công ty hay cơ quan nào. Ví dụ số tiền, phí, SLO và quy mô là giả lập. Dùng nguồn chính thức cho rule; tài liệu CTCK dùng đối chiếu cách phục vụ/giải thích khách hàng. Chỉ dẫn kỹ thuật giao tiếp phải theo tài liệu thành viên được cấp.

| ID | Nguồn | Ngày | Đã xác minh / giới hạn |
|---|---|---|---|
| S01 | [UBCKNN: vận hành chính thức KRX ngày 05/05/2025](https://ssc.gov.vn/webcenter/portal/ubck/pages_r/l/chitit?dDocName=APPSSCGOVVN1620154578) | 2025-05-05 | Đã đọc thông tin công bố; chứng minh mốc vận hành, không chứng minh mọi sản phẩm được triển khai. |
| S02 | [VNX: danh mục quy chế, gồm 22/2026, 23/2026, 39/2026](https://vnx.vn/vi/van-ban-phap-ly/6) | 2026 | Đã đọc metadata, ngày ban hành/hiệu lực và liên kết tài liệu. Không dùng listing thay toàn văn. |
| S03 | [HOSE: metadata quy chế 22 ngày 18/04/2025](https://www.hsx.vn/vi/van-ban-phap-quy/quy-che-niem-yet-va-giao-dich-chung-khoan-niem-yet/2372147) | 2025-04-18 | Nguồn lịch sử; trang động hạn chế đọc. Không dùng làm baseline hiện hành thay bản 2026. |
| S04 | [TCBS: hướng dẫn giao dịch HOSE theo KRX](https://help.tcbs.com.vn/quy-dinh-giao-dich-tai-hsx-krx/) | 2025-05-06 | Hướng dẫn của đơn vị cung cấp dịch vụ; phần lô lẻ có khác SSI và phụ lục 2026, không dùng phần đó làm căn cứ hiện hành. |
| S05 | [TCBS: hướng dẫn HNX/UPCoM theo KRX](https://help.tcbs.com.vn/quy-dinh-giao-dich-chung-khoan-tai-hnx-krx/) | 2025-05-05 | Đã đọc; tên PLO là cách gọi hướng dẫn. Ưu tiên S17 cho phiên sau giờ HNX hiện hành. |
| S06 | [SSI: FAQ KRX thị trường cơ sở](https://www.ssi.com.vn/khach-hang-ca-nhan/krx-thi-truong-co-so-faq) | Không hiện ngày ban hành trong phần đọc | Đã đọc phần thay MP, lô lẻ, sửa lệnh và ưu tiên; dùng đối chiếu trải nghiệm khách, không suy luận kiến trúc SSI. |
| S07 | [UBCKNN đăng hướng dẫn HOSE về ATO/ATC](https://ssc.gov.vn/webcenter/portal/ubck/pages_r/l/chitit?dDocName=APPSSCGOVVN1620153649) | 2025-04-11 | Tài liệu giới thiệu trước triển khai; dùng giải thích bối cảnh, đối chiếu điều 19 bản 2026 tại S16. |
| S08 | [VSDC: công bố hướng dẫn hệ thống chuyển mạch điện nghiệp vụ](https://vsdc.vn/vi/ad/192939) | 2026-03-06 | Xác nhận tồn tại hướng dẫn số 70 ngày 05/03/2026; chưa đọc toàn bộ đặc tả thành viên. |
| S09 | [VSDC: thay đổi thanh toán T+2 năm 2022](https://vsdc.vn/vi/ad/152750) | 2022-08-19 | Nguồn lịch sử giải thích T+2 và phân bổ trước phiên chiều; không thay rulebook/cutoff hiện hành của từng sản phẩm. |
| S10 | [VSDC: quy chế bù trừ thanh toán số 48/2024](https://vsdc.vn/vi/ad/176341) | 2024-11-01 | Đã đọc thông báo về non-prefunding tổ chức nước ngoài; không suy rộng cho nhà đầu tư khác. |
| S11 | [VSDC: dự thảo quy chế triển khai Thông tư 145/2026](https://vsdc.vn/vi/ad/202086) | 2026-11-02 | Đã đọc: Thông tư hiệu lực 16/11/2026; chín quy chế được thông báo lấy ý kiến là dự thảo tại bài đăng. |
| S12 | [VNX: lịch chuyển cổ phiếu niêm yết HNX sang HOSE](https://www.vnx.vn/vi/thong-tin-tu-sgdck/VNX_QLHD/10005424) | 2026-09-30 | Đã đọc thông báo lịch 23/12, 24–25/12 và 28/12/2026; là kế hoạch tương lai tại ngày rà soát. |
| S13 | [FIX Trading Community: Session Layer specification](https://www.fixtrading.org/wp-content/uploads/download-manager-files/FIX_Session_Layer_June_2020.pdf) | 2020-06 | Nguồn chuẩn khái niệm session/recovery; không phải dialect/đặc tả kết nối HOSE/HNX. |
| S14 | [BIS/CPMI-IOSCO: Principles for Financial Market Infrastructures](https://www.bis.org/cpmi/publ/d101a.pdf) | 2012-04 | Nguồn nguyên tắc quốc tế về FMI/DvP/CCP; không thay quy định Việt Nam. |
| S15 | [DNSE: thông báo chuyển đổi KRX thành công](https://www.dnse.com.vn/tin-tuc/thong-bao-chuyen-doi-he-thong-krx-thanh-cong) | 2025 | Nguồn về thông báo công khai của DNSE, không có căn cứ suy ra topology hoặc stack nội bộ. |
| S16 | [VNX: toàn văn Quy chế 22/QĐ-HĐTV ngày 16/03/2026](https://stream.vnx.vn/VNX//Legal/2026031816145088VNX.Quy-che-niem-yet_QD22.pdf) | 2026-03-16 | Đã tải bản scan 48 trang, OCR để tìm và kiểm tra trực quan điều 19, 22, 23 liên quan khớp/sửa/hủy. Chưa review toàn bộ điều khoản niêm yết. |
| S17 | [VNX: phụ lục Quy chế 22/QĐ-HĐTV ngày 16/03/2026](https://stream.vnx.vn/VNX//Legal/20260318161451415VNX.-PL-Quy-che-niem-yet_QD22.pdf) | 2026-03-16 | Đã tải bản scan 56 trang; kiểm tra phần Phụ lục III về thời gian, giao dịch và đơn vị; xem evidence map. |
| S18 | [UBCKNN: giới thiệu Thông tư 145/2026/TT-BTC](https://ssc.gov.vn/webcenter/portal/ubck/pages_r/l/chitit?dDocName=APPSSCGOVVN1620172386&dID=182825) | 2026-10-02 | Đã đọc tóm tắt: hiệu lực 16/11/2026; có phần trước/khi triển khai CCP. Không kết luận CCP cơ sở đã vận hành. |

| S19 | [VSDC: dịch vụ bù trừ và thanh toán](https://vsdc.vn/vi/sd/XAz40d2Q-9j569TvBgLQaQ) | Trang dịch vụ, truy cập 2026-11-07 | Đã đọc chu kỳ theo sản phẩm và dẫn chiếu quy chế 39/QĐ-HĐTV ngày 29/04/2025; không thay toàn văn quy chế. |
| S20 | [Microsoft: DbContext lifetime và threading](https://learn.microsoft.com/en-us/ef/core/dbcontext-configuration/) | Tài liệu trực tuyến | Đối chiếu không dùng đồng thời cùng DbContext; các kiến nghị transaction trong wiki là DESIGN. |
| S21 | [Microsoft: SQL Server table hints](https://learn.microsoft.com/en-us/sql/t-sql/queries/hints-transact-sql-table?view=sql-server-ver17) | Tài liệu trực tuyến | Đối chiếu NOLOCK/READUNCOMMITTED và dirty reads; không dùng làm bảo đảm consistency tài sản. |

## Evidence map theo quy tắc

| Quy tắc / nội dung | Nguồn ưu tiên | Vị trí | Trạng thái |
|---|---|---|---|
| ATO/ATC, lệnh sau giờ | S16 | Điều 19, PDF trang 19–21 | Đọc phần liên quan; không thay wire mapping |
| Price/time và giá liên tục/định kỳ | S16 | Điều 22, PDF trang 22–23 | Đọc và kiểm tra ảnh phần thuật toán |
| Sửa/hủy, thay đổi ưu tiên | S16 | Điều 23, PDF trang 23 | Đọc phần liên quan |
| Phiên và bước giá HOSE/HNX | S17 | Phụ lục III, PDF trang 49–54 | Kiểm tra phần liên quan |
| UPCoM có quy chế 23/2026 | S02 | Metadata và link PDF | Chưa review toàn văn 2026; bảng học cần xác nhận trước production |
| Kết nối CNTT 39/2026 | S02 | Metadata và link PDF | Chưa review toàn văn/đặc tả thành viên |
| Chu kỳ theo sản phẩm, T+2 cổ phiếu | S19; S09 cho lịch sử | Trang dịch vụ VSDC, mục I–II | Chu kỳ đã đối chiếu; cutoff/ngoại lệ phải đọc rulebook operational |
| Thông tư 145 | S11, S18 | Thông báo hiệu lực | Future-effective ở ngày 07/11/2026 |
| Chuyển HNX → HOSE | S12 | Thông báo 30/09/2026 | Lịch đã công bố, chưa xảy ra ở mốc wiki |

## Mâu thuẫn đã nhận diện

- S04 có hướng dẫn lô lẻ chưa đồng nhất với S06 và phụ lục 2026. Không dùng phần lô lẻ cũ để giới hạn giao dịch định kỳ.
- Tên PLO còn xuất hiện trong hướng dẫn khách hàng; S17 ghi lệnh giới hạn không có giá trong phiên sau giờ. Chỉ dùng mapping giao thức được chứng nhận.
- Listing pháp lý có thể gắn nhãn hiệu lực cho văn bản chưa đến ngày áp dụng; ưu tiên điều khoản hiệu lực và thông báo có ngày rõ ràng.
- Cùng số 22 hoặc 23 nhưng năm khác là văn bản khác. ID lưu trữ phải gồm cơ quan và ngày ban hành.

Bộ wiki lưu liên kết và phân tích, không sao chép toàn bộ tài liệu có bản quyền của CTCK. Tài liệu thành viên, thông tin khách hàng và cấu hình nhạy cảm không thuộc repo công khai.

[Danh mục](README.md) · [Trang đầu](../../README.md)
