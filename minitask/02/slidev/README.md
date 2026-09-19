# MiniTask 02: UK Online Retail

[OUTLINE.md](OUTLINE.md) là outline hiện hành: **19 slide tổng cộng**, gồm 14 slide nội dung/bìa/mục lục/cảm ơn và 5 trang mở phần. Thời lượng dự kiến 9 phút 45 giây. `arc-toc` ở slide 2, phạm vi dữ liệu ở slide 4, `thanks` luôn là trang cuối 19/19.

```sh
pnpm install --frozen-lockfile
pnpm dev
pnpm build
pnpm export
pnpm ppt
```

## Cấu trúc nguồn

`slides.md` giữ bìa, `arc-toc`, nhập năm phần rồi kết thúc bằng `thanks`.

| Mục TOC | Thư mục | Trang mở phần |
|---|---|---|
| Bối cảnh | `pages/context/` | 3 |
| Giao dịch hủy bất thường | `pages/cancellations/` | 6 |
| Tập trung doanh số | `pages/customers/` | 9 |
| Cơ hội tăng trưởng | `pages/growth/` | 12 |
| Kế hoạch triển khai | `pages/plan/` | 16 |

Mỗi thư mục có `main.md` dùng `layout: bg-center` và `background: ../../assets/heading.png`, sau đó nhập các trang trong cùng thư mục. Chỉ các trang mở phần xuất hiện trong TOC. Các trang nội dung dùng `layout: shifting-intro`, `hideInToc: true`, `transition: slide-left`; click đầu đưa tiêu đề lên trên.

`assets/main.png` là nền bìa, `assets/heading.png` là nền mở phần. `components/` chứa biểu đồ Vue. Không có phụ lục, chi tiết trả lời câu hỏi nằm trong ghi chú và báo cáo nguồn.

Bìa giữ thông tin nhóm và giảng viên. Số liệu theo `../final-report-revised.docx`. Tài liệu góp ý ở `../minitask2_presentation_instructions.md`; cấu trúc thực hiện theo OUTLINE hiện hành. [REVIEW.md](REVIEW.md) lưu đánh giá báo cáo trước đây, số slide lịch sử không áp dụng bản này.

DOCX nguồn giữ nguyên. Chưa tái chạy CSV. Lộ trình 180 ngày khác cửa sổ theo dõi từng pilot, các mục tiêu pilot còn là minh họa.

PDF/PPTX cần xuất lại nếu dùng bản mới. PPTX do Slidev xuất là ảnh từng slide, không có biểu đồ PowerPoint chỉnh sửa được.
