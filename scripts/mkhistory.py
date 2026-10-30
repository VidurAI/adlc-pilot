#!/usr/bin/env python3
"""Create a plausible multi-commit git history for a generated Kestrel repo.

Usage: mkhistory.py <repo-dir> <plan-name>
Files are grouped by ordered glob patterns; each group becomes one commit with a
believable message, author (team) and date spread over 2025-10 .. 2026-10. Anything
unmatched lands in a final housekeeping commit. Idempotent: skips if .git exists."""
from __future__ import annotations

import fnmatch
import os
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

AUTHORS = {
    "platform": ("Mira Olsen", "mira.olsen@kestrel.example"),
    "booking": ("Tomasz Nowak", "tomasz.nowak@kestrel.example"),
    "pricing": ("Ada Lindqvist", "ada.lindqvist@kestrel.example"),
    "web": ("Jonah Baptiste", "jonah.baptiste@kestrel.example"),
    "guild": ("Sunil Rao", "sunil.rao@kestrel.example"),
}

# (globs, message, author)
PLANS: dict[str, list[tuple[list[str], str, str]]] = {
    "services": [
        (["README.md", ".gitignore", "CODEOWNERS"], "chore: repo skeleton and ownership", "platform"),
        (["booking/pom.xml", "booking/.gitignore", "booking/README.md", "booking/src/main/resources/application*.yml"], "booking: bootstrap Spring Boot 3.3 service", "booking"),
        (["booking/src/main/resources/db/*"], "booking: initial schema, carriers seed", "booking"),
        (["booking/src/main/java/**/domain/*", "booking/src/main/java/**/model/*", "booking/src/main/java/**/entity/*", "booking/src/main/java/**/repository/*", "booking/src/main/java/**/repo/*"], "booking: shipment + carrier entities and repositories", "booking"),
        (["booking/src/main/java/**/lock/*", "booking/src/main/java/**/*Lock*"], "booking: reserve() takes advisory lock (BOOK-398)", "booking"),
        (["booking/src/main/java/**/ratelimit/*", "booking/src/main/java/**/*RateLimit*", "booking/src/main/java/**/*TokenBucket*"], "booking: per-carrier rate limiter per ADR-0007", "booking"),
        (["booking/src/main/java/**/*Eta*"], "booking: add eta_confidence to shipment response (BOOK-412)", "booking"),
        (["booking/src/main/java/**/*"], "booking: services, controllers, validation, problem details", "booking"),
        (["booking/src/test/**/*"], "booking: test suite (controller slices, lock, limiter)", "booking"),
        (["pricing/*.sln", "pricing/.gitignore", "pricing/README.md", "pricing/src/**/*.csproj", "pricing/tests/**/*.csproj"], "pricing: bootstrap .NET 8 minimal API", "pricing"),
        (["pricing/src/**/Tariffs/**/*", "pricing/src/**/appsettings*.json"], "pricing: tariff loaders, legacy loader selectable via appsettings", "pricing"),
        (["pricing/src/**/Common/*", "pricing/src/**/*Money*"], "pricing: Money helpers — decimal + AwayFromZero (ADR-0005)", "pricing"),
        (["pricing/src/**/*Surcharge*", "pricing/src/**/Rules/**/*"], "pricing: surcharge rules engine", "pricing"),
        (["pricing/src/**/*"], "pricing: quote endpoints, calculator, carriers", "pricing"),
        (["pricing/tests/**/*"], "pricing: xunit suite incl. factory + rounding behaviour", "pricing"),
        (["gateway/pyproject.toml", "gateway/.gitignore", "gateway/README.md"], "gateway: bootstrap FastAPI edge service", "platform"),
        (["gateway/gateway/legacy/**/*"], "gateway: keep legacy local pricing formula for parity checks", "platform"),
        (["gateway/gateway/clients/**/*", "gateway/gateway/retry.py", "gateway/gateway/*breaker*"], "gateway: booking + pricing clients with retry and breaker", "platform"),
        (["gateway/gateway/models.py", "gateway/gateway/settings.py", "gateway/gateway/config*.py"], "gateway: wire models and settings", "platform"),
        (["gateway/gateway/**/*"], "gateway: routes, middleware, 429→503 translation", "platform"),
        (["gateway/tests/**/*"], "gateway: pytest suite with respx mocks", "platform"),
    ],
    "web": [
        (["package.json", "package-lock.json", "tsconfig*.json", "vite.config.ts", "index.html", ".gitignore", ".env.example"], "chore: scaffold Vite + React 18 + vitest", "web"),
        (["README.md", "CODEOWNERS"], "docs: readme and ownership", "web"),
        (["src/api/types.ts", "src/api/wire.ts"], "api: wire + domain types for gateway contract", "web"),
        (["src/api/mappers.ts", "src/api/errors.ts"], "api: snake_case mappers and ApiError", "web"),
        (["src/api/**/*"], "api: typed client with routes map", "web"),
        (["src/lib/money.ts"], "lib: money rounding + formatting", "web"),
        (["src/lib/flags.ts", "src/lib/copy.ts"], "lib: feature flags and UI copy", "web"),
        (["src/lib/**/*"], "lib: router, async helpers, recent shipments store", "web"),
        (["src/components/Carrier*", "src/components/Status*", "src/components/Money*"], "components: carrier select, status badge, money text", "web"),
        (["src/components/**/*"], "components: layout, nav, banners, tables, states", "web"),
        (["src/hooks/useQuote*", "src/hooks/useCarriers*"], "hooks: quote and carriers", "web"),
        (["src/hooks/**/*"], "hooks: shipments, mutations, async data", "web"),
        (["src/pages/BookingForm*", "src/pages/QuotePage*"], "pages: booking form and quote page", "web"),
        (["src/pages/**/*"], "pages: shipment list, detail, not found", "web"),
        (["src/**/*"], "app: shell, styles, entry point", "web"),
        (["tests/setup.ts", "tests/helpers*"], "tests: setup (Node 25 localStorage shim) and helpers", "web"),
        (["tests/api/**/*", "tests/lib/**/*"], "tests: api + lib", "web"),
        (["tests/components/**/*"], "tests: components", "web"),
        (["tests/**/*"], "tests: hooks and pages", "web"),
    ],
    "ops": [
        (["README.md", "CODEOWNERS"], "docs: repo index and ownership", "platform"),
        (["glossary.md"], "docs: freight glossary", "platform"),
        (["adr/README.md", "adr/0001-*"], "adr 0001: split monolith into services", "guild"),
        (["adr/0002-*", "adr/0003-*", "adr/0004-*"], "adr 0002-0004: language choices per service", "guild"),
        (["adr/0005-*"], "adr 0005: money as decimal minor units", "guild"),
        (["adr/0006-*"], "adr 0006: idempotent booking references", "guild"),
        (["postmortems/2026-03-02-*"], "postmortem: pricing timeout 2026-03-02", "platform"),
        (["postmortems/2026-06-14-*"], "postmortem: double booking 2026-06-14 (BOOK-398)", "platform"),
        (["postmortems/2026-08-21-*"], "postmortem: gateway 429 storm 2026-08-21", "platform"),
        (["adr/0007-*"], "adr 0007: rate limit per carrier", "guild"),
        (["adr/0008-*"], "adr 0008: eta confidence scoring (BOOK-412)", "guild"),
        (["adr/0009-*"], "adr 0009: team boundaries and CODEOWNERS", "guild"),
        (["runbooks/booking-*", "runbooks/db-*", "runbooks/deploy-*"], "runbooks: booking restart, db failover, rollback", "platform"),
        (["runbooks/*"], "runbooks: pricing reload, 429 storm, credentials, on-call, carrier onboarding", "platform"),
        (["policies/*.md", "scripts/*"], "policies: on-call + change management, pdf build script (OPS-51)", "platform"),
        (["sla/*.md"], "sla: carrier SLA source", "platform"),
        (["policies/*.pdf", "sla/*.pdf"], "docs: publish on-call policy and carrier SLA PDFs", "platform"),
        (["tickets/export.csv"], "tickets: tracker export", "platform"),
        (["tickets/BOOK-*", "tickets/GW-*"], "tickets: booking and gateway notes", "platform"),
        (["tickets/*"], "tickets: pricing, web, ops notes", "platform"),
    ],
}


