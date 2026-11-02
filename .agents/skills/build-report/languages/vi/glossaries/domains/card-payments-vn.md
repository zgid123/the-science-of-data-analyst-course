# Domain glossary: card payments in Vietnam

Card acceptance at the point of sale, acquiring, clearing and settlement, disputes, fees and statements, card security, anti-money laundering, POS e-invoices and the engineering of payment systems. Select it for reports on card payments, acquiring or payment-system design in Vietnam. Terms that Vietnamese law regulates take the wording of the Vietnamese original text, cited in Usage: Thông tư 18/2024/TT-NHNN as amended by Thông tư 45/2025/TT-NHNN (TT 18/2024), Nghị định 52/2024/NĐ-CP (NĐ 52/2024), Nghị định 123/2020/NĐ-CP as amended by Nghị định 70/2025/NĐ-CP (NĐ 70/2025), Thông tư 09/2020/TT-NHNN (TT 09/2020), Nghị định 13/2023/NĐ-CP (NĐ 13/2023) and Luật Phòng, chống rửa tiền số 14/2022/QH15 (Luật PCRT 2022). Engineering terms follow established Vietnamese IT usage and keep the English where Vietnamese engineers write it.

## Parties and documents

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| cardholder / primary cardholder / supplementary cardholder | chủ thẻ / chủ thẻ chính / chủ thẻ phụ | TT 18/2024, Điều 3 khoản 13–15 (khoản 15 sửa đổi bởi TT 45/2025, Điều 1) | người giữ thẻ, chủ sở hữu thẻ |
| issuer | tổ chức phát hành thẻ (TCPHT) | TT 18/2024, Điều 3 khoản 16; first use "tổ chức phát hành thẻ (TCPHT)", then "TCPHT" or "ngân hàng phát hành" in running prose | nhà phát hành thẻ |
| acquirer | tổ chức thanh toán thẻ (TCTTT) | TT 18/2024, Điều 3 khoản 17 and Điều 20; first use "tổ chức thanh toán thẻ (TCTTT, acquirer)" | ngân hàng thu nhận, tổ chức thu nhận thẻ, ngân hàng chấp nhận thẻ, ngân hàng thanh toán thẻ |
| merchant / card-accepting unit | đơn vị chấp nhận thẻ (ĐVCNT) | TT 18/2024, Điều 3 khoản 21; "người bán" only in the invoice sense of NĐ 70/2025 | thương nhân chấp nhận thẻ, điểm chấp nhận thẻ, nhà bán hàng |
| card-accepting unit (general, any payment instrument) | đơn vị chấp nhận thanh toán | NĐ 52/2024, Điều 21; TT 18/2024, Điều 21 khoản 1 | |
| card network / international card organisation | tổ chức thẻ quốc tế (TCTQT) | TT 18/2024, Điều 3 khoản 22; Visa and Mastercard are "tổ chức thẻ quốc tế"; "mạng lưới thẻ" for the network as infrastructure | hiệp hội thẻ, mạng thẻ quốc tế |
| card switch / switching | tổ chức chuyển mạch thẻ / chuyển mạch | TT 18/2024, Điều 3 khoản 19 and Điều 22; NAPAS is "tổ chức chuyển mạch thẻ" | bộ chuyển mạch thẻ, chuyển tiếp giao dịch |
| card clearing organisation | tổ chức bù trừ điện tử giao dịch thẻ | TT 18/2024, Điều 3 khoản 20 | phòng thanh toán bù trừ |
| payment intermediary | tổ chức cung ứng dịch vụ trung gian thanh toán (TCTGTT) | TT 18/2024, Điều 3 khoản 18; NĐ 52/2024. Overrides the short form of digital-banking-vn in card reports | |
| financial switching service / electronic clearing service | dịch vụ chuyển mạch tài chính / dịch vụ bù trừ điện tử | NĐ 52/2024, Điều 3 khoản 13 và 15; NAPAS page "Dịch vụ Chuyển mạch tài chính và Bù trừ điện tử" | |
| four-party model | mô hình bốn bên | | mô hình bốn đảng |
| card transaction | giao dịch thẻ | TT 18/2024, Điều 3 khoản 8 | |
| card-present transaction | giao dịch xuất trình thẻ | TT 18/2024, Điều 3 khoản 10 ("giao dịch nội địa xuất trình thẻ") | giao dịch có mặt thẻ, giao dịch thẻ hiện diện |
| bank identification number (BIN) | mã tổ chức phát hành thẻ (BIN) | TT 18/2024, Điều 3 khoản 26 | số nhận dạng ngân hàng |
| primary account number (PAN) | số thẻ đầy đủ (PAN) | First use "số thẻ đầy đủ (PAN)", then "PAN" | số tài khoản chính |
| card issuance and use contract / card payment contract | hợp đồng phát hành và sử dụng thẻ / hợp đồng thanh toán thẻ | TT 18/2024, Điều 3 khoản 27–28 | |
| merchant category code (MCC) | mã ngành hàng (MCC) | First use "mã ngành hàng của ĐVCNT (MCC)" | mã danh mục thương nhân |
| Vietnam Domestic Chip-based Payment Card Specifications (VCCS) | Tiêu chuẩn cơ sở về thẻ chip nội địa (VCCS) | TT 18/2024, Điều 3 khoản 29 (TCCS 01:2018/NHNNVN, TCCS 02:2018/NHNNVN) | |
| National Payment Corporation of Vietnam (NAPAS) | Công ty Cổ phần Thanh toán Quốc gia Việt Nam (NAPAS) | Keep "NAPAS" after first use | |

