# Rewrite A – Vietnamese twins 00-1 to 04-02 after the reader test

Date: 2026-11-06. Scope: `00-1`, `00-2`, `01-00`, `01-01`, `01-02`, `02-00`, `02-01`, `02-02`, `02-03`, `03-00`, `04-00`,
`04-01`, `04-02` (`*.vi.md` in `reports/milestone-2/report/`). Every twin was rewritten from its English source
(lessons T5), not patched; stale twins (02-01, 02-03, 04-01, 04-02) were brought in line with the current English.
Line numbers below are those of the rewritten twins.

## Findings fixed

| # | File:line | Before | After |
| :-- | :-- | :-- | :-- |
| 1 | 00-1-abbreviations.vi.md:12 | "Message Digest 5 \| Mã kiểm tra do nhà cung cấp đưa ra và được ghi trong manifest" | "Thuật toán tóm lược thông điệp 5 – Message Digest 5 \| Mã kiểm tra (checksum) do nơi phát hành cung cấp. Nhóm ghi mã này vào manifest, là danh sách các tệp đã thu thập kèm mã kiểm tra của từng tệp" (also Vietnamese expansions added for OULAD, SHA-256, UCI) |
| 2 | 00-2-glossary.vi.md:12 | "Module run (presentation) – Đợt mở học phần \| Một lần mở một module của OULAD, … "học phần" chỉ học phần của trường" | "Module run (presentation) – Lượt mở module \| Một lần tổ chức một module của OULAD. … Trong báo cáo, "học phần" chỉ dùng cho học phần của trường đại học" |
| 3 | 01-01-frozen-baseline.vi.md:3 | "vì chính các câu hỏi, chứ không phải dữ liệu, quyết định cần thu thập những gì" | "vì dữ liệu cần thu thập phải xuất phát từ các câu hỏi, không phải từ dữ liệu sẵn có" |
| 4 | 01-01-frozen-baseline.vi.md:5 | "Business Goal (mục tiêu của tổ chức)" | Kept: the task brief says Business Goal stays as the brief writes it, with the glossary's first-use gloss; the sentence was split so the term carries one idea |
| 5 | 01-01-frozen-baseline.vi.md:5 | "KPI phụ 1 là tỷ lệ liên hệ sinh viên có dấu hiệu sớm; KPI phụ 2 là tỷ lệ liên hệ kịp thời" | Each KPI now names its group and denominator: "trong số sinh viên bỏ lỡ hoặc nộp trễ từ hai bài được chấm điểm trở lên tính đến hết tuần 4, bao nhiêu phần trăm được liên hệ trước khi hết tuần 5"; "trong số sinh viên có tên trong danh sách liên hệ, bao nhiêu phần trăm được liên hệ trong vòng bảy ngày sau khi danh sách được gửi" (definitions from milestone-1 `03-03-kpis.md`) |
| 6 | 01-01-frozen-baseline.vi.md:5 | "giống cách Thông tư 83/2026 của Việt Nam thống kê số sinh viên thôi học" | "giống cách Thông tư 83/2026 thống kê sinh viên thôi học" |
| 7 | 01-01-frozen-baseline.vi.md:13 | "D2; các lý do hiển thị trong D1" | "D2; lý do cụ thể ghi cạnh mỗi tên trong danh sách liên hệ (D1)" |
| 8 | 01-01-frozen-baseline.vi.md:14 | "so với quy tắc đơn giản" | "khi so với một quy tắc đơn giản dựa trên kết quả các bài được chấm điểm" (milestone-1 `05-00-analytic-approach.md`: continuous-assessment results) |
| 9 | 01-01-frozen-baseline.vi.md:15 | "trong giới hạn số sinh viên cán bộ liên hệ được mỗi tuần và yêu cầu công bằng" | "trong giới hạn số lượt liên hệ tối đa mỗi tuần của cán bộ và yêu cầu đối xử công bằng giữa các nhóm sinh viên" |
| 10 | 01-02-scope-change-log.vi.md:5 | "Thứ nhất, tổng thể thay đổi:" | "Thứ nhất, tổng thể nghiên cứu thay đổi:" |
| 11 | 01-02-scope-change-log.vi.md:5 | "phần hành động của AQ4 vẫn là yêu cầu dành cho đợt thí điểm, vì không bộ dữ liệu mở nào ghi nhận phần này" | "phần của AQ4 về việc liên hệ sinh viên (liên hệ ai, liên hệ thế nào và kết quả sau đó) chưa được phân tích ở Milestone này; phần này được giữ làm yêu cầu dữ liệu cho đợt thí điểm, vì không bộ dữ liệu mở nào ghi nhận các lần liên hệ" |
| 12 | 01-02-scope-change-log.vi.md:5 | "các thay đổi này chỉ thu hẹp mức độ mà từng câu hỏi trả lời được trên dữ liệu mở" | "Các thay đổi này chỉ làm hẹp phần mà mỗi câu hỏi trả lời được bằng dữ liệu mở." |
| 13 | 02-00-data-requirements.vi.md:3 | "Các yêu cầu được phát biểu bằng khái niệm, không dùng tên cột của một bộ dữ liệu đang có trong tay" | "Các yêu cầu được nêu ở mức khái niệm, không gắn với tên cột của một bộ dữ liệu có sẵn" |
| 14 | 02-01-aq-data-matrix.vi.md:10 | "tuần sinh viên lần đầu bỏ lỡ bài được chấm điểm, ở cả hai nhóm" | "tuần sinh viên lần đầu bỏ lỡ một bài được chấm điểm, tính riêng cho nhóm sinh viên đạt và nhóm sinh viên không đạt" |
| 15 | 02-01-aq-data-matrix.vi.md:11 | "Chênh lệch tỷ lệ sinh viên về sau không hoàn thành học phần giữa sinh viên có và không có từng dấu hiệu" | "Với từng dấu hiệu: tỷ lệ về sau không hoàn thành học phần ở nhóm sinh viên có dấu hiệu, so với nhóm không có dấu hiệu" |
| 16 | 02-01-aq-data-matrix.vi.md:12 | "thông tin nền có tại thời điểm đăng ký" | "đặc điểm cá nhân đã biết khi đăng ký" |
| 17 | 02-01-aq-data-matrix.vi.md:13 | "độ chính xác của danh sách (precision) trong giới hạn số sinh viên cán bộ liên hệ được" | "độ chính xác của danh sách (precision) khi danh sách không vượt quá số lượt liên hệ tối đa mỗi tuần"; "độ chính xác" now appears only here, as precision; accuracy elsewhere is "chất lượng dự báo" |
| 18 | 02-01-aq-data-matrix.vi.md:15 | "những vế câu hỏi dựa vào các biến đó chuyển sang mức đáp ứng một phần (Partial)" | "những phần câu hỏi cần đến chúng chỉ được đáp ứng một phần (Partial)" |
| 19 | 02-01-aq-data-matrix.vi.md:15 | "sáu điều kiện bắt buộc …, từ G1 đến G5, trong đó G2 gồm hai phần" | "sáu điều kiện bắt buộc cho mọi bộ dữ liệu ứng viên. Các điều kiện mang mã từ G1 đến G5, riêng G2 tách thành hai điều kiện G2a và G2b" |
| 20 | 02-01-aq-data-matrix.vi.md:20 | "có một đợt muộn hơn để kiểm thử" | "ít nhất ba lượt tổ chức của cùng các học phần, … trong đó có một lượt muộn hơn để đánh giá mô hình" |
| 21 | 02-02-requirements-by-level.vi.md:10 | "kèm thông tin nền để kiểm tra độ nhất quán giữa các nhóm" | "đặc điểm cá nhân để kiểm tra mức độ liên quan có giống nhau ở từng nhóm sinh viên hay không" |
| 22 | 02-02-requirements-by-level.vi.md:11 | "đủ số học kỳ để đánh giá trên một học kỳ sau" / "Độ chính xác trên một học kỳ sau, …" | "đủ số học kỳ để huấn luyện trên các học kỳ trước và đánh giá trên một học kỳ sau" / "Chất lượng dự báo trên một học kỳ sau (học kỳ không dùng để huấn luyện), với độ dài danh sách cố định" |
| 23 | 02-02-requirements-by-level.vi.md:14 | "thay vì đưa ra một khuyến nghị dưới danh nghĩa phân tích chỉ định" | "thay vì đưa ra một khuyến nghị rồi gọi đó là phân tích chỉ định" |
| 24 | 02-02-requirements-by-level.vi.md:16 | "chỉ để kiểm tra mức độ liên quan và độ chính xác có giữ được giữa các nhóm hay không" | "Các đặc điểm này chỉ dùng để kiểm tra xem mức độ liên quan và chất lượng dự báo có như nhau ở các nhóm sinh viên hay không" |
| 25 | 02-02-requirements-by-level.vi.md:16 | "mức thiếu thốn của khu vực sinh viên cư trú" | "mức khó khăn kinh tế – xã hội của khu vực sinh viên cư trú" (differs from the topic glossary row "deprivation band"; see open term below) |
| 26 | 02-02-requirements-by-level.vi.md:16 | "không bao giờ dùng để chấm điểm" | "Nhà trường chỉ dùng các dữ liệu này để hỗ trợ sinh viên theo mục đích đã nêu, không bao giờ dùng để đánh giá kết quả học tập của sinh viên" |
| 27 | 02-03-prediction-point-leakage.vi.md:3 | "những trường nào sẽ làm rò rỉ thông tin từ sau thời điểm chốt dữ liệu" | "những biến nào sẽ làm lộ thông tin chỉ có sau thời điểm chốt dữ liệu"; column header "Trường không có sẵn" → "Biến chưa có tại thời điểm dự báo" |
| 28 | 02-03-prediction-point-leakage.vi.md:11 | "… phép mã hóa chỉ được ước lượng trên các học kỳ huấn luyện, tính đến thời điểm chốt dữ liệu" | "Giá trị trung bình theo học phần, phép chuẩn hóa thang đo và phép mã hóa biến phân loại, chỉ được ước lượng trên các học kỳ dùng để huấn luyện và chỉ với dữ liệu đến thời điểm chốt" |
| 29 | 02-03-prediction-point-leakage.vi.md:11 | "được ước lượng trên tất cả các học kỳ hoặc trên toàn bộ học kỳ" | "được tính cả trên sinh viên của học kỳ dùng để đánh giá hoặc cả trên dữ liệu của những ngày sau thời điểm chốt" |
| 30 | 02-03-prediction-point-leakage.vi.md:13 | "bảo đảm lần rút học phần của sinh viên không bị tính thành dấu hiệu báo trước chính lần rút đó" | "hai quy tắc bảo đảm rằng việc sinh viên rút học phần không bị tính thành dấu hiệu dự báo chính việc rút đó. … một bài chỉ được tính là bỏ lỡ khi ngày đến hạn của bài nằm trước ngày sinh viên rút học phần; bài đến hạn sau ngày rút không được tính" |
| 31 | 02-03-prediction-point-leakage.vi.md:13 | "sinh viên đã rời học phần trước thời điểm chốt dữ liệu không được tính là sinh viên mà danh sách phát hiện được" | "nếu sinh viên đã rút học phần trước thời điểm chốt dữ liệu, danh sách có tên sinh viên đó cũng không được tính là đã phát hiện đúng" |
| 32 | 03-00-search-strategy.vi.md:4 | "loại các bản tải lại không rõ nguồn gốc dữ liệu" | "nhóm loại các bản do người khác đăng tải lại mà không ghi rõ nguồn gốc dữ liệu" |
| 33 | 03-00-search-strategy.vi.md:6 | "bản sao của một bài mô tả dữ liệu nhóm đã có, địa chỉ cũ đã được thay thế, bản tải lại dữ liệu KDD Cup 2015 của bên thứ ba và metadata thứ cấp" | "Các kết quả bị loại thuộc bốn loại: bản sao của một bài mô tả dữ liệu mà nhóm đã có; địa chỉ cũ đã được nơi phát hành thay bằng địa chỉ mới; dữ liệu của cuộc thi KDD Cup 2015 do bên thứ ba đăng tải lại; trang chỉ chép lại metadata từ nguồn khác (metadata thứ cấp)" |
| 34 | 03-00-search-strategy.vi.md:15 | "Bảng hỏi [7]" | "Phiếu khảo sát, mỗi sinh viên một phiếu [7]" |
| 35 | 04-01-criteria-gates.vi.md:3 | "khả năng xử lý chất lượng dữ liệu" | "khả năng xử lý chất lượng dữ liệu, tức là các lỗi trong dữ liệu có xử lý được hay không" |
| 36 | 04-01-criteria-gates.vi.md:3 | "mức sẵn có và thời điểm có của các biến giải thích" | "mức sẵn có của các biến giải thích và thời điểm các biến này được ghi nhận" |
| 37 | 04-01-criteria-gates.vi.md:6 | "G1 bảo đảm có biến kết quả và ngày ghi nhận kết quả" | "G1 bảo đảm có biến kết quả và có ngày rút của từng sinh viên rút học phần" (matches the current English and 02-01 G1) |
| 38 | 04-02-selection-matrix.vi.md:3 | "Ma trận thể hiện tám trong mười tiêu chí theo các cột của đề bài. Tổng điểm còn gồm hai tiêu chí còn lại là đơn vị phân tích và độ chi tiết cùng phạm vi thời gian" | "Sáu cột tiêu chí của đề bài bao quát tám tiêu chí, vì có hai cột mỗi cột ghép hai tiêu chí: biến kết quả / thời điểm và tài liệu / giấy phép. Tổng điểm còn tính thêm hai tiêu chí không có cột riêng: tiêu chí đơn vị phân tích và độ chi tiết; tiêu chí phạm vi thời gian." (follows the current English) |
| 39 | 04-02-selection-matrix.vi.md:17 | "UCI 697 gán nhãn tình trạng theo chương trình đào tạo cho sinh viên vào cuối năm thứ ba hoặc thứ tư" | "Nhãn của UCI 697 chỉ ở cấp chương trình đào tạo và được ghi vào cuối năm thứ ba hoặc thứ tư, nên bộ dữ liệu này không có kết quả theo từng học phần" |
| 40 | 04-02-selection-matrix.vi.md:17 | "OULAD được chọn vì đây là bộ dữ liệu ứng viên duy nhất có tài liệu đáp ứng … đồng thời ghi nhận ngày rút học phần" | "Trong bảy bộ dữ liệu ứng viên, chỉ OULAD có tài liệu đáp ứng điều kiện về mốc thời gian và giấy phép, đồng thời ghi ngày rút của sinh viên. Vì vậy, nhóm chọn OULAD." |

