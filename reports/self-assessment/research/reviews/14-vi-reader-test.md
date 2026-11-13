# Reader check of the round-4 fixes

Reader: Vietnamese lecturer, Vietnamese files only (01-00, 02-01, 02-02 `.vi.md`). Clarity: 1 = could not work out the meaning; 2 = understood after rereading; 3 = understood but sounds translated.

| # | Passage | Verdict | Note |
| :- | :---- | :---- | :---- |
| 1 | 01-00 Bảng 1.1, dòng chất lượng dữ liệu, cột Tình trạng | Clear | Câu dài nhưng đọc một lần là hiểu: Cliff's delta được định nghĩa ngay, mức thay đổi 0,004 và kết luận nằm cùng câu. |
| 2 | 01-00 Bảng 1.1, dòng tài liệu mô tả không khớp, cột Cách giải quyết | 2 | "Phương án tính các bài kiểm tra ngắn có ngày nộp sau hạn là bài nộp trễ được dùng trong phân tích độ nhạy": chữ "là" khiến lần đọc đầu hiểu thành "phương án … là bài nộp trễ"; phải đọc lại mới thấy "tính … là bài nộp trễ" là một cụm. Gợi ý: "Phân tích độ nhạy dùng thêm phương án coi các bài kiểm tra ngắn có ngày nộp sau hạn là bài nộp trễ." |
| 3 | 01-00 Bảng 1.1, dòng lỗi trong mã chuẩn bị dữ liệu, định nghĩa đợt kiểm tra và cột Cách giải quyết | 3 | Định nghĩa hiểu được, nhưng ngoặc đơn dài tách chủ ngữ khỏi "do AI thực hiện tìm ra", và "thực hiện tìm ra" nghe như dịch. Ở cột giải quyết, "chỉ được đưa ra trên dữ liệu huấn luyện" nghe như dịch ("made on"); tự nhiên hơn: "chỉ dựa trên dữ liệu huấn luyện". Còn lại rõ. |
| 4 | 01-00 Bảng 1.1, dòng cuối: tên vấn đề và cột Tình trạng | 3 (tên vấn đề); Clear (tình trạng) | "Giữ các sản phẩm tiếng Anh và tiếng Việt thống nhất và dùng được": tên vấn đề viết như một mục tiêu, "dùng được" nghe như dịch từ "usable". Cột tình trạng rõ: hai bộ slide được phân biệt bằng số slide; "bộ slide thuyết trình 30 slide" hơi lặp chữ nhưng không gây khó. |
| 5 | 02-01 Bảng A.2 dòng Milestone 4 (Hạn chế chính) và đoạn kết | Clear | Dòng Milestone 4 rõ. Đoạn kết hiểu ngay; chỉ lặp ý: việc đề bài Milestone 4 không quy định số trang được nói hai lần trong cùng đoạn (trong ngoặc và ở vế "trong khi…"), không phải trở ngại. |
| 6a | 02-02 SMART Goal (Milestone 1) | Clear | Mức cơ sở 70% là số giả định, chưa đo thực tế: rõ. |
| 6b | 02-02 Search Log (Milestone 2) | Clear | 16 = 11 + 5 cộng lại khớp; "các nguồn tìm thêm được từ những lượt đó" hiểu được. |
| 6c | 02-02 Presentation & consistency (Milestone 4) | Clear | – |
| 6d | 02-02 Findings & educational decision support (Milestone 5) | 2 | Ngoặc đơn "(ngày 14 là mốc xác định tập sinh viên dùng để tính chỉ số hoàn thành học phần; ngày 13 và ngày 27 là ngày lập danh sách liên hệ)" chen giữa chủ ngữ và con số 45,3%, nên phải đọc lại để nối "Trong 28.061 lượt đăng ký…" với "45,3% không hoàn thành". Gợi ý: tách phần giải thích ngày 14 thành câu riêng sau con số. |

## Decisions on this check

All five suggestions applied (Vietnamese; the last-row problem name and the day-14 sentence also in English): "Phân tích độ nhạy dùng thêm phương án coi…"; the AI audit as its own sentence with "AI tạo sinh" as actor; "chỉ dựa trên dữ liệu huấn luyện"; the last problem named as a problem ("Bản tiếng Anh và bản tiếng Việt chưa thống nhất, tệp Word khó mở…"); the day-14 explanation moved to its own sentence after the evidence. No flag remains open.

## Consistency pass (stage 5)

`glossary.py coverage` (logs/vi_consistency.log): 9 drifting concepts. Fixed: "analytics level" → "loại phân tích" (3 places; also keeps it apart from the rating "mức"). Kept with reason: "enrolment" → "lượt đăng ký học" (OULAD enrolments are in modules, and "học phần" is reserved for the university's courses); "feature" → "biến" (reader test round 1 flag 10); "fact", "Before/After", "Validation" (ordinary English words, not the glossary concepts); "PASS/FAIL" → "không báo lỗi" (keeps check results apart from the rating "Đạt", native review); "main text" → "phần chính" after first use (allowed by the glossary row); "contact list" → the fuller "danh sách sinh viên cần liên hệ". `glossary.py lint`: 0 errors (one size warning on early-warning-evaluation.md, not this task).
