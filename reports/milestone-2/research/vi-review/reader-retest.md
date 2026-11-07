# Reader re-test of the Vietnamese Milestone 2 report

Reader role: a Vietnamese lecturer of data analytics, marking the report and reading only the `.vi.md` files (main text 01-00 to 09-00, plus the abbreviation and glossary pages 00-1 and 00-2). Evidence codes and citations in square brackets were ignored. Line numbers are those of the `.vi.md` files on 2026-11-06.

Overall judgement: yes, a reader of the field could explain the document afterwards. The chain is clear on first reading: frozen Milestone 1 baseline, four AQs turned into data requirements and six must-have gates, seven candidates screened, OULAD chosen on condition, file-level checks, coverage per AQ, eight controlled changes. Most sentences are short, natural Vietnamese and the tables carry the argument well. Comprehension breaks down in a handful of dense spots, not across the document: (a) the data-timing logic (who receives what, when, and why a withdrawal must not count as a signal or as a hit), (b) the G3 / training-versus-evaluation argument about how many runs per module and start month exist, which appears three times (06-00, 07-01, 07-02) and is hard each time, (c) the scoring-matrix arithmetic in 4.2, and (d) the G5 proof via `num_of_prev_attempts`. One real ambiguity ("năm bảng" = five tables or "the year table"?) and one sentence I could not resolve ("bài đến hạn chậm nhất vào cuối tuần 2") need rewording. The term "lượt mở module" is learnable thanks to the glossary but appears about 39 times and, alongside "lượt tổ chức" and "học phần", leaves the reader unsure whether three things or one are meant.

## Passages that stopped me