## Glossary forms applied in every file

- OULAD units: "module", "lượt mở module" (00-2, 01-02, 03-00, 04-02); "đợt mở học phần" removed. Generic runs of a
  university course (G3, G5, 04-01) are "lượt tổ chức học phần".
- "đặc điểm cá nhân" for background attributes (02-01, 02-02, 02-03); "thông tin nền" removed.
- "số liệu gộp" for aggregates (03-00 rows B and F, 04-02); "tổng hợp" removed.
- "chất lượng dự báo" for accuracy (00-2, 02-02); "độ chính xác" only as "độ chính xác của danh sách" (02-01:13).
- "số lượt liên hệ tối đa mỗi tuần" for capacity (01-01, 02-01, 02-02, 04-02); "số sinh viên cán bộ liên hệ được" removed.
- "kiểm thử" removed (02-01 G3: "đánh giá mô hình").
- "nhóm phân tích dữ liệu" once per file, then "nhóm".

## Checks

`check_parity.py --report reports/milestone-2/report --lang vi <file>.md` on all 13 files: 0 errors, 0 warnings each
(after removing five commas before "và"/"hoặc"). Each file then recorded with `translation_status.py --mark`.

## Open term for the main session

- "deprivation band (IMD band)": the topic glossary still says "mức thiếu thốn của khu vực cư trú", which the reader
  flagged (#25 and the recurring-terms table). 02-02 now uses "mức khó khăn kinh tế – xã hội của khu vực cư trú"; the
  glossary row and the other groups' files (08-00 and later) should follow one form.
