# Spot-check sheet (arm hidden)

25 of 126 judged answers. Fill `human:` with 0/1/2.
`adlc scorecard --spotcheck results/spotcheck.md` computes agreement.

## ops-001  (ref: ops-001__graphify-federated__r1)

**Question**

Why does booking keep a separate rate-limit bucket for each carrier instead of one simple
shared limit? What happened that made us change it, and how do the per-carrier numbers
relate to what the carriers themselves allow?

**Reference**

adr/0007-rate-limit-per-carrier.md, driven by postmortems/2026-08-21-gateway-429-storm.md.
Until August 2026 booking had one global token bucket (60 rps). On 2026-08-21 NorthStar
Lines (NSL) slowed to 6-12 s hold calls; retries drained the shared bucket and booking
answered 429 "carrier capacity exhausted" for every carrier, including healthy BLX and PCR
(55% of attempts rejected for 47 minutes, SEV1). Per-carrier buckets (CarrierRateLimiter)
isolate a failing carrier (noisy neighbour) and fit differing contractual caps in
sla/carrier-sla.md (NSL 40, BLX 25, PCR 15 rps; PCR overridden to 8).

**Rubric**

2 = the 2026-08-21 NSL-slowdown incident AND the noisy-neighbour / shared-bucket reason,
    plus the contractual-cap relation (NSL 40 / BLX 25 / PCR 15, default 20, PCR 8);
1 = states the isolation rationale without the incident (or the incident without the why);
0 = generic "to avoid overload" with no source.

**Answer**

```
Booking switched from one shared **60-rps bucket** to independent buckets after the **August 21, 2026** incident. NorthStar Lines (NSL) slowed down—capacity holds took 6–12 seconds—and retries drained the shared bucket. Booking then rejected requests for healthy carriers too: **55% of attempts were rejected over 47 minutes, and 43% of those rejections affected healthy BLX or PCR**. Separate buckets mean a struggling carrier can affect its own bookings without consuming another carrier’s allowance. [Postmortem, Root cause and Impact; ADR-0007, Decision]

The configured sustained rates are **20 rps for NSL and BLX** and **8 rps for PCR**. Their contractual caps are **40, 25, and 15 rps**, respectively, so PCR gets an override because the 20-rps default would exceed its cap. The default bucket capacity is two seconds of that configured rate. Carriers also specify burst allowances—NSL 60 rps for 10 seconds, BLX 35 rps for 5 seconds, and PCR none. **BOOK-418**, which tracks review of the NSL and BLX overrides against their SLAs, is still open; 20 rps is the current setting, not a completed SLA-tuning review. [ADR-0007, Decision; `sla/carrier-sla.md`, Service levels at a glance]
```

judge: 2  ·  human: ___

---

## ops-001  (ref: ops-001__graphify-federated__r2)

**Question**

Why does booking keep a separate rate-limit bucket for each carrier instead of one simple
shared limit? What happened that made us change it, and how do the per-carrier numbers
relate to what the carriers themselves allow?

**Reference**

adr/0007-rate-limit-per-carrier.md, driven by postmortems/2026-08-21-gateway-429-storm.md.
Until August 2026 booking had one global token bucket (60 rps). On 2026-08-21 NorthStar
Lines (NSL) slowed to 6-12 s hold calls; retries drained the shared bucket and booking
answered 429 "carrier capacity exhausted" for every carrier, including healthy BLX and PCR
(55% of attempts rejected for 47 minutes, SEV1). Per-carrier buckets (CarrierRateLimiter)
isolate a failing carrier (noisy neighbour) and fit differing contractual caps in
sla/carrier-sla.md (NSL 40, BLX 25, PCR 15 rps; PCR overridden to 8).

**Rubric**

2 = the 2026-08-21 NSL-slowdown incident AND the noisy-neighbour / shared-bucket reason,
    plus the contractual-cap relation (NSL 40 / BLX 25 / PCR 15, default 20, PCR 8);
1 = states the isolation rationale without the incident (or the incident without the why);
0 = generic "to avoid overload" with no source.

**Answer**

```
Booking uses one bucket per carrier as a **bulkhead**: if one carrier slows down or attracts retries, it can exhaust only its own budget, not starve bookings to healthy carriers. A higher shared limit wouldn’t fix that isolation problem and could exceed the strictest carrier’s cap. *(ADR-0007, “Context” and “Decision”)*

The change followed the **2026-08-21 SEV1**. NorthStar Lines (NSL) slowed from under a second to 6–12 seconds; retries drained the shared 60-rps bucket, so booking rejected requests for every carrier. Over 47 minutes, 2,816 of 5,120 attempts were rejected, including 1,206 for healthy Baltic Express (BLX) and Pacific Reach (PCR). Raising the shared limit to 120 rps and pausing NSL briefly restored BLX and PCR, but the lasting fix was per-carrier limits (BOOK-409). *(Postmortem, “Impact,” “Root cause,” and “Timeline”)*

The configured rates are **Kestrel-side limits**, not copies of the carriers’ caps: the default is 20 rps per carrier, with PCR overridden to 8. The contractual caps are NSL 40, BLX 25, and PCR 15 rps, so 20 is below NSL and BLX’s caps, while PCR’s lower cap calls for the 8-rps override. BOOK-418 is still open to review NSL and BLX overrides. One distinction to keep in mind: the ADR also specifies a default bucket capacity of two seconds’ worth of tokens, while the SLA lists separate burst allowances—60 rps for 10 seconds for NSL, 35 for 5 seconds for BLX, and none for PCR. The configured sustained rates alone don’t establish that those burst envelopes match. *(ADR-0007, “Decision”; `sla/carrier-sla.md`, “Service levels at a glance” and “Rate limits and throttling”)*
```

judge: 2  ·  human: ___

---

## ops-001  (ref: ops-001__graphify-federated__r3)

**Question**

Why does booking keep a separate rate-limit bucket for each carrier instead of one simple
shared limit? What happened that made us change it, and how do the per-carrier numbers
relate to what the carriers themselves allow?

**Reference**

