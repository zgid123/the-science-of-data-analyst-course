## Phụ lục V – Nhật ký quyết định về AI và các prompt

Bảng A.16 là Nhật ký quyết định về AI (AI Decision Log) của sản phẩm bàn giao F; mỗi dòng ứng với một đề xuất quan trọng của AI, kèm quyết định của nhóm và bằng chứng dùng để kiểm chứng.

**Bảng A.16. Nhật ký quyết định về AI**

| # | Vai trò (đề bài, mục 14) | Đề xuất của AI | Quyết định của nhóm | Chấp nhận / từ chối | Bằng chứng kiểm chứng | Tác động đến pipeline |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| A1 | AI diễn giải từ điển dữ liệu (data dictionary interpreter) | Điểm CMA được công bố trong vòng 7 ngày và CMA không thể nộp trễ [3] | Dùng độ trễ 7 ngày cho điểm CMA; không áp dụng quy định cấm nộp trễ cho giai đoạn 2013–2014 | Chấp nhận một phần | 32.991 trên 69.956 bài CMA được nộp sau ngày đến hạn (profile.json) | `cma_score_mean_c` dùng các điểm của bài nộp ≤ c − 7; số bài nộp trễ được tách theo TMA và CMA |
| A2 | AI diễn giải từ điển dữ liệu | IMD của xứ Anh (England) chỉ bao phủ xứ Anh; các quốc gia khác của UK dùng chỉ số riêng [5], [6] | Giữ nguyên imd_band như dữ liệu ghi nhận; "Missing" là một nhóm riêng; không đưa ra nhận định gộp giữa các quốc gia | Chấp nhận | imd_band thiếu ở 40,1% số lượt đăng ký học của North Region và 22,5% số lượt của Ireland (profile.json) | imd_band là cột kiểm tra công bằng; các dòng kiểm tra công bằng tách riêng "Missing" |
| A3 | AI hỗ trợ EDA và danh mục kiểm tra chất lượng (EDA and quality checklist partner) | Kiểm tra xem các dòng lượt nhấp trùng lặp hoàn toàn là bản sao hay là các bản ghi riêng biệt | Chạy phép kiểm tra so với mức ngẫu nhiên trên các nhóm hai dòng | Chấp nhận | 31,5% bằng nhau so với 24,0% kỳ vọng; thấp hơn mức ngẫu nhiên ở bài kiểm tra ngắn (profile.json) | Giữ mọi dòng, dựng phiên bản đã bỏ dòng trùng |
| A4 | AI phản biện quy trình chuẩn bị (preparation critic) | Độ chính xác của danh sách ≥ 50% gần với tỷ lệ nền; nên đo lift và tỷ lệ phát hiện tối đa có thể đạt | Phát biểu lại giới hạn của AQ4 (C13) | Chấp nhận | Tỷ lệ không hoàn thành 45,3% và 44,2% tại hai thời điểm chốt dữ liệu | Bảng độ dài danh sách theo số sinh viên cán bộ liên hệ được; kế hoạch chỉ số cho Milestone 4 |
| A5 | AI phản biện quy trình chuẩn bị | Các cờ suy ra từ biến mục tiêu có thể lọt vào nhóm đặc trưng | Gán vai trò `target_derived`, loại khỏi các bảng đặc trưng | Chấp nhận | Các cờ được định nghĩa từ final_result | V14 và V13 không cho phép các cờ này |
| A6 | AI phản biện quy trình chuẩn bị | Việc nộp trễ CMA, vốn chưa rõ ý nghĩa, chi phối quy tắc | Quy tắc dùng việc nộp trễ TMA; giữ biến thể có tính nộp trễ CMA | Chấp nhận | 47,2% bài nộp CMA trễ so với 16,8% bài nộp TMA | `early_sign_rule`, `early_sign_rule_cma` (C10) |
| A7 | AI gợi ý xây dựng đặc trưng (feature engineering ideator) | Khoảng cách đến lần hoạt động gần nhất, xu hướng, khoảng thời gian trước ngày bắt đầu, lượt nhấp theo loại tài nguyên, bài nộp sớm; ngày nhấp đầu tiên | Thêm tất cả, trừ ngày nhấp đầu tiên, thành một nhóm mở rộng | Chấp nhận một phần | Lượt nhấp trước ngày bắt đầu đã có trong `clicks_pre`, `clicks_pre14` | 10 đặc trưng mở rộng |
| A8 | AI phản biện quy trình chuẩn bị | Trước khi lập mô hình, báo cáo tỷ lệ kết quả của các lượt đăng ký học trong tập kiểm thử thuộc sinh viên đã có mặt năm 2013 | Hiện chỉ báo cáo số lượng các lượt này | Chấp nhận một phần | Xem kết quả của tập kiểm thử trong giai đoạn chuẩn bị làm mất tính độc lập của phép kiểm thử (mục 11 của đề bài) | 1.962 lượt được đánh dấu; kết quả để lại cho Milestone 4 |
| A9 | AI phản biện quy trình chuẩn bị (kiểm tra rò rỉ thông tin) | 93 lượt đăng ký học Withdrawn không có ngày rút nằm trong các bảng thuộc tập kiểm thử dưới dạng mẫu dương dễ đoán | Cờ phục vụ đánh giá; báo cáo chỉ số khi có và khi không có các lượt này | Chấp nhận | 89 trên 92 lượt tại ngày 13 là dòng của tập kiểm thử; 41% không có lượt nhấp sớm nào | `eval_withdrawal_day_unknown` |
| A10 | AI phản biện quy trình chuẩn bị (kiểm tra rò rỉ thông tin) | Các bài đến hạn trước ngày đăng ký bị tính là bỏ lỡ; V13 không thể báo lỗi (FAIL); một dòng của V14 bị vô hiệu hóa bằng chú thích | Sửa công thức và cả hai phép kiểm tra | Chấp nhận | 6 bài tại ngày 27; đọc mã nguồn | Chạy lại pipeline: 22 trên 22 phép kiểm tra PASS |
| A11 | Trợ lý viết mã (code assistant) | Soạn thảo mọi script của gói (hiểu dữ liệu, khảo sát dữ liệu, chuẩn bị, phép biến đổi, kiểm tra, notebook) | Giữ lại sau khi rà soát, kiểm thử đơn vị và đếm lại độc lập | Chấp nhận | 13 trên 13 con số khớp với kết quả đếm lại riêng bằng mã khám phá dữ liệu; 9 kiểm thử đơn vị trên bản ghi giả lập; 6 đặc trưng được tính lại từ dữ liệu gốc cho từng dòng, không có sai khác nào; một dòng được đếm lại thủ công từ các tệp gốc | `src/`, `tests/` của gói |
| A12 | Trợ lý viết tài liệu (documentation assistant) | Soạn thảo từ điển dữ liệu, bảng truy vết nguồn gốc dữ liệu, README và nhật ký biến đổi dữ liệu | Được tạo tự động từ mã nguồn và đã kiểm tra | Chấp nhận | V14: mọi cột đã chuẩn bị đều được mô tả kèm vai trò và nguồn | `data_dictionary.md`, `lineage.md` |
| A13 | Trợ lý tạo dữ liệu giả lập (synthetic-data assistant) | Một vài bản ghi giả lập quy mô nhỏ dùng để kiểm thử công thức | Chỉ dùng dữ liệu mẫu mức A, có gắn nhãn, không bao giờ đưa vào bảng hoặc phát hiện nào | Chấp nhận | Đề bài, mục 8.3, mức A | `tests/test_features.py` |

