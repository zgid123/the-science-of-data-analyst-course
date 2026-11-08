# Vietnamese native review – group G4 (Sections 9–10, references, appendices I–VI)

Reviewer: native-review agent (fresh reader; not the translator). Protocol: `build-report/languages/vi/review.md`, three passes per file (reader, fidelity, checklist), with `guide.md`, `lessons.md` and the merged glossary (`glossary.py --lang vi --task milestone-3 show`) as references. Settled cross-group decisions applied: validation checks and summary → "kiểm tra"; data profiling → "khảo sát dữ liệu (profiling)"; OU tutor → "giảng viên hướng dẫn"; module run → "lượt mở module"/"lượt mở"; enrolment → "lượt đăng ký học"; lineage → "dòng dõi dữ liệu (lineage)"; severity Cao/Trung bình/Thấp. Code names, IDs, numbers, [n] citations and the English quoted prompts (lines starting ">") are unchanged.

Glossary coverage before the passes (`glossary.py --lang vi --task milestone-3 coverage --report reports/milestone-3/report`): 10 drifting concepts. Those touching G4: deprivation band (12-04 C04 said "nhóm IMD" → now "mức khó khăn của khu vực (nhóm IMD)"; 09, 12-03 and 12-05 already use the short glossary form), enrolment (G4 uses "lượt đăng ký học"; 12-03 had "biết khi ghi danh" ×3, now "biết khi đăng ký học"), declared disability (09 now "sinh viên tự khai có khuyết tật"), grain (12-01 DQ01/DQ02 use "mức chi tiết"), non-completion (G4 uses bare "không hoàn thành" for OULAD, as settled), aggregate, scaling/encoding, fact and coverage (not used in G4 prose, or only in table cells where the short form fits).

