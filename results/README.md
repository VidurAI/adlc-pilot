# results/

Never hand-edited. Produced by `adlc eval` / `adlc scorecard` / `adlc regress`.

- `<date>.jsonl` — one record per (task, arm, run). Fields: see `adlc-kit/harness/runner.py::execute`.
- `runs/<task>__<arm>__r<n>/` — scrubbed `events.jsonl`, `stdout.jsonl`, `stderr.txt`, `queries.log`, `record.json`, `tests.log`.
- `spotcheck.md` — 20 % of judged answers, arm hidden, for a human to score.
- `scorecard.md` / `.html` — rendered by `make scorecard`.
- `docs-pass.json` + `raw/docs-pass-kestrel-ops.events.jsonl` — the one semantic docs pass.
- `adoption-test.md` — Phase 8 timed walkthrough log.
