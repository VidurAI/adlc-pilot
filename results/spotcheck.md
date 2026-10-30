# Spot-check sheet (arm hidden)

21 of 108 judged answers. Fill `human:` with 0/1/2.
`adlc scorecard --spotcheck results/spotcheck.md` computes agreement.

## svc-001  (ref: svc-001__graphify-guard__r1)

**Question**

A customer screenshot shows the public API answering with "booking temporarily
unavailable". Where in the gateway is that message defined, and which HTTP status
and machine code go with it?

**Reference**

gateway/gateway/errors.py: class BookingUnavailable (a subclass of UpstreamUnavailable)
sets default_detail = "booking temporarily unavailable" and code = "booking_unavailable";
the HTTP status is 503, inherited from UpstreamUnavailable. It is raised from
gateway/gateway/clients/booking.py (BookingClient.translate_status for booking's 429,
plus unavailable_error for transport failures and an open circuit breaker).

**Rubric**

2 = names errors.py / BookingUnavailable AND the 503 status AND code booking_unavailable;
1 = finds the message in errors.py but misses the status or the code;
0 = wrong file, or only finds the test assertions.

**Answer**

```
It’s defined in `gateway/errors.py` on `BookingUnavailable`: the detail is **“booking temporarily unavailable”** and the machine code is **`booking_unavailable`**. It inherits HTTP **503** from `UpstreamUnavailable`.
```

judge: 2  ·  human: ___

---

## svc-001  (ref: svc-001__graphify-guard__r3)

**Question**

A customer screenshot shows the public API answering with "booking temporarily
unavailable". Where in the gateway is that message defined, and which HTTP status
and machine code go with it?

**Reference**

gateway/gateway/errors.py: class BookingUnavailable (a subclass of UpstreamUnavailable)
sets default_detail = "booking temporarily unavailable" and code = "booking_unavailable";
the HTTP status is 503, inherited from UpstreamUnavailable. It is raised from
gateway/gateway/clients/booking.py (BookingClient.translate_status for booking's 429,
plus unavailable_error for transport failures and an open circuit breaker).

**Rubric**

2 = names errors.py / BookingUnavailable AND the 503 status AND code booking_unavailable;
1 = finds the message in errors.py but misses the status or the code;
0 = wrong file, or only finds the test assertions.

**Answer**

```
It’s defined in `gateway/gateway/errors.py:90–92`, on `BookingUnavailable`. It inherits HTTP **503** from `UpstreamUnavailable`; the machine code is **`booking_unavailable`**.
```

judge: 2  ·  human: ___

---

## svc-001  (ref: svc-001__graphify__r1)

**Question**

A customer screenshot shows the public API answering with "booking temporarily
unavailable". Where in the gateway is that message defined, and which HTTP status
and machine code go with it?

**Reference**

gateway/gateway/errors.py: class BookingUnavailable (a subclass of UpstreamUnavailable)
sets default_detail = "booking temporarily unavailable" and code = "booking_unavailable";
the HTTP status is 503, inherited from UpstreamUnavailable. It is raised from
gateway/gateway/clients/booking.py (BookingClient.translate_status for booking's 429,
plus unavailable_error for transport failures and an open circuit breaker).

**Rubric**

2 = names errors.py / BookingUnavailable AND the 503 status AND code booking_unavailable;
1 = finds the message in errors.py but misses the status or the code;
0 = wrong file, or only finds the test assertions.

**Answer**

```
The message is defined in `gateway/errors.py:92` as `BookingUnavailable.default_detail`. That class inherits HTTP **503** from `UpstreamUnavailable` (`gateway/errors.py:84–85`) and sets the machine code to **`booking_unavailable`** at line 91.
```

judge: 2  ·  human: ___

---

## svc-001  (ref: svc-001__graphify__r2)

**Question**

A customer screenshot shows the public API answering with "booking temporarily
unavailable". Where in the gateway is that message defined, and which HTTP status
and machine code go with it?

**Reference**

gateway/gateway/errors.py: class BookingUnavailable (a subclass of UpstreamUnavailable)
sets default_detail = "booking temporarily unavailable" and code = "booking_unavailable";
the HTTP status is 503, inherited from UpstreamUnavailable. It is raised from
gateway/gateway/clients/booking.py (BookingClient.translate_status for booking's 429,
plus unavailable_error for transport failures and an open circuit breaker).

