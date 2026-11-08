## Phụ lục VI – Bằng chứng sử dụng AI tạo sinh

Một tác tử AI (AI agent) tìm các bộ dữ liệu ứng viên cho nhóm chúng em theo prompt dưới đây. Trong prompt này, mỗi tài liệu được gọi theo mục báo cáo chứa tài liệu đó; các bước xử lý tệp của tác tử được lược bỏ. Phụ lục I ghi mọi truy vấn mà tác tử đã chạy. Chúng em đã đối chiếu từng thông tin làm căn cứ do tác tử ghi lại với bản lưu của trang chính thức.

Prompt của AI hỗ trợ tìm kiếm và AI diễn giải metadata:

```text
You are the research agent for the dataset search of the MTH045 Milestone 2 report ("From requirements to collection").

1. Record every search, fetch and interpretation before the next step, and anchor every fact in a verbatim quote from its source.
2. Read the team's data requirements and the must-have gates G1–G5 (Section 2) and the brief sections 7–8 and 13. Build search keywords from the requirements (e.g. student completion, dropout, withdrawal, LMS/VLE interaction, assessment submission, clickstream, higher education, learning analytics, MOOC dropout).
3. Find and document at least six candidate open education datasets from official sources (landing page, DOI, repository of the provider, or the original paper), reading the documentation/data dictionary and license page of each before judging it. Include at least: OULAD (official page https://research.stem.open.ac.uk/ouanalyse/dataset/ and the Scientific Data paper), UCI "Predict Students' Dropout and Academic Success" (id 697), UCI "Student Performance" (id 320), UCI "Higher Education Students Performance Evaluation" (id 856), and at least two more found by your own search (for example KDD Cup 2015 / XuetangX MOOC dropout data, MOOCCubeX, EdNet, HarvardX-MITx person-course data, xAPI-Edu-Data). When a dataset is found via Kaggle/blog/GitHub, trace it to the official source or record that provenance is unclear.
4. For each candidate record facts with quote anchors: provider/authors, official URL/DOI, license or terms, version/release date, population and context (level, country, years), unit of analysis, outcome/target available (does it separate pass, fail and withdrawal?), within-semester timing (dated activity or dated assessments? granularity), number of semesters/course runs, size (rows/records), file formats, documentation available, anonymisation, sensitive attributes, citation. Only facts found on the source pages; write "not stated" otherwise.
5. Write one section per candidate with those fields, each fact followed by its source, and a short note per gate G1–G5 (met / partly / not met / unclear, with the evidence). Also write the brief's Search Log table (| Date | Query / source | Candidate dataset | URL/DOI | Reason considered | Result |), one row per query/candidate examined, including rejected ones.
6. Do not download any dataset.

Return at most 6 lines: candidates documented, sources fetched/partial/blocked, facts recorded, gate result per candidate in one line, unresolved questions.

Follow-up message sent during the task: the must-have gates were revised (G1 also requires a dated withdrawal; G2 split into G2a dated assessed tasks and G2b dated activity; G3 at least three course runs ordered in time with a later run for testing; G5 adds a persistent pseudonymous identifier); write the gate notes against the revised gates and note early tasks and enrolment dates per candidate.
```

Hai tác tử AI chạy trong hai phiên riêng phản biện công việc của chúng em tại hai thời điểm cố định: AI phản biện yêu cầu nhận xét trước khi chúng em chấm điểm bộ dữ liệu nào, còn AI phản biện lựa chọn nhận xét sau khi chúng em chấm điểm xong. Mỗi tác tử chỉ nhận đề bài và các tài liệu của chúng em có tên trong prompt của tác tử đó. Các prompt giữ nguyên tiếng Anh, trong đó mỗi tài liệu được gọi theo mục báo cáo chứa tài liệu đó. Bảng A.11 và Bảng A.12 tóm tắt từng nhận xét, kèm quyết định của chúng em và nội dung thay đổi.

Prompt của AI phản biện yêu cầu:

```text
You act as the "Requirement critic" role that the MTH045 Milestone 2 brief allows for generative AI (brief section 12: "Chỉ ra AQ nào cần timestamp, target, intervention data hoặc có leakage risk"). Read only: the brief, the team's frozen Milestone 1 baseline (Section 1.1) and the team's data requirements (Section 2). Do not read any dataset file or exploration result, and do not search the web.

Critique the data requirements: for each AQ, is anything missing (timestamps, target definition, denominator, prediction point, intervention data), is any requirement written as a dataset's column rather than a concept, is there leakage risk not covered, are the must-have gates G1–G5 right (too strict, too loose, missing one), and are the requirements consistent with the baseline (KPIs, decisions)? Do not propose datasets and do not rewrite the document.

Write at most 12 numbered critiques, most important first, each with: the passage (quote a few words), the problem, why it matters.
```

