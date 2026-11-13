## Phụ lục VII – Chi tiết bổ sung cho nội dung chính

Phụ lục này trình bày chi tiết làm cơ sở cho một số mục của nội dung chính, lần lượt theo thứ tự các phần: những lý do và bước thực hiện mà nội dung chính chỉ nêu tóm tắt, mỗi mục ghi rõ mục mà nó bổ sung.

### 1. Chốt phiên bản cơ sở, phạm vi và các điều chỉnh có kiểm soát

Mục này trình bày chi tiết làm cơ sở cho Mục 1.1 và Mục 1.2: lý do và cách nhóm chốt phiên bản cơ sở của Milestone 1; cách công việc của Milestone 2 đi theo các bước của đề bài; nội dung thay đổi của từng điều chỉnh trong tám điều chỉnh có kiểm soát.

**Lý do chốt phiên bản cơ sở.** Đề bài yêu cầu nhóm bắt đầu Milestone 2 từ đề xuất chứ không phải từ một bộ dữ liệu: các câu hỏi quyết định cần những dữ liệu nào, còn dữ liệu không được âm thầm làm thay đổi các câu hỏi [1]. Vì vậy, trước khi xem xét bất kỳ bộ dữ liệu nào, nhóm đã chốt phiên bản cơ sở của Milestone 1. Mục tiêu, các chỉ số, câu hỏi, nhu cầu dữ liệu và quyết định của đề xuất được sao chép nguyên văn vào một bản ghi phiên bản cơ sở. Đồng thời, nhóm ghi lại mã kiểm tra (checksum, dấu vân tay của đúng nội dung trong một tệp) cho từng tệp nguồn; nhờ đó, mọi khác biệt về sau giữa đề xuất và báo cáo này đều hiện rõ và phải được giải thích (Phụ lục V). Mọi thay đổi mà dữ liệu đòi hỏi được ghi trong nhật ký thay đổi có kiểm soát (Controlled Change Log), là thuật ngữ đề bài dùng cho danh sách các thay đổi kèm lý do [1].

**Công việc của Milestone 2.** Xuất phát từ phiên bản cơ sở đã chốt, Milestone 2 trả lời hai câu hỏi mà đề bài đặt ra: bốn AQ cần những dữ liệu nào; bộ dữ liệu mở mà nhóm thu thập có thực sự cung cấp các dữ liệu đó hay không [1]. Công việc đi theo các bước của đề bài. Mục 2 chuyển mỗi câu hỏi thành một yêu cầu dữ liệu. Mục 3 mô tả quá trình tìm kiếm các bộ dữ liệu mở ứng viên; tiếp theo, Mục 4 chấm điểm các bộ dữ liệu ứng viên và chọn một bộ. Mục 5 ghi lại cách thu thập bộ dữ liệu được chọn để bất kỳ ai cũng có thể thu thập lại; Mục 6 kiểm tra các tệp đã thu thập có đọc được và có khớp với tài liệu mô tả hay không. Sau đó, Mục 7 đối chiếu từng câu hỏi với các tệp và biến thực tế, đồng thời nêu rõ mỗi câu hỏi trả lời được đến đâu. Mục 8 và Mục 9 trình bày các rủi ro và việc sử dụng AI tạo sinh. Theo yêu cầu của đề bài, các bước làm sạch dữ liệu, điền giá trị thiếu, tạo đặc trưng và huấn luyện mô hình thuộc các Milestone sau [1].

