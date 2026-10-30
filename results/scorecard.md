# ADLC scorecard

181 runs · tasks 16 · arms ['baseline', 'graphify', 'graphify-guard', 'serena']

## By arm

| arm | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 46 | 89,698/167,288 | 18 | 1,538 | 5 | 1 | 22.6s/42.2s | 5 | 13,646 | 85% | 80% | 0.46 |
| graphify | 45 | 205,086/305,983 | 21 | 2,006 | 7 | 1 | 32.1s/60.5s | 7 | 12,363 | 88% | 100% | 0.34 |
| graphify-guard | 45 | 242,535/453,978 | 24 | 2,272 | 8 | 1 | 37.8s/74.4s | 8 | 13,960 | 83% | 93% | 0.48 |
| serena | 45 | 90,028/172,588 | 15 | 1,583 | 5 | 1 | 22.9s/43.8s | 5 | 12,549 | 86% | 87% | 0.51 |

## By arm × category

| arm | category | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | archaeology | 1 | 55,656/55,656 | 13,696 | 1,995 | 5 | 1 | 15.5s/15.5s | 5 | 21,764 | 100% | — | — |
| baseline | edit | 15 | 154,022/180,263 | 24 | 2,230 | 8 | 1 | 36.9s/49.5s | 8 | 14,486 | 80% | 80% | 0.18 |
| baseline | literal | 9 | 46,534/64,006 | 9 | 428 | 3 | 1 | 10.0s/12.1s | 3 | 854 | 83% | — | 0.29 |
| baseline | locate | 6 | 71,422/107,126 | 15 | 1,206 | 5 | 1 | 16.5s/20.3s | 5 | 11,961 | 100% | — | 0.32 |
| baseline | trace | 15 | 88,730/105,605 | 15 | 1,523 | 5 | 1 | 23.1s/32.3s | 5 | 16,026 | 83% | — | 0.19 |
| graphify | edit | 15 | 263,742/319,554 | 27 | 2,558 | 9 | 1 | 38.5s/67.5s | 9 | 12,363 | 100% | 100% | 0.17 |
| graphify | literal | 9 | 130,764/167,298 | 15 | 738 | 5 | 1 | 16.4s/18.9s | 5 | 3,167 | 83% | — | 0.25 |
| graphify | locate | 6 | 169,892/262,076 | 22 | 1,902 | 8 | 1 | 29.3s/33.5s | 8 | 11,790 | 100% | — | 0.30 |
| graphify | trace | 15 | 205,432/324,818 | 21 | 2,224 | 7 | 1 | 32.3s/59.7s | 7 | 24,957 | 73% | — | 0.32 |
| graphify-guard | edit | 15 | 266,237/285,497 | 27 | 2,485 | 9 | 1 | 42.4s/63.8s | 9 | 12,946 | 93% | 93% | 0.14 |
| graphify-guard | literal | 9 | 103,750/167,967 | 12 | 581 | 4 | 1 | 13.1s/19.9s | 4 | 2,942 | 89% | — | 0.28 |
| graphify-guard | locate | 6 | 184,223/284,855 | 20 | 1,754 | 6 | 1 | 28.4s/38.9s | 6 | 17,190 | 83% | — | 0.29 |
| graphify-guard | trace | 15 | 407,615/504,546 | 36 | 3,975 | 12 | 1 | 61.3s/86.4s | 12 | 34,310 | 70% | — | 0.36 |
| serena | edit | 15 | 163,444/200,674 | 27 | 2,187 | 8 | 1 | 39.1s/64.6s | 8 | 13,141 | 87% | 87% | 0.20 |
| serena | literal | 9 | 45,332/55,343 | 9 | 246 | 3 | 1 | 10.4s/11.5s | 3 | 474 | 83% | — | 0.26 |
| serena | locate | 6 | 76,180/97,702 | 14 | 1,080 | 4 | 1 | 19.2s/24.6s | 4 | 8,436 | 92% | — | 0.21 |
| serena | trace | 15 | 86,540/106,090 | 15 | 1,583 | 5 | 1 | 22.0s/27.9s | 5 | 14,652 | 83% | — | 0.23 |

## By arm × language