**Rubric**

2 = names errors.py / BookingUnavailable AND the 503 status AND code booking_unavailable;
1 = finds the message in errors.py but misses the status or the code;
0 = wrong file, or only finds the test assertions.

**Answer**

```
The message is defined in `gateway/errors.py` on `BookingUnavailable.default_detail`. It inherits HTTP **503 Service Unavailable** from `UpstreamUnavailable`; its machine code is **`booking_unavailable`**.
```

judge: 2  ·  human: ___

---

## svc-001  (ref: svc-001__graphify__r3)

**Question**

A customer screenshot shows the public API answering with "booking temporarily
unavailable". Where in the gateway is that message defined, and which HTTP status
and machine code go with it?

**Reference**

gateway/gateway/errors.py: class BookingUnavailable (a subclass of UpstreamUnavailable)
sets default_detail = "booking temporarily unavailable" and code = "booking_unavailable";
the HTTP status is 503, inherited from UpstreamUnavailable. It is raised from
gateway/gateway/clients/booking.py (BookingClient.translate_status for booking's 429,
plus unavailable_error for transport failures and an open circuit breaker).

**Rubric**

2 = names errors.py / BookingUnavailable AND the 503 status AND code booking_unavailable;
1 = finds the message in errors.py but misses the status or the code;
0 = wrong file, or only finds the test assertions.

**Answer**

```
It’s defined in `gateway/errors.py:90–92`, on `BookingUnavailable`. The API responds with **HTTP 503** and machine code **`booking_unavailable`**.
```

judge: 2  ·  human: ___

---

## svc-001  (ref: svc-001__serena__r2)

**Question**

A customer screenshot shows the public API answering with "booking temporarily
unavailable". Where in the gateway is that message defined, and which HTTP status
and machine code go with it?

**Reference**

gateway/gateway/errors.py: class BookingUnavailable (a subclass of UpstreamUnavailable)
sets default_detail = "booking temporarily unavailable" and code = "booking_unavailable";
the HTTP status is 503, inherited from UpstreamUnavailable. It is raised from
gateway/gateway/clients/booking.py (BookingClient.translate_status for booking's 429,
plus unavailable_error for transport failures and an open circuit breaker).

**Rubric**

2 = names errors.py / BookingUnavailable AND the 503 status AND code booking_unavailable;
1 = finds the message in errors.py but misses the status or the code;
0 = wrong file, or only finds the test assertions.

**Answer**

```
It’s defined in `gateway/errors.py` in `BookingUnavailable`: the detail is **“booking temporarily unavailable”** and the machine code is **`booking_unavailable`**. It inherits HTTP **503 Service Unavailable** from `UpstreamUnavailable`.
```

judge: 2  ·  human: ___

---

## svc-003  (ref: svc-003__baseline__r1)

**Question**

I'm tidying the gateway's legacy/ package, which holds the old local pricing formula
from before the pricing service existed. What depends on it, and what would break if I
deleted it?

**Reference**

Nothing depends on it: no module under gateway/ or tests/ imports the pricing_v1 module,
nothing loads it dynamically (no importlib or __import__) or by name from settings or
pyproject, and quotes go through PricingClient to pricing's /v1/quote instead. Only the
gateway README layout listing mentions legacy/. Deleting it breaks nothing; it is dead
code (ticket GW-102, still open in kestrel-ops). Unlike pricing's LegacyTariffLoader,
nothing selects it by name from configuration.

**Rubric**

2 = says it is dead / nothing imports it, AND shows it checked dynamic or config loading
    (or cites GW-102), so deletion is safe;
1 = says nothing imports it but does not rule out dynamic or config-based loading;
0 = claims something uses it, or says it must not be deleted.

**Answer**

```
**Nothing in the gateway’s current runtime or tests depends on `gateway/legacy/`.** The quote route delegates to `QuoteService`, which calls `PricingClient` and the pricing service’s `/v1/quote` endpoint; the legacy formula is not on that path. The quote tests mock the pricing service rather than use the local formula.

Deleting it should not change the gateway’s current API behavior. It would break any external code that imports `gateway.legacy` or `gateway.legacy.pricing_v1`; setuptools’ `gateway*` package discovery currently includes it in distributions. The README’s layout would also become stale. One repo instruction explicitly says not to touch `gateway/legacy/`.
```

