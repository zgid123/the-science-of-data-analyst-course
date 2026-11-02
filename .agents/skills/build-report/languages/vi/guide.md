# Vietnamese translation guide

This guide shapes every Vietnamese text of a task, the report twins (`*.vi.md`) as well as Vietnamese slides and presenter notes, so that each reads as if a Vietnamese academic had written it for Vietnamese readers and listeners, while the report stays structurally identical to the English file. Read it in full before translating, together with the task's glossaries (section 4).

The target is a Vietnamese text that a native reader finishes without noticing it was ever English: the meaning of the source, carried in Vietnamese sentence order, Vietnamese connectors and Vietnamese rhythm. What native reviewers actually change is recorded, with examples, in `lessons.md`; section 2.7 condenses it.

## 1. Write as a Vietnamese author

Work in three passes for each paragraph, slide or note:

1. **Understand.** Read the English unit in full and state its point to yourself in one Vietnamese sentence.
2. **Write.** Write that point in Vietnamese from scratch, in the order a Vietnamese author would use, then add the details. Translate the meaning and let Vietnamese set the word order.
3. **Read aloud.** Read the Vietnamese once with the English set aside. A sentence that needs the English to be understood is rewritten until it stands alone.

The principles below describe what that Vietnamese looks like.

- **Register.** Formal Vietnamese technical writing: complete sentences, precise terms, a calm and objective tone. Reports speak about "báo cáo", "nhóm tác giả", "người dùng"; slides and notes speak as "nhóm chúng em" (a solo presenter: "em") to "thầy cô và các bạn" (section 3).
- **Main point first.** Vietnamese places the topic early and the qualifications after it. Move long English pre-modifiers behind the noun ("a three-stage validated pipeline" → "quy trình ba giai đoạn đã được kiểm chứng") and lead with the claim, then its condition or source.
- **One clear subject per sentence.** Name who or what acts. When a sentence would start from an abstract noun or leave the actor implied, name the actor ("đặc trưng PAD của FSFM không tốt hơn…", not a subjectless "không cho đặc trưng…").
- **Verbs over stacked nouns.** Vietnamese carries actions in verbs: "hệ thống được triển khai và nhờ đó giảm…" reads better than "việc triển khai hệ thống giúp giảm…".
- **Voice.** An active sentence with a clear subject reads best. Use "được" for neutral or positive outcomes ("được công bố", "được chấp nhận") and "bị" for adverse ones ("bị chặn", "bị từ chối"). When the English names an agent with "by", write the agent as the subject or use "do … thực hiện" ("do NIST thực hiện").
- **Sentence length.** Split an English sentence that carries three ideas into two Vietnamese sentences; merge two short English sentences when Vietnamese joins them naturally with a connector.
- **Connectors with variety.** Link ideas cumulatively, each sentence adding evidence or detail to the one before, as the English does, and vary the link: "ngoài ra", "bên cạnh đó", "nhờ đó", "do đó", "vì vậy", "trên cơ sở đó", "đồng thời", "cụ thể là". Two adjacent sentences take two different connectors.
- **Reference words.** Repeat the noun or use "phương pháp này", "mô hình này", "hệ thống đó" to point back. Keep "nó" for spoken notes and short, unambiguous cases.
- **Time.** Mark time with dates and context; add "đã", "đang", "sẽ" where the time would otherwise be unclear.
- **Positive framing.** Keep the English report's style: state what is, what works and what is recommended.
- **Terms.** Use the glossary form; give the English in parentheses at a term's first use in a file when the glossary's Usage says so ("kho dữ liệu (Data Warehouse)"), and keep in English the terms Vietnamese engineers write in English: SQL-on-lake, chunk, embedding, pipeline, Router, typed API, Retrieval API, Query Engine, benchmark, snapshot, manifest, checksum, metadata, prompt, sandbox, blue-green, OCR, RAG, LLM, SSO, ETL, BI, schema, view, materialized view, backend, cache, Recall@k, p50/p95, deepfake, zero-shot.

## 2. From English patterns to natural Vietnamese

English sentence patterns carried over word for word are the main source of text that reads as translated. Each row gives the English habit, the natural Vietnamese form, and an example taken from reviewed project text.

### 2.1. Sentence structure

