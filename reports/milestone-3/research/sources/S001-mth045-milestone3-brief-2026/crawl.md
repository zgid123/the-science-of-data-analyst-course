---
id: S001
url: final-project/milestones/03/milestone-3.md
requested: final-project/milestones/03/milestone-3.md
fetched: 2026-11-06T08:20+07:00
tool: fetch.py local (git show 41299c1; verbatim, 1 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T03
part: 1
raw: raw.txt (32 KB)
conversion: verbatim copy of 1 file(s) from milestone-da at 41299c1
---
===== final-project/milestones/03/milestone-3.md @ 41299c1 =====
MTH045 – The Science of Data Analytics | Milestone 3

**MILESTONE P3**

# FROM UNDERSTANDING TO PREPARATION TỪ HIỂU DỮ LIỆU ĐẾN CHUẨN BỊ DỮ LIỆU

---

_Data Understanding, Data Quality Assessment & Reproducible Data Preparation_

**Lĩnh vực bắt buộc: GIÁO DỤC**

> **Mục tiêu của Milestone 3**
>
> Kiểm chứng mức độ phù hợp và chất lượng của bộ dữ liệu mở đã thu thập ở Milestone 2; hiểu cấu trúc, nội dung, giới hạn và các vấn đề chất lượng dữ liệu; sau đó xây dựng một quy trình chuẩn bị dữ liệu có thể tái lập để tạo Analytic-ready Dataset làm đầu vào cho giai đoạn Modeling & Evaluation.

| **Thông tin nhóm** | **Nội dung** |
|---|---|
| Tên nhóm |  |
| Thành viên |  |
| Project title |  |
| Milestone 1 version |  |
| Milestone 2 dataset/version |  |
| Prepared dataset version |  |
| Ngày nộp |  |

_Tài liệu hướng dẫn thực hiện đồ án – Student Project Guideline_

## 1. Vị trí của Milestone 3 trong Data Analytics Methodology

Milestone 3 tương ứng với giai đoạn **From Understanding to Preparation** trong Data Analytics Methodology. Đây là cầu nối giữa dữ liệu đã thu thập và dữ liệu sẵn sàng cho phân tích/mô hình hóa.

![](milestone-3_assets/milestone-3-p2-1.png)

_Hình 1. Vị trí Milestone 3 trong Data Analytics Methodology (John Rollins)_

| **Milestone** | **Câu hỏi trung tâm** | **Đầu ra chính** |
|---|---|---|
| Milestone 1 – From Problem to Approach | Vấn đề nào cần giải quyết? Câu hỏi phân tích nào cần trả lời? | Business Goal, SMART Goal/KPI, Analytical Questions, Analytics Type, Decision Supported. |
| Milestone 2 – From Requirements to Collection | Để trả lời các câu hỏi đó cần dữ liệu gì? Dataset mở nào thực sự cung cấp dữ liệu cần thiết? | Data Requirements, dataset selection, raw data, provenance, requirement coverage. |
| Milestone 3 – From Understanding to Preparation | Dữ liệu thật sự chứa gì, chất lượng ra sao, cần xử lý như thế nào và có còn trả lời được các câu hỏi đã cam kết không? | Data Understanding Report, Data Quality Decisions, Preparation Pipeline, Analytic-ready Dataset, Model Readiness. |

> **Nguyên tắc xuyên suốt**
>
> Milestone 3 không phải là bước “làm sạch dữ liệu cho đẹp”. Mọi quyết định chuẩn bị dữ liệu phải có lý do gắn với Analytical Question, loại phân tích, cấu trúc dataset và rủi ro làm sai lệch kết quả.

## 2. Mục tiêu học tập và mục tiêu project

Sau khi hoàn thành Milestone 3, nhóm phải chứng minh được các năng lực sau:

- Hiểu và mô tả dataset ở mức schema, semantics, unit of analysis, keys, target/outcome, thời gian và quan hệ giữa các bảng/file.
- Đánh giá chất lượng dữ liệu bằng bằng chứng: missingness, duplicates, invalid values, outliers, class imbalance, temporal coverage, join integrity và các vấn đề consistency.
- Đánh giá lại độ phù hợp giữa dữ liệu thực tế và các Analytical Questions ở bốn mức Descriptive, Diagnostic, Predictive và Prescriptive.
- Phân biệt “missing values” với “missing variables/concepts” và chọn cách xử lý phù hợp, không tạo bằng chứng giả để lấp khoảng trống dữ liệu.
- Thiết kế và thực thi một Data Preparation Pipeline có thể tái lập, giữ được lineage từ raw data đến prepared data.
- Nhận diện và kiểm soát data leakage, target leakage, bias/representativeness và các rủi ro đạo đức trong dữ liệu giáo dục.
- Sử dụng Generative AI như partner hỗ trợ hiểu dữ liệu, viết mã và phản biện quyết định, nhưng không để AI thay thế việc kiểm chứng bằng dữ liệu thật.

## 3. Đầu vào bắt buộc từ Milestone 2

Nhóm chỉ bắt đầu Milestone 3 khi đã có một **Data Collection Package** đủ tối thiểu. Nếu còn thiếu nguồn, license hoặc raw file, phải hoàn thiện Milestone 2 trước.

| **Đầu vào** | **Yêu cầu** |
|---|---|
| Milestone 1 baseline | Business Goal, SMART Goal/KPI, Analytical Questions, Analytics Type và Decision Supported phiên bản đang hiệu lực. |
| Updated Traceability Matrix | AQ → Data Requirement → Dataset/File → Actual Variables → Coverage/Gap. |
| Raw Data Package | File nguyên gốc được giữ bất biến trong data/raw; không chỉnh sửa trực tiếp. |
| Metadata / Data Dictionary | Mô tả biến, codebook, bảng quan hệ, đơn vị đo, license/citation và nguồn chính thức. |
| Collection Evidence | URL/DOI, access date, version, checksum/file size hoặc bằng chứng provenance tương đương. |
| Controlled Change Log | Mọi điều chỉnh từ Milestone 1/2 đã được ghi lại và có rationale. |

> **Entry Gate**
>
> Nếu dataset chỉ hỗ trợ một phần rất nhỏ của proposal, nhóm không nên tiếp tục cleaning/modeling chỉ vì đã tải được dữ liệu. Trước hết phải thực hiện Task 3 của Milestone này để quyết định giữ, sửa, thay hoặc loại câu hỏi phân tích.

## 4. Nguyên tắc làm việc trong Milestone 3

| **Nguyên tắc** | **Yêu cầu thực hiện** |
|---|---|
| Understand before Prepare | Phải hiểu ý nghĩa, phạm vi và chất lượng dữ liệu trước khi sửa/xóa/biến đổi. |
| Raw is immutable | Không chỉnh sửa file trong data/raw. Mọi xử lý tạo file/version mới trong data/interim hoặc data/processed. |
| Question-driven preparation | Chỉ thực hiện biến đổi có mục đích liên quan đến AQ, KPI, target hoặc kỹ thuật dự kiến. |
| Evidence before assumption | Không suy diễn ý nghĩa biến chỉ từ tên cột; đối chiếu documentation, distribution và logic domain giáo dục. |
| Reproducibility | Mọi bước xử lý phải có code/notebook hoặc mô tả đủ để người khác tái lập. |
| No silent revision | Nếu dữ liệu buộc phải đổi AQ/SMART scope, phải cập nhật Controlled Change Log. |
| No modeling yet | Milestone này có thể chuẩn bị split/feature structure, nhưng chưa tối ưu mô hình và chưa dùng model performance để “chọn” cách cleaning trên toàn bộ dữ liệu. |

## 5. Quy trình thực hiện Milestone 3

| **Bước** | **Hoạt động** | **Sản phẩm** |
|---|---|---|
| 1 | Reconfirm scope, dataset, unit of analysis, target và keys. | Dataset Understanding Map |
| 2 | Thực hiện Data Profiling & Data Quality Assessment. | Data Understanding Report |
| 3 | Đối chiếu AQ với bằng chứng dữ liệu thật; xử lý data gaps. | AQ–Data Fit Decision Log |
| 4 | Xây Data Preparation Plan trước khi thay đổi dữ liệu. | Preparation Decision Matrix |
| 5 | Thực thi cleaning, integration, transformation và feature construction. | Reproducible Preparation Pipeline |
| 6 | Kiểm tra leakage, bias, data quality sau xử lý. | Prepared Data Validation Report |
| 7 | Đóng gói analytic-ready dataset và data dictionary phiên bản mới. | Prepared Dataset Package |
| 8 | Đánh giá readiness theo 4 mức analytics và cập nhật proposal. | Model Readiness + Revised Traceability |

## 6. Task 1 – Hiểu cấu trúc và ý nghĩa dữ liệu

Trước khi EDA hoặc cleaning, nhóm phải mô tả dataset theo **ngữ nghĩa của domain giáo dục** chứ không chỉ theo tên cột.

| **Nội dung cần xác định** | **Câu hỏi hướng dẫn** |
|---|---|
| Population | Dữ liệu đại diện cho ai/cái gì? Sinh viên nào, bậc học nào, khóa học nào, thời gian nào? |
| Unit of analysis | Một record đại diện cho student, student-course, student-week, assessment, event hay một đơn vị khác? |
| Primary/foreign keys | Khóa nào xác định duy nhất record? Có cần composite key? Quan hệ giữa các bảng là 1–1, 1–N hay N–N? |
| Outcome / target | Biến kết quả được định nghĩa thế nào? Có phải outcome thật hay proxy? Khi nào outcome được quan sát? |
| Time semantics | Date/time/week nghĩa là thời điểm event, deadline, submission hay snapshot? Có timezone/relative week? |
| Measurement semantics | Score, engagement, completion, attendance... được tính như thế nào? Đơn vị và thang đo? |
| Categorical codes | Các mã category có mapping rõ trong codebook không? Có “unknown/other/not applicable”? |
| Sensitive attributes | Có gender, age, disability, socioeconomic status, location hoặc nhóm dễ bị tổn thương không? |

### 6.1. Dataset Understanding Map bắt buộc

| **File/Table** | **Unit of Analysis** | **Primary Key** | **Foreign Key** | **Main Variables** | **Time Field** | **Role in AQ** |
|---|---|---|---|---|---|---|
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |
|  |  |  |  |  |  |  |

## 7. Task 2 – Data Profiling & Data Quality Assessment

Data Understanding phải dựa trên **evidence** từ dữ liệu. Nhóm cần tạo các bảng/tóm tắt/visualization cần thiết để mô tả những vấn đề sau.

| **Khía cạnh** | **Phải kiểm tra** | **Câu hỏi phản biện** |
|---|---|---|
| Shape & schema | Rows/columns, types, identifiers, table relationships. | Shape có phù hợp documentation? Có grain bị hiểu sai? |
| Missingness | Tỷ lệ missing theo biến/nhóm/thời gian; pattern đồng xuất hiện. | Missing có ngẫu nhiên? Có tập trung ở một nhóm sinh viên/course? |
| Duplicates & key integrity | Duplicate rows, duplicate keys, orphan foreign keys. | Duplicate là lỗi hay là nhiều event hợp lệ? |
| Validity / consistency | Range, category codes, impossible dates, inconsistent formats. | Giá trị nào vi phạm rule/domain? |
| Distribution | Center, spread, skewness, zero inflation, rare categories. | Distribution có ảnh hưởng đến cách phân tích/biến đổi? |
| Outliers | Giá trị cực đoan theo thống kê và theo domain. | Outlier là lỗi hay là trường hợp thật cần giữ? |
| Target / outcome balance | Frequency/rate của outcome hoặc class. | Có imbalance nghiêm trọng? Minority class có đủ quan sát? |
| Temporal coverage | Khoảng thời gian, density theo tuần/tháng, gaps. | Có đủ lịch sử cho trend/prediction point? |
| Join integrity | Coverage sau join, unmatched keys, many-to-many explosion. | Join có làm nhân bản record hoặc làm mất nhóm nào? |
| Representativeness | Population, course, institution, country, mode of study. | Có thể khái quát kết quả đến bối cảnh project không? |

### 7.1. Data Quality Issue Log

| **Issue ID** | **Variable/Table** | **Evidence** | **Impact on AQ** | **Severity** | **Decision** |
|---|---|---|---|---|---|
| DQ01 |  |  |  | High/Med/Low |  |
| DQ02 |  |  |  | High/Med/Low |  |
| DQ03 |  |  |  | High/Med/Low |  |

## 8. Task 3 – Đánh giá lại AQ–Data Fit và xử lý Data Gap

Sau Data Understanding, nhóm phải cập nhật lại từng Analytical Question. Đây là điểm quyết định quan trọng: **không phải câu hỏi nào từ Milestone 1 cũng nên được giữ nguyên khi dữ liệu thật không hỗ trợ**.

| **Mức hỗ trợ** | **Ý nghĩa** | **Hành động** |
|---|---|---|
| GREEN – Full support | Các biến, population, time window và quality đủ để trả lời AQ ở mức claim đã định. | Giữ AQ; chuyển sang preparation. |
| YELLOW – Partial support | Có dữ liệu liên quan nhưng thiếu phạm vi, biến phụ, granularity hoặc chất lượng chưa đủ. | Thu hẹp AQ, đổi claim, hoặc bổ sung dataset tương thích; ghi Change Log. |
| RED – Unsupported | Thiếu concept/variable/target/intervention quan trọng hoặc không thể xác lập đúng bằng dữ liệu hiện có. | Sửa/bỏ/defer AQ. Không được tạo “evidence” giả để giữ câu hỏi. |

### 8.1. Quy trình ra quyết định khi dữ liệu không đáp ứng câu hỏi

- 1\) Kiểm tra lại documentation và semantics: biến cần thiết có tồn tại dưới tên khác hoặc trong bảng khác không?
- 2\) Kiểm tra có thể DERIVE biến một cách hợp lệ từ các trường thực tế hay không (ví dụ tính submission delay từ submission_date và deadline). Nếu có, phải mô tả công thức và giả định.
- 3\) Kiểm tra có thể bổ sung một open dataset khác hay không. Chỉ hợp nhất nếu population, time, granularity và join logic tương thích; không ghép hai dataset chỉ vì “có cùng tên biến”.
- 4\) Nếu vẫn thiếu: thu hẹp scope, hạ mức claim hoặc rewrite AQ để phù hợp với bằng chứng thật.
- 5\) Nếu câu hỏi là cốt lõi nhưng dữ liệu hoàn toàn không hỗ trợ: defer hoặc loại AQ và cập nhật proposal/traceability. Đây là lựa chọn đúng hơn so với tạo dữ liệu giả để chứng minh.
- 6\) Synthetic data chỉ được xem xét cho mục đích THỰC NGHIỆM phương pháp/pipeline theo chính sách ở Mục 8.3, không thay thế dữ liệu bằng chứng.