Recurring patterns corrected: (1) "kiểm định" and "lập hồ sơ dữ liệu / hồ sơ dữ liệu" left over in appendices and section 10 (settled decisions); (2) "due by day d / by c" rendered as "trước ngày d / trước c", which drops the cut-off day itself – now "chậm nhất vào ngày d", "tính đến thời điểm chốt", "chậm nhất tại c"; (3) incomplete or run-on sentences (section 10 enumeration, rule alternatives in C10); (4) meaning shifts on who made the synthetic test records (AI drafted them; the twin said "do nhóm tự tạo"); (5) glossary slips: limitation → "hạn chế", proxy → "chỉ số đại diện"/"biến đại diện", generalisation → "tổng quát hóa", England → "xứ Anh (England)", "tinh chỉnh" (fine-tuning) used for hyperparameter tuning, fold glossed at first use.

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 09-00-ethics-limitations | 1 | 3.3 Glossary forms (limitation = hạn chế) | # 9. Đạo đức, thiên lệch và giới hạn | # 9. Đạo đức, thiên lệch và hạn chế |
| 2 | 09-00-ethics-limitations | 6 | 3.3 Glossary forms (proxy variable) | các biến đại diện gián tiếp (proxy) | các biến đại diện (proxy) |
| 3 | 09-00-ethics-limitations | 9 | 3.5 Plain wording (calque 'bị đại diện thiếu') | sinh viên tự khai có khuyết tật bị đại diện thiếu rõ rệt; | sinh viên tự khai có khuyết tật chiếm tỷ lệ rất thấp trong dữ liệu; |
| 4 | 09-00-ethics-limitations | 12 | 3.5 Head nouns present; 3.3 glossary (declared disability) | gồm 3.164 lượt đăng ký học có khai báo khuyết tật và 216 lượt từ 55 tuổi trở lên | gồm 3.164 lượt đăng ký học của sinh viên tự khai có khuyết tật và 216 lượt của sinh viên từ 55 tuổi trở lên |
| 5 | 09-00-ethics-limitations | 17 | 3.5 Written connectives ('Với' opener) | Với đợt thí điểm | Đối với đợt thí điểm |
| 6 | 09-00-ethics-limitations | 18 | 3.1 Light function words ('việc'); clear actor | [17]; việc xử lý phải gắn với một mục đích cụ thể [17]; luật cũng không quy định ngoại lệ chung cho nghiên cứu đối với yêu cầu về sự đồng ý | [17]; dữ liệu chỉ được xử lý cho một mục đích cụ thể [17]; luật cũng không quy định ngoại lệ chung cho mục đích nghiên cứu đối với yêu cầu phải có sự đồng ý |
| 7 | 09-00-ethics-limitations | 21 | 3.1 Collocations | các module đào tạo từ xa của Vương quốc Anh | các module đào tạo từ xa tại Vương quốc Anh |
| 8 | 09-00-ethics-limitations | 22 | 3.5 Head nouns present (no 'việc + verb') | tác động nào của việc liên hệ sinh viên | tác động nào của hoạt động liên hệ sinh viên |
| 9 | 10-00-genai-reflection | 11 | 3.1 Complete sentence (enumeration ran into 'cùng'); 3.5 semicolons | Các script này được kiểm chứng bằng 13 con số trùng khớp với một lần đếm lại độc lập, chín kiểm thử đơn vị, sáu đặc trưng được tính lại cho từng dòng mà không có khác biệ … | Các script này được kiểm chứng bằng bốn cách: 13 con số trùng khớp với một lần đếm lại độc lập; chín kiểm thử đơn vị; sáu đặc trưng được tính lại cho từng dòng mà không l … |
| 10 | 10-00-genai-reflection | 13 | 3.1 Voice with intent (named actor) | nêu 12 nhận xét: chấp nhận 9, chấp nhận một phần 3. | nêu 12 nhận xét; nhóm chấp nhận 9 nhận xét và chấp nhận một phần 3 nhận xét. |
| 11 | 10-00-genai-reflection | 14 | 3.6 Meaning complete (a role, not a step); 3.3 one term per concept | Ở bước kiểm tra rò rỉ thông tin (leakage auditor), tác tử thứ hai | Trong vai trò AI kiểm tra rò rỉ thông tin (leakage auditor), tác tử thứ hai |
| 12 | 10-00-genai-reflection | 16 | 3.6 Meaning complete (AI drafted the invented records); 3.3 glossary (synthetic = giả lập) | các bản ghi kiểm thử nhỏ do nhóm tự tạo; các bản ghi này | một số bản ghi giả lập nhỏ dùng để kiểm thử; các bản ghi này |
| 13 | 10-00-genai-reflection | 20 | 3.5 Parentheses for side information | Tình trạng nộp trễ CMA, xuất hiện ở 47,2% số bài nộp CMA, nằm ngoài quy tắc dấu hiệu sớm (C10). | Tình trạng nộp trễ CMA (gặp ở 47,2% số bài nộp CMA) không được đưa vào quy tắc dấu hiệu sớm (C10). |
| 14 | 10-00-genai-reflection | 22 | 3.1 Light function words ('một phần một'; 'việc'); one actor | Nhóm chỉ chấp nhận một phần một đề nghị: các lượt đăng ký học trong tập kiểm thử của sinh viên đã có mặt năm 2013 được đếm, nhưng việc báo cáo tỷ lệ kết quả của nhóm này  … | Một đề nghị chỉ được chấp nhận một phần: nhóm đếm các lượt đăng ký học trong tập kiểm thử của sinh viên đã có mặt năm 2013, nhưng không báo cáo tỷ lệ kết quả của nhóm này … |
| 15 | 12-00-appendices | 3 | Settled decision: data profiling = khảo sát dữ liệu (profiling) | toàn bộ kết quả lập hồ sơ dữ liệu (profiling) | toàn bộ kết quả khảo sát dữ liệu (profiling) |
| 16 | 12-00-appendices | 3 | Settled decision: validation checks = kiểm tra | sổ ghi kết quả kiểm định dữ liệu | sổ ghi kết quả kiểm tra dữ liệu |
| 17 | 12-00-appendices | 3 | 3.5 Head nouns present | từ tệp được ghi kèm, nên | từ tệp nguồn ghi kèm bảng đó, nên |
| 18 | 12-01-profiling-details | 1 | Settled decision: profiling | Chi tiết về hiểu dữ liệu, lập hồ sơ dữ liệu và chất lượng dữ liệu | Chi tiết về hiểu dữ liệu, khảo sát dữ liệu (profiling) và chất lượng dữ liệu |
| 19 | 12-01-profiling-details | 61 | 3.1 Collocations | 93 lượt này ở lại trong mọi tổng thể | 93 lượt này vẫn nằm trong mọi tổng thể |
| 20 | 12-01-profiling-details | 62 | 3.5 No empty/duplicated words | 58 lượt đăng ký học đăng ký vào ngày 16–167 | 58 lượt đăng ký học có ngày đăng ký từ ngày 16 đến ngày 167 |
| 21 | 12-01-profiling-details | 64 | 3.5 Head nouns present | Các đại lượng về đúng hạn và bài bỏ lỡ | Các đại lượng về nộp đúng hạn và bài bỏ lỡ |
| 22 | 12-01-profiling-details | 74 | 3.1 Light function words ('việc'); 3.5 'là' vs 'nghĩa là' | Việc không có dòng ghi nhận là không có hoạt động | Không có dòng nghĩa là không có hoạt động |
| 23 | 12-01-profiling-details | 75 | 3.6 Meaning complete ('due by' includes the cut-off day) | các bài đến hạn trước thời điểm chốt | các bài đến hạn tính đến thời điểm chốt |
| 24 | 12-01-profiling-details | 75 | 3.6 Meaning complete ('by day d' = on or before) | có ngày đến hạn trước ngày 13 ở 1 trên 22 lượt mở và trước ngày 27 ở 16 lượt; có từ hai bài trở lên đến hạn trước ngày 27 | có ngày đến hạn chậm nhất vào ngày 13 ở 1 trên 22 lượt mở và chậm nhất vào ngày 27 ở 16 lượt; có từ hai bài trở lên đến hạn chậm nhất vào ngày 27 |
| 25 | 12-01-profiling-details | 76 | 3.3 Glossary forms (generalisation) | Khả năng khái quát hóa | Khả năng tổng quát hóa |
| 26 | 12-01-profiling-details | 78 | Settled decision: profile = kết quả khảo sát dữ liệu | Mười ba con số trong hồ sơ dữ liệu | Mười ba con số trong kết quả khảo sát dữ liệu |
| 27 | 12-01-profiling-details | 82 | Settled decision: profiling | \| Hồ sơ dữ liệu Milestone 3 \| | \| Kết quả khảo sát Milestone 3 \| |
| 28 | 12-02-pipeline-package | 3 | Settled decision: validation = kiểm tra | gói dữ liệu đã được kiểm định | gói dữ liệu đã qua kiểm tra |
| 29 | 12-02-pipeline-package | 22 | Settled decision: validation summary | bản tóm tắt kiểm định | bản tóm tắt kết quả kiểm tra |
| 30 | 12-02-pipeline-package | 38 | Settled decision: profiling | Hồ sơ dữ liệu và bằng chứng chất lượng | Kết quả khảo sát dữ liệu (profiling) và bằng chứng về chất lượng |
| 31 | 12-02-pipeline-package | 91 | 3.6 Meaning complete ('due by') (×2) | + các bài đến hạn trước thời điểm chốt | + các bài đến hạn tính đến thời điểm chốt |
| 32 | 12-02-pipeline-package | 84 | 3.1 Collocations (×2) | cắt tại lúc rút | cắt tại thời điểm rút |
| 33 | 12-02-pipeline-package | 110 | 3.1 Complete sentence (dangling modifier) | , giống hệt nhau qua hai lần chạy | ; các giá trị này giống hệt nhau qua hai lần chạy |
| 34 | 12-03-dictionary-lineage | 43 | 3.3 One term per concept (enrolment = đăng ký học) (×3) | biết khi ghi danh | biết khi đăng ký học |
| 35 | 12-03-dictionary-lineage | 66 | 3.6 Meaning complete ('registered by due day') | đã đăng ký trước ngày đến hạn và hủy đăng ký | đã đăng ký chậm nhất vào ngày đến hạn và hủy đăng ký |
| 36 | 12-03-dictionary-lineage | 80 | 3.6 Meaning complete ('due by c') | TMA/CMA đến hạn trước c và vào hoặc sau | TMA/CMA đến hạn chậm nhất tại c và vào hoặc sau |
| 37 | 12-03-dictionary-lineage | 82 | 3.6 Meaning complete ('by c') | nộp sau ngày đến hạn và trước c | nộp sau ngày đến hạn và chậm nhất tại c |
| 38 | 12-03-dictionary-lineage | 89 | 3.6 Meaning complete ('by c') | các bài đến hạn sau c đã nộp trước c | các bài đến hạn sau c đã nộp chậm nhất tại c |
| 39 | 12-03-dictionary-lineage | 85 | 3.5 Plain wording (coverage) | AQ3 (mức có giá trị của điểm CMA) | AQ3 (tỷ lệ dòng có điểm CMA) |
| 40 | 12-03-dictionary-lineage | 41 | 3.5 Head nouns present (×2) | giới hạn công bằng của AQ4 (C04) | giới hạn về công bằng của AQ4 (C04) |
| 41 | 12-04-traceability-change-log | 21 | 3.3 Glossary forms (limit vs limitation) | được nêu là một giới hạn | được nêu rõ là một hạn chế |
| 42 | 12-04-traceability-change-log | 22 | 3.3 Glossary forms (proxy = chỉ số đại diện) | được tính như một chỉ số gần đúng trên | được tính dưới dạng chỉ số đại diện trên |
| 43 | 12-04-traceability-change-log | 23 | 3.3 Glossary forms (deprivation band drift) | theo nhóm IMD và tình trạng khuyết tật | theo mức khó khăn của khu vực (nhóm IMD) và tình trạng khuyết tật |
| 44 | 12-04-traceability-change-log | 25 | 3.6 Meaning complete ('due by') | có ngày đến hạn trước ngày 13 ở 1 trên 22 lượt mở, trước ngày 27 ở 16 lượt | có ngày đến hạn chậm nhất vào ngày 13 ở 1 trên 22 lượt mở, chậm nhất vào ngày 27 ở 16 lượt |
| 45 | 12-04-traceability-change-log | 29 | 3.6 Meaning complete (three alternatives; 'due by'); 3.5 no comma before 'hoặc'; 3.1 'việc' | có ít nhất một TMA hoặc CMA đến hạn trước thời điểm chốt mà chưa nộp, có một TMA nộp trễ hoặc không có hoạt động …; việc nộp trễ CMA chỉ có trong một biến thể … | Quy tắc dấu hiệu sớm kích hoạt khi có một trong ba điều kiện: … mà chưa nộp; một TMA nộp trễ; không có hoạt động … Nộp trễ CMA chỉ được tính trong một biến thể … |
| 46 | 12-04-traceability-change-log | 29 | 3.6 Meaning complete ('due by') | Có từ hai bài trở lên đến hạn trước ngày 27 ở 1 trên 22 lượt mở, từ một bài trở lên ở 16 lượt; bài đến hạn trước ngày 13 | Có từ hai bài trở lên đến hạn chậm nhất vào ngày 27 ở 1 trên 22 lượt mở, từ một bài trở lên ở 16 lượt; bài đến hạn chậm nhất vào ngày 13 |
| 47 | 12-04-traceability-change-log | 30 | 3.5 Head nouns / double 'và' | trên toàn bộ và theo mức khó khăn của khu vực và tình trạng khuyết tật | tính chung và tách theo mức khó khăn của khu vực, theo tình trạng khuyết tật |
| 48 | 12-05-ai-decision-log | 9 | 3.5 Plain verb (glossary: mark release = công bố điểm) | Điểm CMA có trong vòng 7 ngày | Điểm CMA được công bố trong vòng 7 ngày |
| 49 | 12-05-ai-decision-log | 9 | 3.1 Collocations | 32.991 trên 69.956 bài nộp CMA nằm sau ngày đến hạn | 32.991 trên 69.956 bài CMA được nộp sau ngày đến hạn |
| 50 | 12-05-ai-decision-log | 10 | 3.3 Glossary forms (England = xứ Anh) | IMD của Anh chỉ bao phủ England | IMD của xứ Anh (England) chỉ bao phủ xứ Anh |
| 51 | 12-05-ai-decision-log | 12 | 3.3 Glossary forms (capacity) | \| Bảng số lượt liên hệ; kế hoạch | \| Bảng số lượt liên hệ tối đa; kế hoạch |
| 52 | 12-05-ai-decision-log | 19 | Settled decisions: profiling, validation | (hiểu dữ liệu, lập hồ sơ dữ liệu, chuẩn bị, phép biến đổi, kiểm định, notebook) | (hiểu dữ liệu, khảo sát dữ liệu, chuẩn bị, phép biến đổi, kiểm tra, notebook) |
| 53 | 12-05-ai-decision-log | 21 | 3.6 Meaning complete (AI suggestion, not team-made) | Một vài lượt đăng ký học nhỏ do nhóm tự tạo để kiểm thử công thức | Một vài lượt đăng ký học giả lập quy mô nhỏ để kiểm thử công thức |
| 54 | 12-05-ai-decision-log | 23 | Settled decision: profiling; 3.5 head nouns | các bản đặc tả, nhật ký mức phù hợp và hồ sơ dữ liệu. | các bản đặc tả, nhật ký mức phù hợp giữa AQ và dữ liệu cùng kết quả khảo sát dữ liệu. |
| 55 | 12-05-ai-decision-log | 46 | 3.6 Meaning complete ('due by') | Bài có ngày đến hạn trước ngày 13 | Bài có ngày đến hạn chậm nhất vào ngày 13 |
| 56 | 12-05-ai-decision-log | 46 | Settled decision: validation summary (×2) | bản tóm tắt kiểm định | bản tóm tắt kết quả kiểm tra |
| 57 | 12-05-ai-decision-log | 47 | 3.3 Glossary usage (fold first use) | các fold được nhóm theo | các fold (phần chia trong kiểm định chéo) được nhóm theo |
| 58 | 12-05-ai-decision-log | 48 | 3.3 Glossary ('tinh chỉnh' = fine-tuning) | chỉ có 9 nhóm để tinh chỉnh | chỉ có 9 nhóm để điều chỉnh siêu tham số |
| 59 | 12-05-ai-decision-log | 48 | 3.3 Glossary (leave-one-out = loại trừ từng ...) | dùng các fold bỏ ra một lượt mở trong năm 2013 | dùng các fold loại trừ từng lượt mở (leave-one-run-out) trong năm 2013 |
| 60 | 12-05-ai-decision-log | 49 | 3.6 Meaning ('declared' = set in advance) | đại lượng chính đã công bố | đại lượng chính đã xác định từ trước |
| 61 | 12-05-ai-decision-log | 49 | 3.5 Plain action over image ('hấp thụ') | tỷ số tương đối theo lượt mở hấp thụ khác biệt giữa các lượt mở | tỷ số tương đối theo lượt mở loại bỏ khác biệt ở mức lượt mở |
| 62 | 12-05-ai-decision-log | 50 | 3.5 Plain wording (coverage) | mức có giá trị tại mỗi thời điểm chốt được báo cáo | tỷ lệ dòng có điểm tại mỗi thời điểm chốt được báo cáo |
| 63 | 12-05-ai-decision-log | 57 | 3.5 No pronoun 'chúng' | nhưng không được thay đổi chúng. | nhưng không được thay đổi các tệp này. |
| 64 | 12-05-ai-decision-log | 73 | 3.4 Restate the actor | 8 phát hiện của AI kiểm tra này. | 8 phát hiện của AI kiểm tra rò rỉ thông tin. |
| 65 | 12-05-ai-decision-log | 83 | Settled decision: validation = kiểm tra | phép đếm lại của bộ kiểm định | phép đếm lại trong script kiểm tra |
| 66 | 12-05-ai-decision-log | 85 | 3.1 Collocations | đếm lại lượt nhấp không theo thời điểm chốt nào | đếm lại lượt nhấp mà không áp dụng thời điểm chốt nào |
| 67 | 12-06-validation-ledger | 1 | Settled decision: validation = kiểm tra (×2) | Sổ ghi kết quả kiểm định | Sổ ghi kết quả kiểm tra |
| 68 | 12-06-validation-ledger | 11 | Settled decision: profile (×2) | bằng số liệu trong hồ sơ dữ liệu | bằng số liệu trong kết quả khảo sát dữ liệu |
| 69 | 12-06-validation-ledger | 32 | 3.1 Vietnamese order (object before the aside); settled 'kiểm tra' | Bước kiểm định cũng báo cáo, mà không dùng bất kỳ kết quả nào của tập kiểm thử, các con số mà kế hoạch Milestone 4 dựa vào. | Bước kiểm tra cũng báo cáo các con số mà kế hoạch Milestone 4 dựa vào; các con số này không dùng bất kỳ kết quả nào của tập kiểm thử. |