AI phản biện quy trình chuẩn bị nhận chỉ dẫn dưới đây và chỉ đọc nhật ký vấn đề chất lượng dữ liệu, ma trận quyết định, các bản đặc tả, nhật ký mức phù hợp giữa AQ và dữ liệu cùng kết quả khảo sát dữ liệu. Trong cả hai chỉ dẫn, các tệp được gọi theo vị trí trong Gói dữ liệu đã chuẩn bị.

> You are a critical reviewer of a data preparation plan for an education analytics project (course completion and
> early warning on the Open University Learning Analytics Dataset, OULAD). Read only these files:
> `data/metadata/quality_issue_log.md`,
> `data/metadata/decision_matrix.md`, `feature_spec.md`, `split_spec.md`,
> the AQ–Data Fit Decision Log (Section 4) and, for numbers, `data/metadata/profile.json`.
> Challenge the plan as a sceptical senior analyst would: (1) imputation, de-duplication, outlier and encoding
> choices; (2) any feature that could leak information from after its cut-off or from the test runs; (3) the split
> and the handling of students seen in both years; (4) the population rules and denominators; (5) whether any
> decision is cleaning by habit rather than tied to an analytical question; (6) features that are missing but
> computable from the real fields at the cut-off. Do not invent facts about the data: cite the file and key for
> every number you use, and say "not verifiable from these files" otherwise. Return at most 12 numbered critiques,
> each with: the issue, why it matters (which AQ), a concrete recommendation, and severity (high / medium / low).

