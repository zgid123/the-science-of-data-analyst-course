# Slide review: Vietnamese fluency and stand-alone reading of the Milestone 5 deck

Date: 2026-11-11. Scope: every slide of `N04_Milestone5_Slides-30_VI.pptx` (30 slides), read one slide at a time from
`slidekit.py text`, against two tests: (1) the Vietnamese reads as written natively, not translated; (2) each slide is
understood on its own, as AGENTS.md "Every section reads on its own" requires (restate, then point; define every
identifier on the slide that uses it). The English source changed only where the stand-alone test failed in both
languages. Reviewer: the agent (not a native speaker); a read-aloud by a team member is still to run.

## Findings by slide

| Slide | Test | Finding | Fix |
| :---- | :---- | :---- | :---- |
| 1 | Fluency | "đang dần rời xa học phần" reads literary (calque of "drift away") | "đang dần ngừng tham gia học phần", matching the title |
| 2 | Fluency | "Giảng viên nhận ra rõ"; "rồi im lặng" | "Giảng viên mới chắc chắn"; "rồi ngừng hoạt động hẳn" |
| 3 | Stand-alone | "Cả 5 dấu hiệu sớm (slide 22)" points away without naming the signs | EN and VI name the two kinds (tasks, activity); the term box on the slide defines an early sign |
| 3 | Fluency | lead and "lý do … cho mỗi tên" read translated | rewritten lead; "kèm từng tên" |
| 4 | Fluency | "bên cạnh mỗi tên" (calque of "beside each name"); "đảo ngược được" | "mỗi tên kèm một lý do cụ thể"; glossary pair "dễ / khó đảo ngược" |
| 4 | Layout | needs-source note overlapped the source line (two-line lead) | one-line lead and one-line note |
| 6 | Stand-alone | D1–D3 and the early-sign rule used without definition | definitions added to the slide key (EN and VI) |
| 6 | Fluency | AQ2 "gắn với việc về sau không hoàn thành" | "liên quan đến việc không hoàn thành về sau" (also slides 22, 26, 28 and notes) |
| 7 | Fluency | "câu hỏi chọn dữ liệu chứ không phải ngược lại"; "khoảng trống đã biết" | "chính câu hỏi quyết định việc chọn dữ liệu"; glossary "khoảng trống dữ liệu" |
| 10 | Fluency | "đổi đại lượng đo một mức đã biết" unclear; "Hoạt động lệch mạnh" | "lệch một số đo theo mức đã biết"; "Lượt nhấp lệch mạnh" |
| 12 | Stand-alone | TMA and CMA undefined on the slide; "(slide 22)" pointer for two unnamed signs | TMA/CMA defined in the key; the two signs named (EN and VI) |
| 12 | Layout | heading over the three rule boxes wrapped onto the boxes | "Quy tắc cuối cùng: …" fits one line |
| 13 | Fluency | "PASS"; "Các quyết định chi phối" | "đạt"; "Nguyên tắc xử lý" |
| 14 | Glossary | "cây tăng cường độ dốc" without its first-use gloss | "(gradient-boosted trees)" added |
| 15 | Fluency | "1 = ngẫu nhiên" | "lift bằng 1 nghĩa là không hơn chọn ngẫu nhiên" |
| 16 | Glossary, stand-alone | "Fold" without gloss; "danh sách theo quy tắc" | "Fold (phần chia trong kiểm định chéo)"; "quy tắc dấu hiệu sớm" (EN and VI) |
| 17 | Fluency | "thấp hơn … hơn 10 điểm" | "thấp hơn … quá 10 điểm phần trăm" |
| 19, 20, 22 | Fluency | "râu" for error bars | "thanh sai số" (glossary row added) |
| 23 | Fluency | "chỉ phản ánh một phần xu hướng biến thiên theo mức hoạt động" | "chỉ nắm được một phần quan hệ giữa mức hoạt động và nguy cơ" |
| 24 | Stand-alone | "D1, D2 và D3 là ba quyết định ở slide 4"; S1 and FR1 undefined | D1–D3, S1 and FR1 defined on the slide (EN and VI); the line repeating the column headers removed so the definitions fit |
| 25 | Stand-alone | S1 and FR1 undefined | glossed in place (EN and VI) |
| 26 | Fluency | "(đảo ngược được)"; comma before "và" | "(dễ đảo ngược)", "(khó đảo ngược)"; comma removed |
| 27 | Fluency | "Nơi AI hữu ích nhất"; "mọi mối liên hệ được nêu đúng là mối liên hệ" | "AI giúp ích nhiều nhất ở đâu"; "chỉ được trình bày là liên hệ, không phải nhân quả" |
| 28 | Fluency | "lý do bên cạnh mỗi tên"; "gắn với" | "đi kèm từng tên"; "liên quan đến" |
| 29, 30 | Fluency | "Không khẳng định; chưa chắc chắn."; "trước khi tin"; "phân loại rủi ro theo luật" | "Không kết luận; chưa xác định."; "trước khi mở rộng"; "phân loại rủi ro theo quy định" |