**Những thay đổi do dữ liệu đòi hỏi.** Bộ dữ liệu được chọn là OULAD. Bộ dữ liệu này mô tả các module đào tạo từ xa của một trường đại học ở UK, chứ không phải các học phần của một chương trình đào tạo ở Việt Nam; vì vậy, không thể trả lời các câu hỏi trên OULAD đúng như cách đề xuất đã đặt ra. Nhóm đã ghi lại tám điều chỉnh có kiểm soát, từ C01 đến C08; mỗi điều chỉnh kèm nội dung cũ và nội dung mới, bằng chứng dữ liệu làm căn cứ và tác động đến các câu hỏi, KPI và quyết định. Bốn điều chỉnh quan trọng nhất như sau. OULAD là bộ dữ liệu thay thế cho các học phần của nhà trường trong phân tích, còn hồ sơ của chính nhà trường vẫn là đối tượng hướng tới của đợt thí điểm (C01). Học kỳ được thay bằng kỳ mở module (một lần mở module, kéo dài tám đến chín tháng), với thời gian tính theo số ngày kể từ ngày bắt đầu kỳ mở (C02). Các so sánh theo hình thức học và năm theo học bị bỏ, vì OULAD không có hai thông tin này (C04). Phần hành động của AQ4 (sổ ghi các lần liên hệ và kết quả) vẫn là yêu cầu đối với đợt thí điểm, do không bộ dữ liệu mở nào ghi nhận thông tin này (C08). Bốn điều chỉnh còn lại gồm: điều chỉnh mẫu số của KPI theo khoảng thời gian đăng ký của OULAD (C03); bỏ dấu hiệu chuyên cần (C05); lập danh sách tuần 3 chỉ từ dữ liệu hoạt động và điều chỉnh quy tắc dấu hiệu sớm theo lịch của OULAD (C06); và kiểm tra AQ3 trên các kỳ mở năm 2014 của từng module (C07). Mục 7.2 giải thích từng điều chỉnh, còn Phụ lục V (Bảng A.9) trình bày toàn bộ nhật ký thay đổi.

### 2. Yêu cầu dữ liệu theo cấp độ phân tích

Mục này trình bày chi tiết làm cơ sở cho Mục 2.2: bốn câu hỏi đi dần lên qua các cấp độ phân tích và mỗi cấp độ cần một loại bằng chứng khác [1]. Bảng A.13 trình bày dữ liệu tối thiểu của từng cấp độ, cùng những gì dữ liệu đó có thể và không thể cho thấy.

**Bảng A.13. Yêu cầu dữ liệu theo cấp độ phân tích**

| Cấp độ | AQ | Dữ liệu tối thiểu | Những gì dữ liệu có thể cho thấy |
| :---- | :---- | :---- | :---- |
| Mô tả | AQ1 | Biến kết quả; thông tin học phần và học kỳ để phân nhóm; bài được chấm điểm có ngày; mẫu số là sinh viên còn theo học sau thời gian điều chỉnh đăng ký học phần | Các tỷ lệ và thời điểm sinh viên lần đầu bỏ lỡ bài |
| Chẩn đoán | AQ2 | Dữ liệu của AQ1, thêm các dấu hiệu có ngày và nhóm so sánh, cùng đặc điểm cá nhân để kiểm tra tính nhất quán giữa các nhóm | Mối liên hệ, không phải nguyên nhân |
| Dự báo | AQ3 | Biến kết quả đã gán nhãn; các đặc trưng có dấu thời gian trước thời điểm dự báo; đủ số học kỳ để kiểm tra trên một học kỳ sau đó | Chất lượng dự báo đo trên một học kỳ sau đó, với danh sách có độ dài cố định |
| Chỉ định | AQ4 | Hành động (các lần liên hệ), ràng buộc (số sinh viên cán bộ liên hệ được mỗi tuần) và kết quả sau hành động | Thứ tự ưu tiên trong các ràng buộc; nếu thiếu dữ liệu về hành động và kết quả thì không thể khẳng định việc liên hệ giúp ích cho sinh viên |

### 3. Quy tắc áp dụng cho mọi kết quả và so sánh ban đầu giữa các ứng viên

Mục này trình bày chi tiết làm cơ sở cho Mục 3: các quy tắc áp dụng cho mọi bộ dữ liệu tìm được; những gì bản tóm tắt bảy ứng viên trong Bảng 3.1 đã cho thấy trước bước chấm điểm ở Mục 4.

