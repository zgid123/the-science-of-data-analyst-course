# vi-reader-test-notes15 (re-test)

Fresh reader on the rebuilt deck: clarity 3 on fifteen slides and 2 on slide 13; 6 flags, all fixed: F1 and F2 (slide 3 notes: the unit defined, non-completion named as fail or withdraw), F3 (slide 4 card: 'bỏ lỡ bài lần đầu'), F4 (slide 9 card title: 'Tỷ lệ phát hiện (trong giới hạn danh sách)'), F5 (slide 13 card and notes, both languages: counted per 20 students, the size of one tutor group; the base rate named as 2014 non-completion at day 27), F6 (slide 14 last row wording). check_slides after the fixes: 0 errors, 0 warnings in both languages.

# Reader test 2: Trưởng phòng Đào tạo, Vietnamese 16-slide deck (main16_vi_r2.txt)

Reader: Trưởng phòng Đào tạo who has not read any report. I read each slide, then its notes, and asked whether I could follow the slide end to end.
Clarity: 1 = could not follow; 2 = followed with effort, some passage unclear; 3 = clear.
Ids: `slide.paragraph` from pairs3.json for notes; "slide N (slide text)" for on-slide text (pairs3.json holds notes only).

## Summary

| Slide | Clarity | Flags |
| :-- | :-: | :-- |
| 1 | 3 | none |
| 2 | 3 | none |
| 3 | 3 | F1, F2 |
| 4 | 3 | F3 |
| 5 | 3 | none |
| 6 | 3 | none |
| 7 | 3 | none |
| 8 | 3 | none |
| 9 | 3 | F4 |
| 10 | 3 | none |
| 11 | 3 | none |
| 12 | 3 | none |
| 13 | 2 | F5 |
| 14 | 3 | F6 |
| 15 | 3 | none |
| 16 | 3 | none |

Total: 47 / 48; 15 slides at 3, 1 at 2 (slide 13). Six flags, none blocking; F2 and F5 are the two that can mislead.

## Per slide

### Slide 1 – 3
Coverage: complete. The notes explain the appendix pointer (grey line top right) used on every later slide.

### Slide 2 – 3
Coverage: complete. The orange band, three grey markers, three cards and the "Căn cứ" line are all explained; the notes state that the timings come from AI-simulated interviews.

### Slide 3 – 3
Coverage: complete. Business Goal, SMART Goal, pilot design, 70% → 75% box, "Giả định" and the grey limit card are all explained.