| English habit | Natural Vietnamese | Example (natural form) |
| :---- | :---- | :---- |
| Noun phrase as a whole sentence or label ("Two problems remain: …") | A full clause with a verb | "Hai bài toán vẫn còn mở: …" |
| A caption that begins with a predicate ("is the drop in …") | A caption that begins with its noun, capitalised | "Mức giảm số vụ lừa đảo kể từ khi đối chiếu sinh trắc học" |
| Keyword fragments joined with "·" or slashes | One short clause or sentence per idea | "Bổ sung cảm biến độ sâu, hồng ngoại hoặc nhiệt, như Face ID. Mạnh nhưng tốn kém." |
| Parenthetical apposition mid-sentence ("FSFM, the …, presented at …, answers …") | Two sentences: first introduce, then state | "FSFM, tức mô hình nền tảng cho an ninh khuôn mặt, được công bố tại CVPR 2025. Phương pháp giải quyết các hạn chế đó bằng…" |
| Fronted "Whichever …, the gate can be …" | Concession first with "Dù … thì/cũng …" | "Dù tấn công đi theo con đường nào, cổng kiểm soát cũng có thể sai theo hai cách." |
| "X, that is, Y" repeated as "tức" in every sentence | "tức là", "nghĩa là", "hay" in turn, or a new sentence | "Phát hiện tấn công trình diện, hay PAD, là…" |

### 2.2. Word choice

| English habit | Natural Vietnamese | Example (natural form) |
| :---- | :---- | :---- |
| "interfere with the operation" → "can thiệp vào hoạt động" | The verb that fits the purpose | "nhằm làm sai lệch hoạt động của hệ thống" |
| "transfer poorly" → "khó dùng chéo" | Say what happens | "khó dùng lẫn cho nhau", "khó giữ được hiệu quả khi gặp dữ liệu mới" |
| "the error users feel" → "lỗi tiện lợi" | Name the effect | "lỗi ảnh hưởng đến trải nghiệm người dùng" |
| "summary" of a network → "bản tóm tắt" | The technical term | "biểu diễn" |
| "slowly follows" → "chậm rãi đi theo" | The technical action | "cập nhật chậm theo" |
| "habits" of a method → "thói quen" | The word for a limitation | "hạn chế của cách làm quen thuộc" |
| "weakness" → "điểm yếu" | The glossary form | "điểm hạn chế", "hạn chế" |
| "expert" attacker → "chuyên sâu" | The usual collocation | "người tấn công chuyên nghiệp" |
| "custom masks" → "mặt nạ đặt riêng" | The full collocation | "mặt nạ đặt làm riêng" |
| "Keep … in mind" → "Hãy ghi nhớ" | A spoken, polite prompt | "Xin lưu ý Cấp độ 2, vì…" |

### 2.3. Questions, numbers and lists

| English habit | Natural Vietnamese | Example (natural form) |
| :---- | :---- | :---- |
| A yes/no question ending at the verb | End with "không" or "hay không" | "Sản phẩm xây dựng trên FSFM có đạt ISO 30107 Cấp độ 2 không?" |
| A how-question ending at the verb | End with "ra sao", "như thế nào" | "Cần kết hợp FSFM với bộ phát hiện tấn công chèn dữ liệu ra sao?" |
| "+200% injection attacks" as a label | Name the quantity, then the number's meaning | "Mức tăng số vụ tấn công chèn dữ liệu trong năm 2023" |
| "a", "an" translated as "một" everywhere | "một" only when the count matters | "Bộ phát hiện chấm cho mỗi khuôn mặt một điểm…" (count matters); "Mạng thầy nhìn khuôn mặt đầy đủ" (no count) |
| English plural on every noun | "các", "những" only where plurality matters | "Các tiêu chuẩn cũng phân chia theo đúng ranh giới này" |
| "A, B, and C" | "A, B và C" (no comma before "và") | "chủng tộc, sắc tộc và độ tuổi" |

### 2.4. A complete Vietnamese sentence

Vietnamese grammar carries meaning through word order and function words rather than inflection, so a sentence reads as complete when its core is visible and every function word earns its place.