| # | File:line | Quote | What stopped me | Clarity (1–3) |
| :-- | :-- | :-- | :-- | :-- |
| 1 | 01-01-frozen-baseline.vi.md:3 | "nhờ đó mọi thay đổi về sau đều nhìn thấy được" | Calque of "so that any later change is visible"; a Vietnamese writer would say "nhờ đó có thể phát hiện mọi thay đổi về sau". | 3 |
| 2 | 01-01-frozen-baseline.vi.md:5 | "Cả hai con số này đều là giả định của kịch bản." | "kịch bản" is never introduced: which scenario? I guessed the course's fictional case study. | 2 |
| 3 | 01-01-frozen-baseline.vi.md:5 | "giống cách Thông tư 83/2026 thống kê sinh viên thôi học" | Unclear whether the circular excludes these students or merely counts dropouts; the comparison is compressed. | 3 |
| 4 | 01-01-frozen-baseline.vi.md:5 | "tỷ lệ liên hệ sinh viên có dấu hiệu sớm: trong số sinh viên có dấu hiệu sớm tính đến tuần 4" | Missing head noun: early sign of what (disengagement? risk of failing)? "Dấu hiệu sớm" is never defined; I had to infer "dấu hiệu nguy cơ". | 2 |
| 5 | 01-01-frozen-baseline.vi.md:5 | whole paragraph (Business Goal → SMART Goal → denominator → exclusions → three KPIs) | Too many ideas in one paragraph; the three KPI definitions deserve their own paragraph or a list. | 2 |
| 6 | 01-01-frozen-baseline.vi.md:12 | "tuần sinh viên lần đầu bỏ lỡ một bài được chấm điểm" | Missing relative "mà"; "bài được chấm điểm" is heavy (plainer: "bài kiểm tra tính điểm"). | 3 |
| 7 | 01-01-frozen-baseline.vi.md:13 | "D2; lý do cụ thể ghi cạnh mỗi tên trong danh sách liên hệ (D1)" | D1 is used here before it is defined in the next row; D1–D3 are never introduced as a set. | 2 |
| 8 | 01-02-scope-change-log.vi.md:5 | "được giữ làm yêu cầu dữ liệu cho đợt thí điểm" | Unnatural; I understood "để lại như một yêu cầu dữ liệu, sẽ thu thập trong đợt thí điểm" only after rereading. | 2 |
| 9 | 01-02-scope-change-log.vi.md:5 | "mỗi lượt mở module kéo dài khoảng chín tháng" | First use of "lượt mở module" in the main text without a gloss (glossary has it, main text does not). | 3 |
| 10 | 02-01-aq-data-matrix.vi.md:13 | "kết quả sau khi liên hệ" | Whose outcome: the student's final result, or whether the contact succeeded? Ambiguous. | 3 |
| 11 | 02-01-aq-data-matrix.vi.md:15 | "chỉ được đáp ứng một phần (Partial, Phụ lục V)" | Untranslated "Partial" left in brackets; elsewhere the report says "Một phần". | 3 |
| 12 | 02-01-aq-data-matrix.vi.md:20 | "có ít nhất ba lượt tổ chức của cùng các học phần ... trong đó có một lượt muộn hơn để đánh giá mô hình" | "lượt tổ chức" is a third name for the same thing; "muộn hơn" than what (than the training runs)? | 2 |
| 13 | 02-01-aq-data-matrix.vi.md:22 | "G5 Quyền riêng tư và liên kết" | "liên kết" alone is vague; I guessed "liên kết bản ghi giữa các bảng". | 3 |
| 14 | 02-02-requirements-by-level.vi.md:10 | "để kiểm tra mức độ liên quan có giống nhau ở từng nhóm sinh viên hay không" | "mức độ liên quan" between what and what? (signal and non-completion). Needs the two terms named. | 2 |
| 15 | 02-02-requirements-by-level.vi.md:12 | "Thứ tự ưu tiên trong giới hạn của các ràng buộc" | Abstract and translated; plainer: "thứ tự ưu tiên liên hệ khi số lượt liên hệ bị giới hạn". | 3 |
| 16 | 02-03-prediction-point-leakage.vi.md:3 | "Phiên bản cơ sở giả định dữ liệu đến tay cán bộ chậm khoảng một tuần." | Data does not reach staff; the list does. Also "cán bộ" = which staff (cố vấn học tập?). Had to reread to get the one-week lag logic. | 2 |
| 17 | 02-03-prediction-point-leakage.vi.md:11 | "Giá trị trung bình theo học phần, phép chuẩn hóa thang đo và phép mã hóa biến phân loại, chỉ được ước lượng trên các học kỳ dùng để huấn luyện..." | Too many ideas in one cell; "ước lượng phép mã hóa" is odd Vietnamese (one estimates parameters, not an encoding). | 2 |
| 18 | 02-03-prediction-point-leakage.vi.md:13 | "việc sinh viên rút học phần không bị tính thành dấu hiệu dự báo chính việc rút đó" | Circular wording; understood only after reading the two rules that follow. | 2 |
| 19 | 02-03-prediction-point-leakage.vi.md:13 | "danh sách có tên sinh viên đó không được tính là đã phát hiện đúng" | Subject is "danh sách" but the meaning is "sinh viên đó không được tính là phát hiện đúng"; source-language order. | 2 |
| 20 | 03-00-search-strategy.vi.md:6 | "trang chỉ chép lại metadata từ nguồn khác (metadata thứ cấp)" | Understandable but sounds translated; "metadata thứ cấp" is not a term colleagues use. | 3 |
| 21 | 04-01-criteria-gates.vi.md:6 | "Điểm số làm cơ sở cho phần thảo luận, nhưng các điều kiện bắt buộc mới quyết định lựa chọn." | Fine on reread; "làm cơ sở cho phần thảo luận" is vague (plainer: "điểm số chỉ để tham khảo"). | 3 |
| 22 | 04-01-criteria-gates.vi.md:6 | "Những thông tin mà tài liệu chưa làm rõ nhưng tệp dữ liệu có thể xác nhận được nhóm ghi thành điều kiện cần kiểm tra..." | Garden path: "xác nhận được nhóm" reads first as "confirmed by the team"; long fronted object with no comma. | 2 |
| 23 | 04-02-selection-matrix.vi.md:3 | "Sáu cột tiêu chí của đề bài bao quát tám tiêu chí, vì có hai cột ghép đôi tiêu chí ... Tổng điểm còn tính thêm hai tiêu chí không có cột riêng" | Arithmetic of columns vs criteria (6 → 8 → 10) is hard to hold; I could not check OULAD's 12 from the table without Appendix II. | 2 |
| 24 | 04-02-selection-matrix.vi.md:7 | column header "Biến kết quả / thời điểm" | "thời điểm" of what? I guessed "mốc thời gian của biến giải thích". | 3 |
| 25 | 04-02-selection-matrix.vi.md:9 | "Được chọn, với điều kiện được xác nhận ở Mục 6" | Reads as "the condition was confirmed"; meaning is "conditions to be checked in Section 6". | 3 |
| 26 | 04-02-selection-matrix.vi.md:17 | "XuetangX có hoạt động kèm ngày, nhưng nhãn bỏ học chỉ có hai giá trị" | Why two values disqualify is not stated in the sentence (no withdrawal vs fail distinction, link to G1). | 2 |
| 27 | 04-02-selection-matrix.vi.md:17 | whole paragraph (selection, other candidates, three conditions, result of Section 6) | Very long paragraph mixing reasons, rejections and conditions; I lost track of which condition was met. | 2 |
| 28 | 04-02-selection-matrix.vi.md:19 | "Do đó, mỗi module có ít lượt mở so sánh được với nhau hơn." | Comparative without a clear comparator; understood after rereading. | 3 |
| 29 | 05-00-acquisition-provenance.vi.md:17 | "Bằng chứng toàn vẹn" | Calque of "integrity evidence"; plainer "Kiểm tra tính toàn vẹn". | 3 |
| 30 | 05-00-acquisition-provenance.vi.md:20 | "Hai bản chỉ khác nhau ở cách ghi giá trị thiếu trong năm bảng" | Real ambiguity: "năm bảng" = five tables or "the year table"? Should be "trong 5 trên 7 bảng". | 2 |
| 31 | 06-00-structural-verification.vi.md:3 | "Bước này chưa làm sạch và chưa khám phá dữ liệu" | A step as the subject of "làm sạch"; sounds translated ("ở bước này, nhóm chưa..."). | 3 |
| 32 | 06-00-structural-verification.vi.md:9 | "module, lượt mở module; duy nhất" | Telegraphic "duy nhất"; I inferred "tổ hợp khóa không trùng". | 3 |
| 33 | 06-00-structural-verification.vi.md:11 | "5.243 trang học liệu thiếu tuần dự kiến" | "trang học liệu" and "tuần dự kiến" are unusual; meaning (VLE resource, planned week) only guessed. | 3 |
| 34 | 06-00-structural-verification.vi.md:17 | "đều có dòng tương ứng ở bảng gốc mà bản ghi đó tham chiếu đến" | "bảng gốc" could mean the original/raw table; meaning is "bảng cha" (referential integrity). | 2 |
| 35 | 06-00-structural-verification.vi.md:19 | "Ở cả 1.309 trường hợp một sinh viên học lại cùng một module, số lần đã học trước đó đều tăng lên. Số lần học trước chỉ có thể tăng nếu..." | The proof of stable IDs is compressed; I needed two readings to see the argument (attempt counter increases → same person). | 2 |
| 36 | 06-00-structural-verification.vi.md:19 | "mỗi module có nhiều nhất một lượt mở sớm hơn và một lượt mở muộn hơn có cùng tháng bắt đầu" | Abstract; a concrete example (BBB: 2013B → 2014B) would make it immediate. | 2 |
| 37 | 06-00-structural-verification.vi.md:19 | "1 trong 22 lượt mở module có bài đến hạn chậm nhất vào cuối tuần 2" | Could not decide: "latest due date is end of week 2" or "has an assessment due no later than end of week 2". Plainer: "có bài đến hạn trước khi hết tuần 2". | 1 |
| 38 | 06-00-structural-verification.vi.md:19 | "3.097 lượt đăng ký đã kết thúc vào hoặc trước ngày 0, còn 28.119 lượt vẫn còn đăng ký vào ngày 14; các lượt đăng ký này tạo thành mẫu số" | "các lượt đăng ký này" — which group? And 3.097 + 28.119 ≠ 32.593: where are the rest (withdrew between day 1 and 13)? Not said. | 2 |
| 39 | 07-01-traceability.vi.md:11 | "đánh giá trên các lượt mở năm 2014 của 9 cặp module – tháng bắt đầu có cả lượt năm 2013 và năm 2014" | "cặp module – tháng bắt đầu" is a dense noun stack; understood only after reading 06-00 again. | 2 |
| 40 | 07-01-traceability.vi.md:12 | "Mô phỏng xếp hạng với số lượt liên hệ tối đa mỗi tuần theo giả định" | Understandable; translated noun chain. | 3 |
| 41 | 07-01-traceability.vi.md:14 | "đúng yêu cầu của sản phẩm B trong đề bài, tức ma trận truy vết đã cập nhật" | "sản phẩm B" means nothing to a reader without the brief; deliverable lettering not introduced. | 2 |
| 42 | 07-02-gaps-revisions.vi.md:3 | "khi đó, báo cáo chỉ đưa ra nhận định ở mức hẹp hơn so với khi có dữ liệu đó" | Abstract rule; understood after rereading. | 2 |
| 43 | 07-02-gaps-revisions.vi.md:5 | "Module CCC và các lượt mở tháng 2 của EEE và GGG không có lượt mở sớm hơn có cùng tháng bắt đầu, nên các lượt này chỉ dùng để đánh giá, không dùng để huấn luyện" | Logic gap: if there is no earlier run, what model evaluates them (one trained on other modules?). Not stated. | 2 |
| 44 | 07-02-gaps-revisions.vi.md:5 | "vẫn là yêu cầu cho đợt thí điểm" | "vẫn là" implies a history; plainer "được để lại làm yêu cầu dữ liệu cho đợt thí điểm". | 3 |
| 45 | 08-00-risks-ethics.vi.md:9 | "Ba vấn đề dữ liệu cũng cần được quyết định rõ ở Milestone tiếp theo, thay vì tự ý sửa mà không ghi nhận." | A problem is not "decided"; meaning "cách xử lý ... cần được quyết định". Sounds translated. | 3 |
| 46 | 09-00-genai-reflection.vi.md:14 | "các điều kiện bắt buộc phải đòi hỏi bộ dữ liệu có ngày rút ... Các điều kiện bắt buộc hiện có đòi hỏi đủ hai thông tin đó" | "phải đòi hỏi" double modal; repetition of "đòi hỏi" makes the point (critique accepted, gates already include it) hard to see. | 2 |
| 47 | 09-00-genai-reflection.vi.md:14 | "nhóm hạ điểm xuống đúng mức mà tài liệu ghi nhận" | Translated; plainer "nhóm chỉ cho điểm theo những gì tài liệu ghi rõ". | 3 |

