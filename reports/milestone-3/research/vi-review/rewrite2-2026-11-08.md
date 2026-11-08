# Rewrite after the second reader test – Vietnamese main text, Milestone 3 (2026-11-08)

Source of the flags: the second reader test (82 passages, Vietnamese files only). File:line is the line the reader test
cites in the `.vi.md` file before this rewrite. Each rewrite was checked against the English sentence for meaning and
numbers; no fact was added that the English report does not state. The fidelity fixes F1–F15 of
`rewrite-2026-11-08.md` were kept (no hedge, clause or scope restored that those fixes had removed).

Glossary rows applied (topic glossary `course-completion-early-contact.md`, rows changed before this rewrite):

- lift: glossed once in the document, at its first use (01-01, AQ4 in Table 1.1), as "lift, tức tỷ số giữa độ chính xác
  của danh sách (precision) và tỷ lệ nền (lift bằng 1 nghĩa là không hơn một danh sách ngẫu nhiên)"; plain "lift"
  everywhere else, including 04-01, 08-02, 10-00, 12-04 and 12-05 ("lift so với tỷ lệ nền của kỳ mở" where the English
  says "lift over the run's base rate"); the terms page names it "Lift (tỷ số giữa độ chính xác của danh sách và tỷ lệ
  nền)".
- recorded absence: "không có bản ghi (tính là 0)" in 04-02 (text, caption, table row) and on the terms page; "vắng bản
  ghi có ý nghĩa" no longer occurs.
- weekly contact capacity: gloss "(số sinh viên cán bộ liên hệ được trong một tuần)" kept only at its first use in the
  document (01-01, AQ4); removed in 04-01, 04-02, 07-03, 08-00 and 08-01.
