---
title: "Mini Task 02"
theme: '@alphacifer/slidev-academic-theme'
colorSchema: light
addons:
  - '@alphacifer/slidev-addon-theme'
background: ./assets/main.png
drawings:
  persist: false
transition: slide-left
mdc: true
comark: true
hideInToc: true
fonts:
  sans: Roboto
  serif: Roboto
  mono: Roboto Mono
duration: 10min
exportFilename: minitask-02
---

# Mini Task 02

<div class="text-[#0f172a] text-[30px]">
  UK Online Retail<br />Phân tích kinh doanh và giải quyết vấn đề
</div>
<Speaker
  class="left-[48px] right-auto [&_.alpha-date]:hidden text-[var(--alpha-academic-primary)]"
  :team="['Môn học: Khoa học phân tích dữ liệu', 'GVHD: TS. Nguyễn Trần Minh Thư']"
  date="2026-09-01"
/>
<Speaker
  class="text-[var(--alpha-academic-primary)]"
  :team="['25C12003 - Phan Trần Khanh', '25C12031 - Dương Tấn Huỳnh Phong', '25C12002 - Lê Ngọc Trúc Huỳnh']"
  date="2026-09-19"
/>

<!--
30 giây.

Mục tiêu: Giới thiệu vấn đề kinh doanh và ba câu hỏi chính của bài trình bày.

"Bộ dữ liệu bán lẻ trực tuyến này ghi nhận 9,77 triệu bảng doanh số sau khi trừ các đơn hủy. Tuy nhiên, câu hỏi của nhóm không chỉ là làm thế nào để tăng doanh số, mà còn là liệu các tín hiệu trong dữ liệu đã đủ đáng tin để ra quyết định hay chưa.

Nhóm phát hiện ba điểm cần làm rõ. Hơn một nửa tổng giá trị hủy đến từ chỉ hai giao dịch. Khoảng 60% doanh số của nhóm khách có mã nhận diện đến từ 10% người mua. Và các cơ hội như bán kèm hay mở rộng thị trường vẫn chưa được kiểm chứng về lợi nhuận.

Vì vậy, bài trình bày sẽ đi từ việc kiểm tra dữ liệu, xác định vấn đề ưu tiên, đến một kế hoạch thử nghiệm trong 180 ngày."

Giải thích khi được hỏi:
- Doanh số sau hủy, hay net sales: giá trị bán còn lại sau khi trừ các giao dịch hủy; chưa phải lợi nhuận.
- Kiểm chứng: thử ở quy mô giới hạn và đo kết quả trước khi triển khai rộng.

Chuyển: "Trước tiên, tôi xin trình bày cấu trúc của câu chuyện này."
Nguồn: final-report-revised.docx, mục 1.1-1.2.
-->

---
layout: arc-toc
hideInToc: true
indexed: true
---

# Nội dung

<!--
15 giây.

"Bài trình bày gồm bốn phần. Một là phạm vi dữ liệu và ba câu hỏi kinh doanh. Hai là vấn đề đơn hủy và cách xử lý. Ba là mức độ phụ thuộc vào khách hàng lớn cùng các cơ hội tăng trưởng. Cuối cùng là lộ trình 180 ngày và quyết định cần phê duyệt trước tiên."

Chuyển: "Chúng ta bắt đầu bằng việc xác định dữ liệu gồm những gì và các con số được tính như thế nào."
-->

---
src: ./pages/context/main.md
---

---
src: ./pages/cancellations/main.md
---

---
src: ./pages/customers/main.md
---

---
src: ./pages/growth/main.md
---

---
src: ./pages/plan/main.md
---

---
layout: thanks
hideInToc: true
---

<!--
5 giây.

"Nhóm xin cảm ơn thầy cô và các bạn đã lắng nghe. Nhóm sẵn sàng trả lời câu hỏi về dữ liệu, cách tính hoặc các đề xuất thử nghiệm."
-->