- **Subject and predicate in view.** Each sentence has a subject (chủ ngữ) and a predicate (vị ngữ) that a reader can point to. A phrase such as "Khi kết nối bị gián đoạn sau lúc ngân hàng phát hành đã chấp thuận" is only a clause; it becomes a sentence once its main clause follows: "Khi kết nối bị gián đoạn sau lúc ngân hàng phát hành đã chấp thuận, giao dịch rơi vào trạng thái chưa rõ kết quả."
- **Head noun first, modifiers after.** Vietnamese places the head noun before its modifiers (danh từ trung tâm + định ngữ): "khóa riêng cho từng giao dịch", "bộ máy định giá có phiên bản". A chain of three or more modifiers is split with "có", "được", "dùng để" or a relative clause with "mà".
- **Relational pairs complete.** Paired connectives appear as pairs: "nếu … thì …", "vì … nên …", "tuy … nhưng …", "không chỉ … mà còn …", "vừa … vừa …", "càng … càng …". A sentence that opens one half carries the other.
- **Nominalisers in moderation.** "Việc" and "sự" turn a verb into a noun; Vietnamese prefers the verb itself. "Việc kiểm tra số dư được thực hiện trước" reads better as "Hệ thống kiểm tra số dư trước". One "việc" or "sự" per clause is the ceiling, and lexical words such as "sự cố", "sự kiện", "thực sự" are ordinary nouns, not nominalisers.
- **"Của" in short chains.** A chain of three "của" ("số dư của tài khoản của chủ thẻ của ngân hàng") is rewritten with a compound noun or a clause ("số dư trên tài khoản thẻ mà ngân hàng quản lý").
- **"Được" and "bị" with intent.** "Được" marks a neutral or welcome outcome and "bị" an adverse one (section 1). Three "được" in one sentence signal a chain of passives; turn at least one into an active clause with a named actor.
- **Classifiers and plural markers.** Formal technical prose rarely needs "cái", "con", "chiếc". "Các" marks a known, complete set and "những" a selected or open set; one marker per noun phrase ("các tổ chức", never "các những tổ chức").
- **Fixed collocations.** Use the established verb–noun pair: "đóng vai trò" (not "đóng một vai trò"), "đặt ra yêu cầu", "đưa ra quyết định", "tiến hành kiểm thử", "gây ra sự cố", "áp dụng quy định", "đáp ứng tiêu chuẩn".
- **Sentence length.** A sentence of about 25–45 syllables reads in one breath; past about 70 syllables, split it at its main connective and let the second sentence begin with a reference word ("Cơ chế này …", "Nhờ đó, …").
- **Formal openers.** In report prose, open sentences with a subject, a time or condition phrase, or a connective such as "Ngoài ra", "Do đó", "Tuy nhiên"; "Và", "Nhưng", "Mà", "Còn" at the start of a sentence belong to speech.

### 2.5. Coherence across sentences and paragraphs

A Vietnamese paragraph reads naturally when each sentence takes up what the previous one gave and adds one step (phép liên kết câu).

- **Linking devices.** Vietnamese links sentences by repetition of the key noun (phép lặp: "giao dịch … Giao dịch này …"), by substitution with a reference word (phép thế: "cơ chế này", "bước đó", "thành phần trên"), and by connectives (phép nối: "ngoài ra", "nhờ đó", "tuy vậy"). Each sentence after the first uses at least one of them.
- **Given before new.** A sentence starts from what the reader already has (the topic of the previous sentence) and ends with the new information: "Đảo giao dịch được gửi lặp lại cho đến khi có xác nhận. Nhờ cơ chế lặp lại này, khoản giữ tiền trên thẻ luôn được giải phóng."
- **Topic sentence first.** The first sentence of a paragraph states its point (câu chủ đề); the following sentences give the evidence, the mechanism and the consequence, in that order.
- **One term per concept.** Once a term is chosen from the glossary, it stays the same in the whole file; switching between near-synonyms ("đối soát", "khớp lệnh", "so khớp") makes a reader wonder whether three things are meant.
- **Paragraph bridges.** The last sentence of a paragraph prepares the next one, and the first sentence of a file links to the section before it, as in the English source.

### 2.6. Every section reads on its own, in Vietnamese

An English section of these reports carries the context it needs to be read on its own: it restates a key point before pointing to the section that develops it, keeps the definition, number or rule a sentence needs in the same paragraph, and gives every identifier its words. The Vietnamese twin carries the same self-contained context in Vietnamese form.

- **Identifiers with their words.** "kết quả chưa rõ sau khi hết thời gian chờ (C3.A1.1)", "đảo giao dịch có bảo đảm (P04)": the Vietnamese words carry the meaning and the identifier confirms the link, exactly where the English places them.
- **Restate, then point.** "số tiền ghi nhận không vượt quá số tiền được cấp phép cộng mức dung sai tiền boa (Mục 2.3.1)" keeps the restatement before the pointer.
- **Definitions where first needed.** A Vietnamese term defined in the English file at its first use is defined in the twin at the same place, with the English in parentheses when the glossary's Usage asks for it.
- **Exhibits introduced in the prose.** The sentence before a table or figure says in Vietnamese what it shows ("Bảng 1.3 liệt kê …", "Hình 2.1 cho thấy …").

