## 2.1. Các AQ Modeling Brief

Mỗi Modeling Brief ghi lại tám thuộc tính của một câu hỏi trước khi nêu tên bất kỳ thuật toán nào: mã và nội dung câu hỏi, loại phân tích, quyết định mà câu hỏi hỗ trợ, đơn vị phân tích, biến kết quả hoặc biến mục tiêu, thông tin được phép dùng làm đầu vào và khoảng thời gian được lấy thông tin đó, đầu ra mong đợi và ràng buộc chính [1]. Bản mô tả cần nêu rõ đầu ra mong đợi, vì cùng một kết quả nhị phân có thể được báo cáo dưới dạng nhãn lớp, xác suất hoặc thứ hạng; mỗi dạng cần một thước đo chất lượng riêng [3]. Cả bốn bản mô tả đều dùng bộ dữ liệu đã chuẩn bị OULAD-N04-prepared-1.0. Trong bộ dữ liệu này, một lượt đăng ký học là một sinh viên trong một kỳ mở module; hai thời điểm chốt dữ liệu là hết ngày 13 và hết ngày 27 của kỳ mở; không hoàn thành nghĩa là kết quả cuối cùng là Không đạt (Fail) hoặc Rút khỏi module (Withdrawn).

**AQ1.** Bảng 2.1 trình bày bản mô tả của câu hỏi mô tả; câu hỏi này cần số đếm và tỷ lệ chứ không cần mô hình.

**Bảng 2.1. Modeling Brief của AQ1**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ1: Tỷ lệ lượt đăng ký học kết thúc bằng đạt, không đạt hoặc rút khỏi module là bao nhiêu, theo module, kỳ mở, tháng bắt đầu và năm; sinh viên không hoàn thành lần đầu bỏ lỡ một bài được chấm điểm vào tuần nào? |
| Loại phân tích | Mô tả |
| Quyết định được hỗ trợ | D2 (thời gian của cố vấn học tập được dành vào đâu) và D3 (có mở rộng sau đợt thí điểm hay không): lãnh đạo chương trình đào tạo thấy được module và kỳ mở nào mất nhiều sinh viên nhất và bài bị bỏ lỡ đầu tiên xuất hiện sớm đến mức nào |
| Đơn vị phân tích | Lượt đăng ký học, chỉ gồm các lượt còn hiệu lực tại ngày 14 (đây là nhóm tính KPI). Riêng khi xét bài bị bỏ lỡ đầu tiên, đơn vị phân tích là từng bài được chấm điểm |
| Biến kết quả / biến mục tiêu | Không áp dụng (không có bài toán học có giám sát); các đại lượng đo: tỷ lệ hoàn thành và không hoàn thành, tỷ trọng từng loại kết quả, tuần của bài đầu tiên đến hạn mà chưa nộp |
| Thông tin đầu vào | Bảng lượt đăng ký học (kết quả, module, kỳ mở, tháng bắt đầu, năm); bảng bài đến hạn (bài, ngày đến hạn, bài nộp); toàn bộ kỳ mở, vì câu hỏi mô tả các kỳ mở đã kết thúc |
| Đầu ra mong đợi | Bảng tỷ lệ kèm khoảng tin cậy 95% theo module, kỳ mở, tháng bắt đầu và năm; phân bố tuần có bài bị bỏ lỡ đầu tiên theo từng loại kết quả |
| Ràng buộc chính | Phải dùng đúng mẫu số (lượt đăng ký học còn hiệu lực tại ngày 14) và đúng lịch bài được chấm điểm của từng kỳ mở, vì lịch này khác nhau giữa các module. Ngoài ra, 5 module không có kết quả thi, nên bài bị bỏ lỡ đầu tiên chỉ tính bài do giảng viên hướng dẫn chấm và bài chấm bằng máy |