**Ba quy tắc cho mọi kết quả.** Theo yêu cầu của đề bài, nhóm áp dụng ba quy tắc cho mọi bộ dữ liệu tìm được [1]. Thứ nhất, nhóm đọc tài liệu mô tả và giấy phép trước khi đánh giá dữ liệu. Thứ hai, bộ dữ liệu tìm thấy trên Kaggle, trên blog hoặc ở một bản sao khác được truy nguyên về nhà cung cấp đã công bố bộ dữ liệu đó. Thứ ba, các bản đăng lại không rõ nguồn gốc bị loại.

Bảng 3.1 đã cho thấy điểm khác biệt chính giữa các ứng viên. Chỉ OULAD và dữ liệu XuetangX ghi lại thời điểm sinh viên thực hiện từng hoạt động trong khóa học, là thông tin AQ2 và AQ3 cần đến. Ngoài ra, chỉ OULAD kết hợp thông tin thời gian đó với biến kết quả có ghi nhận việc rút khỏi module và với các bài được chấm điểm có ngày. Mục 4 kiểm tra nhận định ban đầu này bằng các điều kiện bắt buộc và các tiêu chí của đề bài.

### 4. Lý do loại từng ứng viên

Mục này trình bày chi tiết làm cơ sở cho Mục 4.2: lý do loại từng ứng viên ngoài OULAD, kèm các thông tin từ trang chính thức hoặc bài mô tả dữ liệu làm căn cứ cho những điều kiện bắt buộc mà ứng viên đó không đạt trong Bảng 4.1.

**Lý do loại các ứng viên khác.** Mọi ứng viên còn lại đều không đạt ít nhất điều kiện về biến kết quả (G1) và điều kiện về bài được chấm điểm có ngày (G2a). UCI 697 gán nhãn cho sinh viên theo kết quả của cả chương trình đào tạo sau ba hoặc bốn năm chứ không theo học phần; bộ dữ liệu này cũng chỉ có số liệu gộp theo học kỳ, nên không cho biết sinh viên ngừng học vào thời điểm nào trong học phần [4], [5]. UCI 320 và UCI 856 mô tả học sinh trung học hoặc một bảng hỏi duy nhất, có điểm số nhưng không có thông tin rút học phần, cũng không có bài được chấm điểm hoặc hoạt động kèm ngày [6], [7]. Dữ liệu XuetangX có ghi hoạt động kèm ngày, nhưng biến kết quả chỉ là nhãn bỏ học dạng có hoặc không, không phân biệt đạt với trượt; tài liệu cũng không nêu giấy phép [8]. HarvardX chỉ ghi lần hoạt động đầu tiên và cuối cùng của mỗi người học và không có giấy phép mở [10]; còn xAPI-Edu-Data không có bản ghi kèm ngày và chỉ được biết đến qua một trang giới thiệu trên Kaggle [11].

### 5. Các bảng, tên cột và bằng chứng liên kết của OULAD

Mục này trình bày chi tiết làm cơ sở cho Mục 6: nội dung của từng bảng trong bảy bảng của OULAD; ý nghĩa của các tên cột dùng trong Bảng 6.1 và Mục 7; các số liệu cho thấy mã định danh của sinh viên được giữ nguyên qua các kỳ mở module.

Bảy bảng của OULAD chia dữ liệu như sau: courses liệt kê các kỳ mở module; assessments liệt kê các bài được chấm điểm của từng kỳ mở cùng ngày đến hạn; vle liệt kê các trang của VLE; studentInfo có một dòng cho mỗi lượt đăng ký học của một sinh viên trong một kỳ mở module, kèm đặc điểm cá nhân và kết quả cuối cùng; studentRegistration ghi ngày đăng ký của từng lượt đăng ký học và ngày hủy đăng ký nếu có; studentAssessment ghi từng bài đã nộp kèm ngày nộp và điểm; studentVle ghi số lượt nhấp theo ngày của từng sinh viên trên từng trang.

