# ADLC scorecard

144 runs · tasks 12 · arms ['baseline', 'graphify', 'graphify-guard', 'serena']

## By arm

| arm | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | 36 | 87,374/167,288 | 15 | 1,414 | 5 | 1 | 19.3s/39.7s | 5 | 12,932 | 86% | 89% | 0.49 |
| graphify | 36 | 203,980/318,737 | 21 | 2,014 | 7 | 1 | 31.4s/60.4s | 7 | 13,796 | 85% | 100% | 0.38 |
| graphify-guard | 36 | 241,516/461,881 | 24 | 2,209 | 8 | 1 | 38.6s/75.6s | 8 | 14,238 | 82% | 100% | 0.51 |
| serena | 36 | 76,446/181,870 | 15 | 1,325 | 5 | 1 | 20.1s/44.3s | 5 | 10,638 | 89% | 100% | 0.58 |

## By arm × category

| arm | category | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | edit | 9 | 162,925/182,733 | 24 | 2,253 | 8 | 1 | 36.9s/49.5s | 8 | 14,544 | 89% | 89% | 0.08 |
| baseline | literal | 9 | 46,534/64,006 | 9 | 428 | 3 | 1 | 10.0s/12.1s | 3 | 854 | 83% | — | 0.29 |
| baseline | locate | 3 | 62,697/76,656 | 15 | 758 | 5 | 1 | 15.7s/17.0s | 5 | 3,207 | 100% | — | 0.23 |
| baseline | trace | 15 | 88,730/105,605 | 15 | 1,523 | 5 | 1 | 23.1s/32.3s | 5 | 16,026 | 83% | — | 0.19 |
| graphify | edit | 9 | 279,125/326,717 | 27 | 3,005 | 9 | 1 | 48.8s/63.1s | 9 | 13,863 | 100% | 100% | 0.14 |
| graphify | literal | 9 | 130,764/167,298 | 15 | 738 | 5 | 1 | 16.4s/18.9s | 5 | 3,167 | 83% | — | 0.25 |
| graphify | locate | 3 | 135,639/185,675 | 15 | 1,096 | 5 | 1 | 21.5s/29.5s | 5 | 11,674 | 100% | — | 0.19 |
| graphify | trace | 15 | 205,432/324,818 | 21 | 2,224 | 7 | 1 | 32.3s/59.7s | 7 | 24,957 | 73% | — | 0.32 |
| graphify-guard | edit | 9 | 277,275/292,744 | 27 | 2,803 | 9 | 1 | 47.4s/67.4s | 9 | 13,339 | 100% | 100% | 0.10 |
| graphify-guard | literal | 9 | 103,750/167,967 | 12 | 581 | 4 | 1 | 13.1s/19.9s | 4 | 2,942 | 89% | — | 0.28 |
| graphify-guard | locate | 3 | 163,877/185,964 | 18 | 1,199 | 6 | 1 | 23.4s/24.2s | 6 | 12,297 | 67% | — | 0.14 |
| graphify-guard | trace | 15 | 407,615/504,546 | 36 | 3,975 | 12 | 1 | 61.3s/86.4s | 12 | 34,310 | 70% | — | 0.36 |
| serena | edit | 9 | 173,671/213,654 | 3,824 | 2,710 | 8 | 1 | 44.0s/71.1s | 8 | 14,172 | 100% | 100% | 0.15 |
| serena | literal | 9 | 45,332/55,343 | 9 | 246 | 3 | 1 | 10.4s/11.5s | 3 | 474 | 83% | — | 0.26 |
| serena | locate | 3 | 62,255/62,770 | 12 | 604 | 4 | 1 | 16.0s/18.4s | 4 | 4,324 | 100% | — | 0.01 |
| serena | trace | 15 | 86,540/106,090 | 15 | 1,583 | 5 | 1 | 22.0s/27.9s | 5 | 14,652 | 83% | — | 0.23 |

## By arm × language

