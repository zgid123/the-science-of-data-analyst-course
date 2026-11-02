# Vietnamese glossaries

The glossaries fix one Vietnamese form for each recurring English term, so every file of a report, and every report on the same subject, uses the same words. They are organised in three layers, from general to specific.

| Layer | Folder | Loaded | Holds |
| :---- | :---- | :---- | :---- |
| Common | `common/` | For every report | Technical-reporting vocabulary of computer science: report writing, research and evaluation, software and systems, data and databases, AI and machine learning, security and privacy, standards and regulation |
| Domain | `domains/` | When a task selects it | A field that several reports can share: higher education, biometrics and PAD, digital banking in Vietnam |
| Topic | `topics/` | When a task selects it | The vocabulary of one report: its own concepts, component names and research-question labels |

A task selects its domain and topic files in `tasks.toml`:

```toml
[taskN.vi]
glossaries = ["higher-education", "university-bi-chatbot"]   # common/* is always included
```

When a term appears in more than one layer, the most specific one applies (topic, then domain, then common). This lets a field give a general word its own sense, for example a domain may translate "template" as *mẫu sinh trắc học* while common software usage keeps *mẫu*.

## Row format

| Column | Content |
| :---- | :---- |
| English | The term as it appears in the English source; group close forms with " / " (`training / pretraining / fine-tuning`) |
| Vietnamese | The form to use, in the same order as the English group |
| Usage | How to use it: first-use form with the English in parentheses, when the English stays, a typical phrase |
| Replaces | Variants seen in earlier translations, comma-separated; the checks report each one as an error that names the form to use |

## Choosing the layer for a new term

1. A term any computer-science report could use (a method, a metric, a system quality, a reporting phrase) goes into the matching `common/` file.
2. A term that belongs to a field shared by several reports goes into that field's `domains/` file; a new field gets a new file named after it.
3. A term only one report needs (its research-question labels, its architecture names) goes into that report's `topics/` file. A topic keeps only such names; a term that a second report could use moves up to its domain or to common, so each layer stays as small as its scope.
4. A usage note describes the role of a form (a part title, a section heading, a table column), not a section or table number, so the glossary reads on its own, without the report it came from.
5. When a translation used a different word before, add that word to Replaces, so the checks keep every report consistent. In a shared layer, Replaces lists only words that are wrong in every report; a word one report rejected but another uses correctly stays in that report's topic as an override row.

After editing, run `glossary.py --lang vi lint`: it confirms each term has one meaning in the common layer, each variant points to one form, and no variant is itself a preferred form elsewhere.