Bảng A.17 ghi lại quyết định về từng nhận xét trong 12 nhận xét của AI phản biện này.

**Bảng A.17. Quyết định về các nhận xét của AI phản biện quy trình chuẩn bị**

| # | Nhận xét (tóm tắt) | Quyết định | Bằng chứng dùng để kiểm chứng | Tác động đến pipeline |
| :---- | :---- | :---- | :---- | :---- |
| 1 | Độ chính xác của danh sách ≥ 50% trong AQ4 gần với tỷ lệ nền (45,3% tại ngày 13, 44,2% tại ngày 27; 24,9–58,3% theo kỳ mở) | Chấp nhận | P.outcome; danh sách theo số sinh viên cán bộ liên hệ được (3 hoặc 5 sinh viên trên mỗi nhóm 20 sinh viên) đặt mức trần cho tỷ lệ phát hiện | Chất lượng danh sách của AQ4 và AQ3 được đo bằng lift so với tỷ lệ nền của kỳ mở và bằng tỷ lệ phát hiện so với mức tối đa mà một danh sách cùng kích thước có thể đạt, với danh sách ngẫu nhiên và quy tắc dấu hiệu sớm làm mốc so sánh (nhật ký thay đổi, C13); `capacity_by_run` chứa kích thước các danh sách |
| 2 | Các cờ suy ra từ biến mục tiêu và `registration_missing` có thể lọt vào nhóm đặc trưng | Chấp nhận | `withdrawal_day_missing` và `unregistered_not_withdrawn` là hàm của final_result; 39 trên 45 lượt thiếu ngày đăng ký là Withdrawn (P.missing) | Hai cờ này chỉ có trong `enrolment` với vai trò `target_derived`; `registration_missing` được chuyển sang nhóm mở rộng; V14 báo lỗi (FAIL) nếu một cột suy ra từ biến mục tiêu xuất hiện trong bảng đặc trưng |
| 3 | Tại ngày 13, quy tắc thực chất là quy tắc về việc không hoạt động | Chấp nhận | Bài có ngày đến hạn tính đến hết ngày 13 chỉ có ở 1 trên 22 kỳ mở (P.temporal) | Lưu các thành phần của quy tắc (`rule_missed`, `rule_tma_late`, `inactive_last7`); tỷ lệ sinh viên được từng thành phần đánh dấu theo kỳ mở và thời điểm chốt có trong bản tóm tắt kết quả kiểm tra; quy tắc tại ngày 13 được gọi là quy tắc hoạt động |
| 4 | Sinh viên học lại và sinh viên học cùng lúc nhiều module là các đơn vị phụ thuộc nhau | Chấp nhận một phần | `student_in_training_runs` và `concurrent_runs` có trong các bảng | Báo cáo số lượt đăng ký học thuộc tập kiểm thử được đánh dấu (không xem kết quả nào của tập kiểm thử, nên hiện chưa tính tỷ lệ kết quả của nhóm này như đề nghị); quy trình của Milestone 4: các fold (phần chia trong kiểm định chéo) được nhóm theo kỳ mở và sinh viên trong năm 2013, khoảng bootstrap được phân cụm theo sinh viên; danh sách được lập theo từng kỳ mở module, nên một sinh viên học hai module có thể xuất hiện trong danh sách của hai giảng viên hướng dẫn |
| 5 | CCC không có trong tập huấn luyện; chỉ có 9 nhóm để tinh chỉnh siêu tham số | Chấp nhận | `paired_run` = false với CCC-B, CCC-J, EEE-B, GGG-B | Báo cáo như một phép đánh giá trên module mới; dùng các fold loại trừ từng kỳ mở (leave-one-run-out) trong năm 2013, kèm phương sai giữa các fold (Milestone 4) |
| 6 | Tỷ lệ dòng trùng lặp có thể thay đổi giữa hai năm | Chấp nhận | Tỷ lệ dòng thừa là 6,82% ở các kỳ mở năm 2013 và 7,87% ở các kỳ mở năm 2014 (P.duplicates) | Lượt nhấp gốc là đại lượng chính đã xác định từ trước; phiên bản `_dedup` là biến thể dùng để kiểm tra độ nhạy, nếu được chọn thì chỉ chọn trên các fold năm 2013 trước mọi bước đánh giá trên năm 2014; tỷ lệ hoạt động so với trung vị của kỳ mở loại bỏ khác biệt ở mức kỳ mở |
| 7 | Điểm CMA gần như trống tại ngày 13; cách điền giá trị thiếu chưa được xác định | Chấp nhận | Bài đến hạn sớm nhất rơi vào ngày 12–61 tùy kỳ mở (P.temporal) | Thêm `cma_marked_c` (số điểm đã biết); điểm vẫn để rỗng, không điền; tỷ lệ dòng có điểm tại mỗi thời điểm chốt được báo cáo; Milestone 4 chỉ dùng điểm này nếu ít nhất 10% dòng huấn luyện có giá trị |
| 8 | Thiếu các đặc trưng tính được | Chấp nhận một phần | Các trường đều có trước thời điểm chốt | Thêm thành một nhóm mở rộng: khoảng cách đến lần hoạt động gần nhất (`days_since_last_click`), xu hướng (`trend_last_week`), khoảng thời gian cố định trước ngày bắt đầu (`clicks_pre14`), lượt nhấp theo bốn loại tài nguyên được dùng nhiều nhất, các bài nộp trước ngày đến hạn; không thêm ngày nhấp đầu tiên, vì `clicks_pre` và `clicks_pre14` đã phản ánh mức tham gia trước ngày bắt đầu |
| 9 | Có các bản sao tuyến tính giữa các đặc trưng lượt nhấp | Chấp nhận | Tại cả hai thời điểm chốt, bảy ngày gần nhất trùng với tuần lịch gần nhất | `clicks_last7` chỉ được giữ làm nguồn của `inactive_last7`, không làm đặc trưng; từ điển dữ liệu ghi rõ `clicks_0c` = tổng các cột theo tuần, nên mô hình tuyến tính chỉ dùng một trong hai |
| 10 | Ý nghĩa của việc nộp trễ CMA không được ghi trong tài liệu | Chấp nhận | 32.991 trên 69.956 bài nộp CMA sau ngày đến hạn, so với 16.320 trên 97.088 bài nộp TMA (P.validity) | Quy tắc dấu hiệu sớm = bỏ lỡ một bài, nộp trễ một TMA hoặc không có hoạt động trong bảy ngày gần nhất; `early_sign_rule_cma` là biến thể thêm việc nộp trễ CMA, dùng để kiểm tra độ nhạy; phát biểu lại C10 trong nhật ký thay đổi |
| 11 | Các nhóm nhỏ và nhóm imd "Missing" | Chấp nhận một phần | 93 + 45 lượt đăng ký học được gắn cờ; nhóm imd "Missing" tập trung ở hai vùng | KPI được báo cáo khi có và khi không có 138 lượt được gắn cờ trong bản tóm tắt kết quả kiểm tra; "Missing" là một dòng riêng trong bước kiểm tra công bằng; không loại lượt nào |
| 12 | Các phép biến đổi theo thói quen và trung vị bằng 0 | Chấp nhận | Mã hóa one-hot sẽ làm mất thứ tự của các biến phân loại có thứ tự | Tỷ lệ hoạt động so với trung vị của kỳ mở là (lượt nhấp + 1) ÷ (trung vị của kỳ mở + 1); ma trận sẵn sàng cho mô hình chỉ dành cho mô hình tuyến tính: biến phân loại có thứ tự dùng mã thứ bậc kèm biến chỉ báo giá trị thiếu, biến định danh dùng one-hot, các số đếm qua log1p rồi chuẩn hóa; mô hình cây dùng các bảng dữ liệu đã chuẩn bị; cờ khoảng trống trong quá trình ghi nhận dữ liệu chỉ nằm trong `student_week` |

