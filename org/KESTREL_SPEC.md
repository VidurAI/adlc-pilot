# Kestrel Freight — organisation spec (source of truth for repo generation)

Fictional freight-booking company. Four repos, four languages, one shared vocabulary.
Everything below is deliberate: the identifiers are join keys that later tooling
(graph federation, golden tasks) depends on. **Use them exactly.**

## Teams (CODEOWNERS handles)
| Team | Owns |
|---|---|
| `@kestrel/booking-team` | kestrel-services/booking |
| `@kestrel/pricing-team` | kestrel-services/pricing |
| `@kestrel/platform-team` | kestrel-services/gateway, kestrel-ops (runbooks, postmortems), kestrel-services root files |
| `@kestrel/web-team` | kestrel-web |
| `@kestrel/architecture-guild` | kestrel-ops/adr |

## Carriers (fictional)
NorthStar Lines (`NSL`), Baltic Express (`BLX`), Pacific Reach (`PCR`).

## Shared identifiers (join keys)
Tickets (prefix-number, cited verbatim in code comments, commit messages, docs):
- **BOOK-412** — add `eta_confidence` to the `/v2/shipments` response (booking, done).
- **GW-118** — gateway `ShipmentOut` Pydantic model missing `eta_confidence` (open).
- **WEB-77** — web `Shipment` TS type missing `eta_confidence` (open).
- **PRC-233** — rounding mismatch: pricing fuel surcharge uses `Math.Round` (banker's) while
  the rest uses `decimal` + `MidpointRounding.AwayFromZero`; web `money.ts` repeats it
  with `Math.round`. Open. Cites both files by path.
- **BOOK-398** — double booking incident follow-up (advisory lock). Closed.
- **PRC-240** — "remove LegacyTariffLoader?" — answer: NO, it is loaded by name from
  `appsettings.json`. Closed/won't-do.
- **GW-102** — remove dead `legacy/pricing_v1.py`. Open.
- **OPS-51** — on-call policy rewrite. Closed.
- **BOOK-377** — carriers FK missing on JPA entity. Open.
ADRs (kestrel-ops/adr/NNNN-slug.md):
- 0001-split-monolith-into-services
- 0002-java-spring-for-booking
- 0003-dotnet-for-pricing
- 0004-python-fastapi-gateway
- 0005-money-as-decimal-minor-units
- 0006-idempotent-booking-references
- **0007-rate-limit-per-carrier** ← referenced by `// WHY:` in Java `CarrierRateLimiter`
- 0008-eta-confidence-scoring
- 0009-team-boundaries-and-codeowners
Postmortems: `2026-06-14-double-booking.md` (explains why `BookingService.reserve()`
takes an advisory lock; the Java has NO comment), `2026-03-02-pricing-timeout.md`,
`2026-08-21-gateway-429-storm.md`.

## HTTP contracts
### booking (Java 21, Spring Boot 3.3.x, Maven, package `com.kestrel.booking`)
- `POST /v2/shipments` → 201 `ShipmentResponse`
- `GET /v2/shipments/{id}` → 200 `ShipmentResponse`
- `POST /v2/shipments/{id}/reserve` → 200 `ShipmentResponse` (status RESERVED) / 409
- `GET /v2/carriers` → 200 list
- `ShipmentResponse` JSON (snake_case via Jackson naming strategy): `id`, `reference`,
  `origin`, `destination`, `carrier_code`, `status`, `eta`, **`eta_confidence`** (double 0..1).
- `CarrierRateLimiter` — per-carrier token bucket; a `// WHY:` comment cites ADR-0007 and
  the 2026-08-21 429 storm. Error string on reject: `"carrier capacity exhausted"`.
- `BookingService.reserve()` acquires an advisory lock keyed by shipment reference via
  `AdvisoryLock` (interface). `PostgresAdvisoryLock` runs `select pg_advisory_xact_lock(?)`;
  `InMemoryAdvisoryLock` (test profile) uses striped `ReentrantLock`s. No comment anywhere
  saying why. Config key `kestrel.booking.lock.enabled`.
- `src/main/resources/db/schema.sql`: `shipments.carrier_id bigint REFERENCES carriers(id)`.
  The JPA `Shipment` entity declares `private Long carrierId;` with NO `@ManyToOne`.
- Feature flag: `kestrel.booking.features.eta-confidence` (property). Config key
  `kestrel.booking.ratelimit.per-carrier-rps`.
- Tests: JUnit 5 + Spring Boot test, H2, `mvn -q test` green.

### pricing (C# .NET 8 minimal API, xunit, namespace `Kestrel.Pricing`)
- `POST /v1/quote` → 200 `QuoteResponse { quote_id, amount, currency, breakdown[] }`;
  request `{ origin, destination, weight_kg, carrier_code }`. 422 on unknown carrier with
  error string `"unknown carrier code"`.
- `GET /v1/carriers/{code}/surcharges` → 200.
- `QuoteCalculator.ApplyFuelSurcharge` uses `Math.Round(value, 2)` (ToEven). All other
  rounding uses `decimal` + `MidpointRounding.AwayFromZero` via `Money.Round`. Comment on
  the AwayFromZero helper cites ADR-0005. No comment on the Math.Round line.
- `Kestrel.Pricing.Tariffs.LegacyTariffLoader : ITariffLoader` — no static reference in
  code. `appsettings.json`: `"TariffLoader": "Kestrel.Pricing.Tariffs.LegacyTariffLoader"`;
  `TariffLoaderFactory` resolves it with `Type.GetType`. Second impl `CsvTariffLoader`.
- Config keys: `Pricing:FuelSurchargePct`, `Pricing:DefaultCurrency`. Feature flag
  `Pricing:Features:MultiCarrierQuotes`.
- Tests: xunit, `dotnet test` green.

### gateway (Python 3.12, FastAPI, httpx, pytest, package `gateway/`)
- `POST /api/shipments` → calls booking `POST /v2/shipments`; `GET /api/shipments/{id}`;
  `POST /api/shipments/{id}/reserve`; `POST /api/quote` → pricing `POST /v1/quote`;
  `GET /api/carriers` → booking `GET /v2/carriers`.
- `gateway/models.py` `ShipmentOut` has `id, reference, origin, destination, carrier_code,
  status, eta` — **no `eta_confidence`** (GW-118 is open; a `# TODO GW-118` comment exists
  in the ticket file only, NOT in code).
- `gateway/legacy/pricing_v1.py` — dead module, imported nowhere (GW-102).
- Translates upstream 429 (`"carrier capacity exhausted"`) into 503 with
  `"booking temporarily unavailable"`.
- Env/config: `BOOKING_BASE_URL`, `PRICING_BASE_URL`, `KESTREL_FEATURE_MULTI_CARRIER_QUOTES`,
  `GATEWAY_TIMEOUT_SECONDS`. Settings via pydantic-settings.
- Tests: pytest with `respx` or httpx `MockTransport`; `pytest -q` green.

### web (TypeScript, React 18, Vite, vitest, package `kestrel-web`)
- `src/api/types.ts` `Shipment` type mirrors gateway `ShipmentOut` — **no `eta_confidence`**
  (WEB-77 open). `Quote` type mirrors pricing `QuoteResponse`.
- `src/api/client.ts` calls `/api/shipments`, `/api/shipments/:id`, `/api/shipments/:id/reserve`,
  `/api/quote`, `/api/carriers` (paths as string literals or a `routes` map).
- `src/lib/money.ts` `roundMoney(amount)` = `Math.round(amount * 100) / 100` (PRC-233).
- Pages: BookingForm, QuotePage, ShipmentList, ShipmentDetail. Hooks folder. Components.
- Feature flag `VITE_FEATURE_MULTI_CARRIER_QUOTES`. Error copy string
  `"We couldn't reserve that shipment"`.
- Tests: vitest + testing-library; `npm test` green. ~3–5k LOC.

### kestrel-ops (no code)
`adr/` (9 above), `postmortems/` (3 above), `runbooks/` (8: booking-restart,
pricing-tariff-reload, gateway-429-storm, rotate-carrier-credentials, db-failover,
on-call-handover, deploy-rollback, carrier-onboarding), `policies/` (on-call-policy.md,
change-management.md), `tickets/export.csv` (columns: id,title,status,component,
owner_team,files,created,closed) + one `tickets/<ID>.md` per ticket above, `sla/` with
`carrier-sla.pdf` and `policies/on-call-policy.pdf` (generated from the markdown via
reportlab), `glossary.md`, `README.md`. ~40 files.

## Golden seeds (what later tasks will ask; keep these TRUE)
1. Who consumes booking `/v2/shipments`? → gateway (`gateway/clients/booking.py`) and,
   transitively, web (`src/api/client.ts` via `/api/shipments`).
2. Why does `BookingService.reserve()` take an advisory lock? → postmortem 2026-06-14.
3. Why is the rate limiter per carrier not global? → ADR-0007 (+ 2026-08-21 postmortem).
4. Is `LegacyTariffLoader` dead? → No, loaded by name from appsettings.json (PRC-240).
5. Is `legacy/pricing_v1.py` dead? → Yes (GW-102).
6. Which FK is in SQL but not in JPA? → shipments.carrier_id → carriers.id (BOOK-377).
7. Where is rounding inconsistent? → `QuoteCalculator.ApplyFuelSurcharge` (Math.Round)
   vs `Money.Round`; web `src/lib/money.ts` (PRC-233).
8. Which repos are stale on `eta_confidence`? → gateway `ShipmentOut`, web `Shipment`.
9. Who owns the advisory-lock decision? → booking-team (CODEOWNERS) with the postmortem
   authored by platform-team on-call.
10. If pricing changes `/v1/quote`, who is affected? → gateway (platform-team), web
    (web-team) via `/api/quote`.

## Hard rules for generators
- No `AGENTS.md`, no `.mcp.json`, no `.github/workflows`, no `graphify-out/`, no ADLC
  artefacts of any kind. Those arrive via `adlc init` later.
- Every file ≤ 300 lines. Real, compiling, tested code. No secrets, no API keys, no
  placeholder tokens.
- Do not git commit. History is created afterwards by `scripts/mkhistory.py`.
- Snake_case JSON on the wire everywhere; camelCase in TS source.

## Seeds discovered during generation (kept deliberately)
11. Gateway `POST /api/shipments` forwards the field `reference`, but booking's create
    request reads `client_reference`; Jackson ignores the unknown field, so booking
    generates its own reference and gateway-side idempotency is silently broken. No
    ticket exists yet. A cross-language task asks the agent to find this.
