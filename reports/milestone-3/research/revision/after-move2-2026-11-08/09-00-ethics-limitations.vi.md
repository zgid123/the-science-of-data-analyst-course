# 9. Đạo đức, thiên lệch và hạn chế

Dữ liệu đã chuẩn bị giữ giới tính, nhóm tuổi, tình trạng khuyết tật, mức khó khăn của khu vực và vùng cư trú trong mọi
bảng, nằm ngoài nhóm biến dự báo chính, vì bước kiểm tra công bằng cần đến các thuộc tính này. Thiên lệch thuật toán
trong giáo dục là hiện tượng một mô hình dự báo tốt hơn hoặc kém hơn đáng kể cho một nhóm so với nhóm khác. Thiên lệch
này có thể phát sinh qua các biến đại diện (proxy) ngay cả khi không có thuộc tính nhân khẩu học nào làm đầu
vào, còn một bộ dữ liệu không ghi nhóm của từng người thì hoàn toàn không kiểm tra được [14]. Đề bài cũng cho phép giữ
các thuộc tính nhạy cảm để kiểm tra, đồng thời hạn chế dùng chúng làm biến dự báo [1]. Trên OULAD, Riazy và cộng sự
nhận thấy sinh viên tự khai có khuyết tật chiếm tỷ lệ rất thấp trong dữ liệu; phần lớn mô hình tái tạo mức chênh lệch 5–6 điểm phần trăm về tỷ lệ
đạt (disparate impact), nghiêng về sinh viên nam; bỏ các thuộc tính này ra khỏi mô hình hầu như không cải thiện công bằng; và trong một số
trường hợp, sinh viên khuyết tật bị dự báo trượt với xác suất cao hơn [15]. Quy mô các nhóm cần kiểm tra đã biết trước,
gồm 3.164 lượt đăng ký học của sinh viên tự khai có khuyết tật và 216 lượt của sinh viên từ 55 tuổi trở lên. Do đó, các nhóm nhỏ được kiểm tra
gộp qua các kỳ mở, còn nhóm có mức khó khăn "Missing" được báo cáo riêng.

Quy định về quyền riêng tư áp dụng ở hai cấp. OULAD đã được ẩn danh theo chuẩn k-ẩn danh (k-anonymity) với k = 5 [2].
Theo Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 của Việt Nam, dữ liệu đã khử định danh nằm ngoài định nghĩa dữ liệu cá
nhân và hành vi tái định danh dữ liệu đó bị cấm [16], nên OULAD không bao giờ được liên kết với nguồn dữ liệu khác. Đối với
đợt thí điểm trên hồ sơ của trường, thông tin sức khỏe, trong đó có tình trạng khuyết tật, là một ví dụ về dữ liệu cá nhân nhạy cảm [17]; dữ liệu chỉ được
xử lý cho một mục đích cụ thể [17]; luật cũng không quy định ngoại lệ chung cho mục đích nghiên cứu đối với yêu cầu phải có sự đồng ý
[16]. Vì vậy, đợt thí điểm cần có cơ sở pháp lý riêng. Các nhận định chỉ giới hạn trong phạm vi dữ liệu. Kết quả mô tả
các module đào tạo từ xa tại UK trong giai đoạn 2013–2014 và phải được kiểm tra lại trên hồ sơ của trường.
Các mối liên hệ trong AQ2 không phải quan hệ nhân quả; OULAD không cho phép rút ra tác động nào của hoạt động liên hệ sinh
viên; các mức khó khăn của khu vực không được gộp giữa các quốc gia thuộc UK [6].