judge: 1  ·  human: ___

---

## svc-003  (ref: svc-003__graphify__r2)

**Question**

I'm tidying the gateway's legacy/ package, which holds the old local pricing formula
from before the pricing service existed. What depends on it, and what would break if I
deleted it?

**Reference**

Nothing depends on it: no module under gateway/ or tests/ imports the pricing_v1 module,
nothing loads it dynamically (no importlib or __import__) or by name from settings or
pyproject, and quotes go through PricingClient to pricing's /v1/quote instead. Only the
gateway README layout listing mentions legacy/. Deleting it breaks nothing; it is dead
code (ticket GW-102, still open in kestrel-ops). Unlike pricing's LegacyTariffLoader,
nothing selects it by name from configuration.

**Rubric**

2 = says it is dead / nothing imports it, AND shows it checked dynamic or config loading
    (or cites GW-102), so deletion is safe;
1 = says nothing imports it but does not rule out dynamic or config-based loading;
0 = claims something uses it, or says it must not be deleted.

**Answer**

```
**No in-repo gateway code or tests import the legacy package.** Its only internal call is `quote()` using `chargeable_weight()` in `gateway/legacy/pricing_v1.py`. The active `/api/quote` path uses `QuoteService` and `PricingClient` to call pricing’s `POST /v1/quote`, so deleting the package shouldn’t change gateway runtime or API behavior.

Deletion would break any external or untracked code importing the legacy functions or constants. The repository guidance also marks the package for removal under a separate ticket, so follow that process before deleting it. I made no gateway code changes; the graph query left generated records under `graphify-out/`.
```

judge: 1  ·  human: ___

---

## svc-004  (ref: svc-004__graphify__r1)

**Question**

Which of the gateway's calls to booking and pricing get retried automatically when they
fail, how many attempts do they get, and where is that decision made?

**Reference**

Attempts come from GATEWAY_RETRY_ATTEMPTS (Settings.gateway_retry_attempts, default 3,
gateway/gateway/config.py) via RetryPolicy built in gateway/gateway/main.py, with
exponential backoff and jitter (gateway/gateway/retry.py). UpstreamClient.request
(gateway/gateway/clients/base.py) passes an idempotent flag to is_retryable_error:
connect failures are always retried; 502/503/504 and other transport errors or timeouts
only when idempotent. Default idempotent = GET/HEAD/PUT/DELETE/OPTIONS. Overrides:
BookingClient.reserve_shipment is idempotent=False so reserve is never retried (GW-96);
create_shipment is retryable only when the payload carries a reference; PricingClient.quote
is POST but idempotent=True. Booking 429s are translated and not retried.

**Rubric**

2 = decision point (base.py + retry.py), default 3 attempts, AND the reserve=never /
    create=only-with-reference / quote=yes distinction;
1 = describes retry policy and attempts but misses the per-call idempotent overrides;
0 = says everything or nothing is retried.

**Answer**

```
The gateway retries these booking and pricing calls, subject to the failure type:

| Service | Call | Retry safety |
|---|---|---|
| Booking | `GET /v2/shipments/{id}` and `GET /v2/carriers` | Idempotent by default |
| Booking | `POST /v2/shipments` | Idempotent only when the payload includes a reference |
| Booking | `POST /v2/shipments/{id}/reserve` | Not idempotent |
| Pricing | `POST /v1/quote` | Explicitly marked idempotent |
| Pricing | `GET /v1/carriers/{code}/surcharges` | Idempotent by default |

They get **3 attempts total by default**, configurable with `GATEWAY_RETRY_ATTEMPTS`. Connection errors, connect timeouts, and pool timeouts are retried regardless of idempotency. HTTP `502`, `503`, and `504`, and other transport errors, are retried only for idempotent calls; other statuses (such as `429` or `500`) aren’t retried.

The decision is split across the shared retry plumbing and the clients: `gateway/clients/booking.py` and `gateway/clients/pricing.py` set operation idempotency; `gateway/clients/base.py` applies that policy to requests; and `gateway/retry.py` classifies retryable failures and enforces the attempt limit. `gateway/main.py` supplies the configured policy to both clients; the default is in `gateway/config.py`.
```

