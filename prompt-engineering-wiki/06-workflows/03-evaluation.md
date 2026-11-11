# Đánh giá prompt và kết quả code

[Trang chính](../README.md) · [Bài tập](../08-workshops/01-exercises.md)

OpenAI khuyến nghị eval theo nhiệm vụ, dùng trường hợp thực tế và kết hợp đánh giá con người. Không nên coi cảm giác “có vẻ chạy được” là cách đánh giá duy nhất. [OAI-E](https://developers.openai.com/api/docs/guides/evaluation-best-practices)

## Rubric do wiki đề xuất

Chấm mỗi tiêu chí 0/1/2: 0=không đạt, 1=một phần, 2=đạt với evidence. Đây là thang học tập nội bộ, chưa được hiệu chuẩn nghiên cứu.

| Tiêu chí | 2 điểm khi |
|---|---|
| Đúng nhiệm vụ | Đúng contract và acceptance criteria |
| Đủ căn cứ | Facts nối được với line/file/source; unknown không bị điền bừa |
| Đúng phiên bản | API/command khớp dependency/config thực tế |
| Kiểm chứng | Có repro/test thích hợp và ghi chính xác đã chạy/chưa chạy |
| Giới hạn | Không rò secret hoặc thao tác ngoài scope |
| Khả năng review | Patch nhỏ, giải thích tác động và việc còn lại rõ |

Ngưỡng đề xuất cho workshop: ít nhất 10/12, đồng thời không có lỗi nghiêm trọng về dữ liệu/quyền/bịa kết quả. Điểm cao không thay thế review kỹ thuật và điều kiện triển khai.

## So prompt A/B một cách dùng được

1. Chọn bộ case cố định: happy path, lỗi biên, thiếu dữ liệu, concurrency, injection trong log.
2. Giữ cùng model/version nếu truy cập được, cùng tools/quyền/input và output budget.
3. Chạy lặp một số lần theo ngân sách, ghi từng kết quả; không chỉ chọn lần đẹp nhất.
4. Chấm mù tên prompt nếu có người review; kiểm code bằng test phù hợp.
5. So pass rate, lỗi nghiêm trọng, thời gian review và chi phí nếu hệ thống cung cấp số đo.
6. Dùng case giữ lại để kiểm hồi quy sau khi chỉnh prompt; không tinh chỉnh chỉ để khớp một ví dụ.

Các con số lần chạy và ngưỡng cần do nhóm chọn; wiki chưa đo A/B các prompt này.

## Biểu mẫu kết quả

```text
case_id: BE-T01
prompt_version: v1
model_label: <hiển thị trong công cụ; unknown nếu không có>
environment: <version/tools/ref>
input_hash_or_fixture: <artifact không chứa secret>
actual_output: <file>
checks_run: <lệnh, exit status, output>
checks_not_run: <lý do>
rubric: <6 điểm thành phần>
reviewer_findings: <evidence và impact>
```

Với UI, Playwright khuyến nghị locator theo thuộc tính người dùng nhìn thấy/contract rõ; dùng test hành vi thay vì selector phụ thuộc cấu trúc DOM dễ đổi. [PW](https://playwright.dev/docs/best-practices)

## Nguồn

- [OAI-E: OpenAI — Evaluation best practices](https://developers.openai.com/api/docs/guides/evaluation-best-practices) — Đánh giá theo nhiệm vụ, dữ liệu kiểm thử và kết hợp người review.
- [PW: Playwright — Best Practices](https://playwright.dev/docs/best-practices) — Test hành vi và locator theo role/text.