AI kiểm tra rò rỉ thông tin (leakage auditor) nhận chỉ dẫn dưới đây và được phép truy vấn các tệp đã chuẩn bị và các tệp gốc nhưng không được thay đổi các tệp này.

> You are an independent auditor of data leakage in a preparation pipeline for early prediction of course
> non-completion on OULAD (prediction points: end of day 13 and end of day 27 of each module run; training runs 2013,
> test runs 2014). Read `src/prepare_data.py`, `fit_transforms.py`, `validate_prepared.py`,
> `dictionary.py`, `common.py` and `data/metadata/feature_spec.md`, `split_spec.md`,
> `decision_matrix.md`. You may run read-only Python with Python (polars) on
> `data/processed/*.parquet` and `data/raw/*.csv`, writing
> nothing except your report. Look for: (1) any feature that uses information dated after its cut-off or derived from
> the outcome; (2) any population rule that uses future information (who is in a cut-off view); (3) any statistic
> computed across runs or with test rows that a model would learn from; (4) train–test contamination in
> fit_transforms.py; (5) identifiers or columns that could act as a proxy for the target; (6) bugs in the feature
> formulas (off-by-one days or weeks, banked results, exams, duplicates). For every finding give the file and line
> or the query and its result, the risk, and a fix, with severity (high / medium / low). Do not report a finding you
> could not support with code or a query result. At most 10 findings.