## Transaction lifecycle, clearing and settlement

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| authorisation / authorisation request / authorisation code | cấp phép / yêu cầu cấp phép / mã cấp phép | Card sense; first use "cấp phép giao dịch (authorisation)"; "số tiền được cấp phép". Common "authorization" (phân quyền) keeps its access-control sense | ủy quyền giao dịch, chuẩn chi, mã ủy quyền |
| approve / decline (card) | chấp thuận / từ chối | "ngân hàng phát hành chấp thuận giao dịch"; TT 18/2024, Điều 25 "từ chối thanh toán thẻ" | |
| hold / release a hold | khoản giữ tiền / giải phóng khoản giữ tiền | "khoản giữ tiền trên hạn mức của chủ thẻ" | khoản treo, khoản phong tỏa tạm |
| credit limit / open-to-buy | hạn mức tín dụng / hạn mức khả dụng | TT 18/2024, Điều 3 khoản 3 and Điều 13; first use "hạn mức khả dụng (open-to-buy)" | hạn mức mở để mua, hạn mức còn mua |
| capture | ghi nhận giao dịch | First use "ghi nhận giao dịch (capture)"; "số tiền ghi nhận" | chụp giao dịch, bắt giao dịch |
| batch / batch close | lô giao dịch / kết toán cuối ngày | First use "kết toán cuối ngày (batch close)", the POS menu step that sends the day's batch | đóng lô, chốt lô |
| clearing / clear | bù trừ / bù trừ | TT 18/2024, Điều 1 and Điều 22 ("bù trừ điện tử giao dịch thẻ"); NĐ 52/2024, Điều 3 khoản 15 | thanh trừ, giải trừ, làm sạch giao dịch |
| first presentment / second presentment | xuất trình lần đầu / xuất trình lần hai | First use with English: "xuất trình lần đầu (first presentment)" | trình diện lần đầu, trình diện lần hai |
| settlement / settle | quyết toán / quyết toán | TT 18/2024, Điều 1 and Điều 24 ("quyết toán kết quả thanh toán bù trừ giao dịch thẻ"); NĐ 52/2024, Điều 3 khoản 15 | tất toán, dàn xếp, giải quyết thanh toán |
| net settlement / net position | quyết toán ròng / số ròng phải thu, phải trả | NĐ 52/2024, Điều 3 khoản 15 ("số tiền phải thu, phải trả sau khi bù trừ") | quyết toán thuần |
| value date / cut-off time | ngày giá trị / giờ chốt | First use "giờ chốt (cut-off)" | ngày hiệu lực giá trị, thời điểm cắt |
| business day | ngày làm việc | TT 18/2024, Điều 19 ("30 ngày làm việc") | ngày kinh doanh |
| merchant funding / payout | chi trả cho đơn vị chấp nhận thẻ / chi trả | "chi trả cho ĐVCNT sau quyết toán", credited to the merchant account | cấp vốn cho thương nhân, tài trợ thương nhân |
| reserve (merchant) | ký quỹ dự phòng | First use "ký quỹ dự phòng của ĐVCNT (reserve)"; "rolling reserve" → "ký quỹ cuốn chiếu" | khoản dự trữ thương nhân |
| merchant onboarding / know your business (KYB) | tiếp nhận ĐVCNT / nhận biết ĐVCNT (KYB) | TT 18/2024, Điều 20 khoản 9 ("thẩm định, lựa chọn, giám sát ĐVCNT") | nhập môn thương nhân |

