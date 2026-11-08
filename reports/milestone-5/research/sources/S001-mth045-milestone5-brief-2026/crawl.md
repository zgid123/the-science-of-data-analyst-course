---
id: S001
url: milestones/05/milestone-5.md
requested: milestones/05/milestone-5.md
fetched: 2026-11-08T23:20+07:00
tool: fetch.py local (working tree read; verbatim, 1 file(s))
fetch_prompt: "none (verbatim file copy, not a model extract)"
status: ok
task: T03
part: 1
raw: raw.txt (22 KB)
conversion: verbatim copy of 1 file(s) from milestone-da at HEAD
---
===== milestones/05/milestone-5.md @ HEAD =====
MTH045 - The Science of Data Analytics | Milestone 5

# MILESTONE P5

**FINAL INTEGRATION & PROJECT REPORT**

**TỔNG HỢP 4 MILESTONES THÀNH BÁO CÁO ĐỒ ÁN CUỐI KỲ**

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                         ━━━━━
```

_From Project Evidence to a Coherent Analytics Report_

**Lĩnh vực bắt buộc: GIÁO DỤC**

> **Mục tiêu của Milestone 5**
>
> Tích hợp có chọn lọc các kết quả từ Milestone 1–4 thành một Final Project Report thống nhất, có khả năng truy vết từ nhu cầu stakeholder đến dữ liệu, xử lý dữ liệu, lựa chọn phương pháp, thiết kế đánh giá và quyết định giáo dục được hỗ trợ. Đây không phải là thao tác nối bốn báo cáo cũ; nhóm phải rà soát, cập nhật và viết lại thành một câu chuyện phân tích nhất quán.

| **Thông tin nhóm** | **Nội dung** |
|---|---|
| Tên nhóm |  |
| Thành viên |  |
| Project title cuối cùng |  |
| Dataset / version cuối cùng |  |
| Milestone 4 status | □ Level 1 bắt buộc □ Level 2 có thử nghiệm |
| Ngày nộp |  |

_Tài liệu hướng dẫn tổng hợp đồ án – Student Final Project Guideline_

## 1. Vai trò của Milestone 5 trong toàn bộ đồ án

> **Chuỗi logic của đồ án**
>
> M1 – Why & What? → M2 – What Data? → M3 – Is the Data Fit & Ready? → M4 – How to Analyze & Evaluate? → M5 – What is the final, defensible project story?

**Milestone 5 có ba nhiệm vụ chính:**

- Tích hợp: đưa các sản phẩm quan trọng của M1–M4 vào một cấu trúc báo cáo duy nhất.
- Đồng bộ: giải quyết các mâu thuẫn giữa proposal ban đầu, dữ liệu thực tế, câu hỏi cuối cùng và phương pháp đề xuất.
- Truy vết: chứng minh mỗi quyết định kỹ thuật đều quay về một Analytical Question, một nguồn dữ liệu và một mục tiêu/decision của stakeholder.

### 1.1. Quy tắc quan trọng khi tổng hợp

| **Quy tắc** | **Yêu cầu áp dụng** |
|---|---|
| **Không copy-paste bốn milestone rồi ghép lại.** | Final Report phải được viết lại theo một narrative chung; nội dung cũ chỉ là evidence/input. |
| **Sử dụng phiên bản cuối cùng của câu hỏi và dữ liệu.** | Nếu AQ đã sửa/drop ở M3, report phải dùng trạng thái cuối và giải thích thay đổi. |
| **Không che giấu data gaps hoặc model limitations.** | Giới hạn là một phần của kết quả khoa học, không phải lỗi cần giấu. |
| **Phân biệt đề xuất với thực nghiệm.** | Level 1 của M4 là bắt buộc; nếu chưa lập trình, không được viết như thể đã có kết quả thực nghiệm. |
| **Mọi kết luận phải có evidence.** | AI output, assumption hoặc stakeholder simulation không được dùng thay cho evidence từ dữ liệu/tham khảo đáng tin cậy. |

### 1.2. Input bắt buộc trước khi bắt đầu Milestone 5

| **Nguồn** | **Sản phẩm cần mang sang M5** | **Trạng thái cần kiểm tra** | **Nếu chưa hoàn chỉnh** |
|---|---|---|---|
| **Milestone 1** | Business Goal, SMART Goal, KPI, stakeholder needs, Analytical Questions, analytics level | Phiên bản cuối / đã ghi nhận thay đổi | Quay lại làm rõ scope và AQ |
| **Milestone 2** | Selected open dataset, provenance/license, data requirements, AQ–Data mapping | Nguồn dữ liệu kiểm chứng được | Không được tiếp tục nếu nguồn/dataset chưa rõ |
| **Milestone 3** | Data understanding, quality findings, prepared dataset, final AQ status | Prepared data có version + pipeline | Hoàn tất AQ–Data Fit và xử lý leakage/gaps |
| **Milestone 4** | Candidate method/model families, rationale, evaluation plan; optional experiment | Phân biệt rõ mandatory vs optional | Hoàn tất ít nhất Level 1 trước Final Report |

## 2. Bảng hướng dẫn tích hợp 4 Milestones thành Final Project Report

Bảng dưới đây là khung viết chính. Với mỗi phần, nhóm phải lấy evidence từ milestone tương ứng, cập nhật theo phiên bản cuối và viết lại thành nội dung có tính kết nối.

| **Phần Final Report** | **Nguồn** | **Mục tiêu phần viết** | **Nội dung phải trình bày** | **Evidence bắt buộc** | **Câu hỏi tự kiểm tra** |
|---|---|---|---|---|---|
| **Abstract / Executive Summary** | M1–M4 | Tóm tắt toàn bộ project | Problem; data; final AQ; proposed/implemented analysis; key result nếu có; educational value; limitations. | 150–250 từ; không đưa chi tiết không có trong report. | Người đọc có hiểu project giải quyết gì, dùng dữ liệu nào và đạt tới mức nào không? |
| **1. Introduction & Educational Context** | M1 | Đặt bài toán trong bối cảnh giáo dục | Bối cảnh; motivation; stakeholders; phạm vi; project objective. | Business context và stakeholder needs đã tổng hợp. | Vì sao vấn đề này đáng phân tích? Ai sử dụng kết quả? |
| **2. Business Understanding & Success Criteria** | M1 | Xác định outcome và tiêu chí thành công | Business Goal; SMART Goal; Primary/Secondary KPI; decision needs. | Bảng SMART/KPI phiên bản cuối. | Goal có phải business outcome, không phải technical task? |
| **3. Analytical Questions & Analytics Levels** | M1 + M3 | Chốt hệ thống câu hỏi cuối cùng | Final AQ; Descriptive / Diagnostic / Predictive / Prescriptive; scope; decision supported. | AQ quality check; AQ revision status. | AQ có Clear, Specific, Scoped, Data-oriented, Answerable không? |
| **4. Data Requirements & Dataset Selection** | M2 | Giải thích cần dữ liệu gì và vì sao chọn dataset | Unit of analysis; target/outcome; variables/concepts; time; population; candidate datasets; selection rationale; provenance/license. | Data Requirement Matrix + Dataset Selection Matrix. | Dataset được chọn vì fit với AQ hay chỉ vì dễ tải? |
| **5. Dataset Description & Requirement–Data Fit** | M2 + M3 | Mô tả dữ liệu thật và độ phù hợp | Files/tables; keys; dimensions; sample; variables; coverage; gaps; AQ status: keep/modify/defer/drop. | Data dictionary + AQ–Data Fit Matrix. | Câu hỏi nào không được dataset hỗ trợ và nhóm đã xử lý ra sao? |
| **6. Data Understanding & Data Quality** | M3 | Chứng minh nhóm hiểu dữ liệu trước khi modeling | Distribution; missingness; duplicates; invalids; outliers; imbalance; temporal coverage; representativeness; sensitive fields. | Profiling tables/charts + quality findings. | Vấn đề dữ liệu nào có thể thay đổi kết luận? |
| **7. Data Preparation & Analytic-ready Data** | M3 | Mô tả pipeline xử lý có lý do | Cleaning; transformations; joins; derived variables; encoding; missing handling; leakage control; final dataset/version. | Preparation Decision Matrix + reproducible pipeline. | Mỗi bước xử lý có lý do và không làm rò rỉ thông tin? |
| **8. Modeling / Analysis Strategy** | M4 – Level 1 | Ánh xạ AQ sang technical approach | AQ → analytics type → technical task → baseline → candidate method/model families → primary proposal → rationale. | Model/Method Selection Matrix. | Tại sao cách tiếp cận phù hợp với câu hỏi, dữ liệu và mức interpretability cần có? |
| **9. Evaluation Design** | M4 – Level 1 | Thiết kế cách biết giải pháp có đủ tốt | Metric; baseline; split/validation; success criterion; leakage/fairness/interpretability checks. | Evaluation Plan. | Metric có phù hợp mục tiêu và class/data structure không? |
| **10. Experimental Implementation & Results** | M4 – Level 2, optional | Báo cáo prototype nếu nhóm thực hiện | Tools; implementation; experimental setup; model results; comparison; error analysis; interpretation. | Code/notebook + result tables/charts. | Kết quả có reproducible và không bị trình bày quá mức evidence? |
| **11. Findings, Discussion & Decision Support** | M1–M4 | Quay lại trả lời câu hỏi ban đầu | Trả lời từng final AQ; educational meaning; implications; uncertainty; stakeholder decision support. | AQ-by-AQ findings table. | Mỗi conclusion có quay lại AQ và evidence không? |
| **12. Limitations & Future Work** | M2–M4 | Nêu giới hạn một cách có trách nhiệm | Dataset gaps; generalizability; observational/causal limits; model limits; deferred AQ; next data needed. | Limitation log / unresolved gaps. | Nhóm có phân biệt “không thấy bằng chứng” với “không có dữ liệu để kiểm tra” không? |
| **13. Generative AI Use & Reflection** | M1–M5 | Minh bạch vai trò AI | AI used for; suggestion; verification; accepted/rejected; final human decision. | AI Decision Log. | AI có hỗ trợ reasoning hay thay thế reasoning/evidence? |
| **14. Conclusion** | M1–M4 | Khép lại project theo business goal | What was asked; what data supported; what analysis is appropriate; what can/cannot be concluded; next step. | Không thêm kết luận mới. | Kết luận có nhất quán với scope và evidence không? |

## 3. Bảng tổng hợp bắt buộc – Final Project Traceability Matrix

> **Đây là sản phẩm trung tâm của Milestone 5**
>
> Mỗi hàng tương ứng với một Analytical Question cuối cùng. Nhìn ngang một hàng phải thấy được toàn bộ đường đi từ mục tiêu → câu hỏi → dữ liệu → xử lý → phương pháp → đánh giá → decision. Nếu một mắt xích không có bằng chứng, nhóm phải ghi GAP / N.A. và giải thích; không được tự bịa để điền đủ bảng.

| **AQ-ID** | **Business / SMART Goal + KPI** | **Final Analytical Question** | **Analytics Level** | **Required Data / Unit** | **Actual Dataset & Variables** | **Preparation / Feature Logic** | **Candidate Method / Model + Rationale** | **Evaluation / Result** | **Decision Supported** | **Final Status** |
|---|---|---|---|---|---|---|---|---|---|---|
| **AQ1** |  |  | Descriptive / Diagnostic / Predictive / Prescriptive |  |  |  |  |  |  | □ Answered □ Partial<br>□ Deferred □ Dropped |
| **AQ2** |  |  | Descriptive / Diagnostic / Predictive / Prescriptive |  |  |  |  |  |  | □ Answered □ Partial<br>□ Deferred □ Dropped |
| **AQ3** |  |  | Descriptive / Diagnostic / Predictive / Prescriptive |  |  |  |  |  |  | □ Answered □ Partial<br>□ Deferred □ Dropped |
| **AQ4** |  |  | Descriptive / Diagnostic / Predictive / Prescriptive |  |  |  |  |  |  | □ Answered □ Partial<br>□ Deferred □ Dropped |
| **AQ5** |  |  | Descriptive / Diagnostic / Predictive / Prescriptive |  |  |  |  |  |  | □ Answered □ Partial<br>□ Deferred □ Dropped |

_Yêu cầu: số dòng bằng số Final Analytical Questions của nhóm. Không bắt buộc phải có đủ bốn mức analytics nếu dữ liệu hoặc scope không hỗ trợ; mọi thay đổi phải được giải thích trong AQ Revision Log._

### 3.1. AQ Revision Log – theo dõi sự thay đổi từ proposal đến report cuối

| **AQ-ID** | **AQ ở Milestone 1** | **Finding từ M2/M3** | **AQ cuối cùng** | **Action** | **Lý do** | **Ảnh hưởng tới phương pháp** |
|---|---|---|---|---|---|---|
| **AQ1** |  |  |  | □ Keep<br>□ Modify<br>□ Defer<br>□ Drop |  |  |
| **AQ2** |  |  |  | □ Keep<br>□ Modify<br>□ Defer<br>□ Drop |  |  |
| **AQ3** |  |  |  | □ Keep<br>□ Modify<br>□ Defer<br>□ Drop |  |  |
| **AQ4** |  |  |  | □ Keep<br>□ Modify<br>□ Defer<br>□ Drop |  |  |

## 4. Hướng dẫn viết Final Report: không ghép milestone, mà viết lại thành một narrative

Final Report nên đọc như một dự án duy nhất, không phải bốn bài tập đặt cạnh nhau. Nhóm nên sử dụng logic sau để tổ chức lập luận:

> **Narrative chuẩn**
>
> Stakeholder problem → measurable goal → analytical questions → required data → selected open dataset → actual data fit/gaps → prepared data → candidate analytical methods → evaluation design / optional experiment → findings and limitations → educational decision support.

### 4.1. Cấu trúc đề nghị và độ dài

| **Phần** | **Độ dài gợi ý** | **Trọng tâm** | **Ghi chú** |
|---|---|---|---|
| **Abstract** | 0.5 trang | Toàn bộ project | Viết sau cùng |
| **1–3. Context, Goal, AQ** | 2–3 trang | M1 đã được cập nhật | Không kể lại transcript stakeholder |
| **4–5. Data Requirements & Selection** | 2–3 trang | M2 | Cite dataset/source/license |
| **6–7. Understanding & Preparation** | 3–5 trang | M3 | Ưu tiên bảng/biểu evidence |
| **8–9. Modeling & Evaluation Plan** | 3–4 trang | M4 Level 1 bắt buộc | Nêu rationale, không chỉ liệt kê thuật toán |
| **10. Experiment** | 0–4 trang | M4 Level 2 optional | Chỉ có nếu thực sự chạy |
| **11–12. Findings, Decision Support, Limitations** | 2–4 trang | Tổng hợp | Không causal hóa observational data |
| **13–14. AI Reflection & Conclusion** | 1–2 trang | M1–M5 | Minh bạch AI usage |
| **Appendices** | Không giới hạn hợp lý | Evidence chi tiết | Search log, AI log, data dictionary, code link |

### 4.2. Hai trường hợp của Milestone 4 phải được viết khác nhau

| **Tình trạng** | **Final Report phải có** | **Không được làm** |
|---|---|---|
| **Chỉ hoàn thành Level 1 (bắt buộc)** | Modeling Strategy + Candidate Methods + Rationale + Evaluation Design. Viết ở thì đề xuất: “would be evaluated”, “is proposed”. | Không tạo metric, chart, confusion matrix hoặc nói “model achieved…” nếu chưa chạy. |
| **Có Level 2 (optional experiment)** | Bổ sung implementation, real experimental results, baseline comparison, error/limitation analysis. | Không chỉ báo “best model”; phải giải thích metric, validation và ý nghĩa với AQ. |

## 5. Bảng tổng hợp câu trả lời cuối cùng theo Analytical Question

Sau khi viết các phần kỹ thuật, nhóm phải quay lại từng AQ và trả lời ở mức evidence mà project thực sự đạt được. Đây là cầu nối giữa analytics và decision support.

| **AQ-ID** | **Final AQ** | **Evidence/Data Used** | **Method / Analysis** | **Main Finding hoặc Expected Output** | **Confidence / Limitation** | **Implication for Decision** |
|---|---|---|---|---|---|---|
| **AQ1** |  |  |  |  |  |  |
| **AQ2** |  |  |  |  |  |  |
| **AQ3** |  |  |  |  |  |  |
| **AQ4** |  |  |  |  |  |  |
| **AQ5** |  |  |  |  |  |  |
| **Quy tắc diễn giải**<br>Descriptive: mô tả điều đã xảy ra. Diagnostic: nói về association/pattern trừ khi thiết kế cho phép causal inference. Predictive: kết luận về khả năng dự báo trên validation phù hợp, không suy ra nguyên nhân. Prescriptive: nếu chỉ có observational data, trình bày recommendation như giả thuyết/decision option cần kiểm chứng chứ không khẳng định intervention chắc chắn hiệu quả. |  |  |  |  |  |  |

## 6. Generative AI trong Milestone 5 – được dùng như thế nào?

Generative AI được phép sử dụng như một writing/review partner, nhưng không được tạo evidence thay cho project. Mọi nội dung AI đề xuất phải được nhóm kiểm tra với milestone artifacts, dataset và nguồn tham khảo.

| **AI có thể hỗ trợ** | **Ví dụ** | **Yêu cầu kiểm chứng** | **Không được phép** |
|---|---|---|---|
| **Kiểm tra tính nhất quán** | Phát hiện SMART Goal/AQ/dataset/model không còn khớp | Đối chiếu với M1–M4 và sửa bằng quyết định của nhóm | Để AI tự thay đổi scope mà không ghi nhận |
| **Review cấu trúc report** | Gợi ý thứ tự section, chuyển ý, rút gọn trùng lặp | Nhóm tự quyết định narrative cuối | Nộp nguyên output AI như report |
| **Language editing** | Sửa câu, clarity, academic tone | Không làm thay đổi meaning/evidence | AI thêm claim, citation, metric không có thật |
| **Challenge reasoning** | Hỏi ngược: vì sao model này? metric này? | Nhóm trả lời bằng course concept/data evidence | Coi phản hồi AI là đáp án đúng mặc định |
| **Code/documentation review nếu có experiment** | Review README, code comments, reproducibility steps | Chạy lại code và xác minh output | Bịa kết quả, synthetic metric, figure giả |

### 6.1. AI Decision Log tối thiểu

| **Stage** | **AI used for** | **AI suggestion/output** | **Student verification / modification** | **Final human decision** |
|---|---|---|---|---|
| **M1 / M5** |  |  |  |  |
| **M2 / M5** |  |  |  |  |
| **M3 / M5** |  |  |  |  |
| **M4 / M5** |  |  |  |  |

## 7. Gói nộp cuối kỳ – Final Project Package

| **Deliverable** | **Bắt buộc?** | **Nội dung** | **Yêu cầu** |
|---|---|---|---|
| **Final Project Report (.pdf hoặc .docx theo yêu cầu lớp)** | Bắt buộc | Báo cáo đã tích hợp M1–M5 | Khoảng 15–25 trang phần chính, không tính phụ lục; có Traceability Matrix |
| **Project Traceability Matrix** | Bắt buộc | Bảng mục 3 | Phải cập nhật theo Final AQ |
| **Dataset source + provenance/license** | Bắt buộc | Link/source và version đã sử dụng | Có thể truy vết và tái tải |
| **Prepared dataset / access instructions** | Bắt buộc nếu được phép chia sẻ | Dữ liệu sau M3 hoặc hướng dẫn tái tạo | Không vi phạm license/privacy |
| **Data dictionary** | Bắt buộc | Định nghĩa biến cuối | Khớp analytic-ready data |
| **Code / notebook** | Chỉ bắt buộc nếu có Level 2 experiment hoặc giảng viên yêu cầu | Preparation + experiment code | Chạy được hoặc có README rõ |
| **README** | Bắt buộc | Cấu trúc project, cách tái tạo, dependency | Ngắn gọn nhưng đủ reproducibility |
| **AI Decision Log** | Bắt buộc nếu có dùng GenAI | Vai trò, verification, final decision | Đưa phụ lục hoặc file riêng |
| **Appendices / supporting evidence** | Khi cần | Search log, profiling, extended tables, prompts quan trọng | Không làm phần chính quá dài |

## 8. Rubric đề nghị cho Milestone 5 / Final Project Report – 100 điểm

| **Tiêu chí** | **Mô tả** | **Điểm** |
|---|---|---|
| **Problem–Goal–AQ coherence** | Business context, SMART/KPI và Final AQ nhất quán; changes được giải thích. |  |
| **Requirement–Data traceability** | Data requirements, dataset selection, variable coverage và gaps được truy vết rõ. |  |
| **Data understanding & preparation evidence** | Profiling, quality, preparation decisions, leakage/ethics được trình bày có bằng chứng. |  |
| **Modeling/analysis strategy – Level 1** | AQ → task → baseline → candidate methods → rationale hợp lý. |  |
| **Evaluation design** | Metric, validation/split, success criteria và limitations phù hợp. |  |
| **Experimental evidence – nếu có** | Nếu có Level 2: implementation/reproducibility/result interpretation. Nếu không có: điểm này chuyển vào chất lượng Level 1 theo quy định lớp. |  |
| **Findings & educational decision support** | Trả lời AQ ở đúng mức evidence; implications hợp lý, không overclaim. |  |
| **Limitations & research integrity** | Nêu data/model/generalizability/causal limits minh bạch. |  |
| **Traceability Matrix & report integration** | Bảng tổng hợp hoàn chỉnh; report không phải bản ghép cơ học của milestones. |  |
| **Generative AI transparency & human ownership** | AI usage minh bạch, có verification và quyết định cuối của nhóm. |  |
| **Presentation & references** | Format, bảng/figure, citation, language, consistency. |  |

## 9. Checklist trước khi nộp

- [ ] Final Report sử dụng Final AQ, không dùng phiên bản đã bị sửa/drop mà không giải thích.
- [ ] Mỗi Final AQ có thể truy vết đến Business/SMART Goal và decision cần hỗ trợ.
- [ ] Mỗi AQ có dữ liệu/biến thực tế tương ứng hoặc được đánh dấu gap/partial/deferred.
- [ ] Dataset source, version, provenance và license đã được ghi rõ.
- [ ] Data preparation có rationale, version và kiểm soát leakage phù hợp.
- [ ] M4 Level 1 được hoàn thành cho từng AQ có thể phân tích: task, baseline, candidate methods, rationale, evaluation.
- [ ] Nếu không chạy thử nghiệm, report không chứa metric/kết quả giả định như kết quả thật.
- [ ] Nếu có chạy thử nghiệm, kết quả có validation, baseline và khả năng tái lập.
- [ ] Descriptive/Diagnostic/Predictive/Prescriptive được diễn giải đúng mức bằng chứng.
- [ ] Limitations, deferred questions và future data needs được trình bày rõ.
- [ ] Traceability Matrix hoàn chỉnh và nhất quán với các section.
- [ ] Generative AI usage được khai báo; không có fabricated citation/data/result.
- [ ] Tất cả bảng, hình, dataset và nguồn tham khảo có tên/citation phù hợp.
- [ ] Abstract và Conclusion phản ánh đúng mức project thực sự đạt được.

> **Điều kiện hoàn thành Milestone 5**
>
> Một Final Project Report đạt yêu cầu khi người chấm có thể lần theo một đường logic rõ ràng từ stakeholder problem đến Final Analytical Questions, từ câu hỏi đến dữ liệu thực tế, từ dữ liệu đến preparation, từ câu hỏi/dữ liệu đến phương pháp và đánh giá, và cuối cùng quay lại được decision/educational value – đồng thời nhìn thấy rõ những gì project chưa thể kết luận.

Final Integration & Project Report | Education Analytics Project