Bảng A.18 ghi lại bằng chứng và tác động của từng phát hiện trong 8 phát hiện của AI kiểm tra rò rỉ thông tin; nhóm chấp nhận cả 8 phát hiện.

**Bảng A.18. Quyết định về các phát hiện của AI kiểm tra rò rỉ thông tin**

| # | Phát hiện (mức độ nghiêm trọng) | Bằng chứng dùng để kiểm chứng | Tác động đến pipeline |
| :---- | :---- | :---- | :---- |
| F1 | 93 lượt đăng ký học Withdrawn không có ngày rút nằm trong cả hai bảng theo thời điểm chốt dưới dạng mẫu dương; tại ngày 13, 89 trên 92 lượt thuộc các kỳ mở của tập kiểm thử (trung bình) | `eval_withdrawal_day_unknown` đếm được 92 (ngày 13) và 93 (ngày 27), trong đó 89 và 90 thuộc các kỳ mở của tập kiểm thử | Thêm cờ phục vụ đánh giá vào các bảng đặc trưng (vai trò đánh giá, không bao giờ là đặc trưng); Milestone 4 báo cáo chỉ số trên tập kiểm thử khi có và khi không có các dòng này |
| F2 | Các bảng đặc trưng chứa id_student, final_result và non_completion, trong khi mô hình cây được hướng dẫn dùng nguyên các bảng này (trung bình) | Các cột được liệt kê trong schema của bảng | `predictor_sets.json` nêu các đầu vào duy nhất của mô hình cho từng họ mô hình; sửa docstring của `fit_transforms.py` |
| F3 | Biến chỉ báo giá trị thiếu của registration_lead trùng với cờ mở rộng registration_missing trong ma trận chính (thấp) | 5 dòng huấn luyện, đều là sinh viên không hoàn thành | Không dùng biến chỉ báo cho registration_lead; cờ này vẫn là đặc trưng mở rộng |
| F4 | Việc có tạo biến chỉ báo giá trị thiếu hay không được quyết định dựa trên cả các dòng của tập kiểm thử (thấp) | `fit()` đọc df thay vì các dòng huấn luyện | Biến chỉ báo được quyết định trên các dòng huấn luyện; trung vị huấn luyện được tính cho mọi cột số |
| F5 | Các bài đến hạn trước ngày đăng ký của sinh viên đăng ký muộn bị tính là bỏ lỡ tại ngày 27 (thấp) | 6 bài như vậy tại ngày 27 | Một bài chỉ được tính khi đến hạn vào hoặc sau ngày đăng ký; phép đếm lại trong script kiểm tra và kiểm thử đơn vị trên bản ghi giả lập được sửa tương ứng |
| F6 | Sinh viên không có lượt nhấp bị gán trung vị huấn luyện (1 ngày) cho days_since_last_click (thấp) | Trung vị 1,0 trong `transform_params.json` | Gán giá trị c + 1 trong bảng cho sinh viên không có lượt nhấp trong các ngày 0…c |
| F7 | V13 không bao giờ có thể báo lỗi (FAIL), vì dữ liệu đã được lọc trước khi kiểm tra (thấp) | Đọc mã nguồn | V13 đếm lại lượt nhấp mà không áp dụng thời điểm chốt nào và yêu cầu kết quả của pipeline chỉ khác số đếm lại ở đúng những dòng có lượt nhấp về sau (26.755 và 25.663 dòng) |
| F8 | Phép kiểm tra V14 đối với các đặc trưng mở rộng bị vô hiệu hóa do một chú thích đặt sai chỗ (thấp) | Dòng 170 của `validate_prepared.py` | Tách dòng; V14 kiểm tra cả hai danh sách đặc trưng |