## Reversals, refunds and disputes

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| reversal / reversal advice / guaranteed reversal | đảo giao dịch / thông báo đảo giao dịch / đảo giao dịch có bảo đảm | First use "đảo giao dịch (reversal)"; "gửi lại thông báo đảo giao dịch cho đến khi có xác nhận" | đảo ngược giao dịch, hoàn tác giao dịch, giao dịch đảo ngược |
| void | hủy giao dịch | First use "hủy giao dịch (void)", possible only before batch close | vô hiệu giao dịch, làm rỗng giao dịch |
| refund | hoàn tiền | First use "hoàn tiền (refund)"; a credit linked to an earlier sale | trả lại tiền, hoàn lại tiền |
| dispute / dispute resolution | tra soát / giải quyết tra soát | A disputed card sale, as in TT 18/2024, Điều 19 ("tra soát, khiếu nại"); "tranh chấp" only for legal disputes (Điều 19 khoản 3 điểm c, "giải quyết tranh chấp") | |
| inquiry / complaint (cardholder) | tra soát / khiếu nại | TT 18/2024, Điều 19 ("đề nghị tra soát, khiếu nại"); "xử lý tra soát, khiếu nại" | truy vấn giao dịch, phàn nàn |
| chargeback | bồi hoàn | First use "bồi hoàn (chargeback)"; TT 18/2024, Điều 19 khoản 3 ("bên có lỗi thực hiện bồi hoàn cho TCPHT") | hoàn tiền bắt buộc, trả ngược, tính phí ngược |
| representment / dispute response | xuất trình lại / phản hồi tra soát | First use "xuất trình lại (representment)"; "phản hồi tra soát (dispute response)" at Visa | trình diện lại |
| pre-arbitration / arbitration | tiền trọng tài / trọng tài | First use with English: "tiền trọng tài (pre-arbitration)" | trước trọng tài, phân xử |
| reason code / reason category | mã lý do / nhóm lý do | "nhóm lý do gian lận", "nhóm lý do tranh chấp của chủ thẻ" | |
| friendly fraud | gian lận thân thiện | First use "gian lận thân thiện (friendly fraud)" | lừa đảo thân thiện |
| retrieval reference number (RRN) / system trace audit number (STAN) | số tham chiếu truy xuất (RRN) / số theo dõi kiểm toán hệ thống (STAN) | Keep "RRN", "STAN" after first use | |