- "module" for an OULAD module, "học phần" for a course of the university: applied where the distinction carries the
  point (07-03 (4), flag #64).

## Decisions per flag

| # | File:line | Decision | New wording or reason |
| :-- | :-- | :-- | :-- |
| 1 | 01-00:1 | glossary term – decision for the native user | "phiên bản cơ sở" (baseline) kept in the heading |
| 2 | 01-01:3 | fixed | "đợt thí điểm sẽ tính lại mức này từ hồ sơ của trường" |
| 3 | 01-01:5 | fixed | Circular sentence replaced: "Các dấu hiệu sớm này được xác định bằng quy tắc dấu hiệu sớm; ở Milestone 1, quy tắc này là …" (the previous sentence already names "dấu hiệu sớm của việc giảm tham gia học tập") |
| 4 | 01-01:9 | fixed | "so sánh theo hình thức học và theo sinh viên năm thứ mấy được thay bằng so sánh theo module và theo kỳ mở"; "kỳ mở" defined in the sentence before (#5) |
| 5 | 01-01:9 | fixed | Definition at first use: "Tổng thể nghiên cứu gồm các kỳ mở module của OULAD trong năm 2013–2014; mỗi kỳ mở là một lần module được tổ chức giảng dạy." The term "kỳ mở" itself stays for the native user |
| 6 | 01-01:9 | glossary term – decision for the native user | "lượt đăng ký học còn hiệu lực" kept |
| 7 | 01-01:11 | fixed | "Bảng 1.1 trình bày bốn câu hỏi phân tích (AQ) ở dạng hiện hành, tức sau các thay đổi của Milestone 2 và sau các quyết định của milestone này về những phần dữ liệu còn thiếu, …" |
| 8 | 01-01:17 | fixed | "Ở những sinh viên không hoàn thành, bài được chấm điểm đầu tiên bị bỏ lỡ rơi vào tuần nào?" |
| 9 | 01-01:18 | fixed | "D2; ngoài ra, AQ2 là cơ sở cho các lý do hiển thị cạnh tên từng sinh viên trong danh sách D1" |
| 10 | 01-01:19 | fixed | "Nếu dùng dữ liệu tính đến hết tuần 2 và hết tuần 4, mô hình xây dựng trên các kỳ mở năm 2013 dự báo việc không hoàn thành ở các kỳ mở năm 2014 tốt đến mức nào so với quy tắc dấu hiệu sớm?" ("độ chính xác" avoided: the glossary keeps it for precision) |
| 11 | 01-01:20 | glossary term – decision for the native user | "Chỉ định" (prescriptive) kept; the glossary forbids "đề xuất" |
| 12 | 01-01:20 | fixed | Question first, gloss in its own sentence: "Danh sách đó hơn danh sách ngẫu nhiên bao nhiêu và đạt tỷ lệ phát hiện (recall) bao nhiêu, …? Mức hơn được đo bằng lift, tức tỷ số giữa độ chính xác của danh sách (precision) và tỷ lệ nền (lift bằng 1 nghĩa là không hơn một danh sách ngẫu nhiên)." "(precision)" added at the first use, as the glossary Usage says |
| 13 | 01-01:22 | fixed | "các thay đổi này chỉ thu hẹp cách đo các câu hỏi trên OULAD, còn nội dung câu hỏi giữ nguyên" |
| 14 | 01-02:5 | fixed | "Tương tự, tám tệp của bản đề xuất Milestone 1 cũng giữ nguyên nội dung; phiên bản cơ sở được sao chép từ chính tám tệp này." (placed after the SHA-256 sentence, so "giữ nguyên" reads as the same checksum check) |
| 15 | 01-02:7 | fixed | From the updated English: "Như vậy, câu hỏi nào cũng giữ được một phần cốt lõi mà dữ liệu trả lời được; phần cốt lõi đó lớn hơn nhiều so với "một phần rất nhỏ" mà đề bài cảnh báo. Do đó, điều kiện đầu vào được đáp ứng …" |
| 16 | 02-00:5 | fixed | "Mỗi nhận định về dữ liệu trong phần này đều dựa trên một phép kiểm tra được tính bằng mã trên chính dữ liệu. Script đầu tiên …, `src/01_understand.py`, tính các phép kiểm tra đó và ghi kết quả vào …" |
| 17 | 02-01:5 | fixed | Split: "… trước khi nối bảng (Mục 6.2). Nhờ đó, mỗi bảng dữ liệu đã chuẩn bị chỉ có một đơn vị của mỗi dòng (grain) và đơn vị này được nêu rõ." |
| 18 | 02-01:13 | fixed | Time field "độ dài kỳ mở (số ngày)"; role "cho biết ngày kết thúc và tháng bắt đầu của kỳ mở" (the English cells name the same variables) |
| 19 | 02-01:21 | fixed | "mọi dòng của bảng con đều tìm thấy dòng tương ứng ở bảng cha" |
| 20 | 02-02:3 | fixed | "Biến final_result là kết quả thực của lượt đăng ký học, không phải một biến đại diện (proxy) dùng thay cho kết quả." |
| 21 | 02-02:7 | fixed | "đều mang ngày nộp −1, một giá trị giữ chỗ (placeholder) chứ không phải ngày nộp thật, nên …" |
| 22 | 02-02:7 | fixed | Split into four sentences: "Thứ ba, trọng số và số tín chỉ đang học không thể hiểu theo nghĩa trực tiếp của tên trường. Ở các kỳ mở GGG, bài làm trong kỳ có trọng số 0. Số tín chỉ đang học là tổng tín chỉ của mọi module mà sinh viên học cùng lúc [2]; trong đó, 60 tín chỉ …" |
| 23 | 02-03:5 | fixed | "các nhóm nhỏ hơn ngưỡng này được kiểm tra công bằng trên dữ liệu gộp của mọi kỳ mở" |
| 24 | 02-03:7 | fixed | Repetition removed: "Năm thuộc tính là thuộc tính dùng để kiểm tra công bằng; năm thuộc tính này nằm ngoài cả nhóm đặc trưng chính lẫn nhóm đặc trưng mở rộng của mô hình." (glossary form kept once; English change "outside both predictor sets") |
| 25 | 03-00:3 | fixed | Active, two sentences: "nhóm tác giả đếm lại mười ba số liệu khảo sát từ cùng các tệp gốc bằng một đoạn mã riêng, không dùng chung mã với script đó; đoạn mã này là phần khám phá bộ dữ liệu của nhóm tác giả. Cả mười ba số liệu đều khớp nhau …" |
| 26 | 03-01:3 | fixed | Concrete in the same sentence: "Riêng bảng lượt nhấp khác tài liệu ở đơn vị của mỗi dòng (grain), tức mức chi tiết mà một dòng biểu diễn: theo tài liệu, mỗi dòng ghi …, nhưng trên thực tế, 1.614.505 tổ hợp … xuất hiện ở nhiều dòng." |
| 27 | 03-01:3 | fixed | From the updated English, both hypotheses named: "Nếu các dòng này chỉ là những lần truy cập riêng biệt tình cờ có cùng số lượt nhấp, thì hai dòng của cùng một sinh viên, cùng tài nguyên và cùng ngày sẽ có số lượt nhấp bằng nhau với tần suất đúng bằng mức ngẫu nhiên. Mức ngẫu nhiên này được tính từ số lượt nhấp của riêng từng tài nguyên và bằng 24,0% số cặp dòng như vậy. Trên dữ liệu, 31,5% số cặp dòng có số lượt nhấp bằng nhau; tỷ lệ này cao hơn ở diễn đàn và trang nội dung, thấp hơn ở bài trắc nghiệm. Như vậy, có thể một số dòng là bản sao do hệ thống ghi nhật ký tạo ra, còn các dòng khác là những lần truy cập lặp lại thật; dữ liệu không cho biết dòng nào thuộc loại nào." Whether the exact duplicates sit inside the 31.5% is not stated in the English, so it is not added |
| 28 | 03-01:3 | fixed | "kết quả sẽ phình lên tới 89.347.197 dòng, nhiều hơn hẳn số dòng của cả hai bảng gốc" (row counts of both tables in Table 2.1: 173.912 and 10.655.280) |
| 29 | 03-01:3 | fixed | Paragraph split in two, as in the updated English (grain and duplicates; joins) |
| 30 | 03-02:3 | fixed | Reason first: "Do số giá trị thiếu ở ba trường trên (…) đều ít và ba trường nằm ở các bảng khác nhau, nhóm tác giả không kiểm tra các giá trị thiếu này có cùng xuất hiện trong một bản ghi hay không." |
| 31 | 03-03:3 | fixed | "chênh lệch này là dấu hiệu cho thấy thang chấm CMA có bước điểm lớn" (hedge "dấu hiệu" of F4 kept) |
| 32 | 03-03:5 | glossary term – decision for the native user | "nhóm tính KPI" kept, with its gloss at first use |
| 33 | 03-04:3 | fixed | "Số lượt nhấp trung bình mỗi tuần của một sinh viên đang đăng ký học đạt đỉnh ở tuần 3" |
| 34 | 03-04:3 | fixed | Link stated: "Với bài toán dự báo cho một kỳ mở muộn hơn, điều quan trọng là module nào được mở ở cả hai năm, vì chỉ khi đó kỳ mở năm 2014 mới có kỳ mở tương ứng năm 2013. Có 9 cặp …" (paired runs, Sections 5 and 6.3) |
| 35 | 03-05:3 | fixed | "mức Trung bình dành cho vấn đề làm thay đổi một thước đo với mức thay đổi đã biết" (English: "change a measure by a known amount") |
| 36 | 03-05:23 | fixed | DQ15 impact: "Chuỗi thời gian theo ngày, sau tuần 30" |
| 37 | 04-00:3 | fixed | Defined at first use: "… ở đúng mức độ khẳng định mà AQ đặt ra, tức đủ cho kết luận mạnh nhất mà AQ muốn rút ra." (glossary term kept) |
| 38 | 04-00:5 | fixed | "Dữ liệu giả lập không phải là một bước bổ sung, chẳng hạn bước thứ sáu, để giữ lại một AQ mà dữ liệu thực không hỗ trợ: …" |
| 39 | 04-01:10 | fixed | Glossary form with its gloss: "1.382 lượt đăng ký học đồng thời (diễn ra cùng lúc ở hai kỳ mở), 1.370 lượt trong số đó ở năm 2014" |
| 40 | 04-01:14 | fixed | Five paragraphs, one per change, as in the updated English (C09; C12; C06/C10; C11; C13) |
| 41 | 04-01:14 | fixed | From the updated English: "Con số 28.119 của Milestone 2 tính mọi lượt đăng ký học chưa hủy đăng ký vào ngày 14, kể cả 58 sinh viên đăng ký muộn. Quy tắc C09 loại 58 sinh viên này, nên nhóm tính KPI còn 28.061 lượt đăng ký học." |
| 42 | 04-01:14 | glossary term – decision for the native user | "kỳ mở huấn luyện" kept; sentence reworded so that the year comes first: "chỉ 12 lượt thuộc các kỳ mở năm 2013, tức các kỳ mở huấn luyện (C12)" |
| 43 | 04-01:14 | fixed | Appositive already removed by fidelity fix F6; sentence now "Tỷ lệ phát hiện này được so với mức tối đa mà một danh sách cùng độ dài có thể đạt." |
| 44 | 04-02:3 | fixed | Glossary row: "OULAD còn có trường hợp thứ tư trông giống dữ liệu thiếu nhưng thực chất không phải: không có bản ghi (tính là 0). Ở trường hợp này, chính việc thiếu một dòng dữ liệu đã ghi nhận một sự kiện, …"; caption and table row follow |
| 45 | 04-02:9 | fixed | "tham số của phép điền giá trị thiếu chỉ được tính trên các kỳ mở huấn luyện" ("trung vị" not added: the English cell says "filling") |
| 46 | 04-02:16 | fixed | "tăng cường dữ liệu (data augmentation), tức sinh thêm bản ghi nhân tạo để mở rộng dữ liệu" |
| 47 | 05-00:5 | fixed | "phạm vi lượt đăng ký học của từng bảng" |
| 48 | 05-00:11 | fixed | "kèm cờ cho biết lượt đăng ký học có còn hiệu lực vào ngày 13, ngày 14 và ngày 27 hay không" |
| 49 | 05-00:19 | fixed | V13 in two sentences: "V13: đếm lại các đặc trưng lượt nhấp khi bỏ bộ lọc theo ngày. Giá trị chỉ thay đổi ở những sinh viên có lượt nhấp sau thời điểm chốt dữ liệu, chứng tỏ bộ lọc theo ngày hoạt động đúng; …" |
| 50 | 05-00:21 | fixed | From the updated English: "làm cột kiểm tra công bằng, nằm ngoài cả nhóm đặc trưng chính lẫn nhóm đặc trưng mở rộng"; same in 09-00:4, 02-03:7 and the terms page |
| 51 | 05-00:22 | fixed | "Nhận định mà dự án cần chứng minh là khả năng dự báo cho một kỳ mở diễn ra sau (C07)" (glossary: claim → nhận định) |
| 52 | 05-00:24 | fixed | "do đó các kỳ mở của tập kiểm thử vẫn cho một phép đánh giá độc lập" |
| 53 | 06-01:3 | fixed | "gắn cờ cho các bản ghi chưa chắc chắn, tức các bản ghi có thể sai nhưng dữ liệu không đủ để kết luận" (Section 7.3 (3): flagged because the data cannot settle them) |
| 54 | 06-02:5 | fixed | Marked as general background: "Nói chung, một nguồn rò rỉ phổ biến là …" (the English gives no OULAD case, so none is added) |
| 55 | 06-02:24 | fixed | "Tuần của bài đến hạn sớm nhất mà sinh viên chưa nộp; chỉ xét các bài đến hạn trong thời gian sinh viên còn đăng ký học"; source "Bảng dữ liệu đã chuẩn bị assessment_due" (the view name stays as written) |
| 56 | 06-03:14 | fixed | From the updated English: "Số liệu thống kê theo kỳ mở (giá trị được tính trên chính kỳ mở đó)" |
| 57 | 06-03:16 | fixed | "9 kỳ mở này kiểm tra trực tiếp nhận định mà dự án cần chứng minh, tức khả năng dự báo cho một kỳ mở diễn ra sau" (restates Table 5.1, C07) |
| 58 | 06-03:18 | fixed | "Trong mỗi fold, nếu một sinh viên cũng có mặt ở kỳ mở được tách ra để đánh giá thì sinh viên đó bị loại khỏi dữ liệu huấn luyện của fold [13]." |
| 59 | 06-03:18 | fixed | From the updated English: "nhóm tác giả thay đổi giá trị của mọi dòng trong tập kiểm thử, rồi ước lượng lại các phép biến đổi; các tham số thu được vẫn giữ nguyên" |
| 60 | 07-00:3 | fixed | "Đề bài yêu cầu nhóm tác giả chứng minh hai điều: dữ liệu đã chuẩn bị phục vụ phân tích tốt hơn dữ liệu gốc, đồng thời vẫn chính xác và truy ngược được về nguồn." |
| 61 | 07-01:3 | fixed | "Bước chuẩn bị chỉ thay đổi biến kết quả hoặc số đếm khi có một quy tắc nêu rõ." |
| 62 | 07-02:3 | fixed | Gloss already reduced by fidelity fix F10; now "chỉ số mô tả (cột chỉ dùng để mô tả dữ liệu, không dùng làm đặc trưng)" (glossary term kept) |
| 63 | 07-02:5 | fixed | "các biến chính dùng để trả lời các AQ" |
| 64 | 07-03:11 | fixed | Glossary rule applied: "Tỷ lệ hoàn thành một kỳ mở module của OULAD được dùng thay cho tỷ lệ hoàn thành học phần của trường" |
| 65 | 07-03:13 | fixed | "Các kịch bản giả định rằng mỗi giảng viên kiêm cố vấn học tập phụ trách một nhóm như vậy, gồm 20 sinh viên." |
| 66 | 07-03:13 | fixed | From the updated English: "các kịch bản dùng danh sách 30 hoặc 40 sinh viên cho mỗi kỳ mở tại mỗi đợt lập danh sách" |
| 67 | 08-00:7 | fixed | "Ma trận này nối mục tiêu và các KPI với quyết định mà từng AQ hỗ trợ; với mỗi AQ, ma trận ghi các bước trung gian là loại phân tích, các biến gốc, bước chuẩn bị và các biến đã chuẩn bị [1]." |
| 68 | 08-00:12 | fixed | Active: "Riêng lựa chọn cách liên hệ và tỷ lệ liên hệ kịp thời của KPI phụ 2, nhóm tác giả để lại cho đợt thí điểm chứ không lấp bằng các giả định." |
| 69 | 08-01:3 | fixed | "bảng của mỗi mức dựa trên bảng của mức trước và bổ sung thêm thông tin" |
| 70 | 08-01:11 | fixed | "các nhóm lượt đăng ký học theo quy tắc của Mục 4.1 chỉ được ghi thành cột cờ, không dùng để lọc bỏ dòng" |
| 71 | 08-01:16 | glossary term – decision for the native user | "chỉ định" kept; sentence reworded so that the level is named: "biến một kết quả dự báo thành kết quả của phân tích chỉ định chỉ bằng cách kèm thêm lời khuyên [1]" |
| 72 | 08-02:13 | fixed | "số kỳ mở mà sinh viên học đồng thời, chỉ xét cho năm 2014" |
| 73 | 08-02:19 | fixed | "Với danh sách 5 sinh viên trên mỗi nhóm 20, quy tắc đánh dấu nhiều sinh viên hơn độ dài danh sách ở 7 trong 22 kỳ mở tại ngày 13 …" |
| 74 | 08-02:27 | fixed | "tỷ lệ liên hệ kịp thời (KPI phụ 2) cùng phần liên hệ của KPI phụ 1, tức số sinh viên có dấu hiệu sớm đã được liên hệ (C08)" (definition of KPI phụ 1, Section 1.1) |
| 75 | 09-00:10 | fixed (wording) | "vì bằng cấp mà sinh viên có trước khi vào học phản ánh mức độ chuẩn bị của sinh viên cho module"; a fuller comparison with the other five attributes is not added, because the English gives only this reason |
| 76 | 10-00:7 | fixed | "Trong mỗi lượt rà soát, tức một vòng soạn thảo rồi phản biện, một tác tử AI (agent, tức một hệ thống AI được giao một nhiệm vụ riêng) soạn sản phẩm và một tác tử AI khác phản biện sản phẩm đó" |
| 77 | 10-00:22 | fixed | "So sánh với mức ngẫu nhiên trên các cặp dòng cùng sinh viên, cùng tài nguyên và cùng ngày"; evidence "31,5% số cặp có số lượt nhấp bằng nhau, so với 24,0% nếu chỉ do ngẫu nhiên" |
| 78 | 10-00:25 | fixed | The English cell also states a principle; the twin now says so: "Nguyên tắc: xem kết quả của tập kiểm thử trong lúc chuẩn bị dữ liệu sẽ làm mất tính độc lập …" |
| 79 | 10-00:26 | fixed | "6 bài bị tính nhầm là bỏ lỡ tại ngày 27; kiểm tra bằng cách đọc mã nguồn" (restates the suggestion in the same row) |
| 80 | 10-00:29 | fixed | Two sentences: "Bên cạnh đó, AI kiểm tra rò rỉ thông tin (leakage auditor) nêu 8 phát hiện, đều được chấp nhận. Tác tử này là một phần của vai trò AI phản biện quy trình chuẩn bị và không tìm thấy …" |
| 81 | 10-00:35 | fixed | Principle stated at once: "… chỉ được chấp nhận một phần, vì nhóm tác giả luôn giữ nguyên tắc không xem kết quả của tập kiểm thử trong lúc chuẩn bị dữ liệu."; later "vì nếu xem kết quả, tập kiểm thử sẽ tham gia vào bước chuẩn bị, điều mà đề bài không cho phép [1]" |
| 82 | 10-00:39 | fixed | "và phần tự đánh giá những điểm mà các lượt rà soát giúp ích nhiều nhất" |

Totals: 82 flags; 76 fixed, 6 glossary terms for the native user (#1, #6, #11, #32, #42, #71; the sentences of #42 and
#71 were also reworded), 0 rejected. #75 is fixed in wording only: the reasoning the reader asked for is not in the
English.

## Recurring terms of the reader test

| Term | Handling |
| :-- | :-- |
| kỳ mở, lượt đăng ký học, còn hiệu lực, độ chính xác của danh sách, Chỉ định, nhóm tính KPI, phiên bản cơ sở, kỳ mở huấn luyện | Core glossary terms, unchanged: decision for the native user. "kỳ mở" now defined at its first use (01-01); "(precision)" added at the first use of "độ chính xác của danh sách" (01-01) |
| lift gloss | New glossary form, once in the document (01-01); plain "lift" elsewhere |
| vắng bản ghi có ý nghĩa | Replaced by "không có bản ghi (tính là 0)" (04-02, terms page) |
| năng lực liên hệ mỗi tuần (gloss) | Gloss only at the first use (01-01) |
| mức độ khẳng định | Glossary term kept; defined at its first use (04-00) |
| thuộc tính dùng để kiểm tra công bằng | Glossary term kept; repetition removed in 02-03 |
| đặc trưng chính (ambiguity) | Resolved by the English change: "nằm ngoài cả nhóm đặc trưng chính lẫn nhóm đặc trưng mở rộng" (02-03, 05-00, 09-00, terms page) |
| học phần vs module | Existing rule applied where the distinction carries the point (07-03) |
| grain, tập kiểm thử (các kỳ mở năm 2014), được xét | Glossary forms kept; "được xét" removed at the flagged lines (05-00:5, 08-01:11) |

## English changes carried into the twins

- 03-01: the duplicate-row test spelled out (separate visits with the same count would give equal counts as often as
  chance, 24.0% of pairs; observed 31.5%, more for forums and content pages, less for quizzes; some rows may be copies
  and others real repeated visits, and the data cannot tell which); the joins form their own paragraph.
- 01-02: every question keeps a core that the data answer, far from the very small part the brief warns about, so the
  entry gate holds.
- 04-01: five paragraphs, one per change; the Milestone 2 count of 28,119 explained as every enrolment still registered
  on day 14.
- 06-03: leakage-table row "Số liệu thống kê theo kỳ mở (giá trị được tính trên chính kỳ mở đó)"; the check refits the
  transforms after the values of every test row had been altered.
- 07-03: the 10% coverage is the coverage the team requires before the CMA score enters the Milestone 4 predictor set
  ("thấp hơn mức bao phủ 10% mà nhóm tác giả yêu cầu trước khi đưa điểm CMA vào nhóm đặc trưng của Milestone 4"); the
  support-office scenarios use 30 or 40 students per run at each review point.
- 00-2, 02-03, 05-00, 09-00: audit attributes are outside both predictor sets (primary and extended).

## Files changed

Main text: 01-01, 01-02, 02-00, 02-01, 02-02, 02-03, 03-00, 03-01, 03-02, 03-03, 03-04, 03-05, 04-00, 04-01, 04-02,
05-00, 06-01, 06-02, 06-03, 07-00, 07-01, 07-02, 07-03, 08-00, 08-01, 08-02, 09-00, 10-00. Front matter: 00-2 (Audit
attribute, Lift, Recorded absence). Appendices, lift gloss only: 12-04 (traceability row of AQ4, Change Log row C13, C13 paragraph), 12-05
(A4, critique 1). 01-00 is unchanged (its only flag is a glossary term). No English or glossary file was edited.

## Checks

- `venv/bin/python .agents/skills/build-report/scripts/check_parity.py --report reports/milestone-3/report --lang vi`:
  41 pairs, 0 errors, 14 warnings, all inside the verbatim English AI prompts of 12-05 (expected). A first run found
  1 error (glossary: "chương trình" without "đào tạo" in the agent gloss of 10-00) and 2 warnings (comma before "và" in
  01-02 and 06-01); all three were fixed before the final run.
- `venv/bin/python .agents/skills/build-report/scripts/check_abbreviations.py --report reports/milestone-3/report --lang vi`:
  15 abbreviations, 0 violations.
- `venv/bin/python .agents/skills/build-report/scripts/translation_status.py --report reports/milestone-3/report --lang vi --mark …`
  with the 31 English paths of the edited files: recorded 31; status afterwards: 41 sections, 0 need translation.
- Still to run: a fidelity pass by a reviewer other than the rewrite agent (`review.md` pass 2) on the rows above, a
  third reader test on the rewritten files, and the native user's decision on the six deferred glossary terms.

## Fidelity re-read

Passes 1 and 2 of `review.md` on 2026-11-08, by a reviewer other than the rewrite agent (reference.md 4.3, stage 5: the
fixes have been read again). Scope: the 82 rows above, each read first alone in its current `.vi.md` place, as a
Vietnamese lecturer reading it for the first time, then against the English sentence(s) for meaning, numbers, hedges,
actors, negations and citations. In addition, the passages that render the recent English changes were read sentence by
sentence: 03-01 (duplicate-row test; joins paragraph), 01-02 (entry gate), 04-01 (five paragraphs), 06-03 (cohort
statistic row; check with altered test rows), 07-03 (10% coverage; 30 or 40 per run at each review point), and "outside
both predictor sets" in 00-2, 02-03, 05-00 and 09-00. The deferred core terms were left unchanged.

| # | File:line (current) | Problem | Fix |
| :-- | :-- | :-- | :-- |
| R1 | 04-00:5 (row #38) | Unclear: "một bước bổ sung, chẳng hạn bước thứ sáu" says "for example the sixth step"; the English says synthetic data are not a sixth step | "Dữ liệu giả lập không phải là bước thứ sáu, nối tiếp năm bước trên, để giữ lại một AQ …" |
| R2 | 04-00:3 (row #37) | Added fact: the gloss "kết luận mạnh nhất" adds "strongest", which the English ("the level of claim it makes") does not say | "tức đủ cho kết luận mà AQ muốn rút ra" |
| R3 | 03-01:3 (row #27) | "với tần suất đúng bằng mức ngẫu nhiên" adds "exactly"; the English says "as often as chance gives" | "với tần suất ngang mức ngẫu nhiên" |
| R4 | 03-04:3 (row #34) | Not exact: "module nào được mở ở cả hai năm"; the English counts pairs of module and start month | "một module có được mở vào cùng tháng bắt đầu ở cả hai năm hay không" |
| R5 | 02-03:7 (row #24) | Clumsy on first reading: "Năm thuộc tính là thuộc tính …; năm thuộc tính này …" repeats the subject | One sentence: "Năm thuộc tính trong số đó là thuộc tính dùng để kiểm tra công bằng và nằm ngoài cả nhóm đặc trưng chính lẫn nhóm đặc trưng mở rộng của mô hình." |
| R6 | 10-00:7 (row #76) | Two "tức" glosses in one clause | Agent gloss: "(agent, là hệ thống AI được giao một nhiệm vụ riêng)" |
| R7 | 01-01:9 (clause of row #6) | "khi thời hạn đăng ký hai tuần đầu kỳ mở đã đóng" parses awkwardly | "tức sau khi thời hạn đăng ký (kéo dài đến hết hai tuần đầu kỳ mở) đã kết thúc" (C03, Section 2.2) |
| R8 | 00-2:32 (terms page, Recorded absence) | "Trường hợp việc không có dòng dữ liệu tự nó ghi nhận …" is hard to parse | "Trường hợp chính việc thiếu một dòng dữ liệu đã ghi nhận một sự kiện, …", the 04-02 wording |
| R9 | 09-00:8 (paragraph with "outside both predictor sets") | Connector "Ngược lại" marks a contrast where the English adds a point ("and a dataset without group membership cannot be audited at all"); "at all" lost | "Ngoài ra, … thì hoàn toàn không thể kiểm tra công bằng [14]." |
| R10 | 08-02:25 (questions not yet feasible) | Added fact: "chuyển tiếp đến phòng công tác sinh viên" names the referral target, which only the Milestone 1 proposal states, not this report ("a referral") | "giới thiệu sinh viên đến một đơn vị hỗ trợ khác" |

Checked and kept:

- 03-01:5 (row #28) "nhiều hơn hẳn số dòng của cả hai bảng gốc": a comparison with the row counts of Table 2.1 (173,912 and
  10,655,280), which a first reading needs to see why the direct join is wrong.
- 01-01:20 (row #12) "lift bằng 1 nghĩa là không hơn một danh sách ngẫu nhiên": the English terms page (Lift) states it.
- 03-03:3 "(một sinh viên, một tài nguyên, một ngày)" for the 6,977-click record: Appendix I (detail of DQ16) states it.
- 04-01:14 "kể cả 58 sinh viên đăng ký muộn": what the English says when C09 removes the 58 late registrants from 28,119.
- 04-01:22 "trượt" in the precision definition: the same word as in the precision definitions of 00-2 and 12-04; no
  glossary row forbids it.
- 08-02:14 reason for the activity-only day-13 list (fidelity fix F11): Section 3.4.

The recent English changes are rendered in full and in order: the chance test of 03-01 (24.0% expected, 31.5% observed,
more for forums and content pages, less for quizzes; some rows copies, others real repeats, the data cannot tell which)
and its separate joins paragraph; the entry-gate conclusion of 01-02; the five paragraphs of 04-01 (C09 with 28,119 and
28,061; C12; C06/C10; C11; C13); the cohort-statistic row and the altered-test-rows check of 06-03; the 10% coverage the
team requires before the CMA score enters the Milestone 4 predictor set and the 30 or 40 students per run at each review
point in 07-03; and "nằm ngoài cả nhóm đặc trưng chính lẫn nhóm đặc trưng mở rộng" in 00-2, 02-03, 05-00 and 09-00.

English sentences to check (not edited):

- 03-03 (1): "a single record reaches 6,977 clicks" sits in a sentence about clicks per enrolment, so "record" reads as an
  enrolment; Appendix I says it is one click record (one student, one resource, one day).
- The scope question noted after the earlier fidelity check (07-03 (2) against Appendix V, critique 7) is resolved: 07-03
  now states the 10% coverage for the CMA score only.

Result: 82 rows checked; 80 read clearly on first reading, 2 did not (#38, #24); 10 problems fixed in 10 places across
9 files (00-2, 01-01, 02-03, 03-01, 03-04, 04-00, 08-02, 09-00, 10-00): 5 fidelity (R2, R3, R4, R9, R10) and 5 clarity
(R1, R5, R6, R7, R8). No number, citation or identifier was found moved or altered.

- `venv/bin/python .agents/skills/build-report/scripts/check_parity.py --report reports/milestone-3/report --lang vi`:
  41 pairs, 0 errors, 14 warnings, all inside the verbatim English prompts of 12-05 (expected).
- `venv/bin/python .agents/skills/build-report/scripts/check_abbreviations.py --report reports/milestone-3/report --lang vi`:
  15 abbreviations, 0 violations.
- `venv/bin/python .agents/skills/build-report/scripts/translation_status.py --report reports/milestone-3/report --lang vi --mark …`
  with the 9 English paths: recorded 9; status afterwards: 41 sections, 0 need translation, 0 orphaned files.