### 2.7. Economy, explicitness and plain wording (what native reviewers change most)

A human review of a full report part (`lessons.md`, section 2) changed half of all paragraphs, and almost every change moved the text in one direction: **fewer words, but every phrase complete and concrete**. Writing this way from the start is the largest single gain in naturalness.

- **Drop words that carry no meaning.** "Một" before a known or ordinal item ("Nhóm thứ ba", not "Một nhóm thứ ba"), the time words "đã", "đang", "sẽ", "còn" where the context fixes the time, "chính", "mà" and "lường" in "đo lường" when a plain verb says it, and possessive pronouns ("của nó", "của chúng", "của mình", "của họ"). Repeat the noun instead of a pronoun: "Phạm vi của Phần 3", "chỉ số này", "nhóm tác giả này".
- **Name the head noun.** A phrase is complete when its head noun is there: "khái niệm đối lập với tấn công trình diện", "bài toán PAD", "tần suất tấn công thành công", "công sức tấn công", "tên gọi mới". In place of "việc + verb" for a process, name the thing that performs it: "cơ chế phát hiện", "khâu kiểm tra", "bài toán phân loại".
- **Say the action, not the image.** English figures of speech become the plain action they describe: "mở ra con đường … né tránh cảm biến" → "tạo ra đường tấn công … không đi qua cảm biến"; "nhìn xa hơn phân hệ PAD" → "đánh giá toàn bộ hệ thống thay vì riêng phân hệ PAD"; "hỏi bằng chứng đến từ đâu" → "xét nguồn bằng chứng"; "đổi loại lỗi này lấy loại lỗi kia" → "làm tăng loại lỗi này và giảm loại lỗi kia"; "hai đầu của trục" → "hai nguồn bằng chứng"; "trở thành một tín hiệu" → "là tín hiệu".
- **Choose the established word.** "trình bày" (not "xác lập") for what a section does, "cơ sở" (not "nền tảng") for a basis, "áp dụng" a standard (not "tuân theo"), "phân biệt A với B" (not "vạch ranh giới giữa"), "quy định về" for what a standard covers (not "đề cập đến"), "chứng minh rằng" for what a study shows, "ưu điểm và hạn chế", "giải pháp" for a hardware or software approach, "ghi nhận" for what a sensor records, "xử lý" data (not "làm việc trên"), "bỏ qua" for bypass, "mô phỏng" for what a replay imitates.
- **Use parentheses for side information.** A pointer, an affiliation, a year or a short gloss goes in parentheses instead of a relative clause: "Phần 2 (quá trình phát triển của các kỹ thuật)" rather than "Phần 2, nơi trình bày…"; "… sinh trắc học (Hình 1.1)" rather than "như Hình 1.1 thể hiện"; "Määttä, Hadid và Pietikäinen (Đại học Oulu)" rather than "thuộc Đại học Oulu"; "Face Flashing (2018)". Two authors with the same surname are told apart by initials: "Liu S.-Q. và cộng sự (2016)".
- **Connectives in their written form.** "nhưng" (not ", song"), "do" for a cause inside a sentence, "ví dụ" for an example, "Ngoài ra" for an addition, "Trên cơ sở" (not "Với") for what a section builds on, "Trong khi A …, thì B" for a contrast, "Như vậy" for a conclusion drawn from what precedes, "Tóm lại" for a closing paragraph, "hoặc" (not "hay") between alternatives in a statement, "là" (not "tức") when a sentence defines an abbreviation or a measure.
- **Defined abbreviations in use.** Once the full form and the abbreviation are given ("công cụ tấn công trình diện (PAI)"), the text uses the abbreviation, not the Vietnamese words again.
- **Structure stated explicitly.** A section introduction announces its subsections as a list with semicolons: "Cấu trúc của Mục 1.1 như sau: Mục 1.1.1 …; Mục 1.1.2 …; và Mục 1.1.4 …". A section that sums up ends with a separate paragraph beginning "Tóm lại,".

## 3. Slides and presenter notes

Slides are read in a glance and notes are spoken aloud, so each has its own form.