judge: 2  ·  human: ___

---

## svc-004  (ref: svc-004__serena__r1)

**Question**

Which of the gateway's calls to booking and pricing get retried automatically when they
fail, how many attempts do they get, and where is that decision made?

**Reference**

Attempts come from GATEWAY_RETRY_ATTEMPTS (Settings.gateway_retry_attempts, default 3,
gateway/gateway/config.py) via RetryPolicy built in gateway/gateway/main.py, with
exponential backoff and jitter (gateway/gateway/retry.py). UpstreamClient.request
(gateway/gateway/clients/base.py) passes an idempotent flag to is_retryable_error:
connect failures are always retried; 502/503/504 and other transport errors or timeouts
only when idempotent. Default idempotent = GET/HEAD/PUT/DELETE/OPTIONS. Overrides:
BookingClient.reserve_shipment is idempotent=False so reserve is never retried (GW-96);
create_shipment is retryable only when the payload carries a reference; PricingClient.quote
is POST but idempotent=True. Booking 429s are translated and not retried.

**Rubric**

2 = decision point (base.py + retry.py), default 3 attempts, AND the reserve=never /
    create=only-with-reference / quote=yes distinction;
1 = describes retry policy and attempts but misses the per-call idempotent overrides;
0 = says everything or nothing is retried.

**Answer**

```
The gateway allows **up to 3 total attempts** (the initial call plus up to 2 retries) by default. `GATEWAY_RETRY_ATTEMPTS` can change that.

- **Booking:** `GET /v2/shipments/{id}` and `GET /v2/carriers` are retryable as idempotent calls. `POST /v2/shipments` is retryable for upstream responses or transport errors only when the payload includes a `reference`; `POST /v2/shipments/{id}/reserve` is not retried for those failures because it is explicitly non-idempotent.
- **Pricing:** `POST /v1/quote` is explicitly safe to retry, and `GET /v1/carriers/{code}/surcharges` is retryable by default.

For **all** calls, connection failures (`ConnectError`, `ConnectTimeout`, `PoolTimeout`) may be retried. For idempotent calls, the gateway also retries other transport errors and upstream **502, 503, or 504** responses; it does not retry other HTTP statuses.

The decision is implemented in `gateway/clients/base.py` (`request` and `_send_with_retries`) and `gateway/retry.py` (`is_retryable_error` and `retry_async`). The default attempt count is in `gateway/config.py`; `gateway/main.py` builds one shared policy for both clients.
```

judge: 2  ·  human: ___

---

## svc-006  (ref: svc-006__graphify-guard__r2)

**Question**

What is the default timeout for the gateway's calls to booking and pricing, and which
environment variable overrides it?

**Reference**

The environment variable is GATEWAY_TIMEOUT_SECONDS. It maps to Settings.gateway_timeout_seconds
in gateway/gateway/config.py, default 5.0 seconds, validated to be greater than zero. main.py
passes it to the httpx clients for booking and pricing (connect timeout capped at 2 s).

**Rubric**

2 = GATEWAY_TIMEOUT_SECONDS + default 5 seconds + config.py (Settings field);
1 = gets the variable or the default but not both, or no file;
0 = wrong variable or wrong default.

**Answer**

```
The default timeout is **5 seconds** for both booking and pricing calls. Override it with `GATEWAY_TIMEOUT_SECONDS`.
```

judge: 1  ·  human: ___

---

## svc-006  (ref: svc-006__serena__r3)

**Question**

What is the default timeout for the gateway's calls to booking and pricing, and which
environment variable overrides it?

**Reference**

The environment variable is GATEWAY_TIMEOUT_SECONDS. It maps to Settings.gateway_timeout_seconds
in gateway/gateway/config.py, default 5.0 seconds, validated to be greater than zero. main.py
passes it to the httpx clients for booking and pricing (connect timeout capped at 2 s).

**Rubric**

2 = GATEWAY_TIMEOUT_SECONDS + default 5 seconds + config.py (Settings field);
1 = gets the variable or the default but not both, or no file;
0 = wrong variable or wrong default.

**Answer**