### 8.2. Phân biệt Missing Value và Missing Variable

| **Tình huống** | **Ví dụ** | **Có thể xử lý thế nào?** |
|---|---|---|
| Missing value – biến tồn tại nhưng một số record thiếu | Một số sinh viên không có survey satisfaction score. | Phân tích missingness; có thể loại, tạo category, hoặc impute nếu có cơ sở. Phải đánh giá ảnh hưởng/sensitivity. |
| Missing variable/concept – dataset không hề thu thập | Dataset không có thông tin intervention/support received nhưng AQ hỏi “can thiệp nào hiệu quả nhất?”. | Không được impute/sinh giả như dữ liệu thật. Phải bổ sung nguồn dữ liệu hợp lệ hoặc sửa/defer AQ. |
| Missing target/label | Không có outcome dropout/completion nhưng project muốn supervised prediction. | Không thể huấn luyện supervised target thật. Cần dataset khác hoặc đổi loại bài toán. |

### 8.3. Chính sách sử dụng Synthetic / Generative Data

Synthetic data không mặc định là “xấu”, nhưng vai trò của nó phải được giới hạn rõ. Trong đồ án này, **synthetic data không được dùng để tạo bằng chứng thực nghiệm mà dữ liệu thật không có**.

| **Mức sử dụng** | **Trạng thái** | **Điều kiện bắt buộc** |
|---|---|---|
| A. Pipeline / unit-test data | ĐƯỢC PHÉP | Dùng dữ liệu giả nhỏ để kiểm thử code, schema, ETL hoặc visualization. Phải gắn nhãn synthetic và không đưa vào kết luận. |
| B. Simulation / method demonstration | ĐƯỢC PHÉP CÓ ĐIỀU KIỆN | Có thể dùng để minh họa thuật toán hoặc scenario. Phải tách hoàn toàn khỏi real-data findings và ghi rõ assumptions. |
| C. Predictive data augmentation | CHỈ KHI ĐƯỢC GIẢNG VIÊN CHẤP THUẬN | Phải có baseline real-only, train augmentation chỉ trên training partition, đánh giá cuối cùng trên real holdout; báo cáo tác động và bias. |
| D. Fill a missing concept/label/intervention | KHÔNG ĐƯỢC PHÉP | Không tạo student records, target labels, demographic values hay intervention outcomes để “lấp” thứ dataset không thu thập. |
| E. Descriptive/diagnostic evidence | KHÔNG ĐƯỢC PHÉP | Không trộn synthetic data với real data để tính prevalence, trend, correlation hoặc kết luận về người học thật. |

