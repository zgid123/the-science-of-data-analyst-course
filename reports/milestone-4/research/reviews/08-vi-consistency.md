# Vietnamese consistency pass – Milestone 4, 2026-11-08

Stage 5 (first part) of build-report reference.md section 4.3: a whole-report read of the Vietnamese twins in file order after the four group reviews (`review-2026-11-08-{A,B,C,D}.md`). Paths are relative to `reports/milestone-4/report/`. Edits were applied by an exact-match script (`consistency-2026-11-08-scripts/apply_edits.py`; each before-string found the stated number of times, the run aborts otherwise); five single edits were made by hand (last five rows of the table). Line numbers are those of the edited files.

## Checks run

| Step | Command | Result before | Result after |
| :---- | :---- | :---- | :---- |
| 1 | `check_parity.py --report reports/milestone-4/report --lang vi` | 0 errors, 24 warnings (23 in the verbatim English prompts of 10-06, 1 loanword warning on the English term "Sign-flip permutation test" in 00-2) | 0 errors, 24 warnings (the same expected ones) |
| 2 | `check_abbreviations.py --report reports/milestone-4/report --lang vi` | 2 violations: DEFINE ROC (04-00:3), REPEAT UK (10-05:15) | 0 violations (17 abbreviations) |
| 3 | `glossary.py --lang vi --task milestone-4 coverage --report reports/milestone-4/report` | 18 drifting | 20 drifting, all explained below |
| 3 | cross-reference comparison EN vs VI per file (`consistency-2026-11-08-scripts/xref.py`) | no real mismatch | – |
| 3 | first use of English glosses in document order (`first.py`, `vgloss.py`) | 29 terms glossed more than once or after first use | 0 (remaining repeats mirror English labels) |
| 4 | `check_structure.py --report reports/milestone-4/report` | – | VI: 34 files, 33 headings, 2 figures, 29 tables: 0 errors, 0 warnings |
| 5 | `translation_status.py --report reports/milestone-4/report --lang vi --mark <25 English paths>` | – | recorded 25 files; 34 sections, 0 need translation |

## What drifted

1. **English glosses repeated across files.** The group reviews applied "English once per file", while this report gives the English once per document. Twenty-six terms carried their English two to seven times: baseline (7×), recall (5×), lift (4×), odds ratio (4×), fold "(phần chia trong kiểm định chéo)" (8×), separation (6×), challenger (5×), gradient-boosted trees (4×), sign-flip test (4×), proxy (4×), calibration-in-the-large (3×), fixed effects (3×), leave-one-run-out (3×), uplift (3×), Business Goal, Evaluation Design Card and AQ Modeling Brief glosses, the capacity explanation "(số sinh viên giảng viên hướng dẫn liên hệ được: …)" (4×), the two-level bootstrap explanation, Controlled Change Log, AI Decision Log, prototype, precision, normalised recall, calibration slope, net benefit, slicing analysis, post-hoc, performative prediction, non-informative censoring. Each now keeps its gloss only at the first use in document order.
2. **Glosses placed after the first use.** "phương pháp chính (primary approach)" first occurs in 01-00 (gloss was in 03-00); "background-only model", "penalised logistic regression", "gradient-boosted trees" and "uplift" first occur in the Candidate Solution Matrix (03-01 Bảng 3.1; glosses were in 03-03, 07-00 or later); "hazard" first occurs in 03-03 (gloss was in 10-01). Glosses moved to the first use. "calibration" stays glossed at its definition in 04-00 (first mention 02-01:47 is in passing; the glossary row asks for no English).
3. **Milestone 4 forms not yet applied.** "nhãn bị đánh dấu" (10-05 R14) → "dấu cảnh báo" / "sinh viên bị đánh dấu"; "bộ mở rộng", "bộ biến mở rộng", "nhóm biến chính/mở rộng" (02-01, 03-03, 08-00, 10-03) → "bộ biến dự báo chính / bộ biến dự báo mở rộng"; "đặc trưng" for a predictor (05-01:3) → "biến dự báo"; "độ chính xác của danh sách theo hạn mức liên hệ" / "(precision at capacity)" (06-00, 10-02) → "độ chính xác của danh sách dài k"; "kỳ mở kiểm thử", "lượt đăng ký học kiểm thử", "kết quả kiểm thử" (10-03, 10-04, 10-05) → "… của tập kiểm thử" / "… trong tập kiểm thử".
4. **Term variants for one concept.** "sai số chuẩn bền vững" (10-01) vs "sai số chuẩn vững" (03-02, glossary); "hệ số co (shrinkage) kỳ vọng", "độ lạc quan", "nguy cơ tổng thể" (10-03:46) vs "mức co hệ số kỳ vọng", "mức lạc quan", "nguy cơ chung" (04-02:18, glossary); "các thẻ thiết kế đánh giá" (07-00) vs "Evaluation Design Card" elsewhere; paired runs called "kỳ mở có kỳ tương ứng năm 2013" in 04-02 while the terms page entry "kỳ mở có cặp" points to Mục 4.2 and 10-03 uses "kỳ mở có cặp" (04-02 now introduces "kỳ mở có cặp, tức là có kỳ tương ứng năm 2013 …").
5. **Terms and abbreviation pages vs body.** 00-1 gave ROC as "Đường đặc trưng hoạt động của bộ thu", while the body defines ROC as the characteristic ("đường cong đặc trưng hoạt động của bộ thu (ROC)"); 00-1 now reads "Đặc trưng hoạt động của bộ thu", matching the English expansion. 00-2 named the AQ2 task "phân tích mối liên hệ" while Mục 2.2 calls it "đo mối liên hệ"; aligned to the body. All other 00-2 rows match the body forms (capacity, precision at capacity, separation, lift, labels-available variant, sign-flip test, freeze, cut-off, leave-one-run-out folds).
6. **Abbreviations.** UK was spelled out again with "(UK)" in 10-05 after its definition in 05-01; 10-05 now uses "UK".
7. **Sentence fixes found while reading.** 04-04:3 had two "vì" in one sentence; 04-02:10 gained a comma before "và" from the paired-run edit and was rephrased (parity warning cleared).