### 3.1. On the slide

- **Titles** are short noun phrases in sentence case ("Các chỉ số lỗi của PAD", "Hai tín hiệu học"); the section label above them names the part ("FSFM: phương pháp").
- **Every line is a short complete clause** that a presenter can read aloud as it stands: subject, verb, object. Write separate ideas as separate short sentences or bullets.
- **Labels under a large number** begin with a capitalised noun that names what the number measures ("Hồ sơ khách hàng đã được đối chiếu sinh trắc học, tính đến tháng 9/2026").
- **Card headings** are two to five words; card bodies are one or two sentences.
- **Questions** on a slide end with "không", "hay không" or "ra sao".
- **Captions under figures** say what the figure shows in one sentence, then its source ("Tái hiện từ Wang và cộng sự, CVPR 2025").
- **Numbers** follow section 7: decimal comma, "Cấp độ 2", dates as "7/2024" in labels and "tháng 7 năm 2024" in notes.

### 3.2. In the presenter notes

- **Spoken register.** Address the audience as "thầy cô và các bạn"; "ta" and "chúng ta" invite the audience along ("Hãy xem…", "Sau đây, mời thầy cô và các bạn…").
- **Who speaks, who wrote.** The presenting group calls itself "nhóm chúng em" (after naming it once in a note, "chúng em"); a solo presenter says "em". The authors of the work under review are "nhóm tác giả" or "các tác giả", and the work itself "bài báo". Each "nhóm" carries its qualifier: a bare "Nhóm sẽ đối chiếu…" leaves the listener guessing whose analysis it is. Every sentence names its actor: "Theo nhóm chúng em, đây là yếu tố đe dọa quan trọng nhất"; "Nhóm tác giả gọi đây là quy trình chuẩn bạc".
- **Open from the previous slide and hand over to the next.** The first sentence links back ("Các cấp độ này được áp dụng trong thực tế qua kiểm thử độc lập."); the last sentence leads on ("Tiếp theo, ta xem ai đang đặt ra yêu cầu cho PAD.").
- **Sentences of one breath.** About 15–30 words each, one idea each; a long English note becomes two or three Vietnamese sentences.
- **Explain each concept where the listener first meets it.** The slide itself defines the term where it first appears (slides.md section 2: every slide reads on its own); the note of that slide says it again in spoken words, in one plain sentence on what it is and why it matters here ("Tự nhất quán là cách chọn đáp án theo đa số…"), because a listener cannot look a term up mid-talk.
- **Spell out what the eye sees.** Point to the figure in words ("bên trái", "ở cột cuối", "màu đỏ thể hiện mức chú ý cao").
- **Numbers as spoken.** Write "10 triệu đồng", "hơn 173 triệu", "4,2%", "năm 2023"; give the meaning of a number in the same sentence.
- **Timing marker.** Each note starts with "(~N giây)", matching the English note.

## 4. Terms: applying the glossaries

The glossaries (`glossaries/`, explained in its README) give each recurring English term one Vietnamese form, in three layers: `common/` for every computer-science report, then the domain and topic files the task names in `tasks.toml`.

1. Before the first file of a task, print the merged glossary once: `glossary.py --lang vi --task <task> show`. Keep it at hand; `glossary.py … lookup "<term>"` answers a single question later.
2. Use the form of the most specific layer that defines a term (topic, then domain, then common).
3. Follow the Usage column: write the Vietnamese with the English in parentheses at a term's first use in a file when the Usage says so, keep the English where it says "Keep English", and reuse its typical phrase.
4. Translate a group row in order: `training / pretraining / fine-tuning` maps to `huấn luyện / tiền huấn luyện / tinh chỉnh` term by term.
5. A term missing from every layer: choose the established Vietnamese term by sections 1 and 2, use it consistently, and add a row to the right layer (glossaries README, "Choosing the layer") as soon as it recurs; add earlier variants to Replaces.
6. Proper names, product and method names (FSFM, iBeta, OpenAlex), codes and identifiers stay as written; glossaries cover terms, not names.
7. A concept that Vietnamese law regulates takes the wording of the Vietnamese legal text, read in its Vietnamese original rather than in an English translation: for card payments, Circular 18/2024/TT-NHNN says "tổ chức thanh toán thẻ", "đơn vị chấp nhận thẻ", "tra soát", and these forms go into the domain glossary with the article they come from in Usage. A reader who knows the regulation then recognises its terms.