Terms the glossary should settle (not added; the review does not edit glossaries):

- "due by day d / by the cut-off" → "chậm nhất vào ngày d" / "tính đến thời điểm chốt" (never "trước ngày d", which excludes day d). Several G1–G3 files may carry the same slip (e.g. G1 row 9 kept "đến hạn trước thời điểm chốt").
- "hyperparameter tuning" → "điều chỉnh siêu tham số" (keep "tinh chỉnh" for fine-tuning).
- "validation ledger" → "sổ ghi kết quả kiểm tra"; "profile" (the output of data profiling) → "kết quả khảo sát dữ liệu".
- "leave-one-run-out" → "loại trừ từng lượt mở (leave-one-run-out)", following the common row for leave-one-out.

Per-file close (parity: `check_parity.py --report reports/milestone-3/report --lang vi reports/milestone-3/report/FILE.md`; then `translation_status.py --lang vi --mark` recorded all 10 files in `.vi-sync.json`):

- 09-00-ethics-limitations: reviewed, 8 finding(s) fixed, parity 0 errors, 0 warnings.
- 10-00-genai-reflection: reviewed, 6 finding(s) fixed, parity 0 errors, 0 warnings.
- 11-references: reviewed, 0 finding(s) fixed (no findings: APA entries stay as in the English, guide 9; the intro sentence reads naturally), parity 0 errors, 0 warnings.
- 12-00-appendices: reviewed, 3 finding(s) fixed, parity 0 errors, 0 warnings.
- 12-01-profiling-details: reviewed, 10 finding(s) fixed, parity 0 errors, 0 warnings.
- 12-02-pipeline-package: reviewed, 6 finding(s) fixed, parity 0 errors, 0 warnings.
- 12-03-dictionary-lineage: reviewed, 7 finding(s) fixed, parity 0 errors, 0 warnings.
- 12-04-traceability-change-log: reviewed, 7 finding(s) fixed, parity 0 errors, 0 warnings.
- 12-05-ai-decision-log: reviewed, 19 finding(s) fixed, parity 0 errors, 13 warnings (all on the English quoted prompts kept verbatim by the settled decision: 'looks untranslated' and the loanword 'test' inside the prompt lines).
- 12-06-validation-ledger: reviewed, 3 finding(s) fixed, parity 0 errors, 0 warnings.
