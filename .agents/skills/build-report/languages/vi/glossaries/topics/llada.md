# Topic glossary: LLaDA for Vietnamese historical question answering

The vocabulary of one deck: the presentation of "Exploring the Capabilities of Large Language Diffusion Models for Vietnamese Historical Question Answering: A Case Study on Tư Trị Thông Giám". It fixes the project's own names (phase-aware block diffusion, the reasoning QA setting, the chronicle's year titles and question types); the diffusion vocabulary comes from the domain glossary `diffusion-language-models` and the QA and evaluation terms from the common layer. "Reasoning" is written "lập luận" throughout, so that "suy luận" keeps its common-glossary meaning of model inference. Model, dataset, library and format names (LLaDA-8B-Base, LLaDA-8B-Instruct, LLaMA-3-Instruct, Qwen 3.5-4B, Gemini 3.1 Flash Lite, UIT-ViQuAD, PhoBERT, PhoGPT, VinaLLaMA, pydantic, rapidfuzz, faiss, JSONL, ShareGPT, Alpaca) stay as written, as does the title of the chronicle, Tư Trị Thông Giám.

## Models and diffusion

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| phase-aware block diffusion | khuếch tán theo khối nhận biết giai đoạn | "giải mã nhận biết giai đoạn" as the short form | |
| reasoning / reasoning trace | lập luận / chuỗi lập luận | Not "suy luận", which means inference | |

## QA settings and evaluation

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| reasoning QA | hỏi đáp có lập luận | | |

## Dataset pipeline

| English | Vietnamese | Usage | Replaces |
| --- | --- | --- | --- |
| chronicle | bộ biên niên sử | | |
| year title | tiêu đề năm | "Năm thứ hai mươi ba (Mậu Dần – TCN 403)" | |
| sexagenary era name | tên năm can chi | | |
| reverse question | câu hỏi ngược | Gives the object and asks for the subject; chip and table label "Hỏi ngược" | câu đảo chiều |
