# `adlc upgrade` round-trip — kestrel-web, schema 1 → 2

Migration 1→2 adds `owner` (default CODEOWNERS team) to the adlc block so org graphs can
attach ownership without re-parsing CODEOWNERS.

| Step | Result |
|---|---|
| `adlc upgrade --to 2` | block rewritten in place: `schema: 2`, `owner: '@kestrel/web-team'`, `kit: 0.1.0`; prose untouched; kit-owned files refreshed (all `unchanged`) |
| `adlc lint` after upgrade | OK (schema 2 is in the kit's supported set) |
| second `adlc upgrade --to 2` | no-op (idempotent; one `owner:` line) |
| `git checkout -- .` | repo back to schema 1 — the pilot keeps schema 1 as its default |

Covered by `tests/test_init_lint_upgrade.py::test_upgrade_1_to_2_adds_owner_from_codeowners`.
