# Rewrite after the reader test – Milestone 3, Vietnamese twins (stage 5 → stage 3)

Inputs: `reader-test.md` (77 passages), `languages/vi/guide.md`, `lessons.md`, merged glossary
(`glossary.py --lang vi --task milestone-3 show`). Only `report/*.vi.md` were edited; English files and glossaries untouched.

## A. Twins brought in line with changed English

| File | English change | Twin now says |
| :---- | :---- | :---- |
| 01-01 | Secondary KPIs and D1–D3 defined in 1.1 | KPI phụ 1 = tỷ lệ liên hệ sinh viên có dấu hiệu sớm (dấu hiệu tính đến hết tuần 4, liên hệ trước khi hết tuần 5); KPI phụ 2 = tỷ lệ liên hệ kịp thời (trong bảy ngày); D1–D3 defined before Table 1.1 |
| 03-01 | Duplicate chance test explained | Hypothesis stated (bản sao → cùng số lượt nhấp thường hơn ngẫu nhiên), 31,5% vs 24,0% kỳ vọng, pattern by resource type, "bằng chứng nghiêng về cả hai phía" |
| 04-00 | Gap procedure numbered (1)–(5) | Năm bước đánh số (1)–(5) |
| 06-00 | Ten steps / eight stages / five phases | Ba cấp: mười bước = mười hàm trong một script; script đó là một trong tám giai đoạn; tám giai đoạn hợp thành năm pha |
| 06-03 | Transform check reworded | Tham số chỉ ước lượng (fit) trên lượt mở huấn luyện; cố ý thay đổi mọi dòng kiểm thử rồi ước lượng lại, tham số giữ nguyên |
| 07-01 | Leakage row of Table 7.1 | Đếm lại không giới hạn thời điểm chốt chỉ thay đổi đặc trưng ở 26.755 lượt (ngày 13) và 25.663 lượt (ngày 27) có lượt nhấp sau thời điểm chốt |
| 08-02 | Capacity sentence | Quy tắc đánh dấu nhiều hơn số chỗ của danh sách 5 trên 20 ở 7/22 lượt mở (ngày 13) và 10 (ngày 27), nên cán bộ cần thứ hạng – kết quả của AQ3 và AQ4 |

## B. Passages rewritten (reader-test # → new text in brief)

Clarity 1 (7 of 7):

| # | New text |
| :-- | :---- |
| 28 | 03-01: split into hypothesis → test → result → conclusion sentences (see A) |
| 39 | 03-05: "tuần dự kiến sử dụng tài nguyên trong bảng vle, trường thiếu phần lớn giá trị và không được dùng (DQ14)" |
| 41 | 03-05 DQ18: "KPI phụ 1 (tỷ lệ liên hệ sinh viên có dấu hiệu sớm)"; KPI phụ 1/2 also defined in 1.1 |
| 58 | 06-03: "Một số phép biến đổi cần học tham số từ dữ liệu … chỉ được ước lượng (fit) trên các lượt mở huấn luyện. Để kiểm tra điều đó, nhóm tác giả cố ý thay đổi giá trị của mọi dòng kiểm thử …" |
| 61 | 07-01 leakage row (see A) |
| 70 | 08-02: "quy tắc này đánh dấu nhiều sinh viên hơn số chỗ của danh sách 5 trên 20 … cán bộ cần một thứ hạng để biết nên liên hệ ai trước" |
| 71 | 08-02: "Một số nội dung khác cần dữ liệu riêng của đợt thí điểm: cách liên hệ …; các phép so sánh …; tỷ lệ liên hệ kịp thời (KPI phụ 2)" |

Clarity 2 (47 of 47):