Bảng A.11 liệt kê mười hai nhận xét của AI phản biện yêu cầu và quyết định của chúng em đối với từng nhận xét.

**Bảng A.11. AI phản biện yêu cầu: nhận xét của AI, quyết định của chúng em và nội dung thay đổi**

| # | Nhận xét (tóm tắt) | Quyết định | Thay đổi |
| :---- | :---- | :---- | :---- |
| Q1 | Ngày rút học phần chỉ là điều kiện nên có, dù AQ3 cần thông tin này | Chấp nhận | G1 yêu cầu có thông tin rút học phần kèm ngày |
| Q2 | G2 chấp nhận dữ liệu chỉ có hoạt động kèm ngày, trong khi quy tắc của AQ3 và KPI phụ 1 cần bài được chấm điểm có ngày | Chấp nhận | Tách G2 thành hai: G2a là bài được chấm điểm và bài nộp có ngày, G2b là hoạt động trên nền tảng học tập có ngày. Có bài đến hạn trong tuần 1–4 là điều kiện nên có và được báo cáo theo từng kỳ mở module |
| Q3 | Chưa yêu cầu dữ liệu để tính mẫu số của KPI (thời gian điều chỉnh đăng ký học phần, tạm ngừng học, chuyển chương trình đào tạo) | Chấp nhận | Ngày bắt đầu và ngày kết thúc đăng ký, tính so với ngày bắt đầu học phần, là biến tối thiểu. Thông tin phân biệt tạm ngừng học với chuyển chương trình đào tạo vẫn là tùy chọn; nếu thiếu thông tin này, điểm khác so với cách tính KPI được ghi nhận |
| Q4 | Năm theo học và hình thức học chỉ là tùy chọn, dù các AQ có nêu | Chấp nhận một phần | Hai biến này vẫn là tùy chọn. Nếu đặt thành điều kiện bắt buộc thì không bộ dữ liệu mở nào đáp ứng được và chỉ còn dữ liệu giả lập, loại dữ liệu đề bài không cho phép. Chúng em nêu ngay trong yêu cầu dữ liệu những phần câu hỏi sẽ chỉ đạt mức Một phần nếu thiếu hai biến này |
| Q5 | G3 yêu cầu ba kỳ mở trong khi AQ1 cần bốn học kỳ; không yêu cầu thứ tự thời gian | Chấp nhận | G3 yêu cầu ít nhất ba kỳ mở học phần xếp theo thứ tự thời gian, trong đó có kỳ mở muộn hơn để đánh giá; AQ1 đạt mức Một phần khi có ít hơn bốn học kỳ |
| Q6 | Thiếu các nguồn rò rỉ thông tin (điểm trung bình của học phần, ngày công bố điểm, khối lượng học tập, đặc điểm cá nhân được cập nhật, chuẩn hóa) | Chấp nhận | Bổ sung năm dòng vào bảng rò rỉ thông tin |
| Q7 | Bài bị bỏ lỡ được đếm cả sau khi sinh viên rút học phần | Chấp nhận | Quy tắc: một bài chỉ tính là bị bỏ lỡ nếu đến hạn trước ngày sinh viên rút học phần |
| Q8 | Chưa quy định cách đánh số tuần và độ trễ của dữ liệu | Chấp nhận | Ngày bắt đầu học phần là biến tối thiểu. Các thời điểm dự báo (hết tuần 2 và hết tuần 4) đã chừa một tuần cho độ trễ của dữ liệu trước khi có danh sách ở tuần 3 và tuần 5 |
| Q9 | Không có điều kiện bắt buộc về mã định danh liên kết được giữa các bảng và các học phần | Chấp nhận | G5 yêu cầu mã định danh sinh viên đã giả danh hóa, cố định giữa các bảng, các học phần và các học kỳ |
| Q10 | Không có yêu cầu về khối lượng dữ liệu hoặc phân bố kết quả | Chấp nhận một phần | Điều kiện nên có: ở kỳ mở dùng để đánh giá, mỗi nhóm được so sánh có ít nhất 100 sinh viên về sau không hoàn thành học phần (giả định cần xác nhận ở Milestone 3) |
| Q11 | AQ4 trộn lẫn dữ liệu và giả định; thiếu thông tin phân công cố vấn học tập; đã biết trước là không có sổ theo dõi liên hệ | Chấp nhận | Phiên bản cơ sở ghi số sinh viên cán bộ liên hệ được mỗi tuần là giả định. Thông tin phân công cố vấn học tập được bổ sung ở dạng tùy chọn. Mỗi sinh viên chỉ có một dòng trong danh sách, dù học nhiều học phần. Sổ theo dõi liên hệ được nêu ngay là khoảng trống dữ liệu; dữ liệu chuyển tiếp đến phòng công tác sinh viên được đánh dấu là nhạy cảm |
| Q12 | Cách diễn đạt nêu tên cột dữ liệu hoặc tên hệ thống; cách quy đổi điểm chưa rõ | Chấp nhận | Yêu cầu được diễn đạt theo khái niệm ("thông tin rút học phần và ngày rút", "ngày bắt đầu và ngày kết thúc đăng ký", "hoạt động trên nền tảng học tập có ngày"); mọi mức điểm đạt, kể cả các mức cao hơn, đều tính là hoàn thành học phần |