## Cross-references and bridges

Every Mục, Phần, Bảng, Hình and Phụ lục pointer matches the English file by file. The comparison script's differences are all expected: English "Section 4/6" for a whole Part is "Phần 4/6" in Vietnamese (00-1, 00-2, 10-06); the Section column of Bảng 5.1 holds "Mục 5.1/5.2" where the English cell holds the bare number; 06-00 repeats "Bảng 6.1" once more than the English in its prose; "Appendix III – Validation" and the 09 reference title ("Part II") are false matches; the prompt references of 10-06 sit in the verbatim English block quotes. The bridges between consecutive files read naturally (01-02 → 02-00 "Khi điều kiện đầu vào đã đạt (Mục 1.2)", 03-04 → 04-00 "Trên cơ sở các phương pháp đã chọn ở Phần 3", 04-04 → 05-00, 05-02 → 06-00 "Bên cạnh các rủi ro ở Phần 5", 07-00 → 08-00 "Từ Phần 1 đến Phần 7"); none needed a change.

## Coverage warnings after the pass (not real drift)

All 20 remaining coverage warnings are rows of other milestones or general rows whose English word matches a different concept here: capacity rows of Milestone 2 ("số sinh viên cán bộ liên hệ được mỗi tuần"; Milestone 4 uses "hạn mức liên hệ"); predictor / primary-extended rows of Milestone 3 ("đặc trưng"; Milestone 4 uses "biến dự báo", 26 matches of its own row); flag noun row "nhãn bị đánh dấu" (replaced by the Milestone 4 row); test runs (36%: the other English "test runs" occurrences are rendered "tập kiểm thử" or "các kỳ mở năm 2014", both glossary-sanctioned); paired run (Milestone 3 row; Milestone 4 uses the terms-page form "kỳ mở có cặp"); Before/After, enrolment, tutor, non-completion, retention, programme, measure, KPI baseline, proxy (measure), reviewer, Validation column, deprivation band (full form at first use, short form "mức khó khăn của khu vực" after, as its row allows).

## Glossary rows that look wrong

- `topics/early-warning-evaluation.md`, row "flag (on a student, noun) → nhãn bị đánh dấu": contradicts the Milestone 4 row "flag on a student (noun, Milestone 4) → dấu cảnh báo", whose Usage says "nhãn bị đánh dấu" reads worse. Suggest replacing the older row's form with "dấu cảnh báo" and adding "nhãn bị đánh dấu" to Replaces, so coverage stops reporting it.
- `topics/early-warning-evaluation.md`, rows "capacity (Milestone 2 wording)" and "capacity (weekly follow-up capacity of staff)" share the same form and both fire on every English "capacity"; a Milestone 2 qualifier in the English column of the second row (or merging the two) would remove a duplicate warning.
- `topics/early-warning-evaluation.md`, row "primary / extended predictors → đặc trưng chính / đặc trưng mở rộng" has no Milestone 3 qualifier in its English column, so it competes with the Milestone 4 row on every report.
- "robust standard errors" exists as "sai số chuẩn vững" in the topic layer; the translators had produced "sai số chuẩn bền vững" in 10-01, so adding "sai số chuẩn bền vững" to its Replaces would let the checks catch it.

