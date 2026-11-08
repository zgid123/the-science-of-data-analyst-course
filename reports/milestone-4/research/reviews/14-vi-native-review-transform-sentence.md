# Vietnamese native review: predictor-transform passage (2026-11-08)

Scope: the passage added to the "Primary approach" paragraph of Section 3.3, from "A logistic model assumes that each
predictor shifts the log-odds" to "read the predictors untransformed." In the twin it closes the paragraph that begins
"Ngoài bộ biến dự báo chính, nhóm tác giả thử". All other text of the file was left as it was. Reviewer: a fresh agent,
not the translator; protocol `.claude/skills/build-report/languages/vi/review.md` (three passes, checklist section 3).
Copy of the twin before the edits: session scratchpad `03-03-predictive.vi.before.md` (throwaway).

| # | File | Line | Checklist item | Before | After |
| :---- | :---- | :---- | :---- | :---- | :---- |
| 1 | 03-03-predictive.vi.md | 9 | 3.1 One main idea, one breath; 3.2 Connectors (contrast "while") | Mô hình logistic giả định rằng mỗi biến dự báo làm log-odds của khả năng không hoàn thành thay đổi một lượng cố định khi biến đó tăng một đơn vị, trong khi hoạt động học tập có phân phối lệch mạnh: tính trên mỗi lượt đăng ký học, trung vị là 602 lượt nhấp trong cả kỳ mở; 2.503 lượt đăng ký học vượt ngưỡng trên theo khoảng tứ phân vị. | Mô hình logistic giả định rằng khi một biến dự báo tăng một đơn vị, log-odds của biến cố không hoàn thành thay đổi một lượng cố định. Tuy nhiên, hoạt động học tập có phân phối lệch mạnh: trung vị số lượt nhấp của mỗi lượt đăng ký học trong cả kỳ mở là 602, còn 2.503 lượt đăng ký học có số lượt nhấp vượt ngưỡng trên theo khoảng tứ phân vị. |
| 2 | 03-03-predictive.vi.md | 9 | 3.6 Meaning complete (odds is not a probability) | log-odds của khả năng không hoàn thành | log-odds của biến cố không hoàn thành |
| 3 | 03-03-predictive.vi.md | 9 | 3.5 Head nouns present (what lies beyond the fence) | 2.503 lượt đăng ký học vượt ngưỡng trên | 2.503 lượt đăng ký học có số lượt nhấp vượt ngưỡng trên |
| 4 | 03-03-predictive.vi.md | 9 | 3.1 Voice with intent (named actor, fewer stacked "được"); 3.1 One breath | Vì vậy, các biến dự báo được biến đổi trước khi đưa vào mô hình: các biến đếm được lấy logarit của số đếm cộng một; giá trị thiếu được điền … và được đánh dấu bằng một biến chỉ báo giá trị thiếu; mọi biến dự báo được chuẩn hóa …, để phép co hệ số tác động lên mọi hệ số trên cùng một thang đo. | Vì vậy, nhóm tác giả biến đổi các biến dự báo trước khi đưa vào mô hình: biến đếm được thay bằng logarit của số đếm cộng một; giá trị thiếu được điền … và đánh dấu bằng biến chỉ báo giá trị thiếu; mọi biến dự báo được chuẩn hóa …. Nhờ bước chuẩn hóa này, hiệu chỉnh phạt co mọi hệ số trên cùng một thang đo. |
| 5 | 03-03-predictive.vi.md | 9 | 3.3 One term per concept ("penalty" = the paragraph's "hiệu chỉnh phạt"); 3.4 Definitions at first need | để phép co hệ số tác động lên mọi hệ số | hiệu chỉnh phạt co mọi hệ số (the term "phép co hệ số (shrinkage)" stays at its glossed first use in the paragraph "Rủi ro cần kiểm tra…") |
| 6 | 03-03-predictive.vi.md | 9 | 3.3 Glossary forms ("test set" never a bare "kiểm thử"); 3.5 No "chúng" | không dòng dữ liệu kiểm thử nào làm thay đổi chúng | không dòng nào của tập kiểm thử làm thay đổi các phép biến đổi đó |
| 7 | 03-03-predictive.vi.md | 9 | 3.1 One breath (split at "; here"); 3.1 Named actor | …; trong báo cáo này, các phép biến đổi được ước lượng lại trong từng fold (Mục 4.2), còn … | Trong báo cáo này, nhóm tác giả ước lượng lại các phép biến đổi trong từng fold … (new sentence) |
| 8 | 03-03-predictive.vi.md | 9 | 3.3 Glossary forms, first use in the file ("fold", "gradient-boosted trees") | từng fold (Mục 4.2), còn cây tăng cường độ dốc đọc trực tiếp | từng fold (phần chia trong kiểm định chéo, Mục 4.2); riêng cây tăng cường độ dốc (gradient-boosted trees) dùng trực tiếp |
| 9 | 03-03-predictive.vi.md | 9 | 3.5 Plain actions over images ("read" a predictor) | đọc trực tiếp các biến dự báo chưa biến đổi | dùng trực tiếp các biến dự báo chưa biến đổi |

Kept on purpose: "log-odds" stays in English, as everywhere else in the report (Sections 3.2, 4.3, 10.2 and the terms
page); "biến dự báo", "lượt đăng ký học", "kỳ mở", "biến chỉ báo giá trị thiếu", "ngưỡng trên theo khoảng tứ phân vị",
"ước lượng" for fit and "chuẩn hóa" for standardise follow the glossary. Numbers checked against the English: 602, 2.503,
2013, Mục 4.2.

Open for the glossary (not edited here): "log-odds" has no row (the report keeps it in English); "standardise
(with the training mean and standard deviation)" has only the row "scaling → phép chuẩn hóa thang đo"; "penalty (of a
penalised model)" has no row ("hiệu chỉnh phạt" used here, from "penalised logistic regression"); "interquartile-range
fence" matches the row "upper interquartile fence".

Closing line: 03-03-predictive.vi.md reviewed (new passage only), 9 findings fixed, `check_parity.py` 0 errors and
0 warnings; `translation_status.py --mark` recorded.
