# Topic glossary: OULAD data collection, understanding and preparation

The data vocabulary of team N04's course-completion project: the search for and selection of an open dataset, the reproducible collection of the Open University Learning Analytics Dataset (OULAD), its modules, runs, enrolments and fields, the data-quality findings, and the prepared views, features and checks built from it. OULAD names its units in Open University terms (module, presentation, tutor-marked assessment); the Vietnamese forms below keep those units distinct from the university's own courses and terms in course-completion-early-contact.

## Datasets, search and selection

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| aggregate (values) | số liệu gộp | | |
| coverage (Full / Partial / None) | mức đáp ứng (đầy đủ / một phần / không đáp ứng) | table cells: "Đầy đủ / Một phần / Không đáp ứng" | |
| data descriptor (paper) | bài mô tả dữ liệu | | |
| data gap | khoảng trống dữ liệu | | |
| data provider | nhà cung cấp | "nơi phát hành" stays for a distribution point | |
| data repository (UCI, figshare, Dataverse) | kho dữ liệu | "Kho dữ liệu học máy UCI" | |
| dataset / open dataset / candidate dataset | bộ dữ liệu / bộ dữ liệu mở / bộ dữ liệu ứng viên | the brief's words; not "tập dữ liệu" here | |
| Dataset Search Log / Selection Matrix | nhật ký tìm kiếm bộ dữ liệu / ma trận lựa chọn bộ dữ liệu | | |
| gate labels G1–G5 | G1 Kết quả; G2a Bài được chấm điểm có ngày; G2b Hoạt động có ngày; G3 Lịch sử; G4 Quyền truy cập; G5 Quyền riêng tư và liên kết | | |
| MOOC dropout | bỏ học (MOOC) | degree-level dropout is "thôi học"; course withdrawal is "rút học phần" | |
| must-have gate / nice-to-have | điều kiện bắt buộc / điều kiện nên có | G1–G5 keep their codes | |
| Selected / Rejected: fails Gx | Được chọn / Bị loại: không đạt Gx | | |
| stand-in (dataset) | bộ dữ liệu thay thế | | |
| ten selection criteria (AQ coverage; population fit; unit and granularity; outcome availability; feature availability and timing; temporal coverage; documentation and provenance; license and access; quality feasibility; ethics and representativeness) | mức đáp ứng các AQ; mức phù hợp của tổng thể; đơn vị phân tích và độ chi tiết; mức sẵn có của biến kết quả; mức sẵn có và thời điểm có của các biến giải thích; phạm vi thời gian; tài liệu mô tả và nguồn gốc dữ liệu; giấy phép và quyền truy cập; khả năng xử lý chất lượng dữ liệu; đạo đức và tính đại diện | scale 0 = không đáp ứng, 1 = đáp ứng một phần, 2 = đáp ứng tốt | |

## Data requirements, collection and provenance

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| checksum (SHA-256, MD5) | mã kiểm tra (checksum) | | |
| Data Acquisition Plan / Data Collection Package | kế hoạch thu thập dữ liệu / gói thu thập dữ liệu | | |
| data audit | đợt rà soát dữ liệu | | |
| data audit (Milestone 2) | đợt rà soát dữ liệu | | |
| data requirement / Data Requirement Specification | yêu cầu dữ liệu / đặc tả yêu cầu dữ liệu | | |
| distribution point / mirror (copy of a dataset) | nơi phát hành / bản sao | | |
| hash (of a file) | mã băm |  |  |
| license (of a dataset) | giấy phép | "giấy phép CC BY 4.0" | |
| pinned value (checksum) | giá trị tham chiếu ghi sẵn | | |
| provenance | nguồn gốc dữ liệu | | |
| raw data / raw files | dữ liệu gốc / tệp gốc | kept unchanged; avoid "dữ liệu thô" here | |
| required / optional variables | biến bắt buộc / biến tùy chọn | | |
| structural verification | kiểm tra cấu trúc ban đầu | | |

## OULAD modules, runs and enrolments

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| concurrent enrolment | lượt đăng ký học đồng thời | first use: "lượt đăng ký học đồng thời (diễn ra cùng lúc ở hai kỳ mở)"; the terms page form | |
| course presentation (OULAD) | kỳ mở module | short form "kỳ mở"; generic course runs in the gates: "kỳ mở học phần"; "kỳ mở sớm hơn", "kỳ mở muộn hơn" for earlier and later runs | lượt tổ chức học phần, lượt mở module, lượt tổ chức |
| enrolled at day d | đang đăng ký học vào ngày d | "đã đăng ký đến ngày d và chưa rút đến ngày d" |  |
| enrolment (OULAD unit: one student in one module run) | lượt đăng ký học | the unit of analysis of the prepared views; "lượt đăng ký học phần" stays for the university course |  |
| module (OULAD) / module run (presentation) / start month | module / kỳ mở module / tháng bắt đầu | OULAD units; "học phần" stays for the university's courses only | đợt mở học phần |
| paired run (Milestone 3 running text) | kỳ mở có kỳ tương ứng năm 2013 | the terms page keeps "kỳ mở có cặp" as the entry name | |
| registered at day d (still enrolled at the cut-off) | còn hiệu lực tại ngày d | with "lượt đăng ký học" as subject: "lượt đăng ký học còn hiệu lực tại thời điểm chốt dữ liệu"; with a student as subject or for the defined condition: "đang đăng ký học vào ngày d"; avoids "lượt đăng ký học còn đăng ký" |  |
| registration (sign-up) window | thời hạn đăng ký | "thời hạn đăng ký (hai tuần sau ngày bắt đầu kỳ mở)" at first use | |
| tutor (OU, marks TMAs and supports a tutor group) | giảng viên hướng dẫn | OULAD sense; "tutor group" → "nhóm hướng dẫn"; keep "trợ giảng" for a university teaching assistant |  |
| unregistration (day) | (ngày) hủy đăng ký | | |
| withdraw from an OULAD module | rút khỏi module | "rút học phần" only for the university's courses |  |