adr/0007-rate-limit-per-carrier.md, driven by postmortems/2026-08-21-gateway-429-storm.md.
Until August 2026 booking had one global token bucket (60 rps). On 2026-08-21 NorthStar
Lines (NSL) slowed to 6-12 s hold calls; retries drained the shared bucket and booking
answered 429 "carrier capacity exhausted" for every carrier, including healthy BLX and PCR
(55% of attempts rejected for 47 minutes, SEV1). Per-carrier buckets (CarrierRateLimiter)
isolate a failing carrier (noisy neighbour) and fit differing contractual caps in
sla/carrier-sla.md (NSL 40, BLX 25, PCR 15 rps; PCR overridden to 8).

**Rubric**

2 = the 2026-08-21 NSL-slowdown incident AND the noisy-neighbour / shared-bucket reason,
    plus the contractual-cap relation (NSL 40 / BLX 25 / PCR 15, default 20, PCR 8);
1 = states the isolation rationale without the incident (or the incident without the why);
0 = generic "to avoid overload" with no source.

**Answer**

```
Booking switched to **one independent token bucket per carrier** to prevent a slow or overloaded carrier from starving the others. In the August 21, 2026 SEV1, NorthStar Lines (NSL) slowed down and retries drained a **shared 60-rps bucket**, causing 2,816 of 5,120 attempts (55%) to fail over 47 minutes. Of those failures, 1,206 were for healthy Baltic Express (BLX) and Pacific Reach (PCR). The change, tracked as **BOOK-409**, isolates that failure: NSL trouble should affect NSL bookings, not every carrier.

The current sustained limits are set below the carriers’ contractual caps:

| Carrier | Contract cap | Booking limit |
|---|---:|---:|
| NSL | 40 rps | 20 rps default |
| BLX | 25 rps | 20 rps default |
| PCR | 15 rps | 8 rps override |

PCR gets the lower override because its cap is lower and its p95 latency is slowest. NSL and BLX override reviews are still open as **BOOK-418**. These are sustained rates, not copies of the carriers’ burst allowances; Booking’s bucket capacity defaults to two seconds of its configured rate. Per-carrier buckets also mean aggregate outbound capacity can rise as carriers are added, so onboarding must review total load.

Sources: `adr/0007-rate-limit-per-carrier.md`, `postmortems/2026-08-21-gateway-429-storm.md`, `sla/carrier-sla.md`, and `runbooks/carrier-onboarding.md`.
```

judge: 2  ·  human: ___

---

## ops-001  (ref: ops-001__graphify__r2)

**Question**

Why does booking keep a separate rate-limit bucket for each carrier instead of one simple
shared limit? What happened that made us change it, and how do the per-carrier numbers
relate to what the carriers themselves allow?

**Reference**

adr/0007-rate-limit-per-carrier.md, driven by postmortems/2026-08-21-gateway-429-storm.md.
Until August 2026 booking had one global token bucket (60 rps). On 2026-08-21 NorthStar
Lines (NSL) slowed to 6-12 s hold calls; retries drained the shared bucket and booking
answered 429 "carrier capacity exhausted" for every carrier, including healthy BLX and PCR
(55% of attempts rejected for 47 minutes, SEV1). Per-carrier buckets (CarrierRateLimiter)
isolate a failing carrier (noisy neighbour) and fit differing contractual caps in
sla/carrier-sla.md (NSL 40, BLX 25, PCR 15 rps; PCR overridden to 8).

**Rubric**

2 = the 2026-08-21 NSL-slowdown incident AND the noisy-neighbour / shared-bucket reason,
    plus the contractual-cap relation (NSL 40 / BLX 25 / PCR 15, default 20, PCR 8);
1 = states the isolation rationale without the incident (or the incident without the why);
0 = generic "to avoid overload" with no source.

**Answer**

```
Booking uses an independent token bucket per carrier so one carrier’s traffic can’t consume a shared budget and throttle calls to another. The graph links the change (ADR 0007) to the **Aug. 21, 2026 “Global Rate-Limit 429 Storm”** postmortem and “Shared Global Bucket Failure,” but doesn’t include the incident narrative, so I can’t say exactly what triggered the change beyond that connection.

The per-carrier rates are meant to be checked against each carrier’s SLA caps—not treated as universal limits. In particular, **BOOK-418**, which is still open, calls for reviewing NSL and BLX RPS overrides against those caps. The graph doesn’t expose the actual numbers or confirm whether the overrides are currently below the carriers’ contractual allowances. Sources: `adr/0007-rate-limit-per-carrier.md` (Decision), `postmortems/2026-08-21-gateway-429-storm.md` (Root cause), `sla/carrier-sla.md` (Service levels at a glance), and `tickets/export.csv` (BOOK-418).
```

judge: 1  ·  human: ___

---

## ops-002  (ref: ops-002__baseline__r1)

**Question**

Finance noticed a surcharge pricing at 10.12 on an invoice line but 10.13 on the carrier
statement. Why do pricing's fuel surcharge and the web app's money helper round
differently from the rest of the system, what is the intended rule, and what is the status?

**Reference**

adr/0005-money-as-decimal-minor-units.md sets the rule: decimal money, all rounding half
away from zero (MidpointRounding.AwayFromZero) through Money.Round. Two recorded deviations
(amended 2026-09-30) are tracked in tickets/PRC-233.md: QuoteCalculator.ApplyFuelSurcharge
uses Math.Round(value, 2), which is banker's (ToEven), so exact halves like 10.125 give
10.12; and web src/lib/money.ts roundMoney uses Math.round on binary floats. Reported by
Finance operations; owner pricing-team; status open in tickets/export.csv. The web team
will fix its side after the pricing change lands.

**Rubric**

2 = ADR-0005 target rule + both deviations (fuel surcharge Math.Round and web roundMoney)
    + PRC-233 open status;
1 = explains the banker's-vs-away-from-zero cause for one deviation, or lacks the
    ticket/status;
0 = no source, or blames data/currency conversion.

**Answer**