8. A term is right only if a Vietnamese colleague would say it. A noun phrase built to mirror the English ("lượt đăng ký học phần về sau không đạt hoặc rút học phần", "khả năng xem xét", "đợt học", "mốc xem xét") makes every sentence slow even when each word is correct; take the everyday word of the field ("sinh viên về sau không hoàn thành học phần", "số sinh viên cán bộ liên hệ được mỗi tuần", "học phần", "đợt lập danh sách") and keep the technical unit only where the text defines or counts it. When unsure, test the term in a sentence a lecturer would say aloud: a native reader heard "lớp học phần" as a class section rather than the course, and "năng lực xử lý" as machine capacity (lessons T6).

The checks report every variant listed in a Replaces column, in the sources, the Word document and slides, so a fixed term stays fixed across files and reports.

## 5. Orthography and typography

- Headings, captions and table headers take Vietnamese sentence case: only the first word and proper nouns are capitalised ("Kiến trúc dữ liệu cho hệ thống BI", "Bảng 3.6. Các chỉ số đánh giá").
- Use the modern tone placement on the main vowel: hóa, khóa, thủy, lũy, quý.
- Punctuation follows the word without a space and takes one space after it; quotation marks are straight double quotes as in the English source (the Word build renders them as “…”).
- No comma before "và" or "hoặc", whether they join list items or clauses ("bổ sung cho nhau và …"); clauses of an enumeration are separated by semicolons; a colon introduces an explanation that follows ("khác nhau về quy mô: tấn công trình diện …").
- Abbreviations: write the Vietnamese full form at first use with the abbreviation in parentheses, then the abbreviation alone. Use an official Vietnamese abbreviation where one exists (NHNN, CCCD, Bộ GDĐT); otherwise keep the international one (PAD, FAS, ViT).
- Titles and honorifics: Dr. → TS., Assoc. Prof. Dr. → PGS.TS., Prof. → GS.

## 6. Structure (identical to the English file)

- One `.vi.md` per English file, with the same base name and the same order.
- Headings keep their level and number prefix (`## 2.3.`, `### 3.5.10.`); translate the heading text.
- Tables keep their rows, columns, alignment row and bold markers; translate cell text and keep identifiers.
- Lists keep their item count and bold lead-ins.
- Figures keep the image path and `{width=100%}`; the alt text becomes the caption and starts with "Hình" ("Hình 2.1. …").
- Table captions start with "Bảng" and keep their number (`**Bảng 3.6. …**`).
- Footnote labels (`[^layers]`), code fences and block-quote markers stay as in the source; translate block-quote prose.
- Formulas (`$…$`, `$$…$$`) are copied character for character; translate the prose around them.
- Citations (`[n]`, or `[Sxxx]` in a draft) stay where the English places them, with the same numbers in the same order.
- Code and identifiers stay as written: anything in backticks, field and table names, tool names, error codes, test categories, file paths and SQL; also people's names, student IDs, cohort codes (K2021) and official document codes (08/2021/TT-BGDĐT, 2345/QĐ-NHNN).
- House formatting: the en dash "–" for ranges, pairs and asides, and ordered lists numbered `(1)`, `(2)`, `(3)`.
- Front-matter pages keep the row order of the English pages and have forms of their own (lessons F2):
  - terms page (`00-2-*`): each term cell opens with the English term exactly as the English page writes it, then an en dash and the Vietnamese name ("Acquirer – Tổ chức thanh toán thẻ"); a term kept in English in the text still receives a Vietnamese name here ("Deepfake – Video giả mạo bằng công nghệ học sâu"), and the introduction says the terms follow the alphabetical order of the English terms;
  - abbreviation list (`00-1-*`): the abbreviation, then the Vietnamese full form with the English expansion after "–" ("Tỷ lệ lỗi phân loại trung bình – Average classification error rate");
  - title page: names, student IDs, titles of lecturers, course and date exactly as the authors give them; university and faculty as one block ("TRƯỜNG ĐẠI HỌC KHOA HỌC TỰ NHIÊN" over "KHOA CÔNG NGHỆ THÔNG TIN"), then "Giảng viên giảng dạy và hướng dẫn:" with the lecturers first and "Thực hiện: Nhóm N" with the members, each label ending in a colon with its names below it, as the user's reviewer laid it out.

## 7. Numbers, dates and labels