> **Quy tắc ưu tiên**
>
> Khi dữ liệu không hỗ trợ AQ, thứ tự ưu tiên là: (1) kiểm chứng/derive hợp lệ từ real data → (2) bổ sung nguồn real data tương thích → (3) thu hẹp/rewrite AQ → (4) defer/drop AQ. Synthetic data không phải là “bước 5 để cứu câu hỏi”.

## 9. Task 4 – Xây dựng Data Preparation Decision Matrix

Trước khi sửa dữ liệu, nhóm phải lập một **Preparation Plan**. Mỗi thao tác cần nêu issue, rationale, method và rủi ro đối với kết quả.

| **Issue / Need** | **Decision** | **Rationale** | **Implementation** | **Validation** |
|---|---|---|---|---|
| Missing values |  |  |  |  |
| Duplicate / key issue |  |  |  |  |
| Invalid category / type |  |  |  |  |
| Outliers |  |  |  |  |
| Table integration |  |  |  |  |
| Derived feature |  |  |  |  |
| Temporal aggregation |  |  |  |  |
| Encoding / scaling |  |  |  |  |

### 9.1. Hướng dẫn quyết định theo loại vấn đề

| **Vấn đề** | **Không nên làm ngay** | **Cách tiếp cận đúng** |
|---|---|---|
| Missing values | Impute tất cả bằng mean/0 mà không phân tích. | Xem tỷ lệ/pattern, ý nghĩa missing; chọn drop/category/imputation phù hợp và ghi sensitivity. |
| Duplicates | drop_duplicates() toàn bộ không kiểm tra. | Xác định grain và key; phân biệt duplicate lỗi với nhiều event hợp lệ. |
| Outliers | Xóa mọi điểm ngoài IQR. | Kiểm tra domain, data entry error, tail behavior; cân nhắc cap/transform/robust method/giữ nguyên. |
| Categorical values | Gộp category hiếm tùy ý. | Kiểm tra codebook; chỉ gộp khi hợp lý về domain và ảnh hưởng đến AQ/model. |
| Time | Dùng dữ liệu tương lai để tính feature quá khứ. | Cố định cut-off/prediction point; chỉ aggregate event trước thời điểm hợp lệ. |
| Sensitive attributes | Loại bỏ ngay mọi biến nhạy cảm nên không thể audit bias. | Xác định mục đích: có thể giữ để audit fairness nhưng hạn chế dùng làm predictor tùy bối cảnh và policy. |