## Fees, currency and statements

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| interchange / interchange fee | phí trao đổi / phí trao đổi | First use "phí trao đổi (interchange)" | phí giao hoán |
| scheme fee | phí tổ chức thẻ | First use "phí tổ chức thẻ (scheme fee)" | phí sơ đồ, phí lược đồ |
| merchant discount rate (MDR) | tỷ lệ phí chiết khấu (MDR) | TT 18/2024 ("thu phí đối với đơn vị chấp nhận thẻ"); first use "tỷ lệ phí chiết khấu ĐVCNT (MDR)" | tỷ lệ giảm giá thương nhân |
| interchange++ | interchange++ | Keep English; "biểu phí interchange++" | |
| acquirer markup | phần phí cộng thêm của TCTTT | | |
| dynamic currency conversion (DCC) | chuyển đổi ngoại tệ động (DCC) | Keep "DCC" after first use | chuyển đổi tiền tệ năng động |
| exchange rate | tỷ giá | TT 18/2024, Điều 4 ("tỷ giá do các bên thỏa thuận") | tỉ giá hối đoái chéo |
| value-added tax (VAT) / VAT on fees | thuế giá trị gia tăng (thuế GTGT) / thuế GTGT trên phí | Use "thuế GTGT" after first use; card interest is "không chịu thuế GTGT" | |
| statement / statement date / billing cycle | sao kê / ngày sao kê / kỳ sao kê | Banking usage: "sao kê thẻ tín dụng" | bảng kê hóa đơn, chu kỳ hóa đơn |
| due date / grace period | ngày đến hạn thanh toán / thời gian miễn lãi | Banking usage | thời gian ân hạn |
| minimum payment | số tiền thanh toán tối thiểu | TT 18/2024, Điều 12 (hợp đồng nêu khoản trả nợ tối thiểu) | khoản trả tối thiểu bắt buộc |
| payment allocation | thứ tự thu hồi nợ | TT 18/2024, Điều 12 khoản 1 điểm g ("thứ tự thu hồi nợ gốc và lãi") | phân bổ thanh toán |
| instalment conversion | chuyển đổi trả góp | Banking usage | chuyển đổi phân kỳ |
| interest / principal | lãi / nợ gốc | TT 18/2024, Điều 12 | |
| fee invoice / settlement report | hóa đơn phí / báo cáo quyết toán | | |

## Terminal, card and card security

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| point-of-sale terminal | thiết bị chấp nhận thẻ tại điểm bán | TT 18/2024, Điều 3 khoản 24 (sửa đổi bởi TT 45/2025, Điều 1). Overrides "máy chấp nhận thẻ" of digital-banking-vn in card reports | máy cà thẻ |
| POS terminal / mPOS | thiết bị POS / mPOS | First use "thiết bị chấp nhận thẻ tại điểm bán (POS)"; then "thiết bị POS" or "máy POS"; keep "mPOS" | |
| cash register | máy tính tiền | NĐ 70/2025, Điều 3 khoản 2 điểm d | máy thu ngân |
| terminal fleet / terminal management system (TMS) | đội thiết bị đầu cuối / hệ thống quản lý thiết bị đầu cuối (TMS) | "thiết bị đầu cuối" as in TT 18/2024, Điều 3 khoản 24 | hạm đội thiết bị |
| floor limit | hạn mức ngoại tuyến | First use "hạn mức ngoại tuyến (floor limit)", the maximum a terminal approves offline | hạn mức sàn, giới hạn sàn |
| online / offline (transaction) | trực tuyến / ngoại tuyến | "phê duyệt ngoại tuyến", "chấp nhận thẻ ngoại tuyến" | |
| store-and-forward | lưu rồi chuyển tiếp | First use "lưu rồi chuyển tiếp (store-and-forward)" | lưu trữ và chuyển đi, lưu và chuyển tiếp |
| stand-in processing (STIP) | xử lý thay thế (STIP) | First use "xử lý thay thế (stand-in processing, STIP)": the network approves within limits set by an unreachable issuer | xử lý dự bị |
| chip / chip card / magnetic stripe | chip / thẻ chip / dải từ | TT 18/2024, Điều 3 khoản 6 ("có gắn chip điện tử") | sọc từ, vạch từ |
| fallback (to magnetic stripe) | chuyển sang dải từ (fallback) | Card sense only; the software sense keeps common "phản hồi dự phòng (fallback)" | |
| contactless | không tiếp xúc | TT 18/2024, Điều 3 khoản 29 ("chip không tiếp xúc") | phi tiếp xúc |
| cardholder verification method (CVM) | phương thức xác minh chủ thẻ (CVM) | Keep "CVM" after first use | phương pháp kiểm chứng chủ thẻ |
| personal identification number (PIN) / PIN block | mã PIN / khối PIN (PIN block) | TT 18/2024, Điều 3 khoản 23 ("Mã số xác định chủ thẻ (PIN)"); later "mã PIN" | số định danh cá nhân |
| cryptogram / application cryptogram (AC) | cryptogram / cryptogram ứng dụng (AC) | Keep English; first use "cryptogram (giá trị mật mã do chip tạo ra cho từng giao dịch)" | mật mã đồ, mật mã học ứng dụng |
| skimming / shimming | skimming / shimming | Keep English; first use "skimming (gắn thiết bị đọc trộm dải từ)", "shimming (chèn thiết bị đọc trộm vào khe chip)" | lướt thẻ, đệm thẻ |
| relay attack | tấn công chuyển tiếp | First use "tấn công chuyển tiếp (relay attack)", e.g. Ghost Tap over NFC | tấn công rơ-le |
| counterfeit card | thẻ giả | TT 18/2024, Điều 3 khoản 11 | thẻ nhái, thẻ làm giả |
| fraudulent or counterfeit card transaction | giao dịch thẻ gian lận, giả mạo | TT 18/2024, Điều 3 khoản 12 | |
| tamper / tamper-responsive | can thiệp trái phép / tự phản ứng khi bị can thiệp | "thiết bị POS bị can thiệp trái phép" | giả mạo thiết bị |
| key injection | nạp khóa | First use "nạp khóa (key injection)" vào thiết bị POS | tiêm khóa, bơm khóa |
| hardware security module (HSM) | mô-đun bảo mật phần cứng (HSM) | Keep "HSM" after first use | mô-đun an ninh phần cứng |
| derived unique key per transaction (DUKPT) | DUKPT | Keep English; first use "DUKPT (khóa riêng suy diễn cho từng giao dịch)" | |
| point-to-point encryption (P2PE) | mã hóa điểm-điểm (P2PE) | Keep "P2PE" after first use | mã hóa điểm-tới-điểm |
| tokenisation / token vault | token hóa / token vault | First use "token hóa (tokenisation)"; keep "token vault" with gloss "kho lưu ánh xạ token – số thẻ" | |
| PCI DSS / cardholder data environment | PCI DSS / môi trường dữ liệu chủ thẻ | Keep "PCI DSS"; "môi trường dữ liệu chủ thẻ (CDE)" | |