- **F1 (3.4, undefined term at first use).** "khoảng 600 lượt đăng ký học" – the unit "lượt đăng ký học" first appears here and is defined only on slide 4; a manager reads 600 as 600 students. Proposal: in 3.4 add "khoảng 600 lượt đăng ký học, tức 600 lần một sinh viên đăng ký một học phần,".
- **F2 (3.4, contradicts the deck's own term).** "khoảng 180 trong 600 lượt đăng ký học sẽ kết thúc mà không đạt" – 30% is the non-completion share, which slide 11 defines as "Không đạt hoặc Rút khỏi module"; "không đạt" alone suggests only failures. Proposal: "khoảng 180 trong 600 lượt đăng ký học sẽ không hoàn thành học phần (không đạt hoặc rút)".

### Slide 4 – 3
Coverage: complete. Unit, AQ, D1–D3, the four cards, status lines and the legend (cut-off days, early-warning rule) are all explained.

- **F3 (slide 4 slide text, AQ1 card, ambiguous Vietnamese).** "sinh viên không hoàn thành lần đầu bỏ lỡ bài vào tuần nào?" – "không hoàn thành lần đầu" can be read as "students who did not complete the first time". The notes (4.3) say it correctly: "sinh viên không hoàn thành bỏ lỡ bài lần đầu vào tuần nào". Proposal for the card: "sinh viên không hoàn thành bỏ lỡ bài lần đầu vào tuần nào?"

### Slide 5 – 3
Coverage: complete. Six mandatory conditions, scoring, UCI numbers, red cells, the orange OULAD row and the three selection conditions are all explained.

### Slide 6 – 3
Coverage: complete. The slide's "kết quả cần dự đoán / biến đầu vào" appear in the notes as "biến mục tiêu / đặc trưng", but the notes define both terms at once, so the link holds.

### Slide 7 – 3
Coverage: complete. The old rule, "1 trong 22", the three parts, the orange part, the legend, the two extra AQ2 signs and the flag rates are all explained; the notes add why late CMA is excluded.

### Slide 8 – 3
Coverage: complete. Timeline, grey vs red-cross legend, the four leak rows and the green evidence box are all explained. The evidence box is abstract on the slide, but the last paragraph of the notes resolves it ("điều quan trọng là không bản ghi nào khác thay đổi").

### Slide 9 – 3
Coverage: complete. The notes define S1, which slides 10 and 14 rely on.

- **F4 (slide 9 slide text, one metric under two names).** The card is titled "Tỷ lệ phát hiện trong giới hạn danh sách", while the example on the same slide, the notes (9.3) and the slide 10 table say "Tỷ lệ phát hiện". A reader may think these are two metrics. Proposal: card title "Tỷ lệ phát hiện (trong giới hạn danh sách)", or simply "Tỷ lệ phát hiện".

### Slide 10 – 3
Coverage: complete. Level 2, penalised logistic, the four status tiles, all four table rows and the S1 box (including why the normalised rate equals the last column) are explained. Numbers agree with slide 13 (41,5%) and slide 12 (15.724, 44,0%).

### Slide 11 – 3
Coverage: complete. 45,3% with interval, day 14, the definition of non-completion, yearly figures, bar colours, success criterion and confidence line are all explained.

### Slide 12 – 3
Coverage: complete. Five signs, risk difference, dot colours, error bars, dashed line, data scope, the three-part criterion and the "association, not cause" line are all explained.

### Slide 13 – 2
Coverage: complete; every card line is spoken. I followed the slide, but the AQ4 "Thứ tự" line stopped me (F5).

- **F5 (13.3 and slide 13 slide text, unclear basis, may mislead).** "trong mỗi nhóm hướng dẫn 20 sinh viên (một giảng viên phụ trách)" / "nhóm hướng dẫn gồm 20 sinh viên do một giảng viên hướng dẫn phụ trách". No earlier slide mentions tutor groups: slide 9 sets the list as "5 trên 20 sinh viên, tức 25% của một kỳ mở". A manager cannot tell whether these are real groups recorded in the data or a way of saying "per 20 students of a kỳ mở", and so whether 92,4% belongs to real tutors. Proposal (if the groups are a framing of the per-20 ratio): "Nếu chia mỗi kỳ mở thành các nhóm 20 sinh viên, cỡ một nhóm do một giảng viên hướng dẫn phụ trách, thì trong mỗi nhóm, sinh viên xếp hạng cao nhất …"; if they are real groups in the data, say so in one clause.

The opening of the notes, "chưa cho biết cán bộ nào nên liên hệ" (13.1), was readable as "which staff should make the call" and is not flagged.

### Slide 14 – 3
Coverage: complete. Each row is read in order, and the notes define "tinh chỉnh", log loss, S1 and Nhật ký thay đổi. The line "Nguồn: Bản tự đánh giá, Mục 1, Bảng 1.1; Báo cáo Milestone 5, Mục 3.2, 7, 10 và 13." comes after the notes: it is a source line, not speech, and no spoken text refers to it.

- **F6 (slide 14 slide text, last row, unnatural Vietnamese).** "…lên 13; Milestone 5 mới ghi" – the clause has no object and reads as cut off. The notes (14.5) say it fully: "một thay đổi đến Milestone 5 mới được ghi nhận". Proposal: "…lên 13; đến Milestone 5 mới được ghi nhận".

### Slide 15 – 3
Coverage: complete. All three takeaways and the bottom line are explained; the "9 to 16 points" figure matches slide 12 and "từ người thứ bảy" matches slide 13. The legal references appear only in the notes, which is appropriate for spoken detail.

### Slide 16 – 3
Coverage: complete.