Bảng 6.1 và Mục 7 dùng một số tên cột. Trong studentInfo, final_result là biến kết quả, trong đó Distinction là đạt loại xuất sắc, nên hoàn thành nghĩa là Pass hoặc Distinction; imd_band là mức khó khăn kinh tế – xã hội của khu vực cư trú của sinh viên; num_of_prev_attempts là số lần sinh viên đã học cùng module trước đó; studied_credits là số tín chỉ sinh viên đăng ký trong kỳ mở đó. Trong studentVle, sum_click là số lượt nhấp vào một trang trong một ngày, còn id_site và activity_type xác định trang và loại trang. Ngoài ra, code_module và code_presentation là mã module và mã kỳ mở, còn assessment_type phân biệt bài do giảng viên hướng dẫn chấm, bài do máy tính chấm và bài thi.

Mã định danh sinh viên được giữ nguyên qua các kỳ mở, nên điều kiện về liên kết G5 được đáp ứng. OULAD có 32.593 lượt đăng ký học của 28.785 sinh viên; trong đó 3.538 sinh viên xuất hiện ở nhiều hơn một kỳ mở module. Ở cả 1.309 trường hợp một sinh viên đăng ký lại cùng một module, số lần đã học trước đó được ghi đều tăng lên. Số lần này chỉ có thể tăng nếu cùng một mã định danh ứng với cùng một sinh viên ở mọi kỳ mở.

### 6. Giới hạn của AQ3 và KPI phụ 1 trên OULAD

Mục này trình bày chi tiết làm cơ sở cho Mục 7.2: ba giới hạn đi kèm khi giữ AQ3; cách đo quy tắc dấu hiệu sớm của KPI phụ 1 trên OULAD.

**AQ3.** Câu hỏi dự báo giữ biến cần dự đoán, hai thời điểm chốt dữ liệu và bước kiểm thử trên kỳ mở module muộn hơn, kèm ba giới hạn. Thứ nhất, trước khi hết tuần 2, gần như không kỳ mở nào có bài được chấm điểm đến hạn, nên danh sách tuần 3 chỉ dựa trên hoạt động (C06). Thứ hai, mỗi cặp module và tháng bắt đầu có tối đa một kỳ mở sớm hơn để học, nên phương pháp được huấn luyện trên các kỳ mở năm 2013 và kiểm thử trên các kỳ mở năm 2014 của 9 cặp module và tháng bắt đầu có cả hai năm (C07). Module CCC và các kỳ mở tháng 2 của EEE và GGG không có kỳ mở sớm hơn cùng tháng bắt đầu; do đó, các kỳ mở này dùng được để kiểm thử phương pháp đã huấn luyện trên các kỳ mở khác, nhưng không dùng được để huấn luyện phương pháp riêng cho chính chúng. Thứ ba, không thể so sánh sinh viên năm nhất với sinh viên các năm trên, nên phép so sánh này được thay bằng phép kiểm tra theo mức khó khăn kinh tế – xã hội của khu vực cư trú và tình trạng khuyết tật, là hai thông tin OULAD có ghi nhận (C04). Ngoài ra, OULAD không ghi ngày công bố điểm, nên điểm của các bài được chấm điểm không được dùng làm đặc trưng cho danh sách nào; theo yêu cầu của Bảng 2.2, nhóm chỉ dùng thông tin sinh viên có nộp bài hay không và nộp vào lúc nào.

**KPI phụ 1.** Quy tắc dấu hiệu sớm đòi hỏi bỏ lỡ hoặc nộp trễ từ hai bài được chấm điểm trở lên tính đến hết tuần 4, nhưng chỉ 1 trong 22 kỳ mở module có hai bài đến hạn trong khoảng thời gian đó. Vì vậy, trên OULAD, phần dấu hiệu của KPI này được đo bằng một bài bị bỏ lỡ hoặc nộp trễ, trong 16 kỳ mở có bài đến hạn tính đến hết tuần 4; đây là sai lệch được nêu rõ và ghi nhận cùng C06. Quy tắc như đã định nghĩa vẫn là thước đo cho các học phần của trường; đợt thí điểm sẽ kiểm tra lịch đánh giá của các học phần này.