| English | Vietnamese |
| --- | --- |
| Figure 2.1 / Table 3.6 | Hình 2.1 / Bảng 3.6 |
| Section 3.5.3 / Part 3 | Mục 3.5.3 / Phần 3 |
| Appendix I, item 4 | Phụ lục I, mục 4 |
| Step 1 … Step 10 | Bước 1 … Bước 10 |
| Q1, Q2, Q3 | CH1, CH2, CH3 |
| Level 1 … Level 4 (C4 model) | Cấp 1 … Cấp 4 |
| Level 1 … Level 3 (certification levels) | Cấp độ 1 … Cấp độ 3; "ISO 30107 Cấp độ 2" |
| 0.85, 6.4/10, ±0.01, 4.81% | 0,85, 6,4/10, ±0,01, 4,81% (decimal comma in prose, tables and slides) |
| 10,000; 1,607 | 10.000; 1.607 (dot as thousands separator) |
| 1 September 2026, 10 January 2023, September 2026 | 01/09/2026, 10/01/2023 (two-digit day and month), tháng 9 năm 2026 |
| Ho Chi Minh City, October 2026 (title page) | Thành phố Hồ Chí Minh, tháng 10 năm 2026 |
| ISO dates in examples (2026-09-01) | as written |
| Group 4 | Nhóm 4 |
| [12], [3], [5] (citations) | as written |
| Standards, versions, licences: ISO/IEC 30107-3:2023, v4.1, Python 3.9.21, CC BY-NC 4.0 | as written ("phiên bản 4.1") |
| "more than 173 million", "over 59%" | "hơn 173 triệu", "hơn 59%" |
| "eightfold", "3×" | "gấp tám lần", "gấp ba lần" |

## 8. Quotations

- An English quotation that carries a definition or a source's exact claim is translated into Vietnamese inside the quotation marks, with the same citation. For a normative definition (a standard, a law), the original English follows in parentheses inside the quotation on its first use, so the exact wording stays checkable.
- Names and titles quoted as such (paper titles, standard titles, product names) keep their original language; a Vietnamese gloss may follow in parentheses.
- A Vietnamese-language quotation (a legal text, an official statement) is kept verbatim. Where the English adds an explanatory rendering after it ("that is, …"), the Vietnamese twin ends with the quotation itself, because it already reads in Vietnamese.
- Punctuation follows the closing quotation mark when a citation follows: `"…" [12].`
- Text inside quotation marks is exempt from the untranslated-text check, so a kept original reads cleanly.

## 9. References

Keep APA formatting. Sources keep their original titles, English or Vietnamese. Translate only the list's heading ("# Tài liệu tham khảo") and its introductory sentence; the entries stay as in the English file. A reference slide keeps the original titles in their short form ("Wang et al. (2025). FSFM: … CVPR.").

## 10. Pages that only the Vietnamese report carries

Vietnamese university reports often open with pages the English report leaves out. `templates/` holds ready pages, named so that they sort after the title page and are recognised as Vietnamese-only (`extra_files` in `pack.toml`):

| Template | Page | When |
| :---- | :---- | :---- |
| `00-0a-loi-cam-on.vi.md` | Lời cảm ơn (acknowledgements) | When the course or the user asks for it |
| `00-0b-loi-cam-doan.vi.md` | Lời cam đoan (statement of originality) | Theses and graded reports that require it |

Offer these pages to the user at the first Vietnamese build, copy the chosen ones into the report folder and fill in their placeholders together with the user; the Word post-check lists any placeholder still open.

## 11. Before marking a file or deck translated

The translator's own checks come first; a native reviewer then reads every file with the checklist in `review.md` (reference.md section 4.4).

1. **Checks pass.** `check_parity.py` passes for each report pair (structure, citations, formulas, conventions); `check_slides.py --lang vi` passes for a deck, with its warnings read and resolved.
2. **Terms follow the glossaries.** Each new recurring term has its row in the right layer, so later files and reports follow it.
3. **Read-aloud pass.** Read every paragraph, slide line and note aloud once with the English set aside. Each sentence has a clear subject, one main idea and a natural ending; questions end with "không", "hay không" or "ra sao"; captions and labels start with a capitalised noun.
4. **Pattern pass.** Scan the text against the tables of section 2, the grammar rules of sections 2.4–2.6 and the economy rules of section 2.7, and rewrite any line that follows an English habit listed there.
5. **Connector pass.** Adjacent sentences use different connectors, and each paragraph or note builds on the one before it.