```
The two mismatches have different causes. Pricing’s fuel-surcharge code uses `Math.Round(value, 2)`, which defaults to **banker’s rounding** (`ToEven`), so the exact midpoint `10.125` becomes `10.12`. The web helper uses JavaScript `Math.round` on binary floating-point numbers; values such as `1.005` can be represented slightly below the midpoint, and negative half-way values also round differently.

The intended rule in **ADR-0005** is decimal money and **half away from zero** for every monetary rounding, via pricing’s `Money.Round` (or integer minor units/a decimal library in the web app). That makes `10.125` round to `10.13`.

**Status:** Both are documented deviations tracked in **PRC-233**, which is still **open**. Its acceptance criteria call for routing the surcharge through `Money.Round`, correcting the web helper, adding regression tests, and updating ADR-0005. The latest ticket comment says the web fix is planned after the pricing change lands; the docs do not indicate that either fix has landed.
```

judge: 2  ·  human: ___

---

## ops-002  (ref: ops-002__baseline__r3)

**Question**

Finance noticed a surcharge pricing at 10.12 on an invoice line but 10.13 on the carrier
statement. Why do pricing's fuel surcharge and the web app's money helper round
differently from the rest of the system, what is the intended rule, and what is the status?

**Reference**

adr/0005-money-as-decimal-minor-units.md sets the rule: decimal money, all rounding half
away from zero (MidpointRounding.AwayFromZero) through Money.Round. Two recorded deviations
(amended 2026-09-30) are tracked in tickets/PRC-233.md: QuoteCalculator.ApplyFuelSurcharge
uses Math.Round(value, 2), which is banker's (ToEven), so exact halves like 10.125 give
10.12; and web src/lib/money.ts roundMoney uses Math.round on binary floats. Reported by
Finance operations; owner pricing-team; status open in tickets/export.csv. The web team
will fix its side after the pricing change lands.

**Rubric**

2 = ADR-0005 target rule + both deviations (fuel surcharge Math.Round and web roundMoney)
    + PRC-233 open status;
1 = explains the banker's-vs-away-from-zero cause for one deviation, or lacks the
    ticket/status;
0 = no source, or blames data/currency conversion.

**Answer**

```
The mismatch is from two exceptions to the system’s money rule. Pricing’s fuel-surcharge code uses `.NET Math.Round` with its default **to-even** behavior, so exactly 10.125 becomes 10.12. The web helper uses JavaScript `Math.round` on binary floating-point numbers; that can mis-handle decimal halfway values and rounds negative halves differently from pricing’s rule.

The intended rule in ADR-0005 is **decimal money rounded to minor units, with exact halves away from zero**. Pricing should use `Money.Round`; the web should use integer minor units or decimal arithmetic with the same rule. That makes 10.125 → 10.13 and -2.505 → -2.51.

**Status:** PRC-233 is still marked **open** in the ticket and export, with no close date. It tracks fixes and regression tests for both pricing and web; the ticket notes web planned to fix its side after the pricing change lands.
```

judge: 2  ·  human: ___

---

## ops-002  (ref: ops-002__graphify__r1)

**Question**

Finance noticed a surcharge pricing at 10.12 on an invoice line but 10.13 on the carrier
statement. Why do pricing's fuel surcharge and the web app's money helper round
differently from the rest of the system, what is the intended rule, and what is the status?

**Reference**

adr/0005-money-as-decimal-minor-units.md sets the rule: decimal money, all rounding half
away from zero (MidpointRounding.AwayFromZero) through Money.Round. Two recorded deviations
(amended 2026-09-30) are tracked in tickets/PRC-233.md: QuoteCalculator.ApplyFuelSurcharge
uses Math.Round(value, 2), which is banker's (ToEven), so exact halves like 10.125 give
10.12; and web src/lib/money.ts roundMoney uses Math.round on binary floats. Reported by
Finance operations; owner pricing-team; status open in tickets/export.csv. The web team
will fix its side after the pricing change lands.

**Rubric**

2 = ADR-0005 target rule + both deviations (fuel surcharge Math.Round and web roundMoney)
    + PRC-233 open status;
1 = explains the banker's-vs-away-from-zero cause for one deviation, or lacks the
    ticket/status;
0 = no source, or blames data/currency conversion.

**Answer**

```
The **$0.01 discrepancy is a midpoint-rounding mismatch**: 7.5% of $135.00 is exactly **$10.125**. Pricing’s fuel-surcharge code uses `Math.Round`’s default *to-even* rule, producing **$10.12**. The web helper uses `Math.round` on binary floating-point numbers; it can misrepresent decimal midpoints, and its negative-half behavior also differs. These are documented deviations from the shared money rule in [PRC-233](tickets/PRC-233.md) and [ADR-0005](adr/0005-money-as-decimal-minor-units.md).

**Intended rule:** use decimal money and round midpoint values **away from zero**—through `Money.Round` in pricing, and integer minor units or a decimal library in the web app. That gives **$10.13** for $10.125.

**Status:** PRC-233 is still **open**, owned by `@kestrel/pricing-team`. The pricing team confirmed the offending call, and the web team said it would fix its helper after the pricing change lands; the ticket does not show the fixes as complete.
```

judge: 2  ·  human: ___

---

## ops-003  (ref: ops-003__baseline__r2)

**Question**

The booking schema enforces that every shipment points at a real carrier, but the Java
entity has no relationship to the carrier table. Is that known, why does it matter, and is
anyone going to fix it?

**Reference**

Yes, ticket BOOK-377 (tickets/BOOK-377.md; open, booking-team, created 2026-05-19, listed
in tickets/export.csv). db/schema.sql declares shipments.carrier_id REFERENCES carriers(id)
but the JPA Shipment entity has only Long carrierId, no @ManyToOne/@JoinColumn. Effects:
hand-written joins, an extra lookup per shipment to resolve carrier_code, and H2 schema
validation cannot detect a broken relation. Found while writing the carrier summary query;
deprioritised behind the Q2 carrier summary release (no customer impact); still wanted per
the 2026-09-28 comment. Acceptance: lazy @ManyToOne, JSON unchanged, no N+1, mvn -q test green.

**Rubric**