## Left open

- Parity warnings: 23 in the verbatim English prompts of 10-06 and 1 loanword warning on the English term "Sign-flip permutation test" in 00-2 (all expected).
- The Fail / Withdrawn labels keep their English in parentheses in both 01-02:3 and 02-01:3 (dataset values the reader meets in tables), and "trợ lý tìm tài liệu" is repeated per row of Bảng 6.1 as in the English; left as is.
- A reader test (stage 5, second part) has not been run on the edited twins.

## Edits

Edit operations per file: 00-1 1, 00-2 1, 01-00 1, 02-01 2, 03-00 3, 03-01 2, 03-02 2, 03-03 3, 04-01 5, 04-02 5, 04-03 6, 04-04 1, 05-00 4, 05-01 2, 05-02 1, 06-00 7, 07-00 6, 08-00 5, 10-01 14, 10-02 4, 10-03 16, 10-04 7, 10-05 4, 10-06 3, 10-07 2 (107 operations in 25 files; one operation may replace several occurrences in a file).

| File | Line | Reason | Before | After |
| :---- | :---- | :---- | :---- | :---- |
| 01-00-context-continuity.vi.md | 3 | English gloss moved to the first use in document order | phương pháp chính kèm lý do | phương pháp chính (primary approach) kèm lý do |
| 03-00-candidate-approaches.vi.md | 3 | English gloss repeated after its first use in document order | một phương pháp cơ sở (baseline) hợp lý | một phương pháp cơ sở hợp lý |
| 03-00-candidate-approaches.vi.md | 3 | English gloss repeated after its first use in document order | trước khi chọn phương pháp chính (primary approach); | trước khi chọn phương pháp chính; |
| 03-00-candidate-approaches.vi.md | 3 | Explanation of capacity repeated; given once at first use (01-01), as the glossary row says | bài toán xếp hạng theo hạn mức liên hệ (số sinh viên giảng viên hướng dẫn liên hệ được: 3 hoặc 5 trên mỗi nhóm khoảng 20). | bài toán xếp hạng theo hạn mức liên hệ. |
| 02-01-modeling-briefs.vi.md | 56 | English gloss repeated after its first use in document order | tỷ lệ phát hiện (recall) | tỷ lệ phát hiện |
| 03-01-criteria-matrix.vi.md | 15 | English gloss moved to the first use in document order | mô hình logistic chỉ dùng đặc điểm cá nhân; danh sách ngẫu nhiên \| Hồi quy logistic có hiệu chỉnh phạt \| Cây tăng cường độ dốc (mô hình sống sót th… | mô hình logistic chỉ dùng đặc điểm cá nhân (background-only model); danh sách ngẫu nhiên \| Hồi quy logistic có hiệu chỉnh phạt (penalised logistic … |
| 03-01-criteria-matrix.vi.md | 16 | English gloss moved to the first use in document order | nên không xếp hạng theo lợi ích can thiệp \| | nên không xếp hạng theo lợi ích can thiệp (uplift) \| |
| 03-02-descriptive-diagnostic.vi.md | 7 | English gloss repeated after its first use in document order | Mô hình này có hiệu ứng cố định (fixed effects) cho từng | Mô hình này có hiệu ứng cố định cho từng |
| 03-02-descriptive-diagnostic.vi.md | 9 | English gloss repeated after its first use in document order | kèm tỉ số odds (odds ratio). | kèm tỉ số odds. |
| 03-03-predictive.vi.md | 7 | Milestone 4 form "bộ biến dự báo mở rộng" | Bộ biến mở rộng bổ sung 10 biến dự báo ( | Bộ biến dự báo mở rộng bổ sung 10 biến ( |
| 03-03-predictive.vi.md | 9 | English gloss repeated after its first use in document order | Cây tăng cường độ dốc (gradient-boosted trees), tức tổ hợp | Cây tăng cường độ dốc, tức tổ hợp |
| 03-03-predictive.vi.md | 9 | English gloss moved to the first use in document order | nguy cơ rút khỏi module theo từng tuần bằng cùng phần mềm | nguy cơ rút khỏi module theo từng tuần (hazard) bằng cùng phần mềm |
| 04-01-evaluation-cards.vi.md | 3 | English gloss repeated after its first use in document order | Evaluation Design Card (thẻ thiết kế đánh giá) gồm bảy | Evaluation Design Card gồm bảy |
| 04-01-evaluation-cards.vi.md | 3 | English gloss repeated after its first use in document order | phương pháp cơ sở (baseline), phân tích lỗi | phương pháp cơ sở, phân tích lỗi |
| 04-01-evaluation-cards.vi.md | 3 | English gloss repeated after its first use in document order | tỷ lệ phát hiện (recall) quan trọng | tỷ lệ phát hiện quan trọng |
| 04-01-evaluation-cards.vi.md | 5 | English gloss repeated after its first use in document order | mức vượt tỷ lệ nền (lift). Ba chỉ số | mức vượt tỷ lệ nền. Ba chỉ số |
| 04-01-evaluation-cards.vi.md | 27 | English gloss repeated after its first use in document order | tỉ số odds (odds ratio) được báo cáo | tỉ số odds được báo cáo |
| 04-02-validation-strategy.vi.md | 8 | English gloss repeated after its first use in document order | hai mô hình đối sánh (challenger): mô hình dùng cây tăng cường độ dốc (gradient-boosted trees) và | hai mô hình đối sánh: mô hình dùng cây tăng cường độ dốc và |
| 04-02-validation-strategy.vi.md | 6 | English gloss repeated after its first use in document order | một fold (phần chia trong kiểm định chéo) riêng | một fold riêng |
| 04-02-validation-strategy.vi.md | 16 | English gloss repeated after its first use in document order | kiểm định hoán vị đổi dấu (sign-flip test) trên 13 | kiểm định hoán vị đổi dấu trên 13 |
| 04-02-validation-strategy.vi.md | 10 | Paired runs named with the terms-page term "kỳ mở có cặp" (00-2 points to Mục 4.2) | cho 9 kỳ mở có kỳ tương ứng năm 2013 (cùng module và cùng tháng bắt đầu) và cho 4 kỳ mở không có kỳ tương ứng. | cho 9 kỳ mở có cặp, tức là có kỳ tương ứng năm 2013 (cùng module và cùng tháng bắt đầu), và cho 4 kỳ mở không có cặp. |
| 04-03-metrics-success.vi.md | 3 | English gloss repeated after its first use in document order | tỷ lệ phát hiện (recall), độ chính xác của danh sách (precision) và mức vượt tỷ lệ nền (lift) chỉ là | tỷ lệ phát hiện, độ chính xác của danh sách và mức vượt tỷ lệ nền chỉ là |
| 04-03-metrics-success.vi.md | 3 | English gloss repeated after its first use in document order | tỷ lệ phát hiện chuẩn hóa (normalised recall) của danh sách | tỷ lệ phát hiện chuẩn hóa của danh sách |
| 04-03-metrics-success.vi.md | 7 | English gloss repeated after its first use in document order | hiệu chuẩn tổng thể (calibration-in-the-large): hệ số | hiệu chuẩn tổng thể: hệ số |
| 04-03-metrics-success.vi.md | 7 | English gloss repeated after its first use in document order | độ dốc hiệu chuẩn (calibration slope), có | độ dốc hiệu chuẩn, có |
| 04-03-metrics-success.vi.md | 9 | English gloss repeated after its first use in document order | Lợi ích ròng (net benefit) so sánh | Lợi ích ròng so sánh |
| 04-03-metrics-success.vi.md | 17 | English gloss repeated after its first use in document order | bootstrap hai tầng ghép cặp (lấy mẫu lại kỳ mở, rồi lượt đăng ký học trong từng kỳ mở), nằm trên 0; kiểm định hoán vị đổi dấu (sign-flip test) một … | bootstrap hai tầng ghép cặp, nằm trên 0; kiểm định hoán vị đổi dấu một phía |
| 04-04-error-fairness.vi.md | 3 | Two "vì" in one sentence; the colon already introduces the explanation | nhận ra các thuộc tính đó: vì mức hoạt động | nhận ra các thuộc tính đó: mức hoạt động |
| 05-00-risk-ethics.vi.md | 11 | English gloss repeated after its first use in document order | bên trong từng fold (phần chia trong kiểm định chéo); | bên trong từng fold; |
| 05-00-risk-ethics.vi.md | 14 | English gloss repeated after its first use in document order | lợi ích can thiệp (uplift) sau | lợi ích can thiệp sau |
| 05-00-risk-ethics.vi.md | 15 | English gloss repeated after its first use in document order | \| Tỷ lệ phát hiện (recall) thấp hơn | \| Tỷ lệ phát hiện thấp hơn |
| 05-00-risk-ethics.vi.md | 15 | English gloss repeated after its first use in document order | giữa các nhóm (separation) là tiêu chí chính | giữa các nhóm là tiêu chí chính |
| 05-01-leakage-interpretability.vi.md | 3 | Milestone 4 keeps "biến dự báo" for predictors/features | đặc trưng thực chất là biến đại diện | biến dự báo thực chất là biến đại diện |
| 05-01-leakage-interpretability.vi.md | 3 | English gloss repeated after its first use in document order | bên trong từng fold (phần chia trong kiểm định chéo). | bên trong từng fold. |
| 05-02-causal-fairness-use.vi.md | 5 | English gloss repeated after its first use in document order | giữa các nhóm (separation) được dùng | giữa các nhóm được dùng |
| 06-00-genai-usage.vi.md | 3 | English gloss repeated after its first use in document order | các AQ Modeling Brief (bản mô tả yêu cầu mô hình hóa của từng AQ) | các AQ Modeling Brief |
| 06-00-genai-usage.vi.md | 3 | English gloss repeated after its first use in document order | các Evaluation Design Card (thẻ thiết kế đánh giá), | các Evaluation Design Card, |
| 06-00-genai-usage.vi.md | 12 | English gloss repeated after its first use in document order | fold (phần chia trong kiểm định chéo) theo nhóm | fold theo nhóm |
| 06-00-genai-usage.vi.md | 13 | English gloss repeated after its first use in document order | lợi ích can thiệp (uplift) đều | lợi ích can thiệp đều |
| 06-00-genai-usage.vi.md | 13 | English gloss repeated after its first use in document order | dự báo tự tác động (performative prediction) \| | dự báo tự tác động \| |
| 06-00-genai-usage.vi.md | 14 | English gloss repeated after its first use in document order | mô hình đối sánh (challenger), | mô hình đối sánh, |
| 06-00-genai-usage.vi.md | 15 | Milestone 4 form "độ chính xác của danh sách dài k" | S2 (độ chính xác của danh sách theo hạn mức liên hệ) | S2 (độ chính xác của danh sách dài k) |
| 07-00-prototype-protocol.vi.md | 3 | English gloss repeated after its first use in document order | Nguyên mẫu (prototype) không bắt buộc | Nguyên mẫu không bắt buộc |
| 07-00-prototype-protocol.vi.md | 12 | English gloss repeated after its first use in document order | \| 2. Cài đặt phương pháp cơ sở (baseline) \| | \| 2. Cài đặt phương pháp cơ sở \| |
| 07-00-prototype-protocol.vi.md | 12 | English gloss repeated after its first use in document order | mô hình chỉ dùng đặc điểm cá nhân (background-only model) và | mô hình chỉ dùng đặc điểm cá nhân và |
| 07-00-prototype-protocol.vi.md | 13 | English gloss repeated after its first use in document order | Hồi quy logistic có hiệu chỉnh phạt (penalised logistic regression) làm phương pháp chính (primary approach) và cây tăng cường độ dốc (gradient-boo… | Hồi quy logistic có hiệu chỉnh phạt làm phương pháp chính và cây tăng cường độ dốc làm mô hình đối sánh, |
| 07-00-prototype-protocol.vi.md | 15 | Brief term kept in English as everywhere else ("Evaluation Design Card") | các thẻ thiết kế đánh giá (Bảng 4.1–4.4) | các Evaluation Design Card (Bảng 4.1–4.4) |
| 07-00-prototype-protocol.vi.md | 18 | English gloss repeated after its first use in document order | các fold (phần chia trong kiểm định chéo) và | các fold và |
| 08-00-traceability.vi.md | 3 | English gloss repeated after its first use in document order | Business Goal (mục tiêu của tổ chức) đến | Business Goal đến |
| 08-00-traceability.vi.md | 11 | Milestone 4 form "biến dự báo chính / bộ biến dự báo mở rộng" | hoặc bộ biến mở rộng vượt trội | hoặc bộ biến dự báo mở rộng vượt trội |
| 08-00-traceability.vi.md | 11 | Explanation of capacity repeated; given once at first use (01-01), as the glossary row says | theo hạn mức liên hệ (số sinh viên giảng viên hướng dẫn liên hệ được: 3 hoặc 5 trên mỗi nhóm khoảng 20) \| | theo hạn mức liên hệ \| |
| 08-00-traceability.vi.md | 11 | English gloss repeated after its first use in document order | \| Loại trừ từng kỳ mở (leave-one-run-out) trên | \| Loại trừ từng kỳ mở trên |
| 08-00-traceability.vi.md | 16 | English gloss repeated after its first use in document order | nhật ký thay đổi có kiểm soát (Controlled Change Log): | nhật ký thay đổi có kiểm soát: |
| 10-01-candidate-comparison.vi.md | 7 | English gloss repeated after its first use in document order | phương pháp cơ sở (baseline); | phương pháp cơ sở; |
| 10-01-candidate-comparison.vi.md | 13 | English gloss repeated after its first use in document order | hiệu ứng cố định (fixed effects) theo kỳ mở | hiệu ứng cố định theo kỳ mở |
| 10-01-candidate-comparison.vi.md | 18 | English gloss repeated after its first use in document order | tỉ số odds (odds ratio) \| | tỉ số odds \| |
| 10-01-candidate-comparison.vi.md | 20 | One term with 03-02 and the glossary ("sai số chuẩn vững"); English gloss dropped | dùng sai số chuẩn bền vững (robust standard errors); | dùng sai số chuẩn vững; |
| 10-01-candidate-comparison.vi.md | 28 | English gloss repeated after its first use in document order | chỉ dùng đặc điểm cá nhân (background-only model) \| | chỉ dùng đặc điểm cá nhân \| |
| 10-01-candidate-comparison.vi.md | 28 | English gloss repeated after its first use in document order | có hiệu chỉnh phạt (penalised logistic regression) (phương pháp chính) | có hiệu chỉnh phạt (phương pháp chính) |
| 10-01-candidate-comparison.vi.md | 28 | English gloss repeated after its first use in document order | cây tăng cường độ dốc (gradient-boosted trees) \| | cây tăng cường độ dốc \| |
| 10-01-candidate-comparison.vi.md | 30 | English gloss repeated after its first use in document order | theo từng tuần (hazard) [8] | theo từng tuần [8] |
| 10-01-candidate-comparison.vi.md | 33 | English gloss repeated after its first use in document order | Giải thích hậu nghiệm (post-hoc), có thể | Giải thích hậu nghiệm, có thể |
| 10-01-candidate-comparison.vi.md | 35 | English gloss repeated after its first use in document order | các fold (phần chia trong kiểm định chéo) chia theo nhóm | các fold chia theo nhóm |
| 10-01-candidate-comparison.vi.md | 36 | English gloss repeated after its first use in document order | kiểm tra biến thay thế (proxy) \| | kiểm tra biến thay thế \| |
| 10-01-candidate-comparison.vi.md | 40 | English gloss repeated after its first use in document order | mô hình đối sánh (challenger), vì | mô hình đối sánh, vì |
| 10-01-candidate-comparison.vi.md | 46 | English gloss repeated after its first use in document order | lợi ích can thiệp (uplift) \| | lợi ích can thiệp \| |
| 10-01-candidate-comparison.vi.md | 48 | Explanation of capacity repeated; given once at first use (01-01), as the glossary row says | k xác định từ hạn mức liên hệ (số sinh viên giảng viên hướng dẫn liên hệ được: 3 hoặc 5 trên mỗi nhóm khoảng 20) \| | k xác định từ hạn mức liên hệ \| |
| 10-02-metric-definitions.vi.md | 3 | English gloss repeated after its first use in document order | Các Evaluation Design Card (thẻ thiết kế đánh giá) ở | Các Evaluation Design Card ở |
| 10-02-metric-definitions.vi.md | 13 | Milestone 4 form "độ chính xác của danh sách dài k"; English gloss dropped | \| Độ chính xác của danh sách (precision at capacity) \| | \| Độ chính xác của danh sách dài k \| |
| 10-02-metric-definitions.vi.md | 14 | English gloss repeated after its first use in document order | \| Mức vượt tỷ lệ nền (lift) \| | \| Mức vượt tỷ lệ nền \| |
| 10-02-metric-definitions.vi.md | 17 | English gloss repeated after its first use in document order | \| Hiệu chuẩn tổng thể (calibration-in-the-large) \| | \| Hiệu chuẩn tổng thể \| |
| 10-03-validation-protocol.vi.md | 7 | English gloss repeated after its first use in document order | phương pháp cơ sở (baseline). Lần chốt | phương pháp cơ sở. Lần chốt |
| 10-03-validation-protocol.vi.md | 14 | English gloss repeated after its first use in document order | Loại trừ từng kỳ mở (leave-one-run-out): mỗi kỳ mở làm fold (phần chia trong kiểm định chéo) kiểm định | Loại trừ từng kỳ mở: mỗi kỳ mở làm fold kiểm định |
| 10-03-validation-protocol.vi.md | 13 | "predictor sets" → "các bộ biến dự báo"; "nhóm" stays for student groups | phạm vi dữ liệu, nhóm biến dự báo, quy tắc | phạm vi dữ liệu, các bộ biến dự báo, quy tắc |
| 10-03-validation-protocol.vi.md | 16 | Milestone 4 form "biến dự báo chính / bộ biến dự báo mở rộng" | mỗi phương pháp chạy với nhóm biến dự báo chính và với nhóm mở rộng | mỗi phương pháp chạy với bộ biến dự báo chính và với bộ biến dự báo mở rộng |
| 10-03-validation-protocol.vi.md | 16 | Milestone 4 form "biến dự báo chính / bộ biến dự báo mở rộng" | (cũng như nhóm biến mở rộng chỉ thay thế nhóm chính) | (cũng như bộ biến dự báo mở rộng chỉ thay thế bộ biến dự báo chính) |
| 10-03-validation-protocol.vi.md | 22 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | một fold hoặc một kỳ mở kiểm thử có thể | một fold hoặc một kỳ mở của tập kiểm thử có thể |
| 10-03-validation-protocol.vi.md | 24 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | Do chỉ có 13 kỳ mở kiểm thử, | Do chỉ có 13 kỳ mở của tập kiểm thử, |
| 10-03-validation-protocol.vi.md | 24 | English gloss repeated after its first use in document order | kiểm định hoán vị đổi dấu (sign-flip test) một phía | kiểm định hoán vị đổi dấu một phía |
| 10-03-validation-protocol.vi.md | 36 | Milestone 4 form "biến dự báo chính / bộ biến dự báo mở rộng" | \| Số tham số, nhóm biến chính (19 biến dự báo, các số hạng | \| Số tham số, bộ biến dự báo chính (19 biến, các số hạng |
| 10-03-validation-protocol.vi.md | 37 | Milestone 4 form "biến dự báo chính / bộ biến dự báo mở rộng" | \| Số tham số, nhóm biến chính và nhóm mở rộng kèm lượt nhấp theo tuần | \| Số tham số, bộ biến dự báo chính và bộ biến dự báo mở rộng kèm lượt nhấp theo tuần |
| 10-03-validation-protocol.vi.md | 38,39 | Milestone 4 form "biến dự báo chính / bộ biến dự báo mở rộng" | nhóm biến chính / có nhóm mở rộng và lượt nhấp theo tuần | bộ biến dự báo chính / thêm bộ biến dự báo mở rộng và lượt nhấp theo tuần |
| 10-03-validation-protocol.vi.md | 40,41,42,43 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | Lượt đăng ký học kiểm thử | Lượt đăng ký học trong tập kiểm thử |
| 10-03-validation-protocol.vi.md | 19 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | lượt đăng ký học kiểm thử | lượt đăng ký học trong tập kiểm thử |
| 10-03-validation-protocol.vi.md | 44 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | \| Quy mô kỳ mở kiểm thử, | \| Quy mô kỳ mở của tập kiểm thử, |
| 10-03-validation-protocol.vi.md | 46 | Glossary "mức co hệ số kỳ vọng", "mức lạc quan"; "nguy cơ chung" as in 04-02 | hệ số co (shrinkage) kỳ vọng ít nhất 0,9; độ lạc quan của R² Nagelkerke không quá 0,05; nguy cơ tổng thể được | mức co hệ số kỳ vọng ít nhất 0,9; mức lạc quan của R² Nagelkerke không quá 0,05; nguy cơ chung được |
| 10-03-validation-protocol.vi.md | 46 | Milestone 4 form "biến dự báo chính / bộ biến dự báo mở rộng" | mức cần thiết cho nhóm biến chính | mức cần thiết cho bộ biến dự báo chính |
| 10-04-fairness-spec.vi.md | 3 | English gloss repeated after its first use in document order | trong các kỳ mở kiểm thử; cách làm này gọi là phân tích theo từng nhóm con (slicing analysis) [34] | trong các kỳ mở của tập kiểm thử; cách làm này gọi là phân tích theo từng nhóm con [34] |
| 10-04-fairness-spec.vi.md | 3 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | trước khi mở bất kỳ kết quả kiểm thử nào. | trước khi mở bất kỳ kết quả nào của tập kiểm thử. |
| 10-04-fairness-spec.vi.md | 7 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | \| Lượt đăng ký học kiểm thử \| Kỳ mở kiểm thử nhỏ nhất \| | \| Lượt đăng ký học trong tập kiểm thử \| Kỳ mở nhỏ nhất của tập kiểm thử \| |
| 10-04-fairness-spec.vi.md | 15 | English gloss repeated after its first use in document order | giữa các nhóm (separation), đo bằng | giữa các nhóm, đo bằng |
| 10-04-fairness-spec.vi.md | 21 | English label "(separation)" rendered in Vietnamese; gloss already given at first use (04-04) | \| Kiểm định khẳng định về công bằng (separation) \| | \| Kiểm định khẳng định về công bằng (ngang bằng tỷ lệ phát hiện) \| |
| 10-04-fairness-spec.vi.md | 21 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | lượt đăng ký học kiểm thử | lượt đăng ký học trong tập kiểm thử |
| 10-04-fairness-spec.vi.md | 26 | English gloss repeated after its first use in document order | \| Kiểm tra biến thay thế (proxy) \| | \| Kiểm tra biến thay thế \| |
| 10-05-risk-register.vi.md | 17 | Test runs/enrolments: "… của tập kiểm thử", never a bare "kiểm thử" | \| 13 kỳ mở kiểm thử có quy mô | \| 13 kỳ mở của tập kiểm thử có quy mô |
| 10-05-risk-register.vi.md | 23 | English gloss repeated after its first use in document order | Kiểm tra biến thay thế (proxy) theo nhóm | Kiểm tra biến thay thế theo nhóm |
| 10-06-ai-critiques.vi.md | 3 | English gloss repeated after its first use in document order | Nhật ký quyết định về AI (AI Decision Log) ở Phần 6 | Nhật ký quyết định về AI ở Phần 6 |
| 10-06-ai-critiques.vi.md | 15 | English gloss repeated after its first use in document order | kiểm duyệt không mang thông tin (non-informative censoring) được nêu | kiểm duyệt không mang thông tin được nêu |
| 10-06-ai-critiques.vi.md | 18 | English glosses repeated after first use; criterion named in full | kiểm tra biến thay thế (proxy); nêu rõ tiêu chí chính là ngang bằng tỷ lệ phát hiện (separation) \| | kiểm tra biến thay thế; nêu rõ tiêu chí chính là tiêu chí ngang bằng tỷ lệ phát hiện \| |
| 10-07-traceability-full.vi.md | 3 | English gloss repeated after its first use in document order | Business Goal (mục tiêu của tổ chức) và KPI | Business Goal và KPI |
| 10-07-traceability-full.vi.md | 3 | English gloss repeated after its first use in document order | phương pháp cơ sở (baseline), phương pháp chính | phương pháp cơ sở, phương pháp chính |
| 00-2-glossary.vi.md | 39 | Terms page matches the body name of the AQ2 task ("đo mối liên hệ", Mục 2.2) | tổng hợp, phân tích mối liên hệ, phân loại hoặc xếp hạng | tổng hợp, đo mối liên hệ, phân loại hoặc xếp hạng |
| 00-1-abbreviations.vi.md | 18 | Abbreviation: full form matches the body (ROC is the characteristic, not the curve); check_abbreviations DEFINE | \| ROC \| Đường đặc trưng hoạt động của bộ thu – | \| ROC \| Đặc trưng hoạt động của bộ thu – |
| 10-05-risk-register.vi.md | 15 | Abbreviation already defined in 05-01; check_abbreviations REPEAT | đào tạo từ xa ở Vương quốc Anh (UK) khác | đào tạo từ xa ở UK khác |
| 10-05-risk-register.vi.md | 25 | Milestone 4 form for the noun "flag" | Nhãn bị đánh dấu đi theo sinh viên lâu dài \| Nhãn bị đánh dấu dẫn đến hoạt động hỗ trợ và hết hiệu lực | Dấu cảnh báo đi theo sinh viên lâu dài \| Sinh viên bị đánh dấu được chuyển sang hoạt động hỗ trợ; dấu cảnh báo hết hiệu lực |
| 02-01-modeling-briefs.vi.md | 46 | Milestone 4 form "bộ biến dự báo mở rộng" | phương án thay thế là bộ mở rộng gồm thêm 10 biến dự báo cùng | phương án thay thế là bộ biến dự báo mở rộng, gồm thêm 10 biến cùng |
| 04-02-validation-strategy.vi.md | 10 | Parity warning: comma before "và" | (after the scripted edit) …(cùng module và cùng tháng bắt đầu), và cho 4 kỳ mở không có cặp. | …tức là có kỳ tương ứng năm 2013 với cùng module và cùng tháng bắt đầu, cũng như cho 4 kỳ mở không có cặp. |