**AQ2.** Bảng 2.2 trình bày bản mô tả của câu hỏi chẩn đoán. Câu hỏi này đo độ mạnh của mối liên hệ giữa từng dấu hiệu và tình trạng không hoàn thành, nhưng không khẳng định rằng dấu hiệu gây ra tình trạng đó.

**Bảng 2.2. Modeling Brief của AQ2**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ2: Khi so sánh trong từng module, những dấu hiệu nào ghi nhận được tính đến hết tuần 4 (bài bị bỏ lỡ và bài nộp trễ, không hoạt động, mức hoạt động so với trung vị của kỳ mở) đi kèm với việc sinh viên về sau không hoàn thành? |
| Loại phân tích | Chẩn đoán (mối liên hệ; không khẳng định quan hệ nhân quả) |
| Quyết định được hỗ trợ | D2 và lý do đi kèm từng tên trong danh sách của D1: giảng viên hướng dẫn nên chú ý đến những dấu hiệu nào |
| Đơn vị phân tích | Lượt đăng ký học còn hiệu lực tại ngày 27 |
| Biến kết quả / biến mục tiêu | non_completion vào cuối kỳ mở, dùng làm biến kết quả của mô hình đo mối liên hệ chứ không phải biến cần dự đoán |
| Thông tin đầu vào | Các dấu hiệu tính đến hết ngày 27: có bài bị bỏ lỡ, có TMA nộp trễ, không có hoạt động trên nền tảng học tập trong bảy ngày gần nhất, tỷ lệ hoạt động so với trung vị của kỳ mở, hoạt động trước ngày bắt đầu; hiệu chỉnh theo kỳ mở module, số lần học trước và số tín chỉ đang học |
| Đầu ra mong đợi | Chênh lệch nguy cơ tính bằng điểm phần trăm kèm khoảng tin cậy 95%, ở cả dạng chưa hiệu chỉnh và dạng so sánh trong từng kỳ mở module; tỉ số odds (odds ratio) được báo cáo bên cạnh. Ngoài ra, chiều của từng mối liên hệ được nêu cho từng module |
| Ràng buộc chính | Chỉ đo mối liên hệ; bài đến hạn tính đến hết ngày 27 chỉ có ở 16 trên 22 kỳ mở; các dấu hiệu tương quan với nhau; ước lượng trên 9 kỳ mở huấn luyện năm 2013 (6 module) để kết quả của tập kiểm thử năm 2014 vẫn được giữ kín |

**AQ3.** Bảng 2.3 trình bày bản mô tả của câu hỏi dự báo; đầu ra của câu hỏi này là điểm rủi ro cho từng lượt đăng ký học tại mỗi thời điểm chốt dữ liệu.

**Bảng 2.3. Modeling Brief của AQ3**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ3: Khi mô hình xây dựng trên các kỳ mở năm 2013 được áp dụng cho các kỳ mở năm 2014, dữ liệu tính đến hết tuần 2 (ngày 13) và hết tuần 4 (ngày 27) cho phép ước lượng tình trạng không hoàn thành tốt đến đâu so với quy tắc dấu hiệu sớm? |
| Loại phân tích | Dự báo |
| Quyết định được hỗ trợ | D1 (ai có tên trong danh sách liên hệ) |
| Đơn vị phân tích | Lượt đăng ký học còn hiệu lực tại thời điểm chốt dữ liệu |
| Biến kết quả / biến mục tiêu | non_completion (Fail hoặc Withdrawn) vào cuối kỳ mở, chỉ biết được sau khi kỳ mở kết thúc |
| Thông tin đầu vào | 19 biến dự báo chính có thể dùng trong các bảng đặc trưng, tất cả đều ghi nhận tính đến hết thời điểm chốt dữ liệu. Biến điểm trung bình của bài đánh giá chấm bằng máy (CMA) bị loại, vì dưới 10% số dòng huấn luyện có giá trị này. Ngoài ra, bộ biến dự báo mở rộng được thử làm phương án thay thế: bộ này bổ sung vào các biến dự báo chính 10 biến dự báo khác và số lượt nhấp của từng tuần (2 biến tại ngày 13, 4 biến tại ngày 27) |
| Đầu ra mong đợi | Điểm rủi ro cho từng lượt đăng ký học tại mỗi thời điểm chốt dữ liệu, dùng làm thứ hạng trong kỳ mở; chỉ hiển thị dưới dạng xác suất khi mô hình được hiệu chuẩn tốt |
| Ràng buộc chính | Rò rỉ thông tin và khả năng tổng quát hóa sang kỳ mở diễn ra sau; khả năng diễn giải đối với giảng viên hướng dẫn; hiệu chuẩn; huấn luyện trên các kỳ mở năm 2013, kiểm tra một lần duy nhất trên các kỳ mở năm 2014 |