## Fraud, anti-money laundering and data protection

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| fake transaction / POS cash-out | giao dịch thanh toán khống / rút tiền mặt qua POS | TT 18/2024, Điều 3 khoản 9 ("giao dịch thanh toán khống tại đơn vị chấp nhận thẻ"); NĐ 52/2024, Điều 29 | giao dịch ma, giao dịch giả tạo |
| transaction laundering | rửa giao dịch | First use "rửa giao dịch (transaction laundering)": sales of a hidden business pushed through another merchant's terminal | giặt giao dịch |
| money mule | người chuyển tiền thuê | First use "người chuyển tiền thuê (money mule)"; "tài khoản thuê, mượn" for the account | con la tiền, la tiền |
| anti-money laundering (AML) / combating the financing of terrorism (CFT) | phòng, chống rửa tiền / chống tài trợ khủng bố | Luật PCRT 2022; keep "AML/CFT" in tables | chống rửa tiền bẩn |
| know your customer (KYC) | nhận biết khách hàng (KYC) | Luật PCRT 2022, Điều 9 | biết khách hàng của bạn |
| reporting entity | đối tượng báo cáo | Luật PCRT 2022, Điều 4 | |
| suspicious transaction report | báo cáo giao dịch đáng ngờ | Luật PCRT 2022, Điều 26 | báo cáo hoạt động đáng ngờ, báo cáo giao dịch khả nghi |
| large-value transaction | giao dịch có giá trị lớn | Luật PCRT 2022, Điều 25 | |
| sanctions screening / blacklist | sàng lọc danh sách đen / Danh sách đen | Luật PCRT 2022, Điều 3 khoản 9 ("Danh sách đen"); first use "sàng lọc danh sách đen (sanctions screening)" | sàng lọc trừng phạt, rà soát cấm vận |
| sensitive personal data | dữ liệu cá nhân nhạy cảm | NĐ 13/2023, Điều 2 khoản 4 | |
| personal data controller / personal data processor | Bên Kiểm soát dữ liệu cá nhân / Bên Xử lý dữ liệu cá nhân | NĐ 13/2023, Điều 2 khoản 9–10 | bên điều khiển dữ liệu |

