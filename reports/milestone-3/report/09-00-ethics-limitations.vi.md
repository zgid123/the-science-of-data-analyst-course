# 9. Đạo đức, thiên lệch và hạn chế

**Các thuộc tính nhạy cảm được giữ để kiểm tra công bằng.** Dữ liệu đã chuẩn bị giữ giới tính, nhóm tuổi, tình trạng
khuyết tật do sinh viên tự khai, mức khó khăn của khu vực và vùng cư trú trong mọi bảng, nằm ngoài cả nhóm đặc trưng chính lẫn nhóm đặc trưng mở rộng,
vì bước kiểm tra công bằng cần đến các thuộc tính này. Thiên lệch thuật toán trong giáo dục là hiện tượng một mô hình dự
báo tốt hơn hoặc kém hơn đáng kể cho một nhóm sinh viên so với nhóm khác. Thiên lệch này có thể phát sinh qua các biến
thay thế (proxy) ngay cả khi mô hình không dùng thuộc tính nhân khẩu học nào làm đầu vào. Ngoài ra, nếu bộ dữ liệu không ghi
mỗi sinh viên thuộc nhóm nào thì hoàn toàn không thể kiểm tra công bằng [14]. Do đó, bỏ các thuộc tính này đi chỉ che giấu thiên lệch chứ không
ngăn được thiên lệch. Đề bài cũng cho phép giữ các thuộc tính nhạy cảm để kiểm tra, đồng thời hạn chế dùng chúng làm
đặc trưng [1]. Riêng trình độ học vấn cao nhất, thuộc tính thứ sáu nêu ở Mục 2.3, được dùng làm đặc trưng, vì bằng cấp mà sinh viên có trước
khi vào học phản ánh mức độ chuẩn bị của sinh viên cho module. Thuộc tính này cũng có mặt trong mọi bảng, nên các nhóm trình độ
vẫn được kiểm tra công bằng. Có nên đưa cả năm thuộc tính dùng để kiểm tra công bằng vào nhóm đặc trưng hay không là quyết định về chính sách. Milestone 4 xem xét lựa chọn này bằng cách so sánh mô hình có và không có các thuộc tính đó.

**Kết quả của các nghiên cứu trước trên OULAD.** Một nghiên cứu về tính công bằng trên OULAD có bốn phát hiện: sinh viên tự khai có khuyết tật chiếm tỷ lệ rất thấp trong dữ liệu; chênh lệch tác động (disparate impact) từ 5 đến 6 điểm phần trăm,
nghiêng về sinh viên nam, được hầu hết các mô hình tái tạo lại; bỏ các thuộc tính nhạy cảm ra khỏi mô hình hầu như không cải thiện
tính công bằng; trong một số trường hợp, sinh viên khuyết tật bị dự báo trượt với xác suất cao hơn [15]. Nhóm thiết kế bước kiểm tra công bằng của dự án dựa trên những phát hiện này. Quy mô các nhóm cần kiểm tra công bằng đã biết trước:
3.164 lượt đăng ký học có tình trạng khuyết tật do sinh viên tự khai và chỉ 216 lượt đăng ký học của sinh viên từ 55 tuổi trở lên. Nhờ biết trước quy mô này, nhóm xác định được nhóm nào quá nhỏ khi xét riêng từng kỳ mở; các nhóm nhỏ như vậy được kiểm tra gộp trên mọi kỳ mở thay vì theo từng kỳ mở. Nhóm có mức khó khăn "Missing" được báo
cáo riêng, vì sinh viên trong nhóm này có tỷ lệ hoàn thành cao hơn (Mục 3.2); gộp nhóm này vào một mức khác sẽ làm sai
lệch tỷ lệ của mức đó.

**Quyền riêng tư.** Quy định về quyền riêng tư áp dụng ở hai cấp. OULAD đã được ẩn danh theo chuẩn k-ẩn danh
(k-anonymity) với k = 5, nghĩa là mỗi tổ hợp thuộc tính có thể dùng để nhận diện một sinh viên đều xuất hiện ở ít nhất năm sinh viên [2]. Theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 của Việt Nam, dữ liệu đã khử định danh nằm ngoài định
nghĩa dữ liệu cá nhân và hành vi tái định danh dữ liệu đó bị cấm [16]; vì vậy, nhóm không liên kết OULAD với bất kỳ nguồn dữ liệu nào khác. Đợt thí điểm dùng hồ sơ của chính trường phải tuân theo các quy định chặt chẽ hơn về dữ liệu cá nhân nhạy cảm, như tình trạng khuyết tật do sinh viên tự khai [17] và cần có cơ sở pháp lý riêng trước khi chuẩn bị bất kỳ hồ sơ sinh viên nào (Phụ lục I).

**Giới hạn của các nhận định.** Dữ liệu đặt ra bốn giới hạn cho các nhận định. Thứ nhất, các kết quả mô tả các module đào tạo từ xa tại UK trong giai đoạn 2013–2014 và phải được kiểm tra lại trên hồ sơ của trường trước khi dùng làm căn cứ cho một quyết định.
Thứ hai, các mối liên hệ trong AQ2 không phải quan hệ nhân quả: một dấu hiệu đi kèm việc không hoàn thành có thể là biểu
hiện của cùng một khó khăn chứ không phải nguyên nhân gây ra khó khăn đó. Thứ ba, OULAD không cho phép rút ra tác động
nào của việc liên hệ sinh viên, vì bộ dữ liệu không ghi nhận lượt liên hệ nào. Thứ tư, các mức khó khăn của khu vực không
được gộp giữa các xứ thuộc UK, vì mỗi xứ dùng chỉ số riêng [6].
