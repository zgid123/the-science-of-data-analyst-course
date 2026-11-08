# Domain glossary: card payments in Vietnam: Parties and documents; Transaction lifecycle, clearing and settlement; Reversals, refunds and disputes; Fees, currency and statements

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