## OULAD fields: background, assessments and activity

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| background attributes | đặc điểm cá nhân | e.g. age band, education, deprivation band, disability | thông tin nền |
| banked result | kết quả bảo lưu | an assessment result carried over from an earlier run of the module |  |
| click record | bản ghi lượt nhấp |  |  |
| clickstream | dữ liệu lượt nhấp (clickstream) | | |
| declared disability | tình trạng khuyết tật do sinh viên tự khai | group label: "nhóm có tình trạng khuyết tật do sinh viên tự khai" | |
| deprivation band (IMD band) | mức khó khăn kinh tế – xã hội của khu vực cư trú | short form "mức khó khăn của khu vực"; avoid "mức thiếu thốn" | |
| due by day N / by the cut-off (on or before) | đến hạn tính đến hết ngày N / tính đến hết thời điểm chốt dữ liệu | reader test: plainer than "chậm nhất vào"; "trước ngày N" leaves out day N; "tính đến hết thời điểm dự báo" only where the English says "by the prediction point" (Milestone 4) | chậm nhất vào ngày |
| due day (assessment cut-off date) | ngày đến hạn | the OU calls it "cut-off date"; keep "thời điểm chốt dữ liệu" for days 13 and 27 only |  |
| due day (of an assessed task) | ngày đến hạn | | |
| grade band | khoảng điểm | | |
| Index of Multiple Deprivation (IMD) | Chỉ số khó khăn đa chiều (IMD) | the English area index behind imd_band |  |
| learning resource (VLE site) | tài nguyên học tập | OULAD vle table | trang học liệu |
| learning-platform activity | hoạt động trên nền tảng học tập | | |
| mark release day | ngày công bố điểm |  |  |
| outcome column / outcome variable | biến kết quả | not "kết quả học tập" | |
| planned week (of a VLE resource) | tuần theo kế hoạch | Milestone 2 wording; the English field name is week_from | |
| study load (OULAD studied credits) | số tín chỉ đang học | for the credit count of OULAD only; "khối lượng học" stays for workload in general (Milestones 1–2) | |

## Table structure and keys

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| grain (Milestone 3 running text) | đơn vị của mỗi dòng (grain) | Milestone 3 reader test; "mức chi tiết của bảng (grain)" stays on the terms page | |
| grain (of a table) | mức chi tiết của bảng (grain) | "một dòng ứng với một lượt đăng ký học" |  |
| unique (key) | không trùng lặp | composite keys: "Tổ hợp … và …" | |

## Data quality

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| data profiling (of a dataset) | khảo sát dữ liệu (profiling) | not "lập hồ sơ", which is for profiling students |  |
| de-duplicated twin (Milestone 3 running text) | phiên bản đã bỏ dòng trùng | Milestone 3 reader test; "bản đối chiếu đã loại trùng" stays in tables and in Milestone 4 | |
| exact duplicate row; de-duplicated twin | dòng trùng lặp hoàn toàn; bản đối chiếu đã loại trùng | the twin is a second version of a click feature counting each duplicated row once |  |
| heavy users (of the platform) | sinh viên dùng nền tảng rất nhiều | | |
| inconsistency (a counted finding) | loại không nhất quán | "sáu loại không nhất quán"; avoid "điểm không nhất quán", which clashes with "điểm" (score) | điểm không nhất quán |
| logging gap | khoảng trống trong quá trình ghi nhận dữ liệu | | |
| logging system | hệ thống ghi nhật ký | | |
| missing value / missing variable / missing target | giá trị thiếu / biến không được thu thập / thiếu biến mục tiêu | the brief's distinction; never "biến thiếu" alone, which reads as "a variable with gaps" |  |
| placeholder (value) | giá trị giữ chỗ | "ngày nộp giữ chỗ −1" | |
| profile (result of data profiling) | kết quả khảo sát dữ liệu |  |  |
| recorded absence | không có bản ghi (tính là 0) | no row = no activity or no submission; avoid "vắng mặt", which suggests class attendance | vắng mặt có ghi nhận |
| recorded absence (Milestone 3 running text) | không có bản ghi (tính là 0) | as on the terms page; second reader test found "vắng bản ghi có ý nghĩa" opaque | vắng bản ghi có ý nghĩa |
| severity High / Medium / Low | mức độ nghiêm trọng Cao / Trung bình / Thấp |  |  |
| structural gap (missing by design) | khoảng trống mang tính cấu trúc | | |
| validity (of values) | tính hợp lệ |  |  |

