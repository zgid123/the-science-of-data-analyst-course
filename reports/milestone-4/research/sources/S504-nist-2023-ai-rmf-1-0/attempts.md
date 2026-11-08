# Fetch attempts

| Run | Tier | URL | HTTP | Type | KB | Converter | Words | Verdict | Reasons |
| :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- | :---- |
| 2026-11-06T23:08+07:00 | L1 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 200 | application/pdf | 1900 | pdfkit | 15217 | partial | 12 words lost a ligature (fi/ff/fl): quotes may not match |
| 2026-11-06T23:08+07:00 | L1 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 200 | application/pdf | 1900 | pypdf | 15212 | partial | 12 words lost a ligature (fi/ff/fl): quotes may not match |
| 2026-11-06T23:08+07:00 | L1 | https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 200 | application/pdf | 1900 | pdf-stdlib | 15213 | partial | 19 words lost a ligature (fi/ff/fl): quotes may not match |
| 2026-11-06T23:08+07:00 | L3 | https://web.archive.org/web/2id_/https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf | 0 | – | 0 | – | 0 | error | curl: (7) Failed to connect to web.archive.org port 443 after 244 ms: Couldn't connect to server |