## E-invoices

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| e-invoice / POS-generated e-invoice | hóa đơn điện tử / hóa đơn điện tử khởi tạo từ máy tính tiền | NĐ 70/2025 (sửa đổi NĐ 123/2020, Điều 3 khoản 2 điểm c và Điều 11): "hóa đơn điện tử khởi tạo từ máy tính tiền có kết nối chuyển dữ liệu điện tử với cơ quan thuế" | hóa đơn POS, hóa đơn sinh từ máy POS |
| adjustment invoice / replacement invoice | hóa đơn điều chỉnh / hóa đơn thay thế | NĐ 70/2025 (sửa đổi NĐ 123/2020, Điều 19) | hóa đơn sửa đổi, hóa đơn thế chỗ |
| tax authority | cơ quan thuế | NĐ 70/2025 | cơ quan quản lý thuế vụ |
| seller / buyer (invoice) | người bán / người mua | NĐ 70/2025, Điều 11 khoản 3 | |

## Engineering of payment systems

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| idempotency / idempotent receiver | tính lũy đẳng / bộ tiếp nhận lũy đẳng | Builds on common "lũy đẳng (idempotent)"; first use "bộ tiếp nhận lũy đẳng (idempotent receiver)" | tính bất biến khi lặp |
| idempotency key | idempotency key | Keep English; first use "idempotency key (khóa chống xử lý lặp)" | khóa đồng nhất |
| at-least-once delivery / exactly-once | phân phối ít nhất một lần / đúng một lần | First use with English: "phân phối ít nhất một lần (at-least-once delivery)" | giao hàng ít nhất một lần |
| duplicate (message, transaction) | bản trùng / giao dịch trùng lặp | Builds on common "chống trùng lặp" | bản sao chép trùng |
| in-doubt transaction / unknown outcome | giao dịch chưa rõ kết quả / kết quả chưa rõ | "kết quả chưa rõ sau khi hết thời gian chờ" | giao dịch lơ lửng |
| jitter / retry with backoff and jitter | jitter / thử lại có giãn cách và jitter | Builds on common "thử lại / giãn cách thử lại (backoff)"; keep "jitter" | rung pha |
| circuit breaker | bộ ngắt mạch | First use "bộ ngắt mạch (circuit breaker)" | cầu dao điện |
| bulkhead | bulkhead | Keep English; first use "bulkhead (vách ngăn cô lập tài nguyên)" | vách tàu |
| load shedding | cắt giảm tải | First use "cắt giảm tải (load shedding)" | sa thải tải, rụng tải |
| saga / compensating transaction | saga / giao dịch bù | Keep "saga"; first use "giao dịch bù (compensating transaction)" | giao dịch đền bù |
| transactional outbox / relay | outbox giao dịch / bộ chuyển tiếp | First use "outbox giao dịch (transactional outbox)": a table written in the same database transaction as the state change | |
| event stream / event | luồng sự kiện / sự kiện | First use "luồng sự kiện (event stream)" | dòng chảy sự kiện |
| ledger / double-entry ledger | sổ cái / sổ cái bút toán kép | "sổ cái chỉ ghi thêm" | sổ ghi chép kép |
| journal entry / posting | bút toán / hạch toán | "hạch toán vào tài khoản thẻ" | mục nhật ký, mục ghi sổ |
| control account | tài khoản kiểm soát | | |
| reconciliation / reconciliation break | đối soát / chênh lệch đối soát | First use "đối soát (reconciliation)"; first use "chênh lệch đối soát (break)" | khớp lệnh, điều hòa giao dịch, hòa giải giao dịch, đối chiếu khớp |
| tie-out | đối chiếu cân số | First use "đối chiếu cân số (tie-out)": opening balance plus movements equals closing balance | buộc số |
| maker-checker | người lập – người duyệt | First use "nguyên tắc người lập – người duyệt (maker-checker)"; TT 09/2020 ("vừa khởi tạo vừa phê duyệt") | người làm – người kiểm |
| write-once (storage) | ghi một lần (WORM) | First use "lưu trữ ghi một lần (write-once, WORM)" | viết một lần |
| active-active / active-passive | active-active / active-passive | Keep English; first use "active-active (hai trung tâm cùng xử lý)" | |
| failover / failback | chuyển đổi dự phòng / chuyển về hệ thống chính | TT 09/2020 ("chuyển đổi hoạt động thực tế sang hệ thống dự phòng"); first use "chuyển đổi dự phòng (failover)" | chuyển đổi lỗi |
| disaster recovery / disaster recovery site | dự phòng thảm họa / hệ thống dự phòng thảm họa | TT 09/2020, Điều 50 | khôi phục thảm họa, phục hồi sau thảm họa |
| business continuity | bảo đảm hoạt động liên tục | TT 09/2020 | liên tục kinh doanh |
| recovery time objective (RTO) / recovery point objective (RPO) | mục tiêu thời gian khôi phục (RTO) / mục tiêu điểm khôi phục (RPO) | Keep "RTO", "RPO" after first use | |
| split brain / fencing token | split-brain / fencing token | Keep English; first use "split-brain (hai nút cùng tự nhận là nút chính)", "fencing token (số hiệu tăng dần chặn ghi từ nút cũ)" | não phân tách, mã thông báo hàng rào |
| gray failure | sự cố ngầm | First use "sự cố ngầm (gray failure)": the component passes health checks while serving wrong or slow results | thất bại xám |
| health check | kiểm tra sức khỏe | "kiểm tra sức khỏe dịch vụ (health check)" | |
| observability / trace / distributed tracing | khả năng quan sát / trace / truy vết phân tán | First use "khả năng quan sát (observability)"; keep "trace" | dấu vết phân tán |
| service-level objective (SLO) | mục tiêu mức dịch vụ (SLO) | Keep "SLO" after first use | mục tiêu cấp độ dịch vụ |
| canary release / feature flag | triển khai canary / cờ tính năng | First use "triển khai canary (canary release)", "cờ tính năng (feature flag)" | phát hành chim hoàng yến, phát hành chim yến |
| contract test | kiểm thử hợp đồng | First use "kiểm thử hợp đồng (contract test)" | |
| command and query responsibility segregation (CQRS) | CQRS | Keep English; first use "CQRS (tách luồng ghi và luồng đọc)" | |
| multi-factor authentication for administrators | xác thực đa yếu tố khi truy cập quản trị | TT 09/2020 | |
| information system security | an toàn hệ thống thông tin | TT 09/2020 | an ninh hệ thống thông tin |

