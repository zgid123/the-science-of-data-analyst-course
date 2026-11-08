# Vietnamese native review – group B (Sections 4 to 7)

Reviewer: native Vietnamese reviewer agent (not the translator), 2026-11-08. Protocol: `build-report/languages/vi/review.md`
(three passes per file: reader pass, fidelity pass against the English, checklist pass), with `guide.md`, `lessons.md`, the
merged glossary (`glossary.py --lang vi --task milestone-3 show`) and the front matter twins `00-1-abbreviations.vi.md`,
`00-2-glossary.vi.md`.

Glossary coverage before the passes (`glossary.py --lang vi --task milestone-3 coverage --report reports/milestone-3/report`):
21 drifting concepts in the whole report. Those touching this group: capacity scenarios ("các kịch bản về số sinh viên cán bộ
liên hệ được mỗi tuần" in 04-01 and 07-03 → glossary form "kịch bản số sinh viên cán bộ liên hệ được mỗi tuần"); capacity
(heading of 07-03 item 5 → "số sinh viên cán bộ liên hệ được"); level A (04-02 now carries the first-use gloss); fitted
scaling and encoding, checksum (06-01 first use now "mã kiểm tra (checksum)"). The enrolment, flag, baseline and gap
warnings are noise for this group: OULAD enrolments correctly use "lượt đăng ký học", "flag" on data rows is "cờ" (glossary
note), and "baseline"/"gap" occur here in other senses ("khoảng trống dữ liệu").

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 04-00-aq-data-fit | 3 | 3.5 Plain wording (verb that fits) | đánh giá lại từng câu hỏi phân tích (AQ) trên dữ liệu thực | đánh giá lại từng câu hỏi phân tích (AQ) bằng cách đối chiếu với dữ liệu thực |
| 2 | 04-00-aq-data-fit | 3 | 3.6 Meaning complete ('key' qualifies every item) | thiếu một khái niệm then chốt, một biến, biến mục tiêu hoặc biện pháp can thiệp | thiếu một khái niệm, biến, biến mục tiêu hoặc biện pháp can thiệp then chốt |
| 3 | 04-00-aq-data-fit | 5 | 3.5 Plain actions over images | bước thứ sáu để cứu một AQ | bước thứ sáu để giữ lại một AQ |
| 4 | 04-01-fit-ratings | 3 | 3.6 Meaning complete ('carries after') | mức kết luận mà AQ đó đặt ra sau các thay đổi C01–C08 | mức kết luận mà AQ đó còn giữ sau các thay đổi C01–C08 |
| 5 | 04-01-fit-ratings | 3 | 3.5 No empty words | bước trong quy trình xử lý đã giải quyết khoảng trống | bước trong quy trình xử lý giải quyết khoảng trống |
| 6 | 04-01-fit-ratings | 11 | 3.6 Meaning complete ('fires' = flags a student) | Quy tắc … chỉ áp dụng được ở 1 kỳ mở vào ngày 13 | Quy tắc … chỉ đánh dấu được sinh viên ở 1 kỳ mở vào ngày 13 |
| 7 | 04-01-fit-ratings | 12 | 3.3 Glossary forms (capacity scenarios) | dùng cho các kịch bản về số sinh viên cán bộ liên hệ được mỗi tuần | dùng cho kịch bản số sinh viên cán bộ liên hệ được mỗi tuần |
| 8 | 04-01-fit-ratings | 14 | 3.1 Vietnamese order; 3.5 head noun ('concurrent') | vì chỉ 12 trong 1.382 lượt đăng ký học đồng thời rơi vào các kỳ mở huấn luyện năm 2013 | vì trong 1.382 lượt đăng ký học diễn ra đồng thời ở hai kỳ mở, chỉ 12 lượt thuộc các kỳ mở huấn luyện năm 2013 |
| 9 | 04-01-fit-ratings | 14 | 3.6 Meaning complete ('cannot fire'); 3.1 one actor | Quy tắc dấu hiệu sớm … (C06) nên không thể áp dụng ở 6 kỳ mở | Quy tắc dấu hiệu sớm … (C06), nên quy tắc này không thể đánh dấu sinh viên nào ở 6 kỳ mở |
| 10 | 04-01-fit-ratings | 14 | 3.5 Written connectives ('là'/colon, not 'tức', in a definition) | tỷ lệ phát hiện (recall), tức tỷ lệ sinh viên | tỷ lệ phát hiện (recall): tỷ lệ sinh viên |
| 11 | 04-02-gap-decisions | 3 | 3.1 One main idea; 3.6 meaning ('a fourth case') | OULAD còn có một trường hợp …: không có bản ghi (tính là 0), khi chính việc không có dòng dữ liệu ghi nhận một sự kiện | OULAD còn có trường hợp thứ tư …: không có bản ghi (tính là 0). Ở trường hợp này, chính việc thiếu dòng dữ liệu cho biết một sự kiện |
| 12 | 04-02-gap-decisions | 14 | 3.5 Parentheses for side information | Bước thứ ba của quy trình, bổ sung một bộ dữ liệu mở tương thích, không lấp được | Bước thứ ba của quy trình (bổ sung một bộ dữ liệu mở tương thích) không lấp được |
| 13 | 04-02-gap-decisions | 16 | 3.3 Glossary forms (mức A gloss); 3.1 one actor | dự án chỉ dùng mức A, là một lượng nhỏ …: một số lượt đăng ký học kiểm thử tự tạo … dùng để kiểm tra | dự án chỉ dùng mức A (một lượng nhỏ …) [1]: nhóm tác giả tự tạo một số lượt đăng ký học kiểm thử … để kiểm tra |
| 14 | 04-02-gap-decisions | 16 | 3.5 Written connectives ('hoặc') | số liệu thống kê hay phát hiện nào | số liệu thống kê hoặc phát hiện nào |
| 15 | 05-00-preparation-plan | 3 | 3.1 One actor; 3.5 no empty words ('đúng, đúng như') | mỗi vấn đề … đều được gán một quyết định, kèm … phép kiểm tra cho thấy quyết định đó được thực hiện đúng, đúng như đề bài yêu cầu | nhóm tác giả đã gán cho mỗi vấn đề … một quyết định, kèm … phép kiểm tra dùng để xác nhận quyết định đó, theo yêu cầu của đề bài |
| 16 | 05-00-preparation-plan | 3 | 3.5 Plain wording | những cách làm mà đề bài nêu là bước đi sai ngay từ đầu | những cách làm mà đề bài coi là sai lầm ngay từ bước đầu |
| 17 | 05-00-preparation-plan | 3 | 3.3 One term per concept (bias audit = fairness audit) | bước kiểm tra thiên lệch | bước kiểm tra công bằng |
| 18 | 05-00-preparation-plan | 5 | 3.1 Given before new; actor | của script kiểm tra, có kết quả trình bày ở Mục 7 | của script kiểm tra dữ liệu; Mục 7 trình bày kết quả của các phép kiểm tra này |
| 19 | 05-00-preparation-plan | 13 | 3.5 Punctuation (no comma before 'và' chain) | theo lượt đăng ký học và ngày, theo tuần, trước mọi phép nối bảng | theo lượt đăng ký học và ngày cũng như theo tuần, trước mọi phép nối bảng |
| 20 | 05-00-preparation-plan | 14 | 3.6 Meaning complete ('never timed'); 3.5 no 'chúng' | không bao giờ gán thời điểm cho chúng | không tính thời điểm nộp cho các kết quả này |
| 21 | 05-00-preparation-plan | 14 | 3.3 Glossary forms (banked result) | kết quả được chuyển sang | kết quả bảo lưu từ kỳ mở trước |
| 22 | 05-00-preparation-plan | 16 | 3.5 Written connectives ('hoặc') | không lượt nhấp hay bài nộp nào | không lượt nhấp hoặc bài nộp nào |
| 23 | 05-00-preparation-plan | 17 | 3.5 Head nouns present | V09: số dòng bằng bảng bên trái | V09: số dòng bằng số dòng của bảng bên trái |
| 24 | 05-00-preparation-plan | 18 | 3.6 Meaning complete ('fire') | quy tắc phải áp dụng được ở mọi kỳ mở | quy tắc phải đánh dấu được sinh viên ở mọi kỳ mở |
| 25 | 05-00-preparation-plan | 19 | 3.1 Vietnamese order; 3.6 meaning ('later clicks') | V13: đặc trưng lượt nhấp chỉ khác kết quả đếm lại không lọc đúng ở những sinh viên có lượt nhấp muộn hơn | V13: đặc trưng lượt nhấp khác với kết quả đếm lại không lọc theo ngày ở đúng những sinh viên có lượt nhấp sau thời điểm chốt dữ liệu |
| 26 | 05-00-preparation-plan | 20 | 3.6 Meaning complete (what is fitted) | ma trận sẵn sàng cho mô hình tuyến tính được ước lượng trên các kỳ mở năm 2013 | ma trận sẵn sàng cho mô hình tuyến tính có các phép biến đổi ước lượng trên các kỳ mở năm 2013 |
| 27 | 05-00-preparation-plan | 20 | 3.5 Established words | Mã thứ bậc | Mã hóa thứ bậc |
| 28 | 05-00-preparation-plan | 21 | 3.5 No 'chúng' (repeat the noun) | dùng chúng làm biến dự báo | dùng các thuộc tính này làm biến dự báo |
| 29 | 05-00-preparation-plan | 24 | 3.1 Voice with intent (mixed bị/được) | không giá trị nào đã được ghi nhận bị xóa hoặc được điền trong các bảng dữ liệu đã chuẩn bị | các bảng dữ liệu đã chuẩn bị giữ nguyên mọi giá trị đã ghi nhận, không xóa và không điền giá trị thiếu |
| 30 | 05-00-preparation-plan | 24 | 3.5 Written connectives ('hoặc') | như trung vị hay thang đo | như trung vị hoặc thang đo |
| 31 | 06-00-preparation-pipeline | 3 | 3.5 Plain wording | Mục 6.2 trình bày phép tích hợp bảng và cách xây dựng đặc trưng | Mục 6.2 trình bày cách tích hợp các bảng và xây dựng đặc trưng |
| 32 | 06-01-pipeline-steps | 3 | 3.5 No empty words ('một' with apposition) | mười hàm của một script, `src/prepare_data.py`, được chạy theo thứ tự | mười hàm của script `src/prepare_data.py`, chạy theo thứ tự |
| 33 | 06-01-pipeline-steps | 3 | 3.3 Glossary forms (checksum, first use) | đối chiếu các bảng gốc với checksum | đối chiếu các bảng gốc với mã kiểm tra (checksum) |
| 34 | 06-01-pipeline-steps | 5 | 3.1 Vietnamese order (object before destination) | Mỗi giai đoạn ghi vào một tệp nhật ký đầu ra trên màn hình, câu lệnh, … và trạng thái kết thúc | Mỗi giai đoạn ghi đầu ra trên màn hình, câu lệnh, … và trạng thái kết thúc vào một tệp nhật ký |
| 35 | 06-01-pipeline-steps | 7 | 3.1 Complete (missing verb) | Gói dữ liệu theo cấu trúc thư mục | Gói dữ liệu được tổ chức theo cấu trúc thư mục |
| 36 | 06-02-integration-features | 3 | 3.3 Collocations ('asserts' calque); 3.2 linking | pipeline khẳng định số dòng … Kết quả là cả 25 phép nối | pipeline xác nhận số dòng …; cả 25 phép nối |
| 37 | 06-02-integration-features | 5 | 3.2 Connectors accurate ('trong khi đó' is not a contrast here) | biết biến mục tiêu; trong khi đó, những bản ghi … là con đường phổ biến để thông tin | biết giá trị biến mục tiêu; những bản ghi … là con đường phổ biến khiến thông tin |
| 38 | 06-02-integration-features | 5 | 3.5 Head noun; 'việc' removed | vì thông tin này đã biết trước khi việc giảng dạy bắt đầu | vì hoạt động này đã được ghi nhận trước khi bắt đầu giảng dạy |
| 39 | 06-02-integration-features | 5 | 3.5 Plain wording (complete verb) | điểm CMA dự kiến có trong vòng bảy ngày | điểm CMA dự kiến được công bố trong vòng bảy ngày |
| 40 | 06-02-integration-features | 20 | 3.6 Meaning complete ('but by c') | được nộp sau ngày đến hạn nhưng vẫn tính đến hết ngày c | được nộp sau ngày đến hạn nhưng không muộn hơn ngày c |
| 41 | 06-02-integration-features | 26 | 3.2 Connectors accurate (addition, not similarity) | Tương tự, tỷ lệ hoạt động | Ngoài ra, tỷ lệ hoạt động |
| 42 | 06-02-integration-features | 26 | 3.5 Head nouns present | là định danh | là mã định danh |
| 43 | 06-02-integration-features | 26 | 3.1 Complete (subject of the clause) | vì tại OU, bổ sung các thuộc tính này | vì tại OU, việc bổ sung các thuộc tính này |
| 44 | 06-03-split-leakage | 3 | 3.5 Plain actions over images | nếu biện pháp đó bị phá vỡ | nếu biện pháp đó bị vi phạm |
| 45 | 06-03-split-leakage | 16 | 3.5 Parentheses for side information; 3.2 connector | theo đúng thực tiễn của chính OU, là xây dựng mô hình … [12], đồng thời áp dụng nguyên tắc | theo đúng cách làm của chính OU (xây dựng mô hình …) [12] và nguyên tắc |
| 46 | 06-03-split-leakage | 16 | 3.5 No 'nó' (repeat the noun) | học từ chính năm dùng để kiểm thử nó | học từ chính năm dữ liệu được dùng để kiểm thử |
| 47 | 06-03-split-leakage | 16 | 3.1 One main idea (long subject split) | 9 kỳ mở có cùng module và tháng bắt đầu với một kỳ mở năm 2013 kiểm tra trực tiếp kết luận | có 9 kỳ mở trùng module và tháng bắt đầu với một kỳ mở năm 2013; 9 kỳ mở này kiểm tra trực tiếp kết luận |
| 48 | 06-03-split-leakage | 18 | 3.6 Meaning complete ('unseen' = not in training) | trên những sinh viên chưa từng gặp | trên những sinh viên chưa xuất hiện trong dữ liệu huấn luyện |
| 49 | 06-03-split-leakage | 18 | 3.6 Meaning complete ('held-out' read as 'kept') | ở kỳ mở được giữ lại | ở kỳ mở được tách ra để đánh giá |
| 50 | 06-03-split-leakage | 18 | 3.5 Written connectives ('hoặc') | để điền giá trị thiếu hay thang đo | để điền giá trị thiếu hoặc thang đo |
| 51 | 06-03-split-leakage | 18 | 3.1 One clear actor; 3.6 'outcomes' = biến kết quả; tense | khi mọi dòng kiểm thử bị thay đổi …; Kết quả của các kỳ mở năm 2014 không được xem …; kết quả kiểm thử còn được báo cáo thêm | khi nhóm tác giả thay đổi mọi dòng kiểm thử …; Nhóm tác giả không xem biến kết quả của các kỳ mở năm 2014 …; kết quả kiểm thử sẽ được báo cáo thêm |
| 52 | 07-00-prepared-validation | 3 | 3.6 Meaning complete ('outcome counts') | số lượng theo từng kết quả | số lượt theo từng loại kết quả |
| 53 | 07-00-prepared-validation | 3 | 3.1 Complete (enumeration clause without its modal) | không có rò rỉ thông tin …; từ điển dữ liệu được cập nhật và phiên bản được ghi lại | dữ liệu phải không có rò rỉ thông tin …; từ điển dữ liệu phải được cập nhật và phiên bản phải được ghi lại |
| 54 | 07-00-prepared-validation | 3 | 3.2 Connectors varied (three 'trình bày') | Mục 7.1 trình bày các phép so sánh; … Mục 7.3 trình bày các rủi ro | Mục 7.1 so sánh dữ liệu trước và sau chuẩn bị; … Mục 7.3 nêu các rủi ro |
| 55 | 07-01-before-after | 3 | 3.5 Written connectives ('hoặc') | biến kết quả hay số đếm nào | biến kết quả hoặc số đếm nào |
| 56 | 07-01-before-after | 12 | 3.5 Head nouns present | 39.506.354 được giữ cộng 98.745 sau khi rút | 39.506.354 lượt được giữ, cộng 98.745 lượt sau khi rút khỏi module |
| 57 | 07-01-before-after | 19 | 3.1 Vietnamese order (as 05-00 V13) | Đặc trưng chỉ khác kết quả đếm lại không lọc đúng ở 26.755 | Đặc trưng khác với kết quả đếm lại không lọc theo ngày ở đúng 26.755 |
| 58 | 07-02-lineage-dictionary | 3 | 3.5 Head nouns present | Mỗi cột đã chuẩn bị đều được mô tả với trường nguồn | Mỗi cột của dữ liệu đã chuẩn bị đều được mô tả kèm trường nguồn |
| 59 | 07-02-lineage-dictionary | 3 | 3.5 Head nouns present | định danh, biến mục tiêu | mã định danh, biến mục tiêu |
| 60 | 07-02-lineage-dictionary | 3 | 3.5 'hoặc'; 3.3 glossary (descriptive measure) | cột biến mục tiêu hay cột mô tả | cột biến mục tiêu hoặc cột chỉ số mô tả |
| 61 | 07-02-lineage-dictionary | 5 | 3.1 Given before new (predicate after a long apposition) | bảng đầy đủ, gồm một dòng … ở cột mục đích, là Bảng A.12 trong Phụ lục III | bảng đầy đủ là Bảng A.12 trong Phụ lục III, gồm một dòng …, với các biến nhạy cảm được đánh dấu ở cột mục đích |
| 62 | 07-02-lineage-dictionary | 7 | 3.1 Head noun before modifiers (caption) | các biến đã chuẩn bị chính | các biến chính trong dữ liệu đã chuẩn bị |
| 63 | 07-03-residual-risks | 3 | 3.5 No 'chúng'; 3.1 complete | vì muốn giải quyết chúng cần thông tin | vì giải quyết các vấn đề này đòi hỏi thông tin |
| 64 | 07-03-residual-risks | 3 | 3.1 Complete (dangling 'đã đo') | được gắn cờ trong dữ liệu và đã đo quy mô | được gắn cờ trong dữ liệu kèm quy mô đã đo |
| 65 | 07-03-residual-risks | 3 | 3.3 Glossary forms (capacity scenarios) | các kịch bản về số sinh viên cán bộ liên hệ được mỗi tuần | kịch bản số sinh viên cán bộ liên hệ được mỗi tuần |
| 66 | 07-03-residual-risks | 7 | 3.6 Meaning complete ('policy on record') | chính sách chấm điểm của OU hiện có được ban hành năm 2025 | chính sách chấm điểm của OU tìm được là bản năm 2025 |
| 67 | 07-03-residual-risks | 7 | 3.6 Meaning complete ('10% coverage') | thấp hơn mức 10% mà một đặc trưng cần có dữ liệu để được đưa vào | thấp hơn ngưỡng 10% số dòng có dữ liệu mà một đặc trưng cần đạt để được đưa vào |
| 68 | 07-03-residual-risks | 9 | 3.5 No empty words ('Có … có') | Có 93 lượt đăng ký học có kết quả Withdrawn | Trong dữ liệu, 93 lượt đăng ký học có kết quả Withdrawn |
| 69 | 07-03-residual-risks | 13 | 3.3 Glossary forms (capacity); heading as noun phrase | **Số sinh viên liên hệ được là giả định.** | **Giả định về số sinh viên cán bộ liên hệ được.** |
| 70 | 07-03-residual-risks | 13 | 3.5 Head nouns present ('weekly range') | đúng khoảng mỗi tuần mà Milestone 1 đặt ra (2×) | đúng khoảng số sinh viên liên hệ được mỗi tuần mà Milestone 1 đặt ra (2×) |

Patterns corrected most often: "fires" rendered as "áp dụng được" (the rule flags students; 3 places); "hay" in statements → "hoặc" (6); missing head nouns ("mã định danh", "số dòng của bảng", "số sinh viên liên hệ được mỗi tuần"); "chúng"/"nó" → the noun (4); sentences without a named actor where the team acts ("nhóm tác giả", as in the other twins); the V13 sentence order ("chỉ khác … đúng ở") in 05-00 and 07-01.

Terms for the glossary to settle: (1) "concurrent enrolment" (no row; this group uses "lượt đăng ký học diễn ra đồng thời ở hai kỳ mở"); (2) "fire" of a rule (no row; this group uses "đánh dấu được sinh viên"); (3) "held-out run" (no row; "kỳ mở được tách ra để đánh giá", since "được giữ lại" reads as kept); (4) "bias audit" folded into "kiểm tra công bằng" (fairness audit), one concept.

Per file (reviewed, findings fixed, `check_parity.py` result):

- 04-00-aq-data-fit: reviewed, 3 findings fixed, parity 0 errors, 0 warnings.
- 04-01-fit-ratings: reviewed, 7 findings fixed, parity 0 errors, 0 warnings.
- 04-02-gap-decisions: reviewed, 4 findings fixed, parity 0 errors, 0 warnings.
- 05-00-preparation-plan: reviewed, 16 findings fixed, parity 0 errors, 0 warnings.
- 06-00-preparation-pipeline: reviewed, 1 findings fixed, parity 0 errors, 0 warnings.
- 06-01-pipeline-steps: reviewed, 4 findings fixed, parity 0 errors, 0 warnings.
- 06-02-integration-features: reviewed, 8 findings fixed, parity 0 errors, 0 warnings.
- 06-03-split-leakage: reviewed, 8 findings fixed, parity 0 errors, 0 warnings.
- 07-00-prepared-validation: reviewed, 3 findings fixed, parity 0 errors, 0 warnings.
- 07-01-before-after: reviewed, 3 findings fixed, parity 0 errors, 0 warnings.
- 07-02-lineage-dictionary: reviewed, 5 findings fixed, parity 0 errors, 0 warnings.
- 07-03-residual-risks: reviewed, 8 findings fixed, parity 0 errors, 0 warnings.
