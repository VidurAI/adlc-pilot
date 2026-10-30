# DECISION_ADR.md — repo-context layer for Copilot: adopt, and how

Status: PROPOSED — Tier 1 complete (144 runs, 2026-10-30). Numbers below are copied from
`results/scorecard.md` (reproduce: `make tier1 scorecard`). Tier 2/3 sections marked ⏳.

## Context
Kestrel Freight's agent is GitHub Copilot CLI. The question was whether a repo-context
layer (Graphify, Serena, or both) lets it complete real tasks with fewer tokens, fewer
premium requests, less wall-clock and equal-or-better correctness than a grep/read
baseline — and whether the pattern can be packaged so any repo adopts it in ≤ 15 minutes.

## What was measured, and each metric's confidence
| Metric | Source | Confidence |
|---|---|---|
| input/output/cache tokens | `events.jsonl` `session.shutdown.tokenDetails` | high — exact per session |
| model calls | count of `session.usage_record` | high |
| premium requests (billing) | `session.shutdown.totalPremiumRequests`, cross-checked with stdout `result` | high for the number; note it is per prompt × multiplier, not per call (#1582 concerns `/usage`, which we do not use) |
| wall-clock | harness clock around the `copilot` process | high |
| turns, tool calls, MCP tool calls | `assistant.turn_start`, `tool.execution_start` | high |
| bytes read | result length of view/grep/glob/bash tool calls | medium — proxy |
| correctness | arm-blind Copilot judge 0/1/2 with rubric + expected; edit tasks by tests | medium — judge/human agreement reported from the 20 % spot-check |
| model | `auto` on this account; resolved model recorded per run and stratified | confound acknowledged: compare within a model |

## Results — Tier 1 (Python gateway + TypeScript web, 12 tasks × 4 arms × 3 runs)
Same resolved model in every arm (`gpt-6-luna`; a `copilot-search-a` helper appeared in 10
baseline/serena runs). Prompt tokens = input + cache reads + cache writes per session.

| arm | n | prompt tokens p50 / p90 | model calls p50 | wall p50 / p90 | correctness | edit pass |
|---|---|---|---|---|---|---|
| baseline | 36 | 87k / 167k | 5 | 19.3s / 39.7s | 86% | 89% |
| serena | 36 | 76k / 182k | 5 | 20.1s / 44.3s | 89% | 100% |
| graphify | 36 | 204k / 319k | 7 | 31.4s / 60.4s | 85% | 100% |
| graphify-guard | 36 | 242k / 462k | 8 | 38.6s / 75.6s | 82% | 100% |

Per category (correctness; prompt tokens p50):

| category | baseline | serena | graphify | graphify-guard |
|---|---|---|---|---|
| literal (n=9) | 83%; 47k | 83%; 45k | 83%; 131k | 89%; 104k |
| locate (n=3) | 100%; 63k | 100%; 62k | 100%; 136k | 67%; 164k |
| trace (n=15) | 83%; 89k | 83%; 87k | 73%; 205k | 70%; 408k |
| edit (n=9) | 89%; 163k | 100%; 174k | 100%; 279k | 100%; 277k |

**Tool adoption (the finding that explains the table).** Serena's MCP tools were used in
**1 of 36** serena-arm runs (web-010 r2: `get_symbols_overview`, `find_symbol`); every other
run used `rg`/`view`. The serena arm is therefore baseline with Serena connected and
ignored — its differences from baseline (−11k tokens, +3 pts correctness, one fewer edit
failure) are within run-to-run variance (tokens CV 0.5–0.6). The graphify skill was
invoked in **36 of 36** graphify-arm runs (Copilot auto-selects it from its description),
and `graphify query` actually ran in 19/36 (graphify) and 22/36 (guard). The skill text is
48 KB (~12k tokens) and is the bulk of the 2.3×–2.8× token cost; on `literal` tasks the
agent read the skill and then grepped, exactly as the routing policy says.

**Wins.** No context arm beat baseline on tokens or wall-clock in any Tier 1 category.
Correctness: all three context arms reached 100 % edit pass vs 89 % baseline (one
baseline failure on web-009, n=9 — suggestive, not significant). Graphify arms lost on
`trace` (−10 to −13 pts), the category the graph was expected to win; the per-task table
shows the loss concentrated on svc-003 (gateway dead-module trace) and web-005.

**KB currency.** Every run started with a FRESH artifact (p50 = p95 = 0 commits behind);
graph queries p50 = 1 in graphify arms. The ever-current claim holds for L0 in CI-shaped
runs; it has not yet been stressed by drift.

**Judge/human agreement.** `results/spotcheck.md` (29 answers, arm hidden) awaits the
owner; `adlc scorecard --spotcheck results/spotcheck.md` prints agreement. Edit tasks are
judged by overlay tests, not by the model.

## Results — Tier 2 (Java booking + C# pricing, 3 tasks × 4 arms × 3 runs = 36 runs)
| arm | n | prompt tokens p50 | calls p50 | wall p50 | correctness | Serena used | graph queried |
|---|---|---|---|---|---|---|---|
| baseline | 9 | 115k | 6 | 30s | 78% | — | — |
| serena | 9 | 127k | 7 | 30s | 72% | 0/9 | — |
| graphify | 9 | 230k | 8 | 33s | 100% | — | 1/9 |
| graphify-guard | 9 | 265k | 9 | 36s | 89% | — | 2/9 |

Per task: svc-002 (locate, C#) 100/83/100/100 %; svc-009 (edit, C# rounding) 100 % in all
arms; **svc-010 (edit, Java JPA `@ManyToOne`) 33/33/100/67 %** — the only Tier 1+2 cell where
a context arm clearly beat baseline on correctness (n=3 per cell; baseline and serena
failed the overlay test twice each). Serena was again unused in 0/9 runs, so the Java/C#
hypothesis ("symbol tools matter where grep is weakest") is untested, not refuted.
Graphify arms queried the graph in only 1–2 of 9 runs here; the svc-010 win came with the
skill loaded but mostly without graph queries — the mechanism is unclear and the sample
is small. Thresholds below are unchanged by Tier 2.

## Thresholds (set FROM baseline numbers)
Adopt an arm for a category when, within the same resolved model and over ≥ 3 runs:
prompt tokens p50 ≤ 0.8 × baseline (Tier 1 baseline: 87k → ≤ 70k), correctness ≥
baseline − 5 pts (≥ 81 %), wall p50 ≤ 1.2 × baseline (≤ 23 s). `literal` is excluded from
the token criterion by design (grep should win).
**Tier 1 outcome against these thresholds: no arm qualifies.** Serena meets the
correctness and wall criteria but not tokens (76k) and, more importantly, was not used.
Graphify arms fail tokens and wall in every category.

## Decision
1. **Adopt the contract and the kit now** (AGENTS.md + adlc block, routing, freshness,
   CI enforcement, federation). They are vendor-neutral, cost nothing per task, and the
   adoption test shows ≤ 15 min onboarding. This is the durable asset.
2. **Do not roll out Graphify as the default context layer on Copilot CLI.** At the
   vendor's shipped skill size it costs 2.3× tokens and 1.6× time for no correctness gain
   on Tier 1. Re-test with a lean skill profile (`adlc init --skill-profile lean`, ~4 KB,
   query/path/explain + freshness) as its own arm before any further decision; keep the
   graph build in CI because federation and the KB tasks (Tier 3 ⏳) depend on it.
3. **Keep Serena configured but treat it as unproven on Copilot CLI 1.0.105 / gpt-6-luna**:
   the agent does not pick symbol tools over `rg` even when the routing text says so.
   Next experiment: a Serena arm whose routing section *requires* `find_referencing_symbols`
   for trace tasks, and the Java/C# tasks (Tier 2 ⏳) where grep is weakest.
4. The hierarchy (L1/L2) is kept: it is cheap (1.4 s build, 0 ambiguous contract edges on
   Kestrel) and answers questions no single-repo tool can; its value is measured in
   Tier 3 ⏳, not assumed.

## Operating cost per tool (measured where marked)
| Item | Cost | Measured? |
|---|---|---|
| L0 graph build (code only, no LLM) | kestrel-services 1584 nodes in 5.8 s; kestrel-web 2.2 s; kestrel-ops stamp-only | yes |
| Docs semantic pass (`/graphify .` in a Copilot session, 43 files) | 7 min 27 s, 35 model calls, 1 premium request, 2.96 M input tokens (2.84 M cache reads) | yes — `results/docs-pass.json` |
| L1 federation (3 repos, 4 resolvers) | 1.4 s; http-contract 29 edges / 0 ambiguous after prefix resolution; doc-reference 243 edges | yes |
| L1 resolver false-positive rate | ⏳ (hand-check of the 29 contract edges against the spec: expected 100 % for Kestrel; the number that decides whether Graphify Cloud's cross-repo graph is worth paying for) | partial |
| Serena language servers | pinned by Serena commit; jdtls download 322 MB, ts-ls 25 MB, pyright lazy, Roslyn needs .NET 10 runtime | yes (download), first-activation latency ⏳ |
| Devcontainer image | Dockerfile authored; **not built** (no Docker on pilot machine); estimate 3–4 GB | no |
| Serena licence | GPL-3.0-or-later (application) / MIT (SolidLSP). Run as a separate process, shipped in the image with source URL + commit. **Legal review required before org-wide rollout.** | n/a |

## What survives a vendor change
`AGENTS.md` + the `adlc` block, the golden tasks, the harness and its results, this ADR,
the kit's CLI surface and workflows. Graphify and Serena sit behind `adlc baseline` /
`.mcp.json`; removing either touches the kit, not a consuming repo's prose.

## Non-code knowledge
Served: the kestrel-ops docs pass produced 53 document, 24 concept and 16 rationale
nodes; archaeology tasks are the test. Gap: the semantic pass is a Copilot-session-only
step (never headless by policy), so docs freshness lags code freshness — the KB currency
line reports it. ⏳ measured on the kestrel-ops tasks in Tier 3.

## Graphify Cloud — procurement questions (asked before any purchase)
1. Data location and access: where do graphs and source excerpts live, who at the vendor can read them, is there a single-tenant option?
2. SOC 2 Type II report and data-residency commitments (EU/US).
3. Export and exit: full `graph.json` export at any time, format stability, deletion SLA.
4. Pricing at 50 / 200 / 1000 repos, and what "cross-repo graph" costs separately.
5. OSS roadmap now that Cloud exists: which of `merge-graphs`, federation and MCP stay in the Apache-2.0 CLI.

## Rollout plan
| Wave | Scope | Mechanism | Exit criterion (read off the aggregated scorecard) |
|---|---|---|---|
| Canary | kestrel-services, kestrel-web, kestrel-ops | this pilot | Tier 1 thresholds met for ≥ 2 categories; adoption test ≤ 15 min |
| 1 | one volunteer team | opt-in `adlc init` | 4 weekly regress rows with no >15 % drift; zero kit bugs filed in week 4 |
| 2 | new repos | org ruleset makes `adlc-contract-lint` a required check for new repos | 90 % of new repos green on first PR |
| 3 | existing repos | bot PR running `adlc init` | team fills AGENTS.md prose within 2 weeks; drift alarms < 1/repo/month |

Owner: **Platform Engineering lead** (role, not a committee). Revisit: **2027-04-30**.
