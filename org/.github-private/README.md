# .github-private (L2 — organisation level)

- `org-graph.json`, `ORG_REPORT.md` — the coarse org graph (`adlc federate --level org`): teams, projects, repos, service dirs, HTTP contracts, cross-repo subsystems. Thousands of nodes at most, never a merge of code graphs.
- `.github/workflows/adlc-aggregate.yml` — renders one cross-repo scorecard from member repos' `trend.jsonl` artifacts; re-federates the org graph on `adlc-project-federated` dispatches.
- `agents/` — org-level Copilot custom agents (none shipped by the pilot; the kit's contract is `AGENTS.md`, not custom agents).
- `aggregate.yml` — the member list.