## Terms settled during the first translation (2026-10-10)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| operational resilience | khả năng phục hồi hoạt động | First use "khả năng phục hồi hoạt động (operational resilience)"; BCBS and PRA texts | khả năng chống chịu trong hoạt động |
| impact tolerance | ngưỡng chịu đựng tác động | PRA SS1/21 | |
| cascading failure | sự cố dây chuyền | | lỗi xếp tầng |
| retry storm / thundering herd | bão thử lại / hiện tượng dồn dập | First use with the English in parentheses | đám đông dồn dập |
| tail latency | độ trễ đuôi | First use "độ trễ đuôi (tail latency)" | |
| hot partition | phân vùng nóng | "shard" stays English | |
| dual write | ghi kép | First use "ghi kép (dual write)" | |
| silent data corruption | hỏng dữ liệu âm thầm | | |
| alert fatigue | quá tải cảnh báo | | |
| ransomware | mã độc tống tiền | First use "mã độc tống tiền (ransomware)" | |
| core banking system | hệ thống ngân hàng lõi | | |
| chaos engineering / fault injection / game day | kỹ thuật hỗn loạn / thí nghiệm chèn lỗi / ngày diễn tập sự cố | First use with the English in parentheses | |
| error budget | quỹ lỗi | SRE | ngân sách lỗi |
| graceful degradation | suy giảm có kiểm soát | | |
| single point of failure | điểm lỗi đơn lẻ | | |
| fail-open / fail-closed | tiếp tục khi lỗi / dừng khi lỗi | First use with the English in parentheses | mở khi lỗi, đóng khi lỗi |
| liability shift | chuyển dịch trách nhiệm | First use "chuyển dịch trách nhiệm (liability shift)" | |
| technical fallback | chuyển sang dải từ do lỗi kỹ thuật | First use with the English in parentheses | |
| key entry (of the card number) | nhập tay số thẻ | | |
| preauthorisation | cấp phép trước | | |
| netting | xác định số ròng phải thu, phải trả | Distinct from "bù trừ" (clearing) | |
| rolling reserve | ký quỹ cuốn chiếu | | |
| pricing plan / volume tier / true-up | biểu phí / bậc phí / khoản điều chỉnh bù chênh | | |
| settlement bank | ngân hàng quyết toán | | |
| advice (ISO 8583 message) | thông báo | "thông báo đảo giao dịch" for a reversal advice | |
| dual-message | mô hình hai thông điệp | | |
| deadline propagation | lan truyền thời hạn | | lan truyền hạn chót |
| static stability | ổn định tĩnh | AWS | |
| home site | trung tâm dữ liệu chủ quản | | |
| compensation (saga step) | thao tác bù | | |
| pivot transaction (saga) | giao dịch bản lề | First use "giao dịch bản lề (pivot transaction)" | giao dịch then chốt |
| network partition | chia cắt mạng | First use "chia cắt mạng (network partition)"; "phân vùng" stays for data partitions | phân mảnh mạng, phân tách mạng, phân vùng mạng |
| availability zone | vùng khả dụng | Cloud zones; "vùng" alone is a pipeline zone | vùng sẵn sàng |
| terminal intercept | thành phần trung gian chuyển thông điệp | First use "thành phần trung gian chuyển thông điệp từ máy POS (terminal intercept)" | |
| incremental authorisation / final authorisation | cấp phép bổ sung / cấp phép cuối cùng | | |
| data element (ISO 8583) | phần tử dữ liệu | "phần tử dữ liệu 11" | |
| billing currency | đồng tiền ghi nợ | Currency of the cardholder's statement | |
| payment allocation (of a repayment) | thứ tự thu hồi nợ | Order in which a repayment settles balances | phân bổ thanh toán |
| Financial Action Task Force (FATF) | Lực lượng Đặc nhiệm Tài chính về chống rửa tiền | Written in full; the English text does not abbreviate it | |
| job instance (batch) | thực thể tác vụ | Spring Batch | phiên bản tác vụ, thực thể job |
| Prudential Regulation Authority (United Kingdom) | Cơ quan Quản lý Thận trọng của Vương quốc Anh | Written in full | |
| partition mode (CAP) | chế độ vận hành khi chia cắt mạng | Brewer | |
| legal hold (on records) | giữ nguyên hồ sơ theo yêu cầu pháp lý | "phong tỏa" stays for frozen funds and accounts | |
| network token (EMV payment tokenisation) | token do tổ chức thẻ cấp | First use "token do tổ chức thẻ cấp (network token)" | token mạng lưới |
| goodput | goodput | Keep English; first use "goodput (lưu lượng được xử lý thành công)" | |
| Principles for Financial Market Infrastructures (PFMI) | Bộ nguyên tắc về hạ tầng thị trường tài chính | CPMI-IOSCO; written in full, in every part, also where English writes it in lower case | nguyên tắc dành cho hạ tầng thị trường tài chính |
| Basel Core Principles | Bộ nguyên tắc cốt lõi Basel | | |
| set off (a merchant's negative balance against future sales) | cấn trừ | "bù trừ" stays for clearing | |
| currency minor unit | đơn vị lẻ của đồng tiền | | đơn vị tiền tệ nhỏ nhất |
| processor (payment processor, an organisation) | đơn vị xử lý | "bộ xử lý" only for software that consumes events ("các bộ xử lý sự kiện") | |
| terminal fleet / fleet | đội thiết bị đầu cuối / đội thiết bị | Full form in headings and at first mention; "đội thiết bị" in running text, as in C5.B7.1 and C5.B8.1 | |

## Shared terms from report vocabularies (2026-10-28)

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| terminal journal | nhật ký giao dịch trên máy POS | | tạp chí thiết bị đầu cuối |