Slides 5, 8, 9, 11, 18 and 21 passed both tests unchanged. Pointers that already restate their fact (slide 9 "quy tắc
điều chỉnh đăng ký học phần, slide 11"; slide 10 key "slide 12"; slide 11 "slide 20") stay. Terms locked by the
report and glossary stay: "kỳ mở" (757 uses in the report), "tính đến hết", GAP, GREEN/YELLOW/RED, Level 1/2.

## Report consistency

The glossary row "mỗi tên kèm một lý do cụ thể" replaces "bên cạnh mỗi tên"; its four report uses were rewritten in
`00-1-abstract`, `14-00-conclusion`, `16-13-aq2-results` and `16-14-aq3-aq4-answers` (`.vi.md`) and marked synced.
"gắn với" stays in the report (no Replaces entry), so the change is deck-only.

## Checks

- `slidekit.py strings build_slides_milestone5_30.py` → `[]` and no room warnings.
- `check_slides.py … --lang en|vi --task milestone-5` → 0 errors, 0 warnings in both decks.
- `preview_slides.py` renders of slides 3, 4, 6, 12, 24, 29 (VI) and 4, 6, 24 (EN) inspected; contact sheet of all 30
  VI slides inspected. check_slides does not detect one text box overlapping another (slides 4 and 12 overlapped
  before this pass and passed), so the render inspection is the gate for overlaps.
- Still to run: one read-aloud of the Vietnamese deck by a team member.

## Changed on-slide strings (English key, before, after)

| English key | Vietnamese before | Vietnamese after |
| :---- | :---- | :---- |
| A final report on finding students who drift away from online courses … | Báo cáo cuối kỳ về cách nhận ra những sinh viên đang dần rời xa học phần trực tuyến, đủ sớm để kịp hỗ trợ. | Báo cáo cuối kỳ về cách nhận ra sớm những sinh viên đang dần ngừng tham gia học phần trực tuyến, để kịp thời hỗ trợ. |
| Lecturers become sure | Giảng viên nhận ra rõ | Giảng viên mới chắc chắn |
| A student misses a task, opens the course less often and falls silent … | Sinh viên bỏ lỡ một bài, ít mở học phần hơn rồi im lặng, trước khi hệ thống ghi nhận kết quả không đạt hoặc rút học phần. | Sinh viên bỏ lỡ một bài, vào học phần thưa dần rồi ngừng hoạt động hẳn, trước khi hệ thống ghi nhận kết quả không đạt hoặc rút học phần. |
| Early records give staff a factual reason beside each name now; whethe… | Dữ liệu sớm đã cho cán bộ lý do cụ thể cho mỗi tên ngay bây giờ; mô hình có xếp hạng tốt hơn không, liên hệ có giúp ích không, còn chờ lần kiểm tra duy nhất trên năm 2014 và đợt thí điểm ngẫu nhiên. | Dữ liệu những tuần đầu đã cho cán bộ lý do cụ thể kèm từng tên; mô hình có xếp hạng tốt hơn không, liên hệ có giúp ích không, còn chờ một lần kiểm tra trên năm 2014 và một đợt thí điểm ngẫu nhiên. |
| early signs, from tasks and from activity, go with later non-completio… | (new string) | dấu hiệu sớm (về bài và hoạt động) đều liên quan đến việc không hoàn thành về sau ở cả hai năm; bỏ lỡ bài: cao hơn 40,8 (2013) và 39,3 (2014) điểm. |
| Three groups of staff each take one decision, and all of them asked fo… | Ba nhóm cán bộ đưa ra ba quyết định khác nhau, nhưng cả ba đều cần một danh sách ngắn với lý do cụ thể bên cạnh mỗi tên. | Ba nhóm cán bộ, ba quyết định, cùng một nhu cầu: danh sách ngắn, mỗi tên kèm một lý do cụ thể. |
| Operational and reversible | Tác nghiệp, đảo ngược được | Tác nghiệp, dễ đảo ngược |
| Close to irreversible | Gần như không thể đảo ngược | Khó đảo ngược |
| A list at weeks 3 and 5, with a factual reason beside each name. | Một danh sách vào tuần 3 và tuần 5, với lý do cụ thể bên cạnh mỗi tên. | Một danh sách vào tuần 3 và tuần 5, mỗi tên kèm một lý do cụ thể. |
| Source of the needs: simulated interviews with AI on both sides (five … | Nguồn của các nhu cầu: phỏng vấn mô phỏng, trong đó AI đóng cả hai vai (năm bên liên quan, 51 phát biểu chính, sáu chủ đề); các nhu cầu này định hướng thiết kế và không bao giờ được dùng làm bằng chứng. | Nguồn nhu cầu: phỏng vấn mô phỏng, AI đóng cả hai vai (5 bên liên quan, 51 phát biểu, 6 chủ đề); chỉ định hướng thiết kế, không dùng làm bằng chứng. |
| Which signs by week 4 go with later non-completion, within module run? | Dấu hiệu nào tính đến hết tuần 4 gắn với việc về sau không hoàn thành, trong cùng kỳ mở? | Những dấu hiệu nào đến hết tuần 4 liên quan đến việc không hoàn thành về sau, khi so trong cùng kỳ mở? |
| Reads as: a forecast, valid only on data the model never saw. | Cách đọc: dự báo, chỉ có giá trị trên dữ liệu mô hình chưa thấy. | Cách đọc: dự báo, chỉ đúng trên dữ liệu mô hình chưa thấy. |
| Reads as: an option to test, because it comes from observational data. | Cách đọc: phương án cần kiểm chứng, vì rút từ dữ liệu quan sát. | Cách đọc: phương án cần kiểm chứng, vì dựa trên dữ liệu quan sát. |
| Key: orange rungs were run on the data, white rungs are designs. Data … | (new string) | Chú giải: bậc cam đã chạy trên dữ liệu, bậc trắng là thiết kế. Ngày 13 và 27 (hết tuần 2 và 4): thời điểm chốt dữ liệu cho danh sách tuần 3 và 5. D1 – liên hệ với ai, D2 – phân bổ hỗ trợ, D3 – có mở rộng không. Quy tắc dấu hiệu sớm: bỏ lỡ, nộp trễ bài hoặc một tuần không hoạt động. |
| We wrote what the data must contain before searching, so the questions… | Nhóm chúng em viết ra những gì dữ liệu phải có trước khi tìm kiếm, nên câu hỏi chọn dữ liệu chứ không phải ngược lại. | Nhóm chúng em xác định dữ liệu cần có những gì trước khi tìm kiếm, nên chính câu hỏi quyết định việc chọn dữ liệu, không phải ngược lại. |
| Known gap, declared before the search:  | Khoảng trống đã biết, nêu trước khi tìm kiếm:  | Khoảng trống dữ liệu đã biết, nêu trước khi tìm kiếm:  |
| Key: a ticked box is a must-have gate; the grey box is a known gap. | Chú giải: ô có dấu tích là một điều kiện bắt buộc; ô màu xám là khoảng trống đã biết. | Chú giải: ô có dấu tích là điều kiện bắt buộc; ô màu xám là khoảng trống dữ liệu đã biết. |
| 19 issues, rated High (would change a rate, the target or a feature), … | 19 vấn đề: Cao (đổi tỷ lệ, biến mục tiêu hoặc đặc trưng), Trung bình (đổi đại lượng đo một mức đã biết) hoặc Thấp. | 19 vấn đề: Cao (đổi tỷ lệ, biến mục tiêu hoặc đặc trưng), Trung bình (lệch một số đo theo mức đã biết) hoặc Thấp. |
| Skewed activity | Hoạt động lệch mạnh | Lượt nhấp lệch mạnh |
| The median is 602 clicks and 3,365 enrolments have no click, so counts… | Trung vị 602 lượt nhấp; 3.365 lượt không có lượt nhấp; số đếm lấy logarit, không loại giá trị nào. | Trung vị 602 lượt nhấp; 3.365 lượt không có lượt nhấp nào; lấy logarit, không loại giá trị nào. |
| Early-sign rule (final): by the data cut-off, any one of three parts | Quy tắc dấu hiệu sớm cuối cùng: chỉ cần một trong ba phần, tính đến thời điểm chốt | Quy tắc cuối cùng: chỉ cần một trong ba phần, tính đến thời điểm chốt |
| a TMA or CMA due by the cut-off, not submitted | một TMA hoặc CMA đã đến hạn tính đến thời điểm chốt mà chưa nộp | một TMA hoặc CMA đã đến hạn trước thời điểm chốt nhưng chưa nộp |
| Key: the orange part is the activity part added for the data. TMA: tut… | Chú giải: phần màu cam là phần hoạt động được thêm vào để phù hợp với dữ liệu. | Chú giải: phần màu cam là phần hoạt động được thêm vào để phù hợp với dữ liệu. TMA: bài do giảng viên chấm; CMA: bài kiểm tra ngắn chấm bằng máy. |
| One rule serves OULAD and the pilot. AQ2 tests these three parts and t… | Một quy tắc dùng chung cho OULAD và đợt thí điểm. AQ2 kiểm tra ba phần này cùng hai dấu hiệu hoạt động khác (slide 22). | Một quy tắc dùng chung cho OULAD và đợt thí điểm. AQ2 kiểm tra ba phần này cùng hai dấu hiệu hoạt động khác: hoạt động dưới trung vị của kỳ mở và không có lượt nhấp trước ngày bắt đầu. |
| Governing decisions | Các quyết định chi phối | Nguyên tắc xử lý |
| All 22 validation checks pass; 32,593 enrolments and their outcome mix… | Cả 22 phép kiểm tra đều PASS; 32.593 lượt và cơ cấu kết quả giữ nguyên. | Cả 22 phép kiểm tra đều đạt; 32.593 lượt đăng ký học và cơ cấu kết quả giữ nguyên. |
| Penalised logistic regression on the 19 predictors (background, clicks… | Hồi quy logistic có điều chuẩn (penalised) trên 19 biến dự báo (đặc điểm cá nhân, lượt nhấp trước và sau ngày 0, hoạt động so với trung vị kỳ mở, không hoạt động gần đây, bài bỏ lỡ và nộp trễ); mô hình đối sánh: cây tăng cường độ dốc. | Hồi quy logistic có điều chuẩn (penalised) trên 19 biến dự báo (đặc điểm cá nhân, lượt nhấp trước và sau ngày 0, hoạt động so với trung vị kỳ mở, không hoạt động gần đây, bài bỏ lỡ và nộp trễ); mô hình đối sánh: cây tăng cường độ dốc (gradient-boosted trees). |
| the share of non-completers on the list divided by the run's base rate… | tỷ lệ sinh viên không hoàn thành trong danh sách chia cho tỷ lệ nền của kỳ mở (tỷ lệ sinh viên không hoàn thành của cả kỳ mở); 1 = ngẫu nhiên. | tỷ lệ sinh viên không hoàn thành trong danh sách chia cho tỷ lệ nền của kỳ mở (tỷ lệ sinh viên không hoàn thành của cả kỳ mở); lift bằng 1 nghĩa là không hơn chọn ngẫu nhiên. |
| Leave-one-run-out folds on the 9 runs of 2013: each run is held out in… | Fold loại trừ từng kỳ mở trên 9 kỳ mở năm 2013: mỗi kỳ mở lần lượt được tách ra. | Fold (phần chia trong kiểm định chéo) loại trừ từng kỳ mở trên 9 kỳ mở năm 2013: lần lượt tách riêng từng kỳ mở để đánh giá. |
| its pooled normalised recall must exceed the early-sign rule list's. | tỷ lệ phát hiện chuẩn hóa gộp phải cao hơn của danh sách theo quy tắc. | tỷ lệ phát hiện chuẩn hóa gộp phải cao hơn của danh sách theo quy tắc dấu hiệu sớm. |
| A risk difference of at least 5 points, an interval excluding 0, and t… | Chênh lệch nguy cơ ít nhất 5 điểm, khoảng tin cậy không chứa 0, cùng chiều ở ít nhất 2/3 số module; không dùng giá trị p. | Chênh lệch nguy cơ ít nhất 5 điểm phần trăm, khoảng tin cậy không chứa 0, cùng chiều ở ít nhất 2/3 số module; không dùng giá trị p. |
| flag a group for human review when its recall is more than 10 points b… | đánh dấu một nhóm để con người xem xét khi tỷ lệ phát hiện ở nhóm đó thấp hơn của các sinh viên còn lại hơn 10 điểm và khoảng tin cậy một phía của chênh lệch, đã hiệu chỉnh Holm (hiệu chỉnh cho nhiều phép kiểm định), nằm dưới 0. | đánh dấu một nhóm để con người xem xét khi tỷ lệ phát hiện ở nhóm đó thấp hơn của các sinh viên còn lại quá 10 điểm phần trăm và khoảng tin cậy một phía của chênh lệch, đã hiệu chỉnh Holm (hiệu chỉnh cho nhiều phép kiểm định), nằm dưới 0. |
| CCC ran only in 2014. Bar = rate in %; whisker = 95% Wilson interval (… | CCC chỉ mở năm 2014. Cột = tỷ lệ (%); râu = khoảng tin cậy Wilson 95% (khoảng tin cậy 95% của một tỷ lệ). | CCC chỉ mở năm 2014. Cột = tỷ lệ (%); thanh sai số = khoảng tin cậy Wilson 95% (khoảng tin cậy 95% của một tỷ lệ). |
| Key: dot = 2014 minus 2013 in points; whisker = 95% interval, and one … | Chú giải: chấm = 2014 trừ 2013, tính bằng điểm phần trăm; râu = khoảng tin cậy 95%, râu cắt qua 0 nghĩa là không có chênh lệch rõ ràng. Xám = trên mọi lượt đăng ký học; cam = chưa rút tại ngày 14 (quy tắc của KPI). Mỗi loại được trình bày cho mọi kỳ mở và cho sáu module mở cả hai năm. | Chú giải: chấm = 2014 trừ 2013, tính bằng điểm phần trăm; thanh sai số = khoảng tin cậy 95%, thanh nào cắt qua 0 nghĩa là không có chênh lệch rõ ràng. Xám = trên mọi lượt đăng ký học; cam = chưa rút tại ngày 14 (quy tắc của KPI). Mỗi loại được trình bày cho mọi kỳ mở và cho sáu module mở cả hai năm. |
| Runs differ | Các kỳ mở khác nhau | Các kỳ mở chênh lệch nhiều |
| All five early signs, inactivity included, go with later non-completio… | Cả năm dấu hiệu sớm, kể cả tình trạng không hoạt động, đều gắn với việc về sau không hoàn thành trong cùng kỳ mở, với mức tương tự ở năm 2013 và năm 2014. | Cả năm dấu hiệu sớm, kể cả tình trạng không hoạt động, đều liên quan đến việc không hoàn thành về sau trong cùng kỳ mở, với mức tương tự ở năm 2013 và năm 2014. |
| Key: dot = risk difference; whisker = 95% interval; dashed line = the … | Chú giải: chấm = chênh lệch nguy cơ; râu = khoảng tin cậy 95%; nét đứt = tiêu chí 5 điểm. Dấu hiệu về bài tính trên các kỳ mở có bài đến hạn tính đến ngày 27; dấu hiệu lượt nhấp tính trên mọi kỳ mở. | Chú giải: chấm = chênh lệch nguy cơ; thanh sai số = khoảng tin cậy 95%; nét đứt = tiêu chí 5 điểm. Dấu hiệu về bài tính trên các kỳ mở có bài đến hạn tính đến ngày 27; dấu hiệu lượt nhấp tính trên mọi kỳ mở. |
| Two years agree, but the yes-or-no click signs miss part of a graded a… | Kết quả hai năm khớp nhau, nhưng dấu hiệu lượt nhấp dạng có/không chỉ phản ánh một phần xu hướng biến thiên theo mức hoạt động (một chỗ chưa khớp đã biết của mô hình); ngoài ra, các nguyên nhân không được ghi nhận cũng có thể giải thích các mối liên hệ. | Kết quả hai năm khớp nhau, nhưng dấu hiệu lượt nhấp dạng có/không chỉ nắm được một phần quan hệ giữa mức hoạt động và nguy cơ (điểm chưa khớp đã biết của mô hình); ngoài ra, những nguyên nhân không có trong dữ liệu cũng có thể giải thích các mối liên hệ này. |
| Early-sign rule (the baseline) | Quy tắc dấu hiệu sớm (phương pháp cơ sở) | Quy tắc dấu hiệu sớm (cơ sở) |
| Key: grey = the link holds evidence (data, rule or result); blue = des… | Chú giải: xám = mắt xích có bằng chứng (dữ liệu, quy tắc hoặc kết quả); xanh = đã thiết kế, chưa chạy; chữ đỏ trên nền trắng = GAP (mắt xích chưa có bằng chứng) hoặc N.A. (chưa có kết quả); cột cam = trạng thái. | Chú giải: xám = có bằng chứng; xanh = đã thiết kế, chưa chạy; chữ đỏ = GAP (chưa có bằng chứng) hoặc N.A. (chưa có kết quả); cam = trạng thái. |
| GAP marks only what OULAD lacks: delivery mode, year of study, attenda… | GAP chỉ đánh dấu những gì OULAD không có: hình thức học, năm theo học, điểm danh và dữ liệu liên hệ. Phần dấu hiệu của KPI 1 (các sinh viên bị quy tắc đánh dấu) được tính trên OULAD; phần liên hệ cần đợt thí điểm. D1, D2 và D3 là ba quyết định ở slide 4. | GAP: điều OULAD thiếu (hình thức học, năm theo học, điểm danh, liên hệ); phần dấu hiệu của KPI 1 tính được trên OULAD, phần liên hệ cần thí điểm. D1: liên hệ với ai; D2: phân bổ hỗ trợ; D3: có mở rộng không; S1: điều kiện để mô hình thay quy tắc; FR1: quy tắc xem xét công bằng. |
| a list of 3 or 5 per 20 students per run, with the signs behind each n… | danh sách 3 hoặc 5 trên 20 sinh viên cho mỗi kỳ mở, kèm các dấu hiệu làm lý do cho mỗi tên. AQ4 được xem là đã trả lời khi danh sách đạt S1, đạt quy tắc FR1 (hoặc các nhóm bị đánh dấu đã được xem xét) và giả định thứ tự nguy cơ trùng với thứ tự nhu cầu hỗ trợ được nêu rõ là chưa kiểm chứng. | danh sách 3 hoặc 5 trên 20 sinh viên cho mỗi kỳ mở, mỗi tên kèm các dấu hiệu làm lý do. AQ4 được xem là đã trả lời khi danh sách đạt S1 (điều kiện để thay quy tắc), đạt quy tắc FR1 (quy tắc xem xét công bằng) hoặc các nhóm bị đánh dấu đã được xem xét; đồng thời giả định "thứ tự nguy cơ trùng với thứ tự nhu cầu hỗ trợ" được nêu rõ là chưa kiểm chứng. |
| D1 – Whom to contact (reversible) | D1 – Liên hệ với sinh viên nào (đảo ngược được) | D1 – Liên hệ với sinh viên nào (dễ đảo ngược) |
| The early-sign rule as the candidate list: interpretable, computable f… | Dùng quy tắc dấu hiệu sớm làm danh sách đề xuất: quy tắc dễ diễn giải, tính được từ dữ liệu trường đã có; từng phần của quy tắc đều gắn với việc về sau không hoàn thành ở năm 2013 và năm 2014. Một cán bộ kiểm tra từng tên. | Dùng quy tắc dấu hiệu sớm làm danh sách đề xuất: quy tắc dễ diễn giải, tính được từ dữ liệu trường đã có; từng phần của quy tắc đều liên quan đến việc không hoàn thành về sau ở cả năm 2013 và năm 2014. Một cán bộ kiểm tra từng tên. |
| D3 – Whether to extend (close to irreversible) | D3 – Có mở rộng không (gần như không thể đảo ngược) | D3 – Có mở rộng không (khó đảo ngược) |
| Where it helped most | Nơi AI hữu ích nhất | AI giúp ích nhiều nhất ở đâu |
| Keep 2014 out of every AQ3 choice; one early-sign rule; AQ3 and AQ4 as… | Không dùng năm 2014 cho bất kỳ lựa chọn nào của AQ3; một quy tắc dấu hiệu sớm duy nhất; AQ3 và AQ4 ở dạng thiết kế; mọi mối liên hệ được nêu đúng là mối liên hệ. | Không dùng năm 2014 cho bất kỳ lựa chọn nào của AQ3; một quy tắc dấu hiệu sớm duy nhất; AQ3 và AQ4 dừng ở thiết kế; mọi mối liên hệ chỉ được trình bày là liên hệ, không phải nhân quả. |
| On OULAD, an early list cannot rest on missed tasks alone, and the ear… | Trên OULAD, danh sách sớm không thể chỉ dựa vào bài bị bỏ lỡ; các dấu hiệu sớm có thể làm lý do bên cạnh mỗi tên để cán bộ kiểm tra. | Trên OULAD, danh sách sớm không thể chỉ dựa vào bài bị bỏ lỡ; các dấu hiệu sớm có thể đi kèm từng tên làm lý do để cán bộ kiểm tra. |
| All five early signs go with later non-completion in both years, a mis… | Cả năm dấu hiệu sớm gắn với việc về sau không hoàn thành ở cả hai năm (bỏ lỡ bài: 40,8 và 39,3 điểm), cùng chiều qua các module, trừ một ngoại lệ có khoảng tin cậy rộng. Đây là mối liên hệ. | Cả năm dấu hiệu sớm đều liên quan đến việc không hoàn thành về sau ở cả hai năm (bỏ lỡ bài: cao hơn 40,8 và 39,3 điểm phần trăm), cùng chiều qua các module, trừ một ngoại lệ có khoảng tin cậy rộng. Đây là mối liên hệ, không phải nhân quả. |
| No claim; uncertain. | Không khẳng định; chưa chắc chắn. | Không kết luận; chưa xác định. |
| Continuous measures; one add-drop rule. | Đại lượng liên tục; một quy tắc ngày 14. | Số đo liên tục; một quy tắc ngày 14. |
| Recount the baseline under the add-drop rule, replace assumed values, … | Tính lại mức cơ sở theo quy tắc ngày 14, thay giá trị giả định, phân loại rủi ro theo luật. | Tính lại mức cơ sở theo quy tắc ngày 14, thay giá trị giả định, phân loại rủi ro theo quy định. |
| Take-home: a missed task comes too late; count silence too, and test c… | Cần nhớ: dấu hiệu bỏ lỡ bài xuất hiện quá muộn; hãy tính cả tuần không hoạt động và kiểm chứng tác dụng của liên hệ trước khi tin. | Cần nhớ: dấu hiệu bỏ lỡ bài đến quá muộn; hãy tính cả tuần không hoạt động và kiểm chứng tác dụng của liên hệ trước khi mở rộng. |

Speaker notes: 9 notes changed by the same phrase rules ("gắn với việc về sau không hoàn thành", "bên cạnh mỗi tên", "đảo ngược được", slide 1 "rời xa").