Counts: clarity 1 = 1; clarity 2 = 26; clarity 3 = 20 (47 passages).

## Recurring terms that feel invented or unnatural

| Term | Count in main text | Why it hurts | Plainer word a colleague would use |
| :-- | :-- | :-- | :-- |
| lượt mở module (and short form "lượt mở") | 25 (39 incl. "lượt mở") | Invented calque of "presentation"; competes with "lượt tổ chức" and "học phần" for the same idea | "đợt mở lớp", "khóa (kỳ) tổ chức module", or "kỳ học của module" |
| lượt tổ chức | 3 | Third synonym, makes the reader wonder if it is a different unit | use the same term as above throughout |
| bài được chấm điểm | 14 | Heavy passive calque of "graded assessment" | "bài đánh giá tính điểm", "bài kiểm tra" |
| mức độ liên quan | 4 | Used without naming the two variables; colleagues say "mối liên hệ" / "tương quan" | "mối liên hệ giữa dấu hiệu và việc không hoàn thành" |
| dấu hiệu sớm | 2 | Never defined; head noun missing | "dấu hiệu nguy cơ sớm" |
| giữ làm yêu cầu (dữ liệu) | 2 | Unnatural verb choice | "để lại làm yêu cầu dữ liệu", "chuyển thành yêu cầu dữ liệu cho đợt thí điểm" |
| đến tay cán bộ | 2 | Colloquial, and "cán bộ" unspecified | "được gửi đến cố vấn học tập" |
| phiên bản cơ sở (đã chốt) | 6 | Learnable, but "baseline" for a document version sounds technical-translated | "bản đề xuất đã chốt của Milestone 1" |
| thời điểm chốt dữ liệu / thời điểm dự báo | 10 | Two names for one moment; reader checks the glossary to confirm | pick one: "mốc chốt dữ liệu" |
| trang học liệu / tuần dự kiến | 2 | Opaque for VLE site and planned week | "tài nguyên trên VLE", "tuần theo kế hoạch" |
| bảng gốc | 1 | Ambiguous (raw vs parent table) | "bảng cha" or "bảng được tham chiếu" |
| Partial (untranslated) | 1 | Inconsistent with "Một phần" elsewhere | "Một phần" |

The five terms that hurt most: "lượt mở module" (with "lượt tổ chức"), "bài được chấm điểm", "mức độ liên quan", "dấu hiệu sớm", "giữ làm yêu cầu dữ liệu".