```
The default timeout is **5 seconds** for both booking and pricing calls. Override it with **`GATEWAY_TIMEOUT_SECONDS`**.
```

judge: 1  ·  human: ___

---

## web-001  (ref: web-001__baseline__r3)

**Question**

Which environment variable turns on comparing quotes across all carriers in the web app,
where is it read, and what values count as "on"?

**Reference**

VITE_FEATURE_MULTI_CARRIER_QUOTES. src/lib/flags.ts: isMultiCarrierQuotesEnabled() reads
it from import.meta.env and parseFlag treats 1, true, on, yes and enabled (case-insensitive,
trimmed) as true; anything else or unset is false. It is consumed in src/pages/QuotePage.tsx
and documented with default false in .env.example.

**Rubric**

2 = variable name + flags.ts parsing + the accepted truthy values;
1 = variable name and file but not the truthy values (or the reverse);
0 = wrong variable or file.

**Answer**

```
Set `VITE_FEATURE_MULTI_CARRIER_QUOTES` to enable comparing quotes across all active carriers. It’s read from `import.meta.env` in `src/lib/flags.ts` and checked by `QuotePage` in `src/pages/QuotePage.tsx`.

Values count as “on” after trimming whitespace and ignoring case: `1`, `true`, `on`, `yes`, or `enabled`. Unset values and anything else count as off.
```

judge: 2  ·  human: ___

---

## web-001  (ref: web-001__graphify__r2)

**Question**

Which environment variable turns on comparing quotes across all carriers in the web app,
where is it read, and what values count as "on"?

**Reference**

VITE_FEATURE_MULTI_CARRIER_QUOTES. src/lib/flags.ts: isMultiCarrierQuotesEnabled() reads
it from import.meta.env and parseFlag treats 1, true, on, yes and enabled (case-insensitive,
trimmed) as true; anything else or unset is false. It is consumed in src/pages/QuotePage.tsx
and documented with default false in .env.example.

**Rubric**

2 = variable name + flags.ts parsing + the accepted truthy values;
1 = variable name and file but not the truthy values (or the reverse);
0 = wrong variable or file.

**Answer**

```
The flag is **`VITE_FEATURE_MULTI_CARRIER_QUOTES`**. It’s read in `src/lib/flags.ts:12-13` by `isMultiCarrierQuotesEnabled()`, which `src/pages/QuotePage.tsx:55` calls.

Values count as on after trimming whitespace and ignoring case: **`1`, `true`, `on`, `yes`, or `enabled`**. Missing values and anything else count as off.
```

judge: 2  ·  human: ___

---

## web-001  (ref: web-001__serena__r3)

**Question**

Which environment variable turns on comparing quotes across all carriers in the web app,
where is it read, and what values count as "on"?

**Reference**

VITE_FEATURE_MULTI_CARRIER_QUOTES. src/lib/flags.ts: isMultiCarrierQuotesEnabled() reads
it from import.meta.env and parseFlag treats 1, true, on, yes and enabled (case-insensitive,
trimmed) as true; anything else or unset is false. It is consumed in src/pages/QuotePage.tsx
and documented with default false in .env.example.

**Rubric**

2 = variable name + flags.ts parsing + the accepted truthy values;
1 = variable name and file but not the truthy values (or the reverse);
0 = wrong variable or file.

**Answer**

```
Set `VITE_FEATURE_MULTI_CARRIER_QUOTES`. It’s read from `import.meta.env` by `isMultiCarrierQuotesEnabled()` in `src/lib/flags.ts`, which the quote page calls in `src/pages/QuotePage.tsx`.

Values count as “on” after trimming whitespace and ignoring case: `1`, `true`, `on`, `yes`, or `enabled`. Unset values and anything else are off.
```

judge: 2  ·  human: ___

---

## web-002  (ref: web-002__graphify-guard__r2)

**Question**

Where in the web app is a user stopped from firing the reserve request twice by
clicking the Reserve button repeatedly while the first call is still in flight?

**Reference**

src/pages/ShipmentDetail.tsx renders the Reserve button with disabled={reserving}, where
reserving = reserveStatus === 'loading'. That status comes from useReserveShipment
(src/hooks/useReserveShipment.ts), which wraps useMutation (src/hooks/useMutation.ts);
useMutation.run sets status 'loading' before awaiting the API call and the label becomes
"Reserving…". There is no debounce or lock in the API client itself.