Prompt của AI phản biện lựa chọn:

```text
You act as the "Selection reviewer" role that the MTH045 Milestone 2 brief allows for generative AI (brief section 12: "Phản biện Dataset Selection Matrix và phát hiện criteria bị bỏ sót"; "Không chấp nhận recommendation nếu không có evidence"). Read only: the brief, the requirements and gates (Section 2), the candidate facts with their sources and verbatim quotes, and the team's scoring and decision (Section 4). Check that each score rests on a recorded fact. Do not search the web and do not open any dataset file.

Challenge the selection: scores not backed by a recorded fact, criteria applied inconsistently across candidates, gates that were misread, a candidate rejected or kept for a weak reason, a criterion the brief lists that is missing, a supplementary dataset that should have been considered, and anything about the selected dataset that the team treats as settled without evidence. Do not rescore the matrix yourself and do not propose new datasets unless you name the evidence gap they would close.

Write at most 10 numbered critiques, most important first, each with the passage, the problem and why it matters.
```

Bảng A.12 liệt kê mười nhận xét của AI phản biện lựa chọn và quyết định của chúng em đối với từng nhận xét.

**Bảng A.12. AI phản biện lựa chọn: nhận xét của AI, quyết định của chúng em và nội dung thay đổi**

| # | Nhận xét (tóm tắt) | Quyết định | Thay đổi |
| :---- | :---- | :---- | :---- |
| S1 | G3 được coi là đạt, dù chưa chắc chắn ở từng module | Chấp nhận | Quyết định chọn OULAD phụ thuộc vào kết quả kiểm tra cấu trúc ban đầu; nêu rõ phương án dự phòng |
| S2 | Phần quyết định về các điều kiện bắt buộc không ghi rằng G5 chỉ đạt "Một phần" | Chấp nhận | Quyết định chọn OULAD phụ thuộc vào kết quả kiểm tra cấu trúc ban đầu; nêu rõ các phần câu hỏi chỉ đạt mức Một phần |
| S3 | Các loại kết quả được khẳng định mà chưa có thông tin làm căn cứ | Chấp nhận | Tiêu chí mức sẵn có của biến kết quả được chấm 1 điểm; các giá trị đạt/trượt được kiểm tra ở bước kiểm tra cấu trúc ban đầu |
| S4 | Tiêu chí mức sẵn có và thời điểm có của các biến giải thích được chấm 2 điểm dù còn điều kiện chưa rõ | Chấp nhận | Chấm 1 điểm; ghi chú về ngày công bố điểm, bài không nộp và các bài đến hạn sớm |
| S5 | Phần đánh giá bỏ qua việc các module của OULAD được chọn theo tỷ lệ trượt cao | Chấp nhận | Bổ sung vào tiêu chí mức phù hợp của tổng thể, tiêu chí đạo đức và tính đại diện cùng phần lý do lựa chọn |
| S6 | Cách chấm "không nêu" và danh sách điều kiện bắt buộc không đạt chưa nhất quán | Chấp nhận | "Không nêu" được chấm 0 ở mọi ứng viên; HarvardX không đạt G4; G4 của xAPI chưa rõ; mỗi điểm số đều nêu thông tin làm căn cứ; bỏ các số liệu không có căn cứ |
| S7 | Mức đáp ứng các AQ được chấm 2 dù có các phần chỉ đạt mức Một phần | Chấp nhận | Chấm 1 điểm |
| S8 | Không có số phiên bản, có hai nơi phát hành | Chấp nhận | Tiêu chí tài liệu mô tả và nguồn gốc dữ liệu được chấm 1 điểm; phần thu thập dữ liệu ghi rõ bản nào được dùng và mã kiểm tra của bản đó |
| S9 | Mẫu số chưa được kiểm tra | Chấp nhận | Bước kiểm tra cấu trúc ban đầu đếm số lượt hủy đăng ký vào hoặc trước ngày 0 |
| S10 | Lập luận về bộ dữ liệu bổ sung | Chấp nhận | Nêu rõ trở ngại thực sự của XuetangX (giấy phép, biến kết quả); phần kiểm tra khả năng khái quát sang bối cảnh khác được ghi là giới hạn còn mở |
