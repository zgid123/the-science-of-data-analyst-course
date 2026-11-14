# Reader test of the Vietnamese 15-slide deck (main slides and notes)

## Reader test: main slides 1–16 and notes (Vietnamese manager, single hearing)

Inputs: slide images `prev_final/slide-01.png` … `slide-16.png` (read first, without notes) and `vi_main_text.md` (notes read as the spoken talk), both in the vi15 scratch folder. Reviewer role: a manager at a Vietnamese university who hears the talk once and has never seen the English version.

Overall judgement: after one hearing I could retell the project's story: staff notice disengaging students only after weeks 1–4; the team chose OULAD as the only open dataset with dated outcomes; few assignments fall due early, so the early-warning rule adds "a week without clicks"; a model trained on 2013 and tested once on 2014 beats the simple rule only slightly (41,5% vs 40,3%), so a short list of about five or six names per 20 students, each with a reason, is the practical output; whether contacting students helps must be proven in a randomised pilot. The voice is consistently "nhóm", the register is polite and suits a manager, and most notes sit at the right middle level: they explain the reasoning and keep a few key numbers. The obstacles are concentrated in four places: slide 8 (leakage table and the "check that can fail" box) is too technical for a manager and its point is not said aloud; slide 10 uses "điều kiện S1" without defining it on the slide; the recommended list length moves from 5 to "khoảng sáu" (slides 13 and 15) without saying which one the office should use; and slide 14 and the closing notes slip into course jargon (log loss, Level 2, pipeline, English names in parentheses). Slides 7, 8 and 10 carry more text than a listener can read while hearing the notes; slides 2, 3, 7, 11 and 15 work well.

