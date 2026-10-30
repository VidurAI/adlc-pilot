# ADLC pilot report — Tier 1 complete (2026-10-30)

Reproduce every number: `make kit org init doctor baseline federate tasks tier1 scorecard`
(Tier 2/3: `make tier2 tier3 scorecard`, resumable). Scorecard: `results/scorecard.md`.
Decision + rollout: `DECISION_ADR.md`. Every call made without asking: `DECISIONS.md`.

## 1. Scorecard (Tier 1: 12 tasks × 4 arms × 3 runs = 144 runs, one resolved model)
| arm | n | prompt tokens p50 / p90 | calls p50 | premium p50 | wall p50 / p90 | correctness | edit pass |
|---|---|---|---|---|---|---|---|
| baseline | 36 | 87k / 167k | 5 | 1 | 19.3s / 39.7s | 86% | 89% |
| serena | 36 | 76k / 182k | 5 | 1 | 20.1s / 44.3s | 89% | 100% |
| graphify | 36 | 204k / 319k | 7 | 1 | 31.4s / 60.4s | 85% | 100% |
| graphify-guard | 36 | 242k / 462k | 8 | 1 | 38.6s / 75.6s | 82% | 100% |

Per category (correctness; prompt tokens p50): literal — 83/83/83/89 %, 47k/45k/131k/104k ·
trace (n=15) — 83/83/73/70 %, 89k/87k/205k/408k · locate (n=3) — 100/100/100/67 % ·
edit (n=9) — 89/100/100/100 %. KB currency: p50 = p95 = 0 commits behind in every arm;
graph queries p50 = 1 in graphify arms.
Confidence: tokens/calls/turns from events.jsonl (exact); premium requests = billing per
prompt × multiplier, cross-checked with the stdout result event (#1582 concerns /usage,
unused); bytes-read is a proxy; model `auto` recorded per run (10/144 runs also used a
`copilot-search-a` helper); every cell is a median over 3 runs.

### Tier 2 (Java/C#, 3 tasks × 4 arms × 3 runs = 36 runs)
| arm | n | prompt tokens p50 | calls p50 | wall p50 | correctness |
|---|---|---|---|---|---|
| baseline | 9 | 115k | 6 | 30s | 78% |
| serena | 9 | 127k | 7 | 30s | 72% |
| graphify | 9 | 230k | 8 | 33s | 100% |
| graphify-guard | 9 | 265k | 9 | 36s | 89% |
Serena used 0/9; graph queried 1–2/9. One clear context win: svc-010 (Java JPA edit) 100 %
graphify vs 33 % baseline, n=3 per cell.

## 2. Per arm
- **baseline** — won tokens and wall in every category; lost one edit (web-009). Cost: zero.
- **serena** — statistically indistinguishable from baseline because the agent used Serena's
  tools in 1 of 36 runs; 100 % edit pass. Cost: uvx launch 0.8 s/run, LS pinned by Serena
  commit, GPL-3.0 licence review.
- **graphify** — skill invoked 36/36, graph queried 19/36; 2.3× tokens, 1.6× wall, −10 pts on
  trace, +11 pts on edits. Cost: 2–6 s CI build per repo, 48 KB skill per task.
- **graphify-guard** — hook fired every run; 2.8× tokens, 2× wall, worst correctness. Cost: as
  graphify plus the hook adapter. Not recommended.

## 3. Judge/human agreement
Spot-check sheet `results/spotcheck.md` (29 answers, arm hidden) is waiting for a human;
`adlc scorecard --spotcheck results/spotcheck.md` prints agreement. Edits judged by tests.

## 4. Adoption test (kestrel-notify, never seen by the kit)
Machine time 1.1 min, 0 deviations, both arms scored 2 on the golden task; human prose
step pre-supplied (≈5 min typing in reality). Kit fixes needed: 0. Final tag: v0.1.1
(feature release). Run on the dev machine — no Docker, so not in the devcontainer.

## 5. Not completed
- Tier 2 done (above). Tier 3 (KB + federated, 135 runs) still running;
  `make tier2 tier3 scorecard` resumes. The `both` arm was not run: no arm beat baseline.
- Devcontainer image never built; `act` not run (no Docker). Workflows verified by a stub runner.
- Copilot model pinning unavailable on this account (auto, recorded per run).
- Human spot-check not done (yours). Resolver false-positive hand-check on 29 edges not done.
- Lean-skill arm (the obvious next experiment) not run.