2 = BOOK-377 + the missing @ManyToOne on Shipment.carrierId vs the SQL FK + why it matters
    + current open/deprioritised status;
1 = identifies the FK gap without the ticket or its status;
0 = wrong FK or says it is fixed.

**Answer**

```
Yes—this is tracked as **BOOK-377**, an open booking-team ticket. The database foreign key still enforces that each shipment references a real carrier; the gap is that JPA doesn’t model that relationship.

That matters because Hibernate can’t manage the association, carrier joins are handwritten, and resolving `carrier_code` takes an extra lookup per shipment. Tests using H2 also can’t validate the mapping. The ticket was deprioritized in June, then marked “still wanted” on September 28, paired with BOOK-418. It proposes adding a lazy `@ManyToOne` while preserving the JSON contract and preventing N+1 queries. **There’s no stated delivery date or firm commitment** in the ticket.
```

judge: 2  ·  human: ___

---

## ops-004  (ref: ops-004__baseline__r1)

**Question**

Our static analyzer flags LegacyTariffLoader in pricing as having zero references, and
the name says it was replaced. Can we delete it? Has this come up before?

**Reference**

No. tickets/PRC-240.md (closed 2026-10-05, won't do): the class has no static reference but
is selected by name from the top-level "TariffLoader" key in pricing's appsettings.json and
resolved with Type.GetType by TariffLoaderFactory. Production and staging run on it
(adr/0003-dotnet-for-pricing.md, amended); CsvTariffLoader is the factory default for
onboarding and local use. Deleting it would crash pricing at start-up on every pod and fail
LegacyTariffLoaderConfigTests. Follow-ups: policies/change-management.md section 4 now
says no references is not proof of dead code, so search configuration first, and
runbooks/pricing-tariff-reload.md warns not to delete or rename it.

**Rubric**

2 = "do not delete", loaded by name from appsettings.json via TariffLoaderFactory, cites
    PRC-240, and notes production uses it;
1 = says not to delete and mentions config loading without the ticket or production use;
0 = says it is dead and safe to remove.

**Answer**

```
**No—not as things stand.** `LegacyTariffLoader` has no static references because `TariffLoaderFactory` loads it by name from configuration. Production and staging use it; deleting it would break pricing startup, and a config test covers the resolution.

This exact question was addressed in **PRC-240**, opened October 2 and closed October 5, 2026 as **Won’t do**. The resolution says not to delete or rename it. A replacement would need a coordinated configuration migration and deployment.
```

judge: 2  ·  human: ___

---

## ops-004  (ref: ops-004__graphify__r1)

**Question**

Our static analyzer flags LegacyTariffLoader in pricing as having zero references, and
the name says it was replaced. Can we delete it? Has this come up before?

**Reference**

No. tickets/PRC-240.md (closed 2026-10-05, won't do): the class has no static reference but
is selected by name from the top-level "TariffLoader" key in pricing's appsettings.json and
resolved with Type.GetType by TariffLoaderFactory. Production and staging run on it
(adr/0003-dotnet-for-pricing.md, amended); CsvTariffLoader is the factory default for
onboarding and local use. Deleting it would crash pricing at start-up on every pod and fail
LegacyTariffLoaderConfigTests. Follow-ups: policies/change-management.md section 4 now
says no references is not proof of dead code, so search configuration first, and
runbooks/pricing-tariff-reload.md warns not to delete or rename it.

**Rubric**

2 = "do not delete", loaded by name from appsettings.json via TariffLoaderFactory, cites
    PRC-240, and notes production uses it;
1 = says not to delete and mentions config loading without the ticket or production use;
0 = says it is dead and safe to remove.

**Answer**

```
**No—don’t delete or rename it.** `LegacyTariffLoader` is selected by its fully qualified name in `appsettings.json` and resolved via `Type.GetType`; production and staging use it. Removing it would prevent pricing from starting.

This came up directly as **PRC-240** (opened Oct 2, closed Oct 5, 2026): the decision was “Won’t do.” The ticket also records that a config-resolution test would fail and that the analyzer was updated to suppress config-loaded types. See `tickets/PRC-240.md`, `runbooks/pricing-tariff-reload.md`, and ADR-0003.
```

judge: 1  ·  human: ___

---

## ops-005  (ref: ops-005__graphify__r3)

**Question**

I'm on call and customers are getting "booking temporarily unavailable" on bookings. Which
runbook covers it, and who does our policy say I should page if it persists?

**Reference**

runbooks/gateway-429-storm.md: the gateway's 503 is its translation of booking's 429
"carrier capacity exhausted" (GW-110); steps find the rejected carrier via the
booking.ratelimit.rejected metric and lower that carrier's override. Escalation is in
policies/on-call-policy.md section 5: limiter, reservations and advisory-lock symptoms page
@kestrel/booking-team; pure gateway errors stay with platform-team's secondary. Page the
owner after 10 minutes (SEV1) or 20 minutes (SEV2).

**Rubric**

2 = names gateway-429-storm.md AND on-call-policy.md section 5, booking-team for limiter
    symptoms, with the 10/20 minute timers;
1 = finds the runbook but not the owning team or timers (or the reverse);
0 = wrong runbook (for example booking-restart) or no escalation.

**Answer**

```
Use **`runbooks/gateway-429-storm.md`** (“Gateway 429 / ‘booking temporarily unavailable’”). The runbook says to page **`@kestrel/booking-team`** for limiter behavior; **`@kestrel/platform-team`** is secondary for gateway errors or translation.

The policy says not to wait to prove the cause: page the owning team after **10 minutes for SEV1** or **20 minutes for SEV2** without a clear owner-independent fix.
```

judge: 1  ·  human: ___

---

## ops-006  (ref: ops-006__baseline__r2)

**Question**

Where are the contractual request limits for each carrier written down, what are they,
and where does the reasoning for how booking's limiter default relates to them live?

**Reference**

sla/carrier-sla.md section 2 (also rendered as sla/carrier-sla.pdf) lists the contractual
request caps: NSL 40 rps, BLX 25 rps, PCR 15 rps. adr/0007-rate-limit-per-carrier.md
explains how the default kestrel.booking.ratelimit.per-carrier-rps = 20 sits below the NSL
and BLX caps but above PCR's, hence the PCR override of 8; reviewing NSL/BLX overrides is
BOOK-418 (open). runbooks/carrier-onboarding.md requires recording a new carrier's cap in
the SLA before go-live.

**Rubric**

2 = carrier-sla.md with the three caps AND ADR-0007's default-20 / PCR-8 reasoning;
1 = the SLA table with caps but no link to the limiter default (or the reverse);
0 = wrong document or wrong numbers.

**Answer**

```
The repository’s operational summary is [`sla/carrier-sla.md`](sla/carrier-sla.md), §2; it notes that the signed carrier agreements are the commercial source of truth. The request limits are **NSL: 40 rps** (burst 60 rps for 10 seconds), **BLX: 25 rps** (burst 35 rps for 5 seconds), and **PCR: 15 rps** (no burst allowance). The generated PDF is `sla/carrier-sla.pdf`.

The reasoning for booking’s **20 rps default** lives in [`adr/0007-rate-limit-per-carrier.md`](adr/0007-rate-limit-per-carrier.md), under “Decision”: 20 is below NSL and BLX’s caps but above PCR’s, so PCR is configured at **8 rps**. The ADR also points to PCR’s slower p95 latency as a factor and tracks review of NSL/BLX overrides as **BOOK-418**. `sla/carrier-sla.md` and `runbooks/carrier-onboarding.md` repeat the operational guidance.
```

judge: 2  ·  human: ___

---

## ops-006  (ref: ops-006__graphify-federated__r3)

**Question**

Where are the contractual request limits for each carrier written down, what are they,
and where does the reasoning for how booking's limiter default relates to them live?

**Reference**

sla/carrier-sla.md section 2 (also rendered as sla/carrier-sla.pdf) lists the contractual
request caps: NSL 40 rps, BLX 25 rps, PCR 15 rps. adr/0007-rate-limit-per-carrier.md
explains how the default kestrel.booking.ratelimit.per-carrier-rps = 20 sits below the NSL
and BLX caps but above PCR's, hence the PCR override of 8; reviewing NSL/BLX overrides is
BOOK-418 (open). runbooks/carrier-onboarding.md requires recording a new carrier's cap in
the SLA before go-live.

**Rubric**

2 = carrier-sla.md with the three caps AND ADR-0007's default-20 / PCR-8 reasoning;
1 = the SLA table with caps but no link to the limiter default (or the reverse);
0 = wrong document or wrong numbers.

**Answer**

```
The **signed carrier agreements are the commercial source of truth**; the engineering summary is `sla/carrier-sla.md` (the table at lines 23–24), also published as `sla/carrier-sla.pdf`.

| Carrier | Contractual cap | Contractual burst allowance |
|---|---:|---|
| NSL | 40 rps | 60 rps for 10 seconds |
| BLX | 25 rps | 35 rps for 5 seconds |
| PCR | 15 rps | None |

The default relationship is explained in `sla/carrier-sla.md` just below that table and in **ADR-0007**, `adr/0007-rate-limit-per-carrier.md` (decision, lines 40–44): booking uses a per-carrier default of **20 rps**. That is below NSL and BLX’s caps, but above PCR’s, so PCR is overridden to **8 rps**. The onboarding runbook (`runbooks/carrier-onboarding.md`, lines 25–28) repeats the rule for new carriers. Reviewing whether NSL and BLX should also have overrides is tracked as **BOOK-418**.

The carrier burst allowances above are contract terms; the limiter’s bucket capacity is separately configured as `burst-seconds` (default 2) times its rate.
```

judge: 2  ·  human: ___

---

## ops-006  (ref: ops-006__graphify__r3)

**Question**

Where are the contractual request limits for each carrier written down, what are they,
and where does the reasoning for how booking's limiter default relates to them live?

**Reference**

sla/carrier-sla.md section 2 (also rendered as sla/carrier-sla.pdf) lists the contractual
request caps: NSL 40 rps, BLX 25 rps, PCR 15 rps. adr/0007-rate-limit-per-carrier.md
explains how the default kestrel.booking.ratelimit.per-carrier-rps = 20 sits below the NSL
and BLX caps but above PCR's, hence the PCR override of 8; reviewing NSL/BLX overrides is
BOOK-418 (open). runbooks/carrier-onboarding.md requires recording a new carrier's cap in
the SLA before go-live.

**Rubric**

2 = carrier-sla.md with the three caps AND ADR-0007's default-20 / PCR-8 reasoning;
1 = the SLA table with caps but no link to the limiter default (or the reverse);
0 = wrong document or wrong numbers.

**Answer**

```
The **signed carrier agreements are the commercial source of truth**; the operational summary is in [`sla/carrier-sla.md`](sla/carrier-sla.md), “Service levels at a glance” (§2). The same summary is rendered as `sla/carrier-sla.pdf`.

| Carrier | Contractual cap | Burst allowance |
|---|---:|---|
| NSL | 40 rps | 60 rps for 10 seconds |
| BLX | 25 rps | 35 rps for 5 seconds |
| PCR | 15 rps | None |

The reasoning for the booking limiter default lives in [`adr/0007-rate-limit-per-carrier.md`](adr/0007-rate-limit-per-carrier.md), especially **Context**, **Decision**, and **Consequences**. The default is 20 rps per carrier: below NSL and BLX’s caps, but above PCR’s, so PCR is overridden to 8 rps. The ADR also explains why limits are per-carrier (to avoid one degraded carrier starving the others) and notes that reviewing NSL and BLX overrides is tracked as BOOK-418. The onboarding guidance is in [`runbooks/carrier-onboarding.md`](runbooks/carrier-onboarding.md), §3.
```

judge: 2  ·  human: ___

---

## ops-007  (ref: ops-007__baseline__r1)

**Question**

In the ticket export CSV, what is the exact name of the column that says which team a
ticket belongs to?

**Reference**

owner_team, the fifth column in the header row of tickets/export.csv
(id,title,status,component,owner_team,files,created,closed). Values are CODEOWNERS handles
such as @kestrel/booking-team.

**Rubric**

2 = owner_team in tickets/export.csv; 1 = correct column but no file, or "component"
mentioned as well as the answer without choosing; 0 = wrong column.

**Answer**

```
The column is named: owner_team
```

judge: 1  ·  human: ___

---

## ops-007  (ref: ops-007__baseline__r2)

**Question**

In the ticket export CSV, what is the exact name of the column that says which team a
ticket belongs to?

**Reference**

owner_team, the fifth column in the header row of tickets/export.csv
(id,title,status,component,owner_team,files,created,closed). Values are CODEOWNERS handles
such as @kestrel/booking-team.

**Rubric**

2 = owner_team in tickets/export.csv; 1 = correct column but no file, or "component"
mentioned as well as the answer without choosing; 0 = wrong column.

**Answer**

```
The column is `owner_team`.
```

judge: 1  ·  human: ___

---

## ops-008  (ref: ops-008__baseline__r2)

**Question**

Pricing wants to change the shape of the POST /v1/quote response. Which teams and
consumers are affected, and who has to review the change?

**Reference**

Consumers of pricing's /v1/quote are the gateway (kestrel-services/gateway, owned by
@kestrel/platform-team: PricingClient.quote and the QuoteOut model behind POST /api/quote)
and, through /api/quote, the web app (kestrel-web, @kestrel/web-team: Quote type and
mapQuote). Pricing-team owns the change itself. adr/0009-team-boundaries-and-codeowners.md
rule 4 says a contract change names every consuming team on the ticket and adds them as
reviewers; policies/change-management.md section 3 requires owner approval per CODEOWNERS.
tickets/PRC-233.md notes gateway and web are informed of quote changes.

**Rubric**

2 = gateway/platform-team AND web/web-team (via /api/quote) with the ADR-0009 rule or
    change-management requirement that they review;
1 = names only one consumer, or teams without the web-through-gateway path;
0 = only pricing-team, or booking named as a consumer.

**Answer**

```
**Affected teams:** `@kestrel/platform-team` owns the gateway, which forwards pricing responses and exposes `POST /api/quote`; its explicit response models may need updating. `@kestrel/web-team` consumes that public endpoint and may need to adapt. ADR-0009 specifically names both as affected consumers when pricing changes `/v1/quote`. No booking consumer is identified.

**Reviewers:** `@kestrel/pricing-team` as the service owner, plus `@kestrel/platform-team` and `@kestrel/web-team` for the cross-service contract change. If the change also updates an ADR, `@kestrel/architecture-guild` reviews the ADR. (ADR-0009; change-management policy §3.)
```

judge: 2  ·  human: ___

---

## ops-008  (ref: ops-008__graphify-federated__r2)

**Question**

Pricing wants to change the shape of the POST /v1/quote response. Which teams and
consumers are affected, and who has to review the change?

**Reference**

Consumers of pricing's /v1/quote are the gateway (kestrel-services/gateway, owned by
@kestrel/platform-team: PricingClient.quote and the QuoteOut model behind POST /api/quote)
and, through /api/quote, the web app (kestrel-web, @kestrel/web-team: Quote type and
mapQuote). Pricing-team owns the change itself. adr/0009-team-boundaries-and-codeowners.md
rule 4 says a contract change names every consuming team on the ticket and adds them as
reviewers; policies/change-management.md section 3 requires owner approval per CODEOWNERS.
tickets/PRC-233.md notes gateway and web are informed of quote changes.

