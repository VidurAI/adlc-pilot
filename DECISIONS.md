# DECISIONS.md — calls made without asking

Format: date · decision · why. Newest at the bottom. Nothing here is a promise;
everything here is reversible by the pilot owner.

## 2026-10-29

- **Workspace root is `/Users/hpatil/ADLC`**, not a nested `adlc-pilot/`. The spec's
  tree is reproduced one level down from here. One fewer directory to explain.
- **Subagent model routing.** Architecture, contracts, judgment, and the final report
  are done in the main (Fable) session. Bulk generation of the fictional Kestrel repos,
  fixtures, and boilerplate is delegated to Sonnet subagents; trivial chores to Haiku.
  Requested by the pilot owner mid-session to keep token spend proportional to the work.
- **Toolchain installed on the dev machine via Homebrew** (openjdk@21, maven, act) and
  Microsoft's `dotnet-install.sh` into `.toolchain/dotnet` (the Homebrew cask needs
  sudo). This is dev-machine convenience only; the devcontainer is the distributable.
  `.toolchain/env.sh` sources it. Nothing in the kit depends on these paths.
- **Python 3.12 for the kit and the gateway** (`uv python install 3.12`). Graphify pins
  `tree-sitter<0.26` wheels; 3.14 is too new to trust for a pinned toolchain.
- **Graphify pin: `graphifyy[leiden]==0.9.97`** (wheel sha256
  `eb24dd7f…65e01a`), latest on PyPI at verification time. Re-verify before tagging.
- **Serena pin: commit `ede329aaf0c824bea75455a2926f01420d7aa620`** (main,
  2026-10-28). LICENSE read: the Serena application is **GPL-3.0-or-later**, SolidLSP
  is MIT; the combined `serena-agent` package is GPL-3.0-or-later. Flagged for legal in
  the ADR. We run it as a separate MCP process, never link it, and ship it only inside
  the devcontainer image with source URL + commit recorded.
- **Copilot auth for the harness: `COPILOT_GITHUB_TOKEN` is read from env at run time
  only.** On the dev machine the Makefile obtains it via `gh auth token` into the
  process env; it is never written to disk or into results. Transcripts are scrubbed.
- **Copilot model: `auto`, resolved model recorded per run.** Every named `--model`
  value probed (`gpt-5.4`, `gpt-5-mini`, `claude-sonnet-4.5`, `claude-haiku-4.5`, and 15
  others) returns "not available" on this account's plan. The harness therefore runs
  `--model auto`, records `session.auto_mode_resolved.chosenModel` per run, and the
  scorecard stratifies by model. `ADLC_COPILOT_MODEL` overrides this for plans that can
  pin. Confound acknowledged in the report's confidence footnote.
- **Premium-request accounting:** `events.jsonl` `session.shutdown` is primary; the
  stdout `result` event (`usage.premiumRequests`, `totalApiDurationMs`) is the
  per-run cross-check instead of `/usage` (which is interactive-only). #1582 noted.
- **events.jsonl schema discovered from 22 real sessions** on this machine plus the
  smoke run. Documented in `adlc-kit/harness/EVENTS_SCHEMA.md`.
- **Graphify's own `merge-graphs` / `global` commands are NOT used for federation.**
  They merge into `~/.graphify/` (home directory — forbidden by principle 1) and do
  not namespace ids or add cross-repo resolvers. `adlc federate` is built on
  `graph.json` + NetworkX directly, as the spec requires.
- **`.graphifyrc` is key=value**, not YAML/JSON (verified in `rcfile.py`): supports
  `viz_node_limit=<int>` and `language.<ext>=<lang>` only. Template matches that.
- **Graphify skill for Copilot:** `graphify install --platform copilot` targets
  `~/.copilot/skills` (home). `adlc init` instead writes the skill project-scoped into
  `.github/skills/graphify/SKILL.md` with an `adlc stale` preamble prepended.
  Verified empirically (one Copilot run with probe skills in `.github/skills`,
  `.copilot/skills`, `.claude/skills`, `.agents/skills`): only `.github/skills` loads.
  Graphify's `--platform copilot --project` target (`.copilot/skills/`) is therefore
  dead weight for Copilot CLI 1.0.73; the kit copies the skill into place itself.

## 2026-10-30

- **Copilot workspace MCP config needs `--trust-folder`** in prompt mode; without it
  `.mcp.json` / `.github/mcp.json` are silently ignored (verified: `session.mcp_servers_loaded`
  shows only the builtin GitHub server). The harness and `adlc` pass `--trust-folder`
  on every headless run. Server entries must use `"type": "local"` (Copilot's own
  writer emits that; `"stdio"` is accepted but was not needed).
- **The `.mcp.json` `tools` allowlist does not trim what Serena advertises** (23 tools
  loaded regardless of the list). Enforcement moved to Serena's side: a committed
  `.serena/adlc-context.yml` (custom `--context` YAML) with `excluded_tools` yields
  exactly the 10 allowlisted tools. The allowlist is still written for documentation
  and for any future Copilot build that honours it.
- **Serena 2.x defaults to a REPL interface** (`agent_interface: REPL` → only
  `initial_instructions` + `serena_repl`). The kit passes `--agent-interface tools`.
  Also `--project-from-cwd` so the committed `.mcp.json` has no absolute paths, and a
  committed `.serena/project.yml` declares the language servers. Serena still writes
  `~/.serena/serena_config.yml` + logs on first run; that is runtime cache, not
  something any repo depends on (doctor checks nothing in `~`).
- **Serena memories live in `<repo>/.serena/memories/` and are committed**; the
  allowlist deliberately excludes `write_memory`/`edit_memory`/`delete_memory` so agents
  cannot mutate the contract surface at run time. Memory updates go through PRs.