**Các quy tắc hình thành từ các lượt rà soát.** Các lượt rà soát định hình bốn quy tắc mà pipeline áp dụng. Thứ nhất, danh sách của AQ4 được đánh giá theo mức vượt so với một danh sách chọn ngẫu nhiên (lift), vì giới hạn 50% cho độ chính xác của danh sách nằm sát tỷ lệ nền (C13). Thứ hai, việc nộp trễ CMA, gặp ở 47,2% số bài nộp CMA so với 16,8% số bài nộp TMA, không được đưa vào
quy tắc dấu hiệu sớm (C10). Thứ ba, một bài chỉ bị tính là bỏ lỡ khi đến hạn vào hoặc sau ngày đăng ký của sinh viên; AI
kiểm tra rò rỉ thông tin đã chỉ ra sáu bài tại ngày 27 có ngày đến hạn trước ngày sinh viên đăng ký. Thứ tư, phép kiểm tra
rò rỉ thông tin được xây dựng sao cho có thể báo lỗi (FAIL), đúng như AI kiểm tra rò rỉ thông tin yêu cầu.

Trong 12 nhận xét của AI phản biện quy trình chuẩn bị, nhận xét thứ tư (Phụ lục V) chỉ được chấp nhận một phần, vì nhóm luôn giữ nguyên tắc không xem kết quả của tập kiểm thử trong lúc chuẩn bị dữ liệu. Nhận xét này đề nghị báo cáo tỷ lệ kết quả của các lượt đăng ký học trong
tập kiểm thử thuộc sinh viên đã có mặt năm 2013 trước khi lập mô hình. Nhóm báo cáo số lượng các lượt này (1.962) nhưng không báo cáo kết quả, vì nếu xem kết quả, tập kiểm thử sẽ tham gia vào bước chuẩn bị, điều mà đề bài không cho phép [1].

