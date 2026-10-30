# DECISION_ADR.md — repo-context layer for Copilot: adopt, and how

Status: DRAFT until Tier 1 numbers land (`make tier1 && make scorecard`); sections marked
⏳ are filled from `results/scorecard.md` by the owner, never by hand-typed numbers.

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

## Results ⏳
(Scorecard tables pasted from `results/scorecard.md`; wins per category and language;
KB currency line; judge/human agreement.)

## Thresholds (set FROM baseline numbers) ⏳
Adopt an arm for a category when, within the same resolved model and over ≥ 3 runs:
median input tokens ≤ 0.8 × baseline AND correctness ≥ baseline − 0.05 AND wall p50 ≤
1.2 × baseline. `literal` is excluded from the token criterion by design (grep should win).

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