## 10. Task 5 – Thực thi Reproducible Data Preparation Pipeline

Pipeline phải chạy từ raw data đến prepared data một cách lặp lại được. Khuyến nghị tách các bước sau và lưu code/version rõ ràng.

1. Load raw files + validate file/schema assumptions.
2. Select in-scope population/records theo proposal.
3. Standardize data types, category labels, dates/times và identifiers.
4. Resolve key/duplicate issues theo grain đã xác định.
5. Handle missing values theo từng biến/nhóm và rationale đã duyệt.
6. Handle invalid values/outliers nếu cần; không xóa dữ liệu chỉ vì “trông lạ”.
7. Integrate tables/datasets với join validation và row-count checks.
8. Construct derived variables/features từ real fields; ghi công thức, window và timestamp rule.
9. Create analysis-ready tables theo từng mức analytics nếu cần (student-level, student-week, event-level...).
10. Persist prepared dataset, data dictionary, transformation log và validation summary.

### 10.1. Cấu trúc thư mục khuyến nghị

```
project/
  README.md
  data/
    raw/                 # bất biến
    interim/             # kết quả trung gian có thể tái tạo
    processed/           # analytic-ready dataset
    metadata/            # dictionary, lineage, quality logs
  notebooks/
    02_data_understanding.ipynb
    03_data_preparation.ipynb
  src/
    prepare_data.py
  reports/
    milestone3/
```