**Rubric**

2 = ShipmentDetail button disabled while status is loading AND the useMutation/
    useReserveShipment state it derives from;
1 = only the disabled button, without where the loading status originates;
0 = points at the API client, router, or says nothing prevents it.

**Answer**

```
The guard is in **`src/pages/ShipmentDetail.tsx:27, 48–50`**. `reserveStatus === 'loading'` sets `reserving`, which disables the Reserve button and changes its label to “Reserving…”. The reserve hook gets that status from `useMutation` in **`src/hooks/useReserveShipment.ts`**; `useMutation` sets it to `loading` when the request starts (`src/hooks/useMutation.ts:30–32`).

This prevents repeat clicks through the UI while the request is in flight; the mutation hook itself does not independently block duplicate `run` calls.
```

judge: 2  ·  human: ___

---

## web-002  (ref: web-002__graphify__r3)

**Question**

Where in the web app is a user stopped from firing the reserve request twice by
clicking the Reserve button repeatedly while the first call is still in flight?

**Reference**

src/pages/ShipmentDetail.tsx renders the Reserve button with disabled={reserving}, where
reserving = reserveStatus === 'loading'. That status comes from useReserveShipment
(src/hooks/useReserveShipment.ts), which wraps useMutation (src/hooks/useMutation.ts);
useMutation.run sets status 'loading' before awaiting the API call and the label becomes
"Reserving…". There is no debounce or lock in the API client itself.

**Rubric**

2 = ShipmentDetail button disabled while status is loading AND the useMutation/
    useReserveShipment state it derives from;
1 = only the disabled button, without where the loading status originates;
0 = points at the API client, router, or says nothing prevents it.

**Answer**

```
In `src/pages/ShipmentDetail.tsx:27,49`, `reserving` becomes true when the reserve status is `loading`, and that disables the **Reserve shipment** button while changing its label to “Reserving…”. The status comes from `useMutation` via `src/hooks/useReserveShipment.ts:16`.

That’s a UI-level guard; `useMutation.run` itself doesn’t reject overlapping calls.
```

judge: 2  ·  human: ___

---

## web-002  (ref: web-002__serena__r2)

**Question**

Where in the web app is a user stopped from firing the reserve request twice by
clicking the Reserve button repeatedly while the first call is still in flight?

**Reference**

src/pages/ShipmentDetail.tsx renders the Reserve button with disabled={reserving}, where
reserving = reserveStatus === 'loading'. That status comes from useReserveShipment
(src/hooks/useReserveShipment.ts), which wraps useMutation (src/hooks/useMutation.ts);
useMutation.run sets status 'loading' before awaiting the API call and the label becomes
"Reserving…". There is no debounce or lock in the API client itself.

**Rubric**

2 = ShipmentDetail button disabled while status is loading AND the useMutation/
    useReserveShipment state it derives from;
1 = only the disabled button, without where the loading status originates;
0 = points at the API client, router, or says nothing prevents it.

**Answer**

```
On the shipment detail page, `src/pages/ShipmentDetail.tsx:27,49` sets `reserving` from the reserve mutation’s loading status and disables the **Reserve shipment** button while it’s true. `src/hooks/useMutation.ts:30` sets that status to `loading` when the request starts.
```

judge: 2  ·  human: ___

---

## web-003  (ref: web-003__baseline__r3)

**Question**

The money rounding helper in the web app has a known bug. Which parts of the UI
actually show values that pass through it, directly or indirectly?

**Reference**

roundMoney in src/lib/money.ts is called by formatMoney, sumMoney and parseMoneyInput in the
same file. Only formatMoney has a production caller: the MoneyText component
(src/components/MoneyText.tsx). MoneyText is rendered by QuoteBreakdown
(src/components/QuoteBreakdown.tsx, each breakdown line and the total) and directly by
QuotePage (src/pages/QuotePage.tsx, per-carrier quote total). sumMoney and parseMoneyInput
are not used outside tests. So every price shown on the quote page is rounded by it.

**Rubric**

2 = formatMoney -> MoneyText -> QuoteBreakdown and QuotePage, noting sumMoney/
    parseMoneyInput are unused in src;