## Preparation, measures and features

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| activity ratio (against the run's median) | tỷ lệ hoạt động | "tỷ lệ hoạt động so với trung vị của kỳ mở" at first use | |
| analytic-ready dataset | bộ dữ liệu sẵn sàng cho phân tích | Milestone 3 output; first use may add "(analytic-ready dataset)" |  |
| cohort statistic (computed on the same run) | số liệu thống kê theo kỳ mở | | |
| course average (AQ2 sign, on OULAD) | mức trung bình của kỳ mở | | |
| data preparation pipeline | quy trình chuẩn bị dữ liệu (pipeline) | "pipeline" alone after first use is acceptable |  |
| derived feature / derived variable | đặc trưng dẫn xuất / biến dẫn xuất |  |  |
| descriptive measure (column role) | chỉ số mô tả | | |
| evaluation flag | cờ phục vụ đánh giá | | |
| feature view (features_d13, features_d27) | bảng đặc trưng |  |  |
| level A (of the synthetic-data policy) | mức A | "mức A (dữ liệu kiểm thử nhỏ cho mã)" at first use | |
| lineage (of a prepared variable) | truy vết nguồn gốc dữ liệu (lineage) | reader test: plainer than "dòng dõi dữ liệu" in this report | dòng dõi dữ liệu (lineage) |
| measure (a quantity derived from a field) | đại lượng đo | kept apart from "descriptive measure → chỉ số mô tả" and from a KPI | |
| missing-value indicator | biến chỉ báo giá trị thiếu |  |  |
| model-ready matrix | ma trận sẵn sàng cho mô hình |  |  |
| prepared view | bảng dữ liệu đã chuẩn bị | one analytic-ready table with a fixed grain (enrolment, enrolment × task, enrolment × week); avoid: "khung nhìn" |  |
| registration lead (days registered before the start) | khoảng cách từ ngày đăng ký đến ngày bắt đầu | | |
| run-relative ratio (= activity ratio) | tỷ lệ hoạt động | | tỷ số tương đối theo kỳ mở |
| synthetic data | dữ liệu giả lập | "tổng hợp" means aggregated; avoid it for synthetic | |
| synthetic test records (level A) | bản ghi giả lập | "bản ghi giả lập dùng để kiểm thử công thức" at first use | |
| validation check (V01–V15 of the prepared data) | phép kiểm tra | "kiểm tra dữ liệu đã chuẩn bị"; keep "kiểm định" for statistical tests and the validation set only |  |
| whole-run measures | các chỉ số tính trên toàn kỳ mở | | |

## Preparation deliverables and ratings

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| AQ–Data fit; GREEN / YELLOW / RED | mức phù hợp giữa AQ và dữ liệu; GREEN / YELLOW / RED | keep the brief's English labels, explained once: "GREEN (hỗ trợ đầy đủ), YELLOW (hỗ trợ một phần), RED (không được hỗ trợ)" |  |
| Data Quality Issue Log | Nhật ký vấn đề chất lượng dữ liệu (Data Quality Issue Log) | the brief's Task 2 table; issues DQ01–DQ19 |  |
| Dataset Understanding Map | bảng mô tả cấu trúc bộ dữ liệu (Dataset Understanding Map) | the brief's Task 1 table; English name in brackets at first use (Milestone 3 reader test) | Bản đồ hiểu bộ dữ liệu |
| feature specification / split and leakage specification | bản đặc tả đặc trưng / bản đặc tả cách chia dữ liệu và kiểm soát rò rỉ thông tin | | |
| fit rating (GREEN, YELLOW, RED) | mức hỗ trợ (GREEN, YELLOW, RED) | the brief's own column name "Mức hỗ trợ" for the rating; the concept itself stays "mức phù hợp giữa AQ và dữ liệu"; GREEN, YELLOW, RED stay in English | |
| Model Readiness Matrix | Ma trận mức sẵn sàng cho mô hình (Model Readiness Matrix) | the brief's Task 7 table; "Ready" → "Sẵn sàng", "Revise" → "Cần điều chỉnh" |  |
| Preparation Decision Matrix | Ma trận quyết định chuẩn bị dữ liệu (Preparation Decision Matrix) | the brief's Task 4 table |  |
| Prepared Data Package | Gói dữ liệu đã chuẩn bị (Prepared Data Package) | the brief's deliverable D; after first use "gói dữ liệu đã chuẩn bị" |  |
| Ready / Revise (readiness) | Sẵn sàng / Cần điều chỉnh |  |  |
| transformation log | nhật ký biến đổi dữ liệu |  |  |
| validation ledger | sổ ghi kết quả kiểm tra |  |  |
| version manifest | bản kê phiên bản | lists hashes of raw files, code and prepared files |  |