def git(repo: Path, *args: str, env: dict | None = None) -> None:
    subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True, env=env)


def all_files(repo: Path) -> list[str]:
    out = []
    ignored = subprocess.run(["git", "-C", str(repo), "ls-files", "-o", "-i", "--exclude-standard", "--directory"],
                             capture_output=True, text=True).stdout.split()
    for p in repo.rglob("*"):
        if p.is_dir() or ".git/" in str(p.relative_to(repo)) + "/":
            continue
        rel = str(p.relative_to(repo))
        if any(rel.startswith(i.rstrip("/")) for i in ignored):
            continue
        out.append(rel)
    return sorted(out)


def match(rel: str, pat: str) -> bool:
    if "**" in pat:
        head, tail = pat.split("**", 1)
        tail = tail.lstrip("/")
        return rel.startswith(head) and fnmatch.fnmatch(rel[len(head):].split("/")[-1] if "/" not in tail else rel[len(head):], tail or "*")
    return fnmatch.fnmatch(rel, pat)


def main() -> int:
    repo, plan = Path(sys.argv[1]).resolve(), PLANS[sys.argv[2]]
    if (repo / ".git").exists():
        print(f"{repo}: history exists, skipping")
        return 0
    git(repo, "init", "-q", "-b", "main")
    remaining = all_files(repo)
    start, end = datetime(2025, 10, 6, 9, 0), datetime(2026, 10, 20, 17, 0)
    step = (end - start) / (len(plan) + 1)
    n = 0
    for i, (globs, msg, who) in enumerate(plan):
        picked = [f for f in remaining if any(match(f, g) for g in globs)]
        if not picked:
            continue
        remaining = [f for f in remaining if f not in picked]
        when = (start + step * (i + 1)).strftime("%Y-%m-%dT%H:%M:%S")
        name, email = AUTHORS[who]
        env = {**os.environ, "GIT_AUTHOR_NAME": name, "GIT_AUTHOR_EMAIL": email, "GIT_COMMITTER_NAME": name,
               "GIT_COMMITTER_EMAIL": email, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when}
        git(repo, "add", "--", *picked, env=env)
        git(repo, "commit", "-q", "-m", msg, env=env)
        n += 1
    if remaining:
        name, email = AUTHORS["platform"]
        when = end.strftime("%Y-%m-%dT%H:%M:%S")
        env = {**os.environ, "GIT_AUTHOR_NAME": name, "GIT_AUTHOR_EMAIL": email, "GIT_COMMITTER_NAME": name,
               "GIT_COMMITTER_EMAIL": email, "GIT_AUTHOR_DATE": when, "GIT_COMMITTER_DATE": when}
        git(repo, "add", "--", *remaining, env=env)
        git(repo, "commit", "-q", "-m", "chore: housekeeping", env=env)
        n += 1
    print(f"{repo.name}: {n} commits")
    return 0


if __name__ == "__main__":
    sys.exit(main())