**Các quyết định khác và phản tư.**

Đề xuất của AI diễn giải từ điển dữ liệu về chính sách năm 2025 của OU cũng được nhóm chấp nhận một phần. Từ chính sách này, AI rút ra một quy tắc dùng được cho điểm CMA: điểm được công bố trong vòng bảy ngày. Tuy nhiên, quy tắc rằng CMA không được nộp trễ không khớp với dữ liệu, trong đó có 32.991 bài nộp CMA trễ hạn, nên nhóm không áp dụng quy tắc này.

**Phản tư.** Các lượt rà soát hữu ích nhất ở những chỗ AI phản biện phải lập luận từ dữ liệu thay vì từ lời khuyên
chung: phép kiểm tra dòng trùng lặp, lập luận về tỷ lệ nền và phát hiện về lỗi ngày đăng ký đều làm thay đổi pipeline. Mỗi điểm này đều được xác nhận bằng một phép đếm trước khi nhóm chấp nhận.

**Vai trò của AI và cách kiểm chứng.** Bảng dưới đây nêu bảy vai trò, việc AI đã làm trong từng vai trò và cách kiểm
chứng kết quả.

| Vai trò (đề bài) | Việc AI đã làm | Cách kiểm chứng kết quả |
| :---- | :---- | :---- |
| AI diễn giải từ điển dữ liệu | Đọc bài mô tả dữ liệu, chính sách đánh giá của OU và tài liệu về IMD | Mỗi thông tin làm căn cứ chỉ được giữ khi có đoạn trích nguyên văn; quy định năm 2025 rằng CMA không được nộp trễ được kiểm tra trên dữ liệu và không được áp dụng |
| AI hỗ trợ EDA và danh mục kiểm tra chất lượng | Đề xuất phép kiểm tra xem các dòng lượt nhấp trùng lặp có phải là bản sao hay không | Chạy phép kiểm tra trên dữ liệu: 31,5% nhóm có số lượt nhấp bằng nhau, so với 24,0% nếu chỉ do ngẫu nhiên |
| Trợ lý viết mã | Soạn thảo mọi script của gói | 13 con số khớp với kết quả đếm lại độc lập; 9 kiểm thử đơn vị; 6 đặc trưng được tính lại cho từng dòng mà không có sai khác; một dòng được đếm lại thủ công |
| AI phản biện quy trình chuẩn bị | Rà soát kế hoạch trong một phiên riêng (12 nhận xét) và kiểm tra rò rỉ thông tin (8 phát hiện) | Mỗi nhận xét được kiểm tra trên dữ liệu hoặc mã nguồn trước khi nhóm quyết định |
| AI gợi ý xây dựng đặc trưng | Đề xuất khoảng cách đến lần hoạt động gần nhất, xu hướng, khoảng thời gian trước ngày bắt đầu, lượt nhấp theo loại tài nguyên và bài nộp sớm | Mỗi đặc trưng đều tính được từ các trường thật trước thời điểm chốt dữ liệu; các đặc trưng này được thêm thành nhóm đặc trưng mở rộng |
| Trợ lý viết tài liệu | Soạn thảo từ điển dữ liệu, bảng truy vết nguồn gốc dữ liệu, hướng dẫn sử dụng gói và nhật ký biến đổi dữ liệu | Được tạo từ mã nguồn; V14 báo lỗi (FAIL) nếu một cột không có mục mô tả |
| Trợ lý tạo dữ liệu giả lập | Viết một vài bản ghi giả lập nhỏ có gắn nhãn | Chỉ dùng mức A trong chính sách của đề bài; không bao giờ đi vào bảng dữ liệu hoặc phát hiện nào |