| arm | languages | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | python | 15 | 63,117/174,871 | 15 | 1,454 | 5 | 1 | 17.6s/36.8s | 5 | 13,640 | 77% | 100% | 0.62 |
| baseline | typescript | 21 | 88,730/160,040 | 15 | 1,375 | 5 | 1 | 23.1s/42.4s | 5 | 12,225 | 93% | 83% | 0.40 |
| graphify | python | 15 | 205,086/302,452 | 21 | 2,224 | 7 | 1 | 31.3s/53.6s | 7 | 15,175 | 70% | 100% | 0.43 |
| graphify | typescript | 21 | 199,404/322,824 | 21 | 2,005 | 7 | 1 | 31.5s/60.9s | 7 | 11,906 | 95% | 100% | 0.33 |
| graphify-guard | python | 15 | 218,310/396,124 | 21 | 2,194 | 7 | 1 | 35.3s/61.3s | 7 | 13,339 | 77% | 100% | 0.52 |
| graphify-guard | typescript | 21 | 276,869/503,294 | 27 | 2,221 | 9 | 1 | 45.5s/76.9s | 9 | 15,136 | 86% | 100% | 0.49 |
| serena | python | 15 | 61,022/153,717 | 15 | 1,866 | 5 | 1 | 17.5s/37.0s | 5 | 13,170 | 77% | 100% | 0.59 |
| serena | typescript | 21 | 86,540/190,900 | 15 | 1,277 | 5 | 1 | 20.9s/58.0s | 5 | 10,579 | 98% | 100% | 0.54 |

## By arm × resolved model

| arm | models | n | prompt tokens p50/p90 | (uncached in p50) | out p50 | calls p50 | premium p50 | wall p50/p90 | turns p50 | bytes read p50 | correctness | edit pass | tokens CV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| baseline | gpt-6-luna | 30 | 88,288/172,188 | 15 | 1,275 | 5 | 1 | 21.0s/42.5s | 5 | 10,846 | 87% | 89% | 0.50 |
| baseline | gpt-6-luna,copilot-search-a | 6 | 76,870/101,343 | 11,785 | 2,390 | 6 | 1 | 19.3s/32.3s | 6 | 14,833 | 83% | — | 0.27 |
| graphify | gpt-6-luna | 36 | 203,980/318,737 | 21 | 2,014 | 7 | 1 | 31.4s/60.4s | 7 | 13,796 | 85% | 100% | 0.38 |
| graphify-guard | gpt-6-luna | 36 | 241,516/461,881 | 24 | 2,209 | 8 | 1 | 38.6s/75.6s | 8 | 14,238 | 82% | 100% | 0.51 |
| serena | gpt-6-luna | 32 | 76,446/188,429 | 14 | 1,263 | 4 | 1 | 20.1s/44.6s | 4 | 10,061 | 88% | 100% | 0.60 |
| serena | gpt-6-luna,copilot-search-a | 4 | 84,814/129,970 | 15,000 | 2,662 | 6 | 1 | 20.6s/33.4s | 6 | 22,214 | 100% | 100% | 0.37 |

## KB currency (artifact staleness at query time, commits behind HEAD)

| arm | p50 | p95 | graph queries p50 |
|---|---|---|---|
| baseline | 0 | 0 | 0 |
| graphify | 0 | 0 | 1 |
| graphify-guard | 0 | 0 | 1 |
| serena | 0 | 0 | 0 |

## Per task

| task | arm | n | tokens p50 | calls p50 | wall p50 | correctness | tokens CV |
|---|---|---|---|---|---|---|---|
| svc-001 | baseline | 3 | 45,877 | 3 | 9.1s | 100% | 0.18 |
| svc-001 | graphify | 3 | 101,874 | 4 | 13.0s | 100% | 0.23 |
| svc-001 | graphify-guard | 3 | 131,635 | 5 | 17.0s | 100% | 0.26 |
| svc-001 | serena | 3 | 46,085 | 3 | 10.4s | 100% | 0.19 |
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