1 = gets money.ts internals and MoneyText but misses QuoteBreakdown or QuotePage;
0 = only money.ts or wrong components.

**Answer**

```
The bug affects **quote pricing displays**:

- **Quote card total** in `QuotePage` (`src/pages/QuotePage.tsx:43`).
- **Each breakdown line amount and the breakdown total** in `QuoteBreakdown` (`src/components/QuoteBreakdown.tsx:21,30`).

Those values flow through `MoneyText` → `formatMoney` → `roundMoney` (`src/components/MoneyText.tsx:11`, `src/lib/money.ts:10`). Shipment list/detail and booking screens don’t display values through this path. The helper’s `sumMoney` and `parseMoneyInput` also call `roundMoney`, but have no other callers in the app.
```

judge: 2  ·  human: ___

---

## web-003  (ref: web-003__graphify-guard__r3)

**Question**

The money rounding helper in the web app has a known bug. Which parts of the UI
actually show values that pass through it, directly or indirectly?

**Reference**

roundMoney in src/lib/money.ts is called by formatMoney, sumMoney and parseMoneyInput in the
same file. Only formatMoney has a production caller: the MoneyText component
(src/components/MoneyText.tsx). MoneyText is rendered by QuoteBreakdown
(src/components/QuoteBreakdown.tsx, each breakdown line and the total) and directly by
QuotePage (src/pages/QuotePage.tsx, per-carrier quote total). sumMoney and parseMoneyInput
are not used outside tests. So every price shown on the quote page is rounded by it.

**Rubric**

2 = formatMoney -> MoneyText -> QuoteBreakdown and QuotePage, noting sumMoney/
    parseMoneyInput are unused in src;
1 = gets money.ts internals and MoneyText but misses QuoteBreakdown or QuotePage;
0 = only money.ts or wrong components.

**Answer**

```
The displayed values all go through **`roundMoney` → `formatMoney` → `MoneyText`**. In the quote UI, that means:

- **Each carrier quote’s headline total** (`QuotePage.tsx:43`).
- **Each breakdown line amount and the breakdown’s repeated total** (`QuoteBreakdown.tsx:21,30`).

With quote comparison enabled, those same displays appear for each carrier result. I found no other UI call sites. `sumMoney` and `parseMoneyInput` also call `roundMoney`, but neither is used by the app UI.
```

judge: 2  ·  human: ___

---

## web-005  (ref: web-005__graphify-guard__r1)

**Question**

On the quote page, when the pricing call for one carrier fails, how does that failure get
from the fetch to the screen, and does one failing carrier hide the others' quotes?

**Reference**

QuotePage (src/pages/QuotePage.tsx) calls fetchQuote/fetchQuotes from useQuote
(src/hooks/useQuote.ts), which runs requestQuote in src/api/client.ts for each carrier with
Promise.allSettled. A rejected call (ApiError from request()) is stored as that carrier's
CarrierQuote.error with quote null, so other carriers' quotes still render. The failing
card shows an ErrorBanner with QUOTE_ERROR_COPY (src/lib/copy.ts) and detail from
describeError (src/api/errors.ts). Only when every carrier fails does useQuote set a
top-level error and status 'error'.

**Rubric**

2 = useQuote allSettled per-carrier error handling + QuotePage per-card ErrorBanner with
    QUOTE_ERROR_COPY, and says other carriers still show;
1 = describes the error path but not the per-carrier isolation (or the reverse);
0 = claims one failure blanks all quotes or misses useQuote.

**Answer**

```
The graph traces `requestQuote()` (`src/api/client.ts:111`) → `UseQuote` (`src/hooks/useQuote.ts:33`) → `QuotePage()` (`src/pages/QuotePage.tsx:57`). The request calls `quoteRequestToWire()` and `mapQuote()`; the page calls `describeError()` and `ErrorBanner()` at `QuotePage.tsx:88`, and renders `QuoteCard()` at `QuotePage.tsx:137`.

**Whether one carrier’s failure hides other quotes isn’t established by the graph.** It shows the request and display connections, but not the rejection handling or per-carrier aggregation logic needed to answer that definitively.
```

judge: 1  ·  human: ___

---