**AQ4.** Bảng 2.4 trình bày bản mô tả của câu hỏi xếp hạng. Câu hỏi này biến điểm rủi ro của AQ3 thành một danh sách có độ dài bằng số sinh viên mà cán bộ liên hệ lại được.

**Bảng 2.4. Modeling Brief của AQ4**

| Thuộc tính | Nội dung |
| :---- | :---- |
| Mã và nội dung AQ | AQ4: Với hạn mức liên hệ giả định, những lượt đăng ký học nào nên đứng đầu danh sách; danh sách đó vượt danh sách ngẫu nhiên bao nhiêu và đạt tỷ lệ phát hiện bao nhiêu, xét chung và theo mức khó khăn kinh tế – xã hội của khu vực cư trú và tình trạng khuyết tật? |
| Loại phân tích | Chỉ định (xếp hạng), ở vai trò hỗ trợ ra quyết định; việc chọn hình thức liên hệ được hoãn |
| Quyết định được hỗ trợ | D1: giảng viên hướng dẫn nhận danh sách đã xếp hạng và quyết định liên hệ với ai |
| Đơn vị phân tích | Lượt đăng ký học, xét trong kỳ mở module tương ứng |
| Biến kết quả / biến mục tiêu | Dùng biến mục tiêu của AQ3 để đánh giá danh sách; dữ liệu không có kết quả của việc liên hệ |
| Thông tin đầu vào | Điểm rủi ro của AQ3 và lý do của từng điểm; độ dài danh sách của từng kỳ mở ứng với 3 hoặc 5 sinh viên được liên hệ trên mỗi nhóm hướng dẫn giả định gồm 20 sinh viên |
| Đầu ra mong đợi | Danh sách xếp hạng cho từng kỳ mở, có độ dài theo hạn mức liên hệ, kèm các dấu hiệu giải thích vì sao từng tên có trong danh sách |
| Ràng buộc chính | Hạn mức liên hệ cố định; nguy cơ cao không đồng nghĩa với lợi ích lớn khi được liên hệ; con người ra quyết định; công bằng giữa các mức khó khăn của khu vực cư trú và giữa sinh viên có và không có khuyết tật; không khẳng định việc liên hệ có hiệu quả |

Khi đọc chung, bốn bản mô tả cho thấy các câu hỏi phụ thuộc vào nhau như thế nào. AQ3 và AQ4 dùng chung một biến mục tiêu và một phạm vi dữ liệu, nên AQ4 dùng lại điểm rủi ro của AQ3. AQ4 chỉ bổ sung một quy tắc: giữ lại phần đầu của bảng xếp hạng, với số tên đúng bằng hạn mức liên hệ. Trong khi đó, AQ1 và AQ2 mô tả các kỳ mở đã kết thúc nên không cần dự báo. Thiết kế này tương tự hệ thống cảnh báo sớm của chính OU, vốn cũng gửi cho giảng viên hướng dẫn một danh sách sinh viên có nguy cơ mỗi tuần. Tuy nhiên, hệ thống đó dự báo sinh viên có nộp bài tiếp theo hay không chứ không dự báo sinh viên có hoàn thành kỳ mở hay không [4].
