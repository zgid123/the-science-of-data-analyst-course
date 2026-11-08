# Topic glossary: early-warning prediction, evaluation and fairness

The modelling vocabulary of team N04's course-completion project: the prediction set-up, time-based splits and leakage controls, the candidate models, the evaluation measures and statistical tests, the capacity-limited contact list, fairness and governance checks, and the limits on causal claims. General statistical and machine-learning terms live in the common layer (research-and-evaluation, ai-and-ml); the rows here fix the project's own sense of a term or its wording around the contact list.

## Prediction set-up

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| feature (predictor) | đặc trưng | | |
| prediction point | thời điểm dự báo | equals the data cut-off in this report | |
| prediction target / unit / horizon | biến cần dự đoán / đơn vị phân tích / khoảng thời gian dự đoán | | |
| predictor (in running text) | đặc trưng | follows the row "feature (predictor)"; Milestone 3 uses "đặc trưng" throughout; Milestone 4 keeps its own "biến dự báo" | |
| primary / extended predictors | đặc trưng chính / đặc trưng mở rộng | the 20 default columns and the 10 comparison columns of the feature views | |
| risk score | điểm rủi ro | never a bare "điểm", which reads as a grade | |
| smaller class (of the target) | lớp nhãn ít mẫu hơn | avoid "lớp nhỏ hơn", which reads as a classroom |  |
| smaller class (outcome balance) | lớp thiểu số | | |
| technical task (Milestone 4) | bài toán kỹ thuật | "bài toán kỹ thuật của AQ3 là phân loại nhị phân" |  |

## Splits, folds and leakage

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| fitted transform; fit (a transform or model) | phép biến đổi có tham số ước lượng từ dữ liệu; ước lượng (fit) | "ước lượng trên tập huấn luyện"; avoid "khớp", which reads as "match" | khớp trên dữ liệu |
| fold (cross-validation) | fold | keep English; first use "fold (phần chia trong kiểm định chéo)" |  |
| freeze (first / second) | chốt (lần thứ nhất / lần thứ hai) | "chốt kế hoạch trước khi huấn luyện", "chốt mô hình trước khi kiểm tra" |  |
| held-out run (in a fold) | kỳ mở được tách ra để đánh giá | not "được giữ lại", which reads as "kept" | kỳ mở được giữ lại |
| leakage | rò rỉ thông tin | | |
| leave-one-run-out (folds) | loại trừ từng kỳ mở (leave-one-run-out) |  |  |
| scaling / encoding (fitted) | phép chuẩn hóa thang đo / phép mã hóa (được ước lượng) | | |
| single test (on the 2014 runs) | kiểm tra một lần duy nhất | "chấm điểm các kỳ mở năm 2014 đúng một lần" |  |
| target leakage / train–test contamination / student leakage / temporal leakage / augmentation leakage | rò rỉ biến mục tiêu / lẫn dữ liệu giữa tập huấn luyện và tập kiểm thử / rò rỉ theo sinh viên / rò rỉ theo thời gian / rò rỉ do tăng cường dữ liệu | the brief's five leakage risks |  |
| test set (the 2014 runs) | tập kiểm thử (các kỳ mở năm 2014) | Milestone 3 reader test: never a bare "kiểm thử"; "kiểm thử đơn vị" for unit tests; "bản ghi giả lập" for synthetic test records | |
| time split | chia dữ liệu theo thời gian | training 2013 runs, test 2014 runs |  |
| unseen module (absent from training) | module không có trong dữ liệu huấn luyện | "CCC chỉ có ở năm 2014" |  |

## Models and approaches

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| background-only model | mô hình chỉ dùng đặc điểm cá nhân | first use: "mô hình chỉ dùng đặc điểm cá nhân (background-only model)": module, tháng bắt đầu, số lần học trước, tín chỉ, trình độ, thời điểm đăng ký; không dùng hoạt động học tập |  |
| challenger (model) | mô hình đối sánh | first use: "mô hình đối sánh (challenger)"; the candidate that must beat the primary approach by a fixed margin |  |
| events per parameter | số sự kiện trên mỗi tham số | "sự kiện" = sinh viên không hoàn thành |  |
| fixed effects (of module run) | hiệu ứng cố định | first use: "hiệu ứng cố định (fixed effects) theo kỳ mở" |  |
| labels-available variant | phương án huấn luyện chỉ trên các kỳ mở tháng 2 năm 2013 | scores the 2014 February runs; first use adds why: "vì kết quả các kỳ mở tháng 10 năm 2013 chưa có khi đó" | phương án chỉ dùng kết quả đã biết |
| primary approach | phương pháp chính | first use: "phương pháp chính (primary approach)" |  |