## 11. Task 6 – Kiểm soát Leakage, Split và các biến đổi phụ thuộc dữ liệu

Đây là yêu cầu đặc biệt quan trọng nếu proposal có **Predictive Analytics**. Nếu preparation sử dụng thông tin của test/future data, model evaluation ở Milestone 4 có thể bị lạc quan giả.

| **Rủi ro** | **Ví dụ trong giáo dục** | **Quy tắc** |
|---|---|---|
| Target leakage | Dùng final grade, withdrawal date hoặc late-semester activity để dự báo risk ở tuần 4. | Feature chỉ được dùng nếu tồn tại trước prediction point. |
| Train-test contamination | Chuẩn hóa/impute bằng thống kê tính trên toàn dataset rồi mới split. | Split trước các transform cần “fit”; fit transform trên training và apply sang validation/test. |
| Student leakage | Cùng một sinh viên xuất hiện ở cả train và test trong bài toán cần generalize sang unseen students. | Chọn split theo entity phù hợp với claim. |
| Temporal leakage | Random split khi mục tiêu là dự báo học kỳ tương lai. | Cân nhắc temporal split/rolling validation. |
| Augmentation leakage | Synthetic samples được tạo từ toàn bộ data, kể cả holdout. | Nếu augmentation được duyệt, chỉ sinh từ training partition; holdout phải là real data. |