**Rubric**

2 = gateway/platform-team AND web/web-team (via /api/quote) with the ADR-0009 rule or
    change-management requirement that they review;
1 = names only one consumer, or teams without the web-through-gateway path;
0 = only pricing-team, or booking named as a consumer.

**Answer**

```
A response-shape change affects **three teams**:

- **Pricing** owns `POST /v1/quote` and the change.
- **Platform** owns the gateway, which consumes pricing’s response.
- **Web** consumes the quote through the gateway’s `/api/quote` endpoint.

Get review from **pricing-team** as the service owner, plus **platform-team** and **web-team** as the consuming teams. The **architecture guild** reviews an ADR if the change requires one; it isn’t a required reviewer for every contract-change PR. **Booking** isn’t listed as a consumer.

That follows [ADR-0009](adr/0009-team-boundaries-and-codeowners.md), which explicitly names gateway and web as reviewers for pricing quote contract changes; [ADR-0001](adr/0001-split-monolith-into-services.md) says browsers go through the gateway. Track it with a `PRC` ticket and preserve backward compatibility for one release per the [change-management policy](policies/change-management.md).
```

judge: 2  ·  human: ___

---

## ops-008  (ref: ops-008__graphify__r3)

**Question**

Pricing wants to change the shape of the POST /v1/quote response. Which teams and
consumers are affected, and who has to review the change?

