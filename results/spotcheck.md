# Spot-check sheet (arm hidden)

5 of 27 judged answers. Fill `human:` with 0/1/2.
`adlc scorecard --spotcheck results/spotcheck.md` computes agreement.

## svc-001  (ref: svc-001__graphify-lean__r2)

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
It’s defined in `gateway/errors.py:90–92` as `BookingUnavailable`. It inherits HTTP **503 Service Unavailable** from `UpstreamUnavailable` (`gateway/errors.py:85`) and uses machine code **`booking_unavailable`**.
```

judge: 2  ·  human: ___

---

## svc-003  (ref: svc-003__graphify-lean__r2)

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
**No in-repo code or tests depend on the legacy formula.** A repository-wide search found no imports or references to it; the fresh graph also didn’t include a node for the package, so that conclusion comes from the source search. The gateway’s quote route goes through `QuoteService` to `PricingClient`, which posts to the pricing service’s `/v1/quote` endpoint (`gateway/gateway/routes/quote.py:16–20`, `gateway/gateway/services.py:48–62`, `gateway/gateway/clients/pricing.py:14–25`).

Deleting `gateway/gateway/legacy/` therefore shouldn’t break the gateway’s current routes or runtime. It would remove the old module’s direct-import API—`quote`, `chargeable_weight`, and its formula constants (`gateway/gateway/legacy/pricing_v1.py:11–31,47–72`)—so external scripts or consumers importing it could break. The package is included by the setuptools `gateway*` discovery rule (`gateway/pyproject.toml:25–26`).

One caveat: `gateway/AGENTS.md:13` says not to touch `gateway/legacy/`; follow the separate removal ticket/process noted there before deleting it.
```

judge: 1  ·  human: ___

---

## svc-006  (ref: svc-006__graphify-lean__r2)

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
The default timeout is **5 seconds** for calls to both booking and pricing. Set **`GATEWAY_TIMEOUT_SECONDS`** to override it (`gateway/config.py:26,54`); both clients use that setting (`gateway/main.py:51–54`).
```

judge: 2  ·  human: ___

---

## web-001  (ref: web-001__graphify-lean__r1)

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
The flag is **`VITE_FEATURE_MULTI_CARRIER_QUOTES`**. It’s read in `src/lib/flags.ts` by `isMultiCarrierQuotesEnabled()`, which defaults to `import.meta.env`.

Values count as “on” after trimming whitespace and ignoring case: **`1`**, **`true`**, **`on`**, **`yes`**, and **`enabled`**. Missing values and other strings are off.
```

judge: 2  ·  human: ___

---

## web-003  (ref: web-003__graphify-lean__r3)

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
The affected UI is the **quote results on the Quote page**. `MoneyText` calls `formatMoney`, which calls `roundMoney`; QuotePage uses it for each carrier’s quote total, and `QuoteBreakdown` uses it for every line item and the breakdown total (`src/pages/QuotePage.tsx:43`, `src/components/QuoteBreakdown.tsx:21,30`; rounding path: `src/components/MoneyText.tsx:11`, `src/lib/money.ts:10`).

I found no UI calls to `sumMoney` or `parseMoneyInput`, the other helpers that call `roundMoney`. Shipment and booking screens don’t display values through this path.
```

judge: 2  ·  human: ___

---
