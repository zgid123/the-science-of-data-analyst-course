# Domain glossary: uncertainty quantification for medical image segmentation and radiotherapy auto-contouring

Terms of medical image segmentation on CT and MRI, radiotherapy contouring and the conformal methods that put a guarantee on segmentation sets. Radiotherapy terms follow established Vietnamese clinical usage (cơ quan nguy cấp, thể tích bia). "Conformal" stays as a technical loanword: Vietnamese has no settled term, and "bảo giác" names conformal mappings in mathematics, which would mislead. Method and data-set names (Consema, sem-CRC, RW-CP, TotalSegmentator, nnU-Net, AMOS, RAOS, HaN-Seg, CURVAS) stay as written.

## Imaging and radiotherapy

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| radiotherapy / treatment planning | xạ trị / lập kế hoạch điều trị | | |
| auto-contouring / auto-contour | khoanh vùng tự động / đường viền tự động | First use: "khoanh vùng tự động (auto-contouring)" | |
| contour / contouring | đường viền / khoanh vùng | | |
| organ at risk (OAR) | cơ quan nguy cấp (OAR) | Established term in Vietnamese radiotherapy | cơ quan có nguy cơ |
| target volume / clinical target volume (CTV) | thể tích bia / thể tích bia lâm sàng (CTV) | | thể tích mục tiêu |
| planning organ-at-risk volume (PRV) | thể tích lập kế hoạch cho cơ quan nguy cấp (PRV) | | |
| margin / margin recipe | biên / công thức tính biên | "biên an toàn" when the planning margin is meant | lề |
| computed tomography (CT) | chụp cắt lớp vi tính (CT) | "ảnh CT", "khối ảnh CT" for the image volume | |
| magnetic resonance imaging (MRI) | chụp cộng hưởng từ (MRI) | | |
| Hounsfield unit (HU) | đơn vị Hounsfield (HU) | | |
| voxel / voxel spacing | voxel / khoảng cách voxel | Keep "voxel" | |
| slice / slice direction | lát cắt / hướng lát cắt | | |
| segmentation / segmentation model (segmenter) | phân đoạn / mô hình phân đoạn | "phân đoạn ảnh" for the task | phân vùng ảnh |
| predicted mask / ground-truth mask | mặt nạ dự đoán / mặt nạ chuẩn | | |
| anatomical structure | cấu trúc giải phẫu | "cấu trúc" after first use | |
| surface Dice | Dice bề mặt | | |
| inter-rater variation | khác biệt giữa các người chú thích | | |
| automation bias | thiên kiến tự động hóa | First use: "thiên kiến tự động hóa (automation bias)" | thiên lệch tự động hóa |
| influencer structures | cấu trúc dẫn dắt | First use with "(influencer)" | |
| edit audit | kiểm tra lịch sử chỉnh sửa | | |
| clinical audit | đợt đánh giá (audit) | Clinical sense; "kiểm toán" is the finance and security sense | |
| setup error | sai số đặt tư thế bệnh nhân | | |

## Uncertainty and conformal methods

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| uncertainty quantification | định lượng độ bất định | | |
| conformal prediction | dự đoán conformal | First use: "dự đoán conformal (conformal prediction)" | dự đoán bảo giác, dự đoán phù hợp |
| conformal risk control (CRC) | kiểm soát rủi ro conformal (CRC) | | |
| Learn then Test (LTT) | Learn then Test (LTT) | Method name, keep English | |
| prediction set | tập dự đoán | | |
| uncertainty set | tập bất định | | tập độ bất định |
| nested sets / nested family | tập lồng nhau / họ tập lồng nhau | | |
| calibration / calibration set / calibrate | hiệu chuẩn / tập hiệu chuẩn / hiệu chuẩn | Measurement sense, as in probability calibration | hiệu chỉnh |
| recertification / recertify | hiệu chuẩn lại | | tái chứng nhận |
| exchangeable / exchangeability | hoán đổi được / tính hoán đổi được | | |
| coverage | độ bao phủ | | |
| loss / expected loss / empirical risk | hàm tổn thất / tổn thất kỳ vọng / rủi ro thực nghiệm | | |
| marginal guarantee / high-probability guarantee | bảo đảm trung bình / bảo đảm với xác suất cao | | |
| family-wise error rate | tỷ lệ lỗi theo họ | | |
| multiple testing | kiểm định nhiều giả thuyết | | |
| majority vote | bỏ phiếu đa số | | |
| union / intersection | hợp / giao | Set operations | |
| dilation / erosion | phép giãn / phép co | Morphological operations | |
| structuring element | phần tử cấu trúc | | |
| distance transform / sublevel set | biến đổi khoảng cách / tập mức dưới | | |
| geodesic / geodesic distance | trắc địa / khoảng cách trắc địa | | |
| softmax score / logit | điểm softmax / logit | Keep English | |
| vacuous set / vacuity | tập không còn thông tin / tình trạng mất thông tin | | |
| stretch | độ giãn | Set volume over predicted volume | |
| failure detection | phát hiện thất bại | | |
| site / change of site (site transfer) | cơ sở / chuyển sang cơ sở khác | | |

## Shared terms from report vocabularies (2026-10-28)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| 2D slice / pixel | lát cắt 2D / điểm ảnh | A 2D CT slice and its picture elements | |
| image-processing operator / label-free operator | toán tử xử lý ảnh / toán tử không dùng nhãn | | |
| contour-tolerance loss | hàm tổn thất về dung sai đường viền | | |