## Evaluation measures and statistical tests

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| accuracy (of an estimate, in general) | chất lượng dự báo | "độ chính xác" only for precision, always "độ chính xác của danh sách" | |
| base rate | tỷ lệ nền | share of non-completers among enrolled students |  |
| discrimination (of a model) | khả năng phân biệt | ability to rank non-completers above completers |  |
| false alarm | cảnh báo nhầm | | |
| gain over the base rate (lift) | mức vượt tỷ lệ nền (lift) |  |  |
| hierarchical (two-level) bootstrap | bootstrap phân tầng | "bootstrap hai tầng" for the project's run-then-enrolment scheme |  |
| lift (Milestone 3 first use) | lift | first use, once in the document: "lift, tức tỷ số giữa độ chính xác của danh sách và tỷ lệ nền (lift bằng 1 nghĩa là không hơn một danh sách ngẫu nhiên)"; second reader test: "số lần … vượt" read as a count; "mức vượt tỷ lệ nền (lift)" stays the row of Milestone 4 | |
| precision (of a list) | độ chính xác của danh sách | first use: "độ chính xác của danh sách (precision)" |  |
| recall (of a list) | tỷ lệ phát hiện | first use: "tỷ lệ phát hiện (recall)"; avoid: "độ bao phủ" | độ phủ |
| two-level bootstrap (runs, then enrolments) | bootstrap hai tầng | first use: "bootstrap hai tầng (lấy mẫu lại kỳ mở, rồi lượt đăng ký học trong từng kỳ mở)" |  |
| usefulness for decisions | giá trị hỗ trợ ra quyết định |  |  |
| wins, ties and losses (per run) | số kỳ mở thắng, hòa và thua |  |  |

## Contact lists, flags and capacity

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| attainable recall | tỷ lệ phát hiện tối đa có thể đạt | "mức trần mà danh sách dài k có thể đạt" |  |
| capacity (contact limit of a list, Milestone 4) | hạn mức liên hệ | first use: "hạn mức liên hệ (số sinh viên giảng viên hướng dẫn liên hệ được: 3 hoặc 5 trên mỗi nhóm khoảng 20)"; "danh sách dài k theo hạn mức liên hệ"; Milestone 4 only, Milestones 1–3 keep "số sinh viên cán bộ liên hệ được" |  |
| capacity (Milestone 2 wording) | số sinh viên cán bộ liên hệ được mỗi tuần | one term with the capacity row above; phrase the sentence around who can contact how many students | |
| capacity scenarios (list sizes under assumed capacity) | kịch bản năng lực liên hệ | first use: "kịch bản năng lực liên hệ mỗi tuần"; then the short form | |
| capacity (weekly follow-up capacity of staff) | số sinh viên cán bộ liên hệ được mỗi tuần | phrase the sentence around who can contact how many students; avoid an abstract noun; avoid: "năng lực xử lý", "khả năng liên hệ của cán bộ" | |
| contact deferred (AQ4) | phần liên hệ được hoãn | "AQ4: chỉ xếp hạng, phần liên hệ được hoãn" |  |
| flag (a student) | đánh dấu |  |  |
| flag (on a student, noun) | nhãn bị đánh dấu | "cờ" only for data-quality flag columns |  |
| list stability | độ ổn định của danh sách | whether a student near rank k stays on the list under resampling |  |
| normalised recall | tỷ lệ phát hiện chuẩn hóa | first use: "tỷ lệ phát hiện chuẩn hóa (normalised recall)"; recall divided by attainable recall |  |
| operating point | thiết lập chính | "thiết lập chính: ngày 27, 5 trên 20" | điểm vận hành |
| override (an entry of the list) | bác bỏ | "giảng viên có thể bác bỏ bất kỳ tên nào trong danh sách" |  |
| random list (baseline) | danh sách ngẫu nhiên |  |  |
| reachable non-completer | sinh viên không hoàn thành còn liên hệ được | not withdrawn within 7 days after the cut-off |  |
| recall at capacity | tỷ lệ phát hiện trong giới hạn danh sách | the list length is set by contact capacity |  |
| risk tier | nhóm mức nguy cơ | "nhóm thứ nhất: 3 sinh viên đầu trên 20" |  |
| rule-ranked list | danh sách xếp theo quy tắc dấu hiệu sớm |  |  |
| weekly contact capacity | năng lực liên hệ mỗi tuần | first use in the document only: "năng lực liên hệ mỗi tuần (số sinh viên cán bộ liên hệ được trong một tuần)"; then the short form; avoid "số lượt liên hệ tối đa mỗi tuần" | số lượt liên hệ tối đa mỗi tuần |

