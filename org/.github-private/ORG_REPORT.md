# Org graph  (2026-11-01T10:55:28+00:00)

- 32 nodes · 56 edges · projects: kestrel @ 2026-11-01T10:55:27+00:00

## Team ↔ project ↔ service dependency table
| team | owns (repo / dir) | project | contracts its repos consume |
|---|---|---|---|
| @kestrel/architecture-guild | kestrel-ops/adr | kestrel | — |
| @kestrel/booking-team | kestrel-services/booking | kestrel | — |
| @kestrel/platform-team | kestrel-ops, kestrel-services, kestrel-services/booking, kestrel-services/gateway, kestrel-web/src | kestrel | GET /v1/carriers/{code}/surcharges, GET /v2/carriers, GET /v2/shipments/{id}, POST /v1/quote, POST /v2/shipments, POST /v2/shipments/{id}/reserve |
| @kestrel/pricing-team | kestrel-services/pricing | kestrel | — |
| @kestrel/web-team | kestrel-web, kestrel-web/src | kestrel | GET /api/carriers, GET /api/shipments/{shipment_id}, POST /api/quote, POST /api/shipments, POST /api/shipments/{shipment_id}/reserve |

## Contracts and who depends on them
| contract | provider | consumers |
|---|---|---|
| `GET /api/carriers` | kestrel-services/gateway | kestrel-web |
| `GET /api/carriers/{code}/surcharges` | kestrel-services/gateway | — |
| `GET /api/shipments/{shipment_id}` | kestrel-services/gateway | kestrel-web |
| `GET /healthz` | kestrel-services/pricing | — |
| `GET /v1/carriers/` | kestrel-services/pricing | — |
| `GET /v1/carriers/{code}/surcharges` | kestrel-services/pricing | kestrel-services/gateway |
| `GET /v1/quotes/{quoteId}` | kestrel-services/pricing | — |
| `GET /v2/carriers` | kestrel-services/booking | kestrel-services/gateway |
| `GET /v2/carriers/{code}` | kestrel-services/booking | — |
| `GET /v2/shipments/{id}` | kestrel-services/booking | kestrel-services/gateway |
| `POST /api/quote` | kestrel-services/gateway | kestrel-web |
| `POST /api/shipments` | kestrel-services/gateway | kestrel-web |
| `POST /api/shipments/{shipment_id}/reserve` | kestrel-services/gateway | kestrel-web |
| `POST /v1/quote` | kestrel-services/pricing | kestrel-services/gateway |
| `POST /v2/shipments` | kestrel-services/booking | kestrel-services/gateway |
| `POST /v2/shipments/{id}/reserve` | kestrel-services/booking | kestrel-services/gateway |

## Cross-repo subsystems (from project-level Leiden communities)
- kestrel subsystem 0: kestrel-ops, kestrel-services, kestrel-web
- kestrel subsystem 1: kestrel-ops, kestrel-services, kestrel-web