| arm | languages | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | csharp | 3 | 110,979/129,640 | 18 | 2,230 | 6 | 1 | 30.0s/30.0s | 6 | 13,394 | 100% | 100% | 0.17 |
| baseline | docs | 1 | 55,656/55,656 | 13,696 | 1,995 | 5 | 1 | 15.5s/15.5s | 5 | 21,764 | 100% | — | — |
| baseline | java | 6 | 119,828/156,777 | 22 | 1,580 | 6 | 1 | 29.9s/54.2s | 6 | 19,754 | 67% | 33% | 0.31 |
| baseline | python | 15 | 63,117/174,871 | 15 | 1,454 | 5 | 1 | 17.6s/36.8s | 5 | 13,640 | 77% | 100% | 0.62 |
| baseline | typescript | 21 | 88,730/160,040 | 15 | 1,375 | 5 | 1 | 23.1s/42.4s | 5 | 12,225 | 93% | 83% | 0.40 |
| graphify | csharp | 3 | 202,849/235,927 | 21 | 2,128 | 7 | 1 | 32.1s/37.2s | 7 | 12,363 | 100% | 100% | 0.09 |
| graphify | java | 6 | 243,218/265,796 | 26 | 1,819 | 8 | 1 | 34.1s/66.2s | 8 | 10,616 | 100% | 100% | 0.20 |
| graphify | python | 15 | 205,086/302,452 | 21 | 2,224 | 7 | 1 | 31.3s/53.6s | 7 | 15,175 | 70% | 100% | 0.43 |
| graphify | typescript | 21 | 199,404/322,824 | 21 | 2,005 | 7 | 1 | 31.5s/60.9s | 7 | 11,906 | 95% | 100% | 0.33 |
| graphify-guard | csharp | 3 | 207,989/254,923 | 21 | 2,324 | 7 | 1 | 32.1s/37.4s | 7 | 12,796 | 100% | 100% | 0.18 |
| graphify-guard | java | 6 | 265,474/284,855 | 27 | 2,332 | 9 | 1 | 38.7s/49.2s | 9 | 15,136 | 83% | 67% | 0.15 |
| graphify-guard | python | 15 | 218,310/396,124 | 21 | 2,194 | 7 | 1 | 35.3s/61.3s | 7 | 13,339 | 77% | 100% | 0.52 |
| graphify-guard | typescript | 21 | 276,869/503,294 | 27 | 2,221 | 9 | 1 | 45.5s/76.9s | 9 | 15,136 | 86% | 100% | 0.49 |
| serena | csharp | 3 | 128,932/141,364 | 21 | 2,150 | 7 | 1 | 29.8s/32.2s | 7 | 13,069 | 100% | 100% | 0.12 |
| serena | java | 6 | 113,237/155,271 | 26 | 1,648 | 7 | 1 | 29.6s/41.3s | 7 | 12,916 | 58% | 33% | 0.23 |
| serena | python | 15 | 61,022/153,717 | 15 | 1,866 | 5 | 1 | 17.5s/37.0s | 5 | 13,170 | 77% | 100% | 0.59 |
| serena | typescript | 21 | 86,540/190,900 | 15 | 1,277 | 5 | 1 | 20.9s/58.0s | 5 | 10,579 | 98% | 100% | 0.54 |

## By arm × resolved model

| arm | models | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | gpt-6-luna | 37 | 91,584/166,416 | 15 | 1,375 | 5 | 1 | 23.5s/42.8s | 5 | 11,049 | 84% | 79% | 0.45 |
| baseline | gpt-6-luna,copilot-search-a | 9 | 70,602/120,479 | 13,425 | 2,288 | 6 | 1 | 19.1s/34.4s | 6 | 19,736 | 89% | 100% | 0.44 |
| graphify | gpt-6-luna | 44 | 205,259/308,150 | 21 | 2,006 | 7 | 1 | 32.2s/60.6s | 7 | 12,221 | 88% | 100% | 0.34 |
| graphify | gpt-6-luna,copilot-search-a | 1 | 141,600/141,600 | 19,309 | 3,150 | 8 | 1 | 27.1s/27.1s | 8 | 28,403 | 100% | — | — |
| graphify-guard | gpt-6-luna | 45 | 242,535/453,978 | 24 | 2,272 | 8 | 1 | 37.8s/74.4s | 8 | 13,960 | 83% | 93% | 0.48 |
| serena | gpt-6-luna | 39 | 89,461/176,951 | 15 | 1,277 | 5 | 1 | 22.9s/44.1s | 5 | 10,698 | 85% | 86% | 0.53 |
| serena | gpt-6-luna,copilot-search-a | 6 | 97,702/123,866 | 14,625 | 2,778 | 7 | 1 | 23.2s/32.0s | 7 | 27,845 | 92% | 100% | 0.30 |