> **Không “học” từ test set trong Milestone 3**
>
> Các lựa chọn cleaning/feature construction có thể dựa trên domain và training data. Không được lặp đi lặp lại nhìn test outcome để tối ưu preprocessing, vì như vậy test set không còn là đánh giá độc lập.

## 12. Task 7 – Chuẩn bị dữ liệu theo bốn mức Analytics

Một project có thể cần nhiều analytic-ready views thay vì một bảng duy nhất. Nhóm phải chỉ ra cấu trúc dữ liệu nào phục vụ từng mức câu hỏi.

| **Analytics Level** | **Prepared data cần có** | **Điểm kiểm tra trước Milestone 4** |
|---|---|---|
| Descriptive | Population rõ, denominator đúng, measures/dimensions sạch, time grain phù hợp. | Có thể tạo summary/trend mà không double-count hoặc bias vì join. |
| Diagnostic | Descriptive view + explanatory factors + comparison groups; xử lý confound/context ở mức phù hợp. | Association được tính từ real data; không diễn giải association thành causation. |
| Predictive | Target rõ, prediction point, pre-point features, entity/time split, leakage-safe transforms. | Có đủ sample/target classes; target balance và split strategy hợp lý. |
| Prescriptive | Action/intervention/constraint/cost/outcome data hoặc bằng chứng đủ để đánh giá lựa chọn. | Nếu không đủ, chỉ giữ ở mức decision requirement/future work; không “nâng cấp” từ predictive thành prescriptive bằng lời khuyên AI. |

### 12.1. Model Readiness Matrix

| **AQ** | **Analytics Type** | **Prepared View/Table** | **Target/Measure** | **Feature Set / Dimensions** | **Split/Time Rule** | **Readiness** |
|---|---|---|---|---|---|---|
| AQ1 |  |  |  |  |  | Ready / Revise |
| AQ2 |  |  |  |  |  | Ready / Revise |
| AQ3 |  |  |  |  |  | Ready / Revise |
| AQ4 |  |  |  |  |  | Ready / Revise |

## 13. Task 8 – Validate và đóng gói Prepared Dataset

Sau preparation, nhóm phải chứng minh rằng dữ liệu tốt hơn cho mục tiêu phân tích nhưng vẫn giữ được tính đúng đắn và traceability.

- So sánh row count / entity count / target distribution trước và sau xử lý; giải thích mọi thay đổi lớn.
- Kiểm tra lại missingness, key uniqueness, join coverage, invalid ranges và temporal order.
- Đối chiếu derived features với công thức/sample manual check.
- Xác nhận prepared data không chứa biến leakage so với prediction point.
- Cập nhật data dictionary với source field, transformation, datatype, role và sensitivity.
- Lưu version, code commit/notebook version, input raw version và timestamp tạo prepared dataset.

### 13.1. Data Lineage Table

| **Prepared Variable** | **Source File/Field** | **Transformation** | **Window/Filter** | **Purpose/AQ** | **Sensitivity** |
|---|---|---|---|---|---|
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |
|  |  |  |  |  |  |

## 14. Sử dụng Generative AI như partner trong Milestone 3

Generative AI được phép hỗ trợ cả Data Understanding và Data Preparation, nhưng **mọi phát hiện về dữ liệu phải được xác nhận bằng code, thống kê, visualization, documentation hoặc kiểm tra trực tiếp trên dataset**.

