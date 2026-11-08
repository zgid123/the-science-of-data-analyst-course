import re,glob,os,sys
d=sys.argv[1]
files=[f for f in sorted(glob.glob(os.path.join(d,'*.vi.md'))) if not os.path.basename(f).startswith(('00-1','00-2','09-'))]
M={'baseline':'phương pháp cơ sở','prototype':'nguyên mẫu','Controlled Change Log':'nhật ký thay đổi có kiểm soát','recall':'tỷ lệ phát hiện','lift':'mức vượt tỷ lệ nền','odds ratio':'tỉ số odds','primary approach':'phương pháp chính','fixed effects':'hiệu ứng cố định','shrinkage':'co hệ số','gradient-boosted trees':'cây tăng cường độ dốc','challenger':'mô hình đối sánh','precision':'độ chính xác của danh sách','normalised recall':'tỷ lệ phát hiện chuẩn hóa','calibration-in-the-large':'hiệu chuẩn tổng thể','calibration slope':'độ dốc hiệu chuẩn','net benefit':'lợi ích ròng','leave-one-run-out':'loại trừ từng kỳ mở','sign-flip test':'kiểm định hoán vị đổi dấu','slicing analysis':'phân tích theo từng nhóm con','separation':'ngang bằng tỷ lệ phát hiện','uplift':'lợi ích can thiệp','post-hoc':'giải thích hậu nghiệm','performative prediction':'dự báo tự tác động','AI Decision Log':'nhật ký quyết định về ai','background-only model':'chỉ dùng đặc điểm cá nhân','penalised logistic regression':'hồi quy logistic có hiệu chỉnh phạt','non-informative censoring':'kiểm duyệt không mang thông tin','proxy':'kiểm tra biến thay thế','calibration':'hiệu chuẩn','automation bias':'thiên kiến tự động hóa','target trial':'thử nghiệm mục tiêu','hierarchical bootstrap':'bootstrap phân tầng','binned residuals':'phần dư trung bình theo khoảng','external validation':'kiểm định ngoài','expected shrinkage':'mức co hệ số kỳ vọng','proxy check':'kiểm tra biến thay thế','robust standard errors':'sai số chuẩn','temporal validation':'đánh giá theo thời gian','precision at capacity':'độ chính xác của danh sách dài k','seed':'giá trị khởi tạo ngẫu nhiên','model card':'thẻ mô hình','datasheet':'bảng mô tả dữ liệu','AQ–Data Fit':'mức phù hợp giữa aq và dữ liệu','literature assistant':'trợ lý tìm tài liệu','entanglement':'chằng chịt','hazard':'nguy cơ rút'}
for g,t in M.items():
    first=None; gl=[]
    for f in files:
        for i,l in enumerate(open(f),1):
            if l.startswith('>'): continue
            low=l.lower()
            if first is None and t in low: first=(os.path.basename(f)[:5],i)
            if '('+g+')' in l: gl.append((os.path.basename(f)[:5],i))
    ok = gl and first==gl[0] and len(gl)==1
    print('OK ' if ok else '-- ',g,'| first term',first,'| glosses',gl)