**Reference**

Consumers of pricing's /v1/quote are the gateway (kestrel-services/gateway, owned by
@kestrel/platform-team: PricingClient.quote and the QuoteOut model behind POST /api/quote)
and, through /api/quote, the web app (kestrel-web, @kestrel/web-team: Quote type and
mapQuote). Pricing-team owns the change itself. adr/0009-team-boundaries-and-codeowners.md
rule 4 says a contract change names every consuming team on the ticket and adds them as
reviewers; policies/change-management.md section 3 requires owner approval per CODEOWNERS.
tickets/PRC-233.md notes gateway and web are informed of quote changes.

**Rubric**

2 = gateway/platform-team AND web/web-team (via /api/quote) with the ADR-0009 rule or
    change-management requirement that they review;
1 = names only one consumer, or teams without the web-through-gateway path;
0 = only pricing-team, or booking named as a consumer.

**Answer**

```
The **Pricing** team owns the endpoint; changing the `POST /v1/quote` response also affects:

- **Platform** — owns the gateway, which consumes pricing’s response.
- **Web** — consumes the gateway’s `/api/quote` response.

Add **`@kestrel/pricing-team`, `@kestrel/platform-team`, and `@kestrel/web-team`** as reviewers. ADR-0009 says cross-team contract changes need the owners’ approval and must name every consuming team on the ticket. If the change also updates an ADR, **`@kestrel/architecture-guild`** reviews that ADR. Sources: `adr/0009-team-boundaries-and-codeowners.md` (Decision, rules 1, 3–4) and `policies/change-management.md` (§3–4).
```