| **Vai trò AI được phép** | **Ví dụ sử dụng** | **Giới hạn / kiểm chứng** |
|---|---|---|
| Data dictionary interpreter | Giải thích ý nghĩa codebook, gợi ý câu hỏi cần kiểm tra về schema. | Không chấp nhận diễn giải nếu trái documentation hoặc data profile. |
| EDA / quality checklist partner | Gợi ý kiểm tra missingness, keys, outliers, imbalance, time coverage. | Nhóm phải tự chạy kiểm tra và báo evidence. |
| Code assistant | Draft Python/R/SQL cho profiling, cleaning, joins, transformations. | Phải review code, test trên sample, kiểm tra row counts và results. |
| Preparation critic | Phản biện imputation/outlier/encoding strategy và cảnh báo leakage. | Team quyết định cuối cùng và ghi rationale. |
| Feature engineering ideator | Gợi ý derived features từ fields đang có. | Chỉ dùng feature có thể tính từ real data và đúng prediction timing. |
| Documentation assistant | Hỗ trợ viết transformation log, README, data dictionary. | Không để AI bịa statistics, source field hoặc transformation đã không thực hiện. |
| Synthetic-data assistant | Tạo test records/pipeline fixtures; mô phỏng khi được phép. | Phải tuân thủ chính sách synthetic data ở Mục 8.3. |

### 14.1. AI Decision Log bắt buộc

| **AI suggestion** | **Team decision** | **Accepted / Rejected** | **Evidence used to verify** | **Effect on pipeline** |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

> **AI không phải một nguồn dữ liệu**
>
> Không được dùng câu trả lời của Generative AI để xác nhận “sinh viên có xu hướng…”, “biến X gây ra Y”, “dataset có N record”, hoặc để tạo giá trị missing rồi coi đó là quan sát thật. AI là partner cho reasoning/coding; evidence phải đến từ dữ liệu và nguồn chính thức.

## 15. Ví dụ minh họa – Project về Course Completion

Ví dụ dưới đây minh họa cách nối Milestone 1 → 2 → 3. Không phải đáp án mẫu để sao chép.

| **Thành phần** | **Ví dụ minh họa** |
|---|---|
| Business Goal | Cải thiện khả năng hoàn thành môn học của sinh viên trong môi trường học trực tuyến/blended. |
| AQ Descriptive | Completion rate thay đổi thế nào theo course/presentation? |
| AQ Diagnostic | Engagement và assessment behavior khác nhau thế nào giữa nhóm Complete và Withdraw/Fail? |
| AQ Predictive | Có thể dự báo sớm nguy cơ không hoàn thành ở cuối tuần 4 không? |
| Potential Data Gap | Dataset không có thông tin về loại hỗ trợ/can thiệp mà sinh viên đã nhận. |
| Decision for Prescriptive AQ | Không tạo synthetic intervention outcome. Giữ “Which intervention should be used?” như future requirement hoặc rewrite thành câu hỏi về nhóm cần ưu tiên hỗ trợ. |
| Preparation implication | Tạo student-week features chỉ từ events trước/tới tuần 4; giữ final outcome làm target; không dùng activity sau tuần 4 làm predictor. |

## 16. Sản phẩm phải nộp cho Milestone 3

Nhóm nộp **01 báo cáo Milestone 3** và **01 Prepared Data Package**. Báo cáo nên khoảng 8–12 trang nội dung chính, không tính phụ lục, code và data files.

| **Deliverable** | **Nội dung bắt buộc** |
|---|---|
| A. Milestone 3 Report | Dataset understanding; profiling; data quality issues; AQ–Data fit decisions; preparation decisions; validation; risks/limitations; AI usage. |
| B. Updated Traceability | Business Goal/SMART/KPI → AQ → Analytics Type → Raw Variables → Preparation → Prepared Variables/View → Decision Supported. |
| C. Preparation Pipeline | Notebook/script có thể chạy lại từ raw data; không thao tác thủ công không ghi nhận. |
| D. Prepared Data Package | data/processed + data dictionary + lineage + version/provenance + validation summary. |
| E. Controlled Change Log | Mọi AQ/scope/claim thay đổi do data understanding hoặc data gaps. |
| F. AI Decision Log | Prompt/suggestion quan trọng, team decision, evidence kiểm chứng, accepted/rejected. |

### 16.1. Cấu trúc báo cáo khuyến nghị