## KB currency (artifact staleness at query time, commits behind HEAD)

| arm | p50 | p95 | graph queries p50 |
|---|---|---|---|
| baseline | 0 | 0 | 0 |
| graphify | 0 | 0 | 0 |
| graphify-guard | 0 | 0 | 1 |
| serena | 0 | 0 | 0 |

## Per task

| task | arm | n | tokens p50 | calls p50 | wall p50 | correctness | tokens CV |
|---|---|---|---|---|---|---|---|
| ops-001 | baseline | 1 | 55,656 | 5 | 15.5s | 100% | — |
| svc-001 | baseline | 3 | 45,877 | 3 | 9.1s | 100% | 0.18 |
| svc-001 | graphify | 3 | 101,874 | 4 | 13.0s | 100% | 0.23 |
| svc-001 | graphify-guard | 3 | 131,635 | 5 | 17.0s | 100% | 0.26 |
| svc-001 | serena | 3 | 46,085 | 3 | 10.4s | 100% | 0.19 |
| svc-002 | baseline | 3 | 99,654 | 5 | 18.5s | 100% | 0.28 |
| svc-002 | graphify | 3 | 256,304 | 8 | 32.2s | 100% | 0.26 |
| svc-002 | graphify-guard | 3 | 268,243 | 9 | 34.5s | 100% | 0.21 |
| svc-002 | serena | 3 | 95,782 | 7 | 22.6s | 83% | 0.04 |
| svc-003 | baseline | 3 | 95,045 | 6 | 32.5s | 33% | 0.08 |
| svc-003 | graphify | 3 | 275,611 | 9 | 46.5s | 17% | 0.24 |
| svc-003 | graphify-guard | 3 | 407,615 | 12 | 65.4s | 33% | 0.09 |
| svc-003 | serena | 3 | 98,380 | 5 | 29.9s | 33% | 0.25 |
| svc-004 | baseline | 3 | 62,162 | 6 | 17.6s | 100% | 0.13 |
| svc-004 | graphify | 3 | 205,086 | 7 | 31.3s | 83% | 0.16 |
| svc-004 | graphify-guard | 3 | 249,519 | 8 | 39.4s | 83% | 0.24 |
| svc-004 | serena | 3 | 61,022 | 5 | 17.5s | 100% | 0.30 |
| svc-006 | baseline | 3 | 30,321 | 2 | 6.7s | 50% | 0.38 |
| svc-006 | graphify | 3 | 130,764 | 5 | 15.5s | 50% | 0.25 |
| svc-006 | graphify-guard | 3 | 101,062 | 4 | 11.6s | 67% | 0.15 |
| svc-006 | serena | 3 | 30,462 | 2 | 5.5s | 50% | 0.00 |
| svc-008 | baseline | 3 | 177,017 | 9 | 36.9s | 100% | 0.02 |
| svc-008 | graphify | 3 | 282,123 | 9 | 44.9s | 100% | 0.16 |
| svc-008 | graphify-guard | 3 | 240,496 | 8 | 37.8s | 100% | 0.16 |
| svc-008 | serena | 3 | 163,444 | 8 | 37.5s | 100% | 0.08 |
| svc-009 | baseline | 3 | 110,979 | 6 | 30.0s | 100% | 0.17 |
| svc-009 | graphify | 3 | 202,849 | 7 | 32.1s | 100% | 0.09 |
| svc-009 | graphify-guard | 3 | 207,989 | 7 | 32.1s | 100% | 0.18 |
| svc-009 | serena | 3 | 128,932 | 7 | 29.8s | 100% | 0.12 |
| svc-010 | baseline | 3 | 141,723 | 8 | 42.1s | 33% | 0.13 |
| svc-010 | graphify | 3 | 230,132 | 8 | 36.6s | 100% | 0.12 |
| svc-010 | graphify-guard | 3 | 264,710 | 9 | 41.4s | 67% | 0.06 |
| svc-010 | serena | 3 | 148,613 | 8 | 39.1s | 33% | 0.10 |
| web-001 | baseline | 3 | 60,649 | 4 | 11.9s | 100% | 0.12 |
| web-001 | graphify | 3 | 131,629 | 5 | 17.5s | 100% | 0.10 |
| web-001 | graphify-guard | 3 | 131,339 | 5 | 15.9s | 100% | 0.18 |
| web-001 | serena | 3 | 53,957 | 3 | 11.2s | 100% | 0.12 |
| web-002 | baseline | 3 | 62,697 | 5 | 15.7s | 100% | 0.23 |
| web-002 | graphify | 3 | 135,639 | 5 | 21.5s | 100% | 0.19 |
| web-002 | graphify-guard | 3 | 163,877 | 6 | 23.4s | 67% | 0.14 |
| web-002 | serena | 3 | 62,255 | 4 | 16.0s | 100% | 0.01 |
| web-003 | baseline | 3 | 88,730 | 5 | 23.5s | 100% | 0.07 |
| web-003 | graphify | 3 | 164,425 | 6 | 30.2s | 100% | 0.17 |
| web-003 | graphify-guard | 3 | 223,158 | 8 | 28.2s | 100% | 0.46 |
| web-003 | serena | 3 | 90,028 | 5 | 20.9s | 100% | 0.19 |
| web-004 | baseline | 3 | 90,665 | 7 | 24.2s | 100% | 0.11 |
| web-004 | graphify | 3 | 235,652 | 8 | 42.1s | 100% | 0.23 |
| web-004 | graphify-guard | 3 | 503,294 | 13 | 92.7s | 83% | 0.39 |
| web-004 | serena | 3 | 86,540 | 5 | 22.9s | 100% | 0.13 |
| web-005 | baseline | 3 | 86,903 | 5 | 18.6s | 83% | 0.14 |
| web-005 | graphify | 3 | 180,819 | 6 | 29.1s | 67% | 0.31 |
| web-005 | graphify-guard | 3 | 452,858 | 13 | 66.7s | 50% | 0.02 |
| web-005 | serena | 3 | 85,694 | 5 | 18.6s | 83% | 0.12 |
| web-009 | baseline | 3 | 160,040 | 8 | 30.7s | 67% | 0.08 |
| web-009 | graphify | 3 | 279,125 | 9 | 37.2s | 100% | 0.12 |
| web-009 | graphify-guard | 3 | 282,080 | 9 | 45.5s | 100% | 0.02 |
| web-009 | serena | 3 | 173,671 | 8 | 44.0s | 100% | 0.09 |
| web-010 | baseline | 3 | 148,095 | 8 | 49.5s | 100% | 0.05 |
| web-010 | graphify | 3 | 268,022 | 9 | 60.9s | 100% | 0.12 |
| web-010 | graphify-guard | 3 | 276,869 | 9 | 65.0s | 100% | 0.07 |
| web-010 | serena | 3 | 190,900 | 8 | 69.0s | 100% | 0.11 |

Models seen: copilot-search-a, gpt-6-luna · Copilot versions: 1.0.105

---

**Metric confidence.** `prompt tokens` = input + cache_read + cache_write per session (Copilot's `input.tokenCount` alone is only the uncached slice — 15–40 tokens in practice — so it is shown separately). Tokens, model calls, turns, tool calls and API time come from Copilot CLI `events.jsonl` (`session.shutdown`, `session.usage_record`) — primary. `premium_requests` is the billing number from the same event, cross-checked against the stdout `result` event; it counts prompts × model multiplier, not model calls (github/copilot-cli#1582 documents the interactive `/usage` undercount; we do not use `/usage`). `bytes_read` is a proxy: result length of view/grep/glob/bash tool calls. Model is `auto` unless pinned; tables list every resolved model and Copilot version seen — compare within a model only. No single-run number appears anywhere: every cell is a median (p50) or p90 over ≥ 3 runs.