judge: 2  ·  human: ___

---

## ops-009  (ref: ops-009__baseline__r3)

**Question**

Who owns the decision to serialise concurrent reserves in booking with a database lock,
and which team was on call and wrote up the incident that led to it?

**Reference**

The decision owner is @kestrel/booking-team (owners of BookingService; stated in
postmortems/2026-06-14-double-booking.md, tickets/BOOK-398.md and adr/0009-team-boundaries-
and-codeowners.md rule 2; kestrel-services CODEOWNERS gives /booking/ to booking-team).
The postmortem was authored by the platform-team on-call (primary on the day) and reviewed
2026-06-18; a booking-team engineer joined at 14:48. It took 39 minutes to find the right
team, which led to ADR-0009 and the OPS-51 on-call rewrite (tickets/OPS-51.md). No
individual is named.

**Rubric**

2 = booking-team as decision owner AND platform-team on-call as postmortem author, with a
    supporting source (postmortem, ADR-0009 rule 2 or BOOK-398);
1 = only one of the two teams, or swaps the roles;
0 = architecture guild or pricing-team named as owner.

**Answer**

```
The **booking team** (`@kestrel/booking-team`) owns the decision to serialize concurrent reserves with a PostgreSQL advisory lock. **Platform team** (`@kestrel/platform-team`) was on call and wrote the postmortem for the double-booking incident that prompted it.

Sources: `postmortems/2026-06-14-double-booking.md` and `adr/0009-team-boundaries-and-codeowners.md`.
```

judge: 2  ·  human: ___

---

## ops-010  (ref: ops-010__baseline__r3)

**Question**

We want to add a column to the booking shipments table. Which teams must approve it, and
what change process and rollback rules apply?

**Reference**

Ownership is in kestrel-services CODEOWNERS: /booking/src/main/resources/db/ is owned by
both @kestrel/booking-team and @kestrel/platform-team, so both approve (adr/0009-team-
boundaries-and-codeowners.md rule 1: cross-team changes need both owners). Under
policies/change-management.md a deploy with a schema change is a Normal change: owning
team lead plus platform-team approval, ticket linked, tests green (mvn -q test), rollback
plan, and schema changes are expand-then-contract, backward compatible for one release;
runbooks/deploy-rollback.md adds that schema is forward-only and app rollback never rolls
it back. If the column surfaces in the API, consuming teams (gateway, web) are named on
the ticket.

**Rubric**

2 = booking-team AND platform-team (db/ path in CODEOWNERS) + Normal change +
    expand/contract or forward-only rule;
1 = names the right teams or the process but not both;
0 = says only booking-team, or architecture guild approves.

**Answer**

```
A new column in the booking schema is a **Normal** production change. Get approval from the **booking team lead** and **platform team**; the booking team also owns the booking-service path. If the change affects a contract used by other services, name each consuming team on the ticket and add them as reviewers. An architecture-guild review is needed if the change requires a new or changed ADR, not just for an ordinary column addition. (Change Management §2–5; ADR-0009)

Create a `BOOK-` ticket linked from the PR, include tests and a rollback plan, and keep the schema change backward-compatible for one release using **expand then contract**. Deploy staging then production with a 30-minute soak per environment; normal changes are not deployed Fridays after 14:00 UTC or before public holidays. (Change Management §3, §5)

If error rate exceeds 2%, p95 latency exceeds twice baseline, readiness fails, or a data-affecting bug is suspected for five minutes after deployment, roll back the application; rolling forward is allowed only with a fix already merged and tested. **Schema migrations are forward-only:** an application rollback does not revert the schema. If the migration is the cause, escalate to the owning team—do not manually drop the column. (Deploy Rollback: Decision rule, Database migrations)
```

judge: 2  ·  human: ___

---

## svc-007  (ref: svc-007__graphify-federated__r1)

**Question**

Which services and apps call booking's POST /v2/shipments, and what path does a browser
request take to reach it?

**Reference**

The only direct caller is the gateway: BookingClient.create_shipment in
gateway/gateway/clients/booking.py, reached from the create_shipment route in
gateway/gateway/routes/shipments.py (POST /api/shipments). The web app (kestrel-web,
src/api/client.ts createShipment, route /api/shipments) reaches booking only transitively
through the gateway, since browsers talk only to the gateway. On the booking side the
endpoint is ShipmentController.create, which delegates to BookingService.create.

**Rubric**

2 = gateway client as the direct consumer AND web via /api/shipments as the transitive
    consumer, with the route chain;
1 = names only the gateway, or claims the web app calls booking directly;
0 = wrong or no consumers.

**Answer**

```
**Direct caller:** `kestrel-gateway` is the only backend service caller I found. Its `BookingClient.create_shipment()` sends `POST /v2/shipments` to the configured `BOOKING_BASE_URL` (default `http://localhost:8081`). The web app does **not** call booking directly.

**Browser path:** `kestrel-web`’s `useCreateShipment` hook → `src/api/client.ts::createShipment()` → `POST /api/shipments` on the gateway → `gateway/gateway/routes/shipments.py::create_shipment()` → `BookingClient.create_shipment()` → booking’s `ShipmentController.create()`.