## Fairness, risk and governance

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| audit attribute | thuộc tính dùng để kiểm tra công bằng | sensitive attribute kept for the fairness audit, not a primary predictor |  |
| audit group | nhóm cần kiểm tra công bằng |  |  |
| automation bias | thiên kiến tự động hóa | first use: "thiên kiến tự động hóa (automation bias)": người dùng làm theo danh sách mà không tự đánh giá |  |
| bias audit / fairness audit | kiểm tra công bằng | one term for both | kiểm tra thiên lệch |
| confirmatory check (fairness) | kiểm định khẳng định | the three groups fixed in advance and tested with Holm adjustment; other checks are "mô tả" | kiểm tra xác nhận |
| conformity assessment | đánh giá sự phù hợp | legal term for high-risk AI systems before use |  |
| gap (between two rates) | chênh lệch | "chênh lệch tỷ lệ phát hiện 10 điểm phần trăm"; avoid "khoảng cách" for a rate gap (it stays right for a distance in time) |  |
| govern / map / measure / manage (NIST AI RMF) | quản trị / lập bản đồ / đo lường / quản lý |  |  |
| high-risk AI system | hệ thống trí tuệ nhân tạo có rủi ro cao | Vietnamese legal term (Luật Trí tuệ nhân tạo 134/2025/QH15; Quyết định 33/2026/QĐ-TTg) | hệ thống AI rủi ro cao |
| high-stakes (use) | hệ trọng | "sử dụng trong bối cảnh hệ trọng"; keeps "rủi ro cao" for the legal category |  |
| human oversight | giám sát của con người |  |  |
| Low / Medium (residual risk) | Thấp / Trung bình |  |  |
| not cleared (fairness check, small group) | chưa được xác nhận đạt | "không đủ dữ liệu, chưa được xác nhận đạt" |  |
| post-hoc explanation | giải thích hậu nghiệm | first use: "giải thích hậu nghiệm (post-hoc)" |  |
| proxy (for an excluded attribute) | biến thay thế | "hoạt động có thể là biến thay thế cho tình trạng khuyết tật"; differs from "chỉ số đại diện" (a KPI proxy) |  |
| proxy variable | biến đại diện | for the KPI itself use "chỉ số đại diện" |  |
| residual risk | rủi ro còn lại |  |  |
| risk register | danh mục rủi ro |  | sổ đăng ký rủi ro |
| selection rate (onto the list) | tỷ lệ được chọn vào danh sách |  |  |
| separation (fairness criterion) | tiêu chí ngang bằng tỷ lệ phát hiện | first use: "tiêu chí ngang bằng tỷ lệ phát hiện giữa các nhóm (separation)" |  |
| slicing analysis | phân tích theo từng nhóm con | first use: "phân tích theo từng nhóm con (slicing analysis)" |  |

## Causal questions and the limits of observational data

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| association (statistical) | mối liên hệ | name the two variables | mức độ liên quan |
| counterfactual | phản thực (counterfactual) | | phản thực tế |
| observational data | dữ liệu quan sát | | |
| performative prediction | dự báo tự tác động | first use: "dự báo tự tác động (performative prediction): dự báo làm thay đổi chính kết quả nó dự báo" |  |
| self-selection | hiện tượng tự chọn (self-selection) | | |
| target trial | thử nghiệm mục tiêu | first use: "thử nghiệm mục tiêu (target trial)" |  |
| time zero (trial) | thời điểm gốc | first use: "thời điểm gốc (time zero)" |  |
| unadjusted rate difference | chênh lệch tỷ lệ chưa hiệu chỉnh |  |  |
| uplift (benefit) ranking | xếp hạng theo lợi ích can thiệp | first use: "xếp hạng theo lợi ích can thiệp (uplift)" |  |

## Modelling deliverables and success criteria

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| AQ Modeling Brief | AQ Modeling Brief | brief's own term, keep English; first use "AQ Modeling Brief (bản mô tả yêu cầu mô hình hóa của từng AQ)" |  |
| Candidate Solution Matrix | Candidate Solution Matrix | brief's own term, keep English; first use "Candidate Solution Matrix (ma trận các giải pháp ứng viên)" |  |
| Evaluation Design Card | Evaluation Design Card | brief's own term, keep English; first use "Evaluation Design Card (thẻ thiết kế đánh giá)" |  |
| gate (success criterion S1) | điều kiện đạt | "điều kiện đạt duy nhất S1" |  |
| prototype (Level 2) | nguyên mẫu | first use: "nguyên mẫu (prototype)"; "giao thức chạy nguyên mẫu" for the protocol |  |
| success criterion | tiêu chí thành công |  |  |