| # | New text |
| :-- | :---- |
| 2 | 01-01: "mỗi module đóng vai trò một học phần của trường" |
| 3 | 01-01: "mỗi lượt mở là một lần module được giảng dạy (Mục 2.1)"; 2.1 gives the full definition and the short form "lượt mở" |
| 6 | 01-01: D1–D3 defined in the paragraph before Table 1.1 |
| 7 | 01-01 AQ3: "quy tắc dấu hiệu sớm (bỏ lỡ bài, nộp trễ hoặc không hoạt động; Mục 4.1)", "một lượt mở diễn ra sau" |
| 8 | 01-01 AQ4: two questions – who ranks first under "số lượt liên hệ tối đa mỗi tuần"; which lift and recall, overall and by subgroup; "Sinh viên nào" |
| 9 | "phần đánh giá việc liên hệ sinh viên được hoãn" (01-01, 01-02, 04-01, 04-02, 08-02) |
| 11 | 01-02: "phiên bản cơ sở của Milestone 1 (bản đề xuất đã chốt, với mục tiêu, KPI và các AQ)" |
| 13 | 01-02: "dữ liệu đáp ứng phần lớn bản đề xuất chứ không chỉ một phần nhỏ, đúng như điều kiện đầu vào của đề bài yêu cầu" |
| 16 | 02-00: "được kiểm chứng bằng một phép tính chạy trực tiếp trên dữ liệu" |
| 18 | 02-01 courses row: "độ dài lượt mở (số ngày)"; role "xác định ngày kết thúc và tháng bắt đầu của lượt mở" |
| 19 | 02-01 studentRegistration row: "xác định sinh viên đang học tại mỗi mốc; tính KPI" |
| 21 | 02-02: "OU gọi ngày này là cut-off date; báo cáo gọi là ngày đến hạn để phân biệt với hai thời điểm chốt dữ liệu" |
| 22 | 02-02: "Điểm này không có ngay vào ngày đến hạn: …"; "Trong khi đó, OULAD không ghi lại ngày công bố điểm" |
| 23 | 02-02: documented rule stated ("các bài làm trong kỳ chia nhau trọng số và mỗi lượt mở có một bài thi"), then the five runs that depart |
| 24 | 02-03: "18 ô (nhóm tuổi × lượt mở) và 29 ô (nhóm trình độ học vấn × lượt mở)" |
| 26 | 03-01: "Một số tên trong tệp khác với tên trong tài liệu: …" |
| 27 | 03-01: grain explained in three sentences ("Theo tài liệu … Trên thực tế … Vì vậy …") |
| 30 | "gộp" (aggregate) → "tổng hợp (aggregate)" in 03-01, 03-05, 05-00 |
| 32 | 03-02: "sau khi hết thời hạn đăng ký, vốn kết thúc hai tuần sau ngày bắt đầu" |
| 34 | 03-03: "đã đăng ký tính đến hết ngày 14 (ngày hết hạn đăng ký) và chưa rút tính đến hết ngày đó" |
| 36 | 03-04: "Tính đến hết ngày 13, chỉ 1 trong 22 lượt mở có TMA hoặc CMA đến hạn" |
| 37 | 03-04: "Để kiểm tra dự báo trên một lượt mở diễn ra sau (học trên năm 2013, đánh giá trên năm 2014), cần những cặp … Có 9 cặp như vậy" |
| 38 | 03-05: "Trung bình … có làm thay đổi một thước đo, nhưng mức thay đổi đã đo được và có giới hạn" |
| 40 | 03-05 DQ10: "Tính nộp trễ riêng cho TMA và CMA; quy tắc dấu hiệu sớm chỉ dùng nộp trễ TMA, vì ý nghĩa của CMA nộp trễ chưa rõ" |
| 44 | 04-00 steps numbered (1)–(5); 04-01 says the column cites them |
| 45 | 04-01 AQ2: "số lượt mở sinh viên học song song năm 2014 (dấu hiệu khối lượng học)" |
| 46 | 04-01 AQ3: "chỉ dùng điểm CMA, vì điểm TMA được trả muộn" |
| 47 | 04-01: old rule, why it fails, then "ba dấu hiệu" each in its own sentence |
| 48 | 04-01: lift and recall each defined in its own sentence; why 50% precision says little |
| 49 | 04-02: "Không có bản ghi (tính là 0)"; class explained before Table 4.2 |
| 50 | 05-00: "các bảng dữ liệu đã chuẩn bị giữ nguyên ô thiếu" / "Riêng ma trận đầu vào của mô hình điền ô thiếu bằng trung vị …" |
| 51 | 05-00: "tham số … được ước lượng (fit) trên các lượt mở năm 2013" |
| 53 | 06-01: "Đề bài khuyến nghị mười bước … Mỗi bước là một hàm …"; then three sentences for what the functions do |
| 54 | 06-00 three levels (see A); 06-01 "cả tám giai đoạn (script chứa mười bước trên là một trong số đó)" |
| 56 | 06-02 tma/cma_late_c: "đến hạn tính đến hết ngày c và được nộp sau ngày đến hạn, nhưng vẫn trong phạm vi đến hết ngày c" |
| 57 | 06-03 row: "Trung vị, tham số chuẩn hóa thang đo và danh sách nhóm giá trị của biến phân loại được ước lượng (fit) …" |
| 59 | 06-03: "mỗi fold để riêng một lượt mở làm phần đánh giá, đồng thời các fold được nhóm theo sinh viên …" |
| 60 | 07-01: "số sinh viên đang học tại ngày 13 lớn hơn tại ngày 14, vì số sinh viên rút vào ngày 14 nhiều hơn số đăng ký thêm" |
| 64 | 07-03: "văn bản chính sách chấm điểm duy nhất của OU mà nhóm tác giả tìm được ban hành năm 2025" |
| 65 | 07-03: "1,4% số dòng huấn luyện tại ngày 13 và 5,2% tại ngày 27" |
| 66 | 07-03: "số lượt liên hệ tối đa mỗi tuần"; why it is a risk (OU figure, not the university's) |
| 67 | 08-01: "bổ sung thêm một thời điểm chốt dữ liệu sớm hơn tại ngày 13" |
| 68 | 08-01: "trình bày một kết quả dự báo như một kết quả chỉ định chỉ bằng cách thêm khuyến nghị" |
| 69 | 08-02: "danh sách 3 hoặc 5 trên 20" explained before Table 8.1 |
| 73 | 09-00: "5–6 điểm phần trăm về tỷ lệ đạt (disparate impact)" (source S902) |
| 75 | 10-00: "cả bên soạn thảo lẫn bên phản biện đều là tác tử AI (agent)" |
| 76 | 10-00: "vì dữ liệu 2013–2014 có nhiều CMA nộp trễ, nhóm tác giả không áp dụng quy định này" |

Clarity 3 rewritten (21 of 23):

| # | New text |
| :-- | :---- |
| 1 | 01-00: "phiên bản mới nhất của các câu hỏi" |
| 4 | 01-01: "đã cập nhật theo các thay đổi trên và theo các quyết định xử lý khoảng trống dữ liệu (Mục 4)" |
| 5 | 01-01 AQ1 as questions: "Sinh viên lần đầu bỏ lỡ một bài được chấm điểm vào tuần nào?" |
| 10 | 01-01: "thu hẹp phạm vi đo các AQ cho phù hợp với OULAD" |
| 12 | 01-02: "không được sao chép mà được trỏ thẳng tới chính các tệp đó (hard link) và chỉ cho phép đọc" |
| 14 | 01-02: "việc chuyển sang bước chuẩn bị dữ liệu là hợp lý" |
| 17 | 02-01: "Bảng 2.1 (Dataset Understanding Map, bản mô tả tổng quan bộ dữ liệu) liệt kê bảy tệp dữ liệu gốc" |
| 20 | 02-02: "khác với tên trong tệp (Mục 3.1)" |
| 25 | 03-00: "kích thước và cấu trúc bảng (schema)" |
| 29 | "phiên bản đã loại dòng trùng" (03-01, 03-05, 05-00, 07-03, 12-01, 12-04, 12-05) |
| 31 | 03-02: "bộ dữ liệu vốn không chứa phần lớn kết quả bài thi" |
| 33 | 03-02: "quy định hiện hành của OU (ban hành năm 2025)" |
| 35 | "lớp thiểu số" (03-03, 08-01) |
| 43 | 04-01: "theo kết luận mà AQ đó cần đưa ra" |
| 52 | 05-00: reason "Cần để so sánh kết quả giữa các nhóm sinh viên" |
| 55 | 06-02: "ở OULAD, điểm số là ví dụ, vì dữ liệu không ghi ngày công bố điểm" |
| 62 | "truy vết nguồn gốc dữ liệu (lineage)" (07-02, 10-00, 12-00, 12-02, 12-03, 12-05) |
| 63 | 07-02: "Bản kê phiên bản (version manifest)" – glossary form kept, English added |
| 72 | 08-02: entry conditions as clauses with verbs, separated by semicolons |
| 74 | 09-00: "thông tin sức khỏe, trong đó có tình trạng khuyết tật" |
| 77 | 10-00: "bước kiểm tra rò rỉ thông tin thực sự có khả năng phát hiện lỗi: nếu một đặc trưng dùng dữ liệu sau thời điểm chốt, phép kiểm tra sẽ báo không đạt" |

Kept (2): #15 "khảo sát dữ liệu (profiling)" and #42 GREEN/YELLOW/RED follow the glossary and the task instruction.

## C. Term replacements across all twins

| Old | New | Where |
| :---- | :---- | :---- |
| chậm nhất vào (ngày c / thời điểm chốt) | tính đến hết ngày c / tính đến hết thời điểm chốt | 03-04, 03-05, 04-01, 06-02, 06-03, 07-01, 08-02, 00-2, 12-01, 12-02, 12-03, 12-04, 12-05 |
| khớp (fit sense) | ước lượng (fit) | 05-00, 06-03, 08-01, 12-01, 12-02, 12-04 |
| vắng mặt có ghi nhận | không có bản ghi (tính là 0) | 04-02, 03-05 (DQ17 decision) |
| dòng dõi dữ liệu | truy vết nguồn gốc dữ liệu (lineage) | 07-02, 10-00, 12-00, 12-02, 12-03, 12-05 |
| số sinh viên cán bộ liên hệ được mỗi tuần | số lượt liên hệ tối đa mỗi tuần | 01-01, 04-01, 04-02, 07-03, 08-01 |
| câu hỏi phân tích (after 1.1) | AQ | 03-05, 04-00, 08-02, 12-04 |
| gộp (aggregate) | tổng hợp | 03-01, 03-05, 05-00 |
| bản đối chiếu đã loại trùng | phiên bản đã loại dòng trùng | 03-01, 03-05, 05-00, 07-03, 12-01, 12-04, 12-05 |
| lượt mở module (explained once) | definition at 2.1 ("một lần module được giảng dạy, bắt đầu vào một tháng nhất định"), then "lượt mở" | 02-01; short gloss at first use in 01-01 and 02-00 |

## Checks

- `check_parity.py --report reports/milestone-3/report --lang vi`: 0 errors, 13 warnings (all in the kept English prompts of 12-05).
- `check_abbreviations.py --report reports/milestone-3/report --lang vi`: 14 abbreviations, 0 violations.
- `translation_status.py --lang vi`: 41 sections, 0 need translation; 36 edited files marked.