| # | Slide | Slide/Notes | Quote | What stopped me | Clarity |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | 2–15 | Slide | "Chi tiết trong phụ lục: A2–A9" | Appendix of which document? Readable only if the report is handed out with the talk. | 3 |
| 2 | 2 | Slide | "(giả định của kịch bản)" | First mention of a "kịch bản"; I do not know which scenario until the slide 3 notes. | 3 |
| 3 | 3 | Slide | "Business Goal và SMART Goal" | English title and terms on a Vietnamese slide; "Mục tiêu của tổ chức" and "mục tiêu SMART" would read naturally. | 3 |
| 4 | 4 | Slide | "Dữ liệu đến ngày 13 và 27 dự báo…" | "Ngày 13" of what? Only the footer says ngày 13 = hết tuần 2, counted from the module start. | 2 |
| 5 | 4 | Slide | "một kỳ mở module (một lần mở module)" | Mixes "module" and "học phần" (the title says học phần); are they the same? Recurs throughout the deck. | 3 |
| 6 | 4 | Notes | "D1, liên hệ với sinh viên nào; D2, phân bổ thời gian hỗ trợ vào đâu; D3…" | Seven codes (D1–D3, AQ1–AQ4) in one minute; at slide 11 ("quyết định D2") I had to recall what D2 was, though the notes restate it. | 3 |
| 7 | 5 | Slide | "UCI 697", "UCI 320", "UCI 856" | Bare numbers mean nothing to me; a short descriptive name would help. "Ứng viên" for datasets sounds translated. | 3 |
| 8 | 5 | Slide | "Được chọn, có điều kiện" | Which conditions? The slide does not say. | 2 |
| 9 | 5 | Notes | "nhóm chọn OULAD kèm những điều kiện mà các tệp dữ liệu phải xác nhận" | Still unclear what the conditions are or whether they were met. | 2 |
| 10 | 6 | Slide | "Trung bình = lệch một đại lượng theo mức đã biết" | Abstract; "đại lượng" and "mức đã biết" made me reread twice. | 2 |
| 11 | 6 | Slide | "xử lý bằng cờ, cắt ngưỡng hoặc nhóm \"Thiếu\"" | "Cờ" and "cắt ngưỡng" are technical jargon for a manager. | 3 |
| 12 | 6 | Notes | "chỉ số chênh lệch chính về lượt nhấp sớm thay đổi không quá 0,004" | Which index, in what unit (điểm phần trăm or tỷ lệ)? I cannot judge whether 0,004 is small. | 2 |
| 13 | 7 | Slide | "Không tính bài kiểm tra ngắn nộp trễ: chưa rõ CMA nộp trễ năm 2013–2014 nghĩa là gì; nếu tính, … tăng từ 28,8% lên 41,2%" | Three text blocks of detail under the three rule cards; too dense to read while listening. | 3 |
| 14 | 8 | Slide | "Trung vị, thang đo, mức mã hóa tính trên mọi kỳ mở" | I cannot see why computing a median over all runs is leakage; technical. | 2 |
| 15 | 8 | Slide | "1.586 lượt kiểm thử của sinh viên đã học 2013 — Giữ lại; loại ra khi kiểm tra chặt" | Kept or removed? "Kiểm tra chặt" is not defined. | 2 |
| 16 | 8 | Slide | "Phép kiểm tra có thể báo lỗi: khi tắt bộ lọc ngày, chỉ những lượt … bị thay đổi (26.755 tại ngày 13, 25.663 tại ngày 27)" | Only after rereading did I see that this proves the check works; the two numbers have no total to compare with. | 2 |
| 17 | 8 | Notes | "chẳng hạn một phép kiểm tra không bao giờ có thể báo lỗi" | Heard once, it sounds like praise; it needs "luôn báo đạt nên không phát hiện được gì". | 2 |
| 18 | 8 | Notes | "Khung màu xanh lá cho thấy một ví dụ: khi tắt bộ lọc ngày, chỉ những lượt … bị thay đổi" | The conclusion (so the check would catch leakage) is not said aloud. | 2 |
| 19 | 9 | Slide | "ở các kỳ mở huấn luyện, mức trần này dao động từ 46% đến 100%" | "Mức trần" of what: the highest possible detection rate? Understood on rereading. | 2 |
| 20 | 9 | Slide | "Lift", "TRIPOD+AI", "hiệu chuẩn" | English term and an unexplained guideline name; none is used again in the talk. | 3 |
| 21 | 10 | Slide | "Đạt điều kiện S1 để thay quy tắc" | S1 is not defined on this slide; it is spoken in the slide 9 notes and defined only in the slide 14 legend. Reading the slide alone, I could not tell what S1 is. | 1 |
| 22 | 10 | Slide | "tỷ lệ phát hiện chuẩn hóa (bằng cột cuối ở độ dài danh sách này) 0,725" | Why does the normalised rate equal the precision column; 72,5% in the table vs 0,725 in the box. | 2 |
| 23 | 10 | Notes | "nhóm chạy Level 2, tức nguyên mẫu tùy chọn" / "không mô hình đối sánh phức tạp nào" | Course jargon ("Level 2") and a translated term ("mô hình đối sánh"); a manager does not need either. | 3 |
| 24 | 10 | Notes | "Hãy xem cột giữa" | The table has four columns; the column meant is "Tỷ lệ phát hiện" (third); name it. | 3 |
| 25 | 11 | Slide | "Đạt tiêu chí thành công: số đếm từ dữ liệu đã chuẩn bị và dữ liệu gốc khớp ở cả 176 ô" | What are the 176 cells? Reads like an internal data check on a findings slide. | 2 |
| 26 | 12 | Notes | "40,8 năm 2013 và 39,3 năm 2014 … 14,5 và 15,8 điểm … khoảng 9 đến 11 điểm" | Many numbers to hear in one minute; "9 đến 11" while the chart shows 8,7 and 10,6. Slightly dense. | 3 |
| 27 | 13 | Slide | "59,7% số sinh viên chỉ mô hình chọn không hoàn thành, so với 50,6% ở nhóm chỉ quy tắc chọn" | Parsed only on the second reading. | 2 |
| 28 | 13 | Slide | "quy tắc FR1" | An internal code; "quy tắc công bằng" is enough. | 3 |
| 29 | 13, 15 | Notes and slide | "khoảng sáu tên trên hai mươi" vs "danh sách 5 trên 20" | Every result uses 5 names, the recommendation says 6; which should the office use, and why the change? Not reconciled. | 2 |
| 30 | 14 | Slide | "Dòng trùng làm lệch chỉ số lượt nhấp sớm ≤ 0,004" | Same unit problem as finding 12. | 2 |
| 31 | 14 | Slide | "Kế hoạch thiếu thước đo tinh chỉnh" | "Thước đo tinh chỉnh" puzzled me; only the legend and notes hint it is about the model. | 2 |
| 32 | 14 | Notes | "nhóm chọn log loss và công bố rõ thời điểm chọn" | Log loss is not explained aloud; this detail is below a manager's level. | 3 |
| 33 | 15 | Notes | "phân loại mức độ rủi ro của danh sách theo yêu cầu của pháp luật Việt Nam" | Appears for the first time in the last minute; which law and what the classification involves are not said. | 2 |
| 34 | 15, 16 | Notes | "… Xin cảm ơn." then "Xin cảm ơn đã cùng nhóm theo dõi…" | Two thank-yous in a row. | 3 |
| 35 | 16 | Notes | "Gói nộp cuối kỳ (Final Project Package) … pipeline … Nhật ký quyết định về AI (AI Decision Log)"; "quy tắc điều chỉnh đăng ký học phần" | English names in parentheses and "pipeline" sound translated; "quy tắc điều chỉnh đăng ký học phần" is unclear as a question topic. | 3 |

Counts: clarity 1: 1; clarity 2: 18; clarity 3: 16 (35 findings).