| **Section** | **Nội dung** |
|---|---|
| 1. Project Baseline & Dataset | Tóm tắt M1/M2; dataset/version; scope; AQ hiện tại. |
| 2. Data Understanding | Population, unit, schema, keys, target, time semantics, sensitive attributes. |
| 3. Data Profiling & Quality | Missingness, duplicates, validity, outliers, distributions, target balance, temporal/join/representativeness. |
| 4. AQ–Data Fit & Data Gap Decisions | Green/Yellow/Red; derive/add real data/rewrite/drop; synthetic-data decision nếu có. |
| 5. Data Preparation Plan | Issue → decision → rationale → implementation → validation. |
| 6. Data Preparation Pipeline | Cleaning, integration, transformations, feature construction, split/leakage rules. |
| 7. Prepared Data Validation | Before/after checks, lineage, dictionary, residual risks. |
| 8. Analytics / Model Readiness | Prepared views theo 4 analytics levels; target/features/split; questions còn chưa khả thi. |
| 9. Ethics, Bias & Limitations | Sensitive variables, representativeness, fairness/audit use, limitations of claims. |
| 10. Generative AI Usage & Reflection | AI roles, accepted/rejected suggestions, verification evidence. |

## 17. Checklist trước khi nộp

- [ ] Raw data trong data/raw vẫn giữ nguyên và có provenance/version.
- [ ] Nhóm xác định đúng unit of analysis, keys, target/outcome và time semantics.
- [ ] Data profiling có bằng chứng cho missingness, duplicates, validity, outliers, target balance, time và joins.
- [ ] Mỗi data quality issue có decision và rationale, không cleaning theo thói quen.
- [ ] Nhóm phân biệt rõ missing values với missing variables/concepts.
- [ ] AQ không được “cứu” bằng synthetic data khi real data không hỗ trợ.
- [ ] Nếu có synthetic data, mục đích nằm trong chính sách cho phép và được tách khỏi real-data evidence.
- [ ] Predictive AQ có prediction point, split strategy và kiểm soát leakage.
- [ ] Transformations cần fit được fit trên training partition khi thích hợp.
- [ ] Derived features có công thức, source field, time window và lineage.
- [ ] Prepared data được kiểm tra lại row/entity counts, target distribution, missingness và key integrity.
- [ ] Traceability đã cập nhật từ AQ đến prepared variables/views thực tế.
- [ ] Có Data/Model Readiness Matrix cho Descriptive, Diagnostic, Predictive và Prescriptive.
- [ ] AI suggestions đã được kiểm chứng bằng dữ liệu/code/documentation và ghi AI Decision Log.
- [ ] Limitations và câu hỏi phải rewrite/drop/defer được trình bày minh bạch.

## 18. Thang đánh giá – 100 điểm

| **Tiêu chí** | **Điểm** |
|---|---|
| Liên kết Milestone 1–2 và consistency của scope / Change Log | NA |
| Dataset Understanding: population, unit, keys, target, time, semantics | NA |
| Data Profiling & Data Quality Assessment có evidence | NA |
| AQ–Data Fit + quyết định xử lý data gaps / synthetic data hợp lý | NA |
| Data Preparation Decision Matrix và rationale | NA |
| Reproducible Preparation Pipeline + data lineage | NA |
| Leakage control / split strategy / predictive readiness | NA |
| Prepared Data Validation + analytics/model readiness | NA |
| Ethics, representativeness, sensitive attributes và limitations | NA |
| Generative AI usage có kiểm chứng, phản biện và AI Decision Log | NA |
| Tổng | 100 |

## 19. Điều kiện chuyển sang Milestone 4 – From Modeling to Evaluation

Nhóm chỉ nên bắt đầu Modeling khi đáp ứng được các điều kiện sau:

- Ít nhất các Analytical Questions cốt lõi có Prepared Dataset/View phù hợp và traceability rõ.
- Target/measure và feature/dimension definitions đã ổn định đủ để model/analysis có ý nghĩa.
- Data leakage và split strategy đã được xác định cho predictive tasks.
- Các data quality issues quan trọng đã được xử lý hoặc được giữ lại có chủ đích và ghi limitation.
- Không còn sử dụng synthetic data như bằng chứng thay thế cho thông tin không tồn tại trong real data.
- Prepared data có thể tái tạo từ raw data bằng pipeline đã nộp.

> **Output cuối của Milestone 3**
>
> Một Analytic-ready Dataset không có nghĩa là dữ liệu “hoàn hảo”. Nó có nghĩa là nhóm hiểu rõ dữ liệu, biết các giới hạn còn lại, đã chuẩn bị dữ liệu theo cách có lý do và tái lập được, và có thể giải thích vì sao dữ liệu này phù hợp với các phân tích/mô hình sẽ thực hiện ở Milestone 4.

**END OF MILESTONE 3 GUIDELINE**

From Understanding to Preparation | Education Analytics Project