The gateway README documents the `/api/shipments` to `/v2/shipments` mapping; the gateway client and route are in `gateway/gateway/clients/booking.py:33` and `gateway/gateway/routes/shipments.py:18`.
```

judge: 2  ·  human: ___

---

## web-006  (ref: web-006__baseline__r2)

**Question**

Booking started returning an ETA confidence score on shipments weeks ago, but the web app
never shows it. Where along the way does it get lost, and which layers still need work?

**Reference**

Booking emits eta_confidence (ShipmentResponse, behind the kestrel.booking.features.
eta-confidence flag; BOOK-412 done). The gateway drops it: ShipmentOut in
kestrel-services/gateway/gateway/models.py is an explicit Pydantic model without the
field and is not a pass-through (ADR-0004; GW-118 open). The web app is also stale:
Shipment in src/api/types.ts, ShipmentWire in src/api/wire.ts and mapShipment in
src/api/mappers.ts have no eta_confidence/etaConfidence (WEB-77 open, blocked on GW-118).
So the stale layers are the gateway first, then web; the production flag must stay off.

**Rubric**

2 = gateway ShipmentOut drops it AND web types/wire/mapper lack it, with booking as the
    source (tickets or ADR-0008 rollout order a bonus);
1 = identifies only the gateway or only the web layer;
0 = blames booking or the UI component only.

**Answer**

```
The score is dropped in **`mapShipment`**. The API client parses booking, detail, reserve, and list responses as `ShipmentWire` (`src/api/client.ts:95–108`), but `ShipmentWire` has no confidence field (`src/api/wire.ts:3–10`), and the mapper explicitly builds a new `Shipment` containing only the existing fields (`src/api/mappers.ts:33`). So even if the server response includes the score, it never reaches the UI. The domain type also has no place for it (`src/api/types.ts:15–22`).

The remaining work is to add the server’s exact field name and type to the wire contract, map it to a domain property, and render it where wanted: shipment detail currently shows only ETA (`src/pages/ShipmentDetail.tsx:46`), and the shipment table does too (`src/components/ShipmentTable.tsx:16`). Booking submission navigates to detail, which fetches the shipment again, so the detail endpoint must also return the score. Tests and fixtures need updating; notably, the mapper test currently asserts that unknown wire fields are dropped (`tests/api/mappers.test.ts:25–28`). The repo doesn’t establish the score’s exact wire name, range, or nullability, so those should match the backend contract.
```

judge: 1  ·  human: ___

---

## web-006  (ref: web-006__graphify__r3)

**Question**

Booking started returning an ETA confidence score on shipments weeks ago, but the web app
never shows it. Where along the way does it get lost, and which layers still need work?

**Reference**

Booking emits eta_confidence (ShipmentResponse, behind the kestrel.booking.features.
eta-confidence flag; BOOK-412 done). The gateway drops it: ShipmentOut in
kestrel-services/gateway/gateway/models.py is an explicit Pydantic model without the
field and is not a pass-through (ADR-0004; GW-118 open). The web app is also stale:
Shipment in src/api/types.ts, ShipmentWire in src/api/wire.ts and mapShipment in
src/api/mappers.ts have no eta_confidence/etaConfidence (WEB-77 open, blocked on GW-118).
So the stale layers are the gateway first, then web; the production flag must stay off.

**Rubric**

2 = gateway ShipmentOut drops it AND web types/wire/mapper lack it, with booking as the
    source (tickets or ADR-0008 rollout order a bonus);
1 = identifies only the gateway or only the web layer;
0 = blames booking or the UI component only.

**Answer**

```
The score is **not being stripped by the HTTP client**: it parses the response as JSON and returns it. The first actual loss is `mapShipment` (`src/api/mappers.ts:33–42`), which constructs a new object containing only the fields it knows. `ShipmentWire` (`src/api/wire.ts:3–11`) doesn’t declare a confidence field, and the domain `Shipment` type (`src/api/types.ts:13–23`) and mapper don’t carry one through. The mapper tests even codify dropping unknown fields (`tests/api/mappers.test.ts:26–30`).

The same mapper handles booking, shipment fetches, and reservations (`src/api/client.ts:91–108`), so the score can be dropped on any of those responses. The UI then has nothing to display: the detail page renders ETA only (`src/pages/ShipmentDetail.tsx:38–46`), as does the shipment table (`src/components/ShipmentTable.tsx:16–30`). To surface it, align the wire field name and value semantics with the backend contract, add it to the wire and domain types, map it, and render it on the intended shipment views. The booking flow navigates to the detail page, which fetches the shipment again, so that GET response needs to carry the score too.
```

judge: 1  ·  human: ___

---

## web-007  (ref: web-007__graphify__r2)

**Question**

The booking form generates a reference up front so that a double submit or a retry should
not create a second shipment. Follow that field from the form to the booking service: is
the retry actually idempotent end to end?

**Reference**

No. The web form generates the reference (generateReference in src/lib/validation.ts,
used in src/pages/BookingForm.tsx) and createShipmentToWire (src/api/mappers.ts) sends it
as "reference". The gateway ShipmentIn (kestrel-services/gateway/gateway/models.py) accepts
reference and BookingClient.create_shipment (gateway/gateway/clients/booking.py) forwards
it and even marks the call retryable when it is set. But booking's CreateShipmentRequest
(booking/.../web/dto/CreateShipmentRequest.java) reads client_reference, not reference;
Jackson ignores the unknown field, so booking derives its own reference and idempotency
(ADR-0006) is silently broken. A retried POST can create a duplicate shipment. No ticket
exists yet.

**Rubric**

2 = traces reference through web, gateway AND names the client_reference mismatch in
    booking, concluding idempotency is broken;
1 = notices the field is passed along and ADR-0006 but misses the name mismatch (or finds
    the mismatch without tracing the web/gateway hops);
0 = concludes retries are safe.

**Answer**

```
**No—the frontend does not make retries idempotent.** When the reference is blank, `BookingForm` calls `generateReference()` inside `onSubmit` and sends it without saving it to form state (`src/pages/BookingForm.tsx:49–55`). A retry therefore generates a new reference. The reference does pass through the mapper into the POST body (`src/api/mappers.ts:71–77`), but the request adds no idempotency key (`src/api/client.ts:59–66, 89–97`). The button is disabled while a request is loading, but that is not a durable deduplication guarantee.

A user-entered reference stays the same on retry, but that only helps if the booking service atomically treats it as a unique idempotency key. This repository contains the web client, not the service implementation, so I can’t verify that behavior. If the service doesn’t deduplicate by reference, a retry—especially after a lost response—can create a second shipment.
```

judge: 0  ·  human: ___

---
