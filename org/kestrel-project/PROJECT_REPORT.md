# Project graph — kestrel  (2026-11-01T15:08:45+00:00)

- 2164 nodes · 5374 edges · kit 0.1.4

## Members (freshness stamps)
| repo | commit_sha |
|---|---|
| kestrel-services | `12c1b6d0c51e` |
| kestrel-web | `04df6672f7a1` |
| kestrel-ops | `2989b162f913` |

## Cross-repo resolvers
| resolver | edges | nodes | ambiguous |
|---|---|---|---|
| ownership | 33 | 14 | 0 |
| http-contract | 29 | 16 | 0 |
| shared-package | 0 | 0 | 0 |
| doc-reference | 243 | 64 | 0 |

## HTTP contracts (provider → consumers)
- `GET /api/carriers` provided by **kestrel-services/gateway** ← kestrel-web:src/api/client.ts
- `GET /api/carriers/{code}/surcharges` provided by **kestrel-services/gateway** ← _no consumers found_
- `GET /api/shipments/{shipment_id}` provided by **kestrel-services/gateway** ← kestrel-web:src/api/client.ts
- `GET /healthz` provided by **kestrel-services/pricing** ← _no consumers found_
- `GET /v1/carriers/` provided by **kestrel-services/pricing** ← _no consumers found_
- `GET /v1/carriers/{code}/surcharges` provided by **kestrel-services/pricing** ← kestrel-services:gateway/gateway/clients/pricing.py
- `GET /v1/quotes/{quoteId}` provided by **kestrel-services/pricing** ← _no consumers found_
- `GET /v2/carriers` provided by **kestrel-services/booking** ← kestrel-services:gateway/gateway/clients/booking.py
- `GET /v2/carriers/{code}` provided by **kestrel-services/booking** ← _no consumers found_
- `GET /v2/shipments/{id}` provided by **kestrel-services/booking** ← kestrel-services:gateway/gateway/clients/booking.py
- `POST /api/quote` provided by **kestrel-services/gateway** ← kestrel-web:src/api/client.ts
- `POST /api/shipments` provided by **kestrel-services/gateway** ← kestrel-web:src/api/client.ts
- `POST /api/shipments/{shipment_id}/reserve` provided by **kestrel-services/gateway** ← kestrel-web:src/api/client.ts
- `POST /v1/quote` provided by **kestrel-services/pricing** ← kestrel-services:gateway/gateway/clients/pricing.py
- `POST /v2/shipments` provided by **kestrel-services/booking** ← kestrel-services:gateway/gateway/clients/booking.py, kestrel-services:gateway/gateway/routes/shipments.py
- `POST /v2/shipments/{id}/reserve` provided by **kestrel-services/booking** ← kestrel-services:gateway/gateway/clients/booking.py

## God nodes (most connected across the project)
1. `org.junit.jupiter.api.Test` (kestrel-services) — 113 edges
2. `Fact` (kestrel-services) — 78 edges
3. `BOOK-398: Double booking incident follow-up (advisory lock)` (kestrel-ops) — 52 edges
4. `json_response()` (kestrel-services) — 48 edges
5. `Carrier` (kestrel-services) — 46 edges
6. `Shipment` (kestrel-services) — 44 edges
7. `client.ts` (kestrel-web) — 44 edges
8. `ShipmentControllerTest.java` (kestrel-services) — 40 edges
9. `QuotePage.tsx` (kestrel-web) — 39 edges
10. `main.py` (kestrel-services) — 36 edges
11. `errors.py` (kestrel-services) — 33 edges
12. `BookingForm.tsx` (kestrel-web) — 33 edges

## Cross-repo communities (subsystems spanning ≥2 repos)
- community 0: kestrel-ops×87, kestrel-services×45, kestrel-web×1 — hubs: `BOOK-398: Double booking incident follow-up (advisory lock)`, `Public API Gateway`, `Concurrent Reserve Double-Booking Incident`, `BOOK-398 Advisory Lock for Concurrent Reservations`
- community 1: kestrel-ops×1, kestrel-services×3, kestrel-web×1 — hubs: `kestrel`, `@kestrel/platform-team`, `kestrel-services`, `kestrel-services/booking`

## AMBIGUOUS — needs a human (0)

## Diff vs previous build
- no changes
