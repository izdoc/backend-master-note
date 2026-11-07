# Site Wiki Hệ thống Chứng khoán Việt Nam

Trang đọc 38 bài học từ `securities-wiki/` trong cùng repository. Bản Site được lưu dưới `securities-wiki-site/`; bản Markdown gốc vẫn nằm trong `securities-wiki/docs/`.

## Cấu trúc

- `content/`: snapshot Markdown và catalog được đồng bộ từ wiki gốc.
- `src/`: giao diện HTML, CSS, JavaScript thuần, không minify.
- `scripts/sync_content.py`: đồng bộ bài mới từ wiki gốc.
- `scripts/build.py`: dựng trang tĩnh vào `dist/` bằng Pandoc.
- `.openai/hosting.json`: cấu hình triển khai Site.

## Cập nhật nội dung

Chạy tại thư mục `securities-wiki-site/`:

```bash
python3 scripts/sync_content.py --wiki ../securities-wiki
python3 scripts/build.py
```

Yêu cầu: Python 3.10+ và Pandoc. Có thể xem cục bộ bằng `python3 -m http.server 8000 -d dist` rồi mở `http://localhost:8000`. Source giữ định dạng đọc được, không có bước minify. Khi bổ sung bài, thêm mục vào `securities-wiki/config/catalog.json` và chạy lại hai lệnh trên. Kiểm tra link và nội dung gốc theo `securities-wiki/scripts/validate.py`.

Các sơ đồ Mermaid dùng thư viện từ CDN lúc mở bài; nếu CDN không tải được, mã sơ đồ vẫn hiện để đọc. Site được triển khai ở chế độ riêng tư cho chủ sở hữu.
