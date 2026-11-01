# Mẫu tham khảo Slidev

Bộ slide hoàn chỉnh về phân tích kinh doanh bán lẻ trực tuyến UK, giữ làm **mẫu tham khảo độc lập** cho các bộ
slide mới của môn học. Thư mục này tự chạy được: có `package.json`, `pnpm-lock.yaml`, hình nền,
component và toàn bộ trang; sao chép cả thư mục sang nơi khác vẫn cài đặt và build được.

## Chạy

Yêu cầu Node 22 và pnpm 10.

```sh
pnpm install --frozen-lockfile   # lần đầu khoảng 4 phút (có playwright-chromium để xuất file)
pnpm dev                         # xem và trình chiếu, mở trình duyệt
pnpm build                       # bản web tĩnh vào dist/
pnpm export                      # PDF (dark), tên file slidev-sample
pnpm ppt                         # PPTX (mỗi slide là một ảnh)
```

`node_modules/`, `dist/`, `.slidev/` và file PDF/PPTX xuất ra nằm ngoài git (xem `.gitignore`).

## Cấu trúc: 19 slide, khoảng 10 phút

`slides.md` giữ bìa, mục lục, nhập năm phần bằng `src:` rồi kết thúc bằng trang cảm ơn. Mỗi phần là một thư mục
trong `pages/` có `main.md` (trang mở phần) và các trang nội dung đánh số.

| Slide | Nội dung | Nguồn |
|---|---|---|
| 1 | Bìa: tiêu đề, môn học, giảng viên, thành viên | `slides.md` |
| 2 | Mục lục tự động (`arc-toc`) | `slides.md` |
| 3–5 | Bối cảnh: phạm vi dữ liệu, câu hỏi kinh doanh | `pages/context/` |
| 6–8 | Giao dịch hủy bất thường | `pages/cancellations/` |
| 9–11 | Tập trung doanh số vào khách lớn | `pages/customers/` |
| 12–15 | Cơ hội tăng trưởng: bán kèm, thị trường | `pages/growth/` |
| 16–18 | Lộ trình 180 ngày và kết luận | `pages/plan/` |
| 19 | Cảm ơn | `slides.md` |

## Các mẫu dùng lại được

- **Theme và addon.** `@alphacifer/slidev-academic-theme` với addon `@alphacifer/slidev-addon-theme`, nền sáng,
  font Roboto, `transition: slide-left`, `mdc: true`; khai báo trong frontmatter đầu `slides.md`.
- **Bốn layout cho bốn vai trò.**
  - Bìa: nền `assets/main.png` và hai component `<Speaker>` (môn học/giảng viên, thành viên/ngày).
  - Mục lục: `layout: arc-toc`, chỉ liệt kê các trang có `indexed: true`.
  - Trang mở phần: `layout: bg-center`, `background: ../../assets/heading.png`, `indexed: true`, `transition: fade`.
  - Trang nội dung: `layout: shifting-intro`, `hideInToc: true`, `transition: slide-left`; click đầu đưa tiêu đề lên trên.
- **Chia file theo phần.** Mỗi phần có `main.md` nhập các trang con bằng `src: ./01-….md`, nên thêm, bỏ hay đổi thứ
  tự trang chỉ sửa một chỗ.
- **Biểu đồ bằng Vue.** `components/StoryEvidence.vue` (chọn biểu đồ qua prop `kind`),
  `CustomerConcentration.vue`, `BriefEvidence.vue`; số liệu đặt trong component, màu theo bảng màu của theme.
  Bộ `HexTriad*` của theme dùng cho sơ đồ ba ý.
- **Lớp CSS dùng chung** trong `style.css`: `.metrics`, `.evidence-list`, `.evidence-table`, `.note`, `.takeaway`,
  `.closing-statement`.
- **Ghi chú người nói có cấu trúc** (`<!-- … -->` cuối mỗi trang): thời lượng, `Mục tiêu`, lời nói, `Giải thích
  khi được hỏi` (định nghĩa, cách tính), `Chuyển` (câu nối sang trang sau), `Nguồn` (mục trong báo cáo gốc).

## Lưu ý khi dùng làm mẫu

- Số liệu và dòng `Nguồn:` trong ghi chú lấy từ báo cáo gốc của bộ slide (`final-report-revised.docx`), là nội
  dung của bài này; khi làm bộ slide mới, thay bằng số liệu và nguồn của bài mới.
- Lộ trình 180 ngày và các mục tiêu pilot trong bài là minh họa cho đề xuất, chưa phải kết quả đo được.
- PPTX do Slidev xuất gồm ảnh của từng slide; khi cần biểu đồ chỉnh sửa được trong PowerPoint, dựng lại biểu đồ
  ngay trong PowerPoint.
