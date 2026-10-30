# Spot-check sheet (arm hidden)

2 of 12 judged answers. Fill `human:` with 0/1/2.
`adlc scorecard --spotcheck results/spotcheck.md` computes agreement.

## svc-002  (ref: svc-002__baseline__r3)

**Question**

In the booking service, where does an incoming create or reserve request actually get
rate limited per carrier, and where does a rejection turn into the HTTP 429 response?

**Reference**

Enforcement is in the service layer, not a filter or controller:
booking/src/main/java/com/kestrel/booking/service/BookingService.java calls
rateLimiter.acquire(carrier.getCode()) in both create() and reserve(). CarrierRateLimiter.acquire
(ratelimit/CarrierRateLimiter.java) draws a token from that carrier's own TokenBucket
(ratelimit/TokenBucket.java) and throws CarrierCapacityExhaustedException when empty.
ApiExceptionHandler.capacityExhausted (web/ApiExceptionHandler.java) maps it to 429 with a
Retry-After header and the "carrier capacity exhausted" error string.

**Rubric**

2 = BookingService create/reserve call sites + CarrierRateLimiter/TokenBucket + the
    ApiExceptionHandler 429 mapping;
1 = finds CarrierRateLimiter but not the call sites or not the exception-to-429 mapping;
0 = points at the controller, a filter, or the wrong class.

**Answer**

```
Both paths call `CarrierRateLimiter.acquire(carrier.getCode())` in `BookingService`: `create()` after carrier lookup and validation, and `reserve()` after loading the shipment’s carrier and checking it is active.

The per-carrier token buckets are implemented in `ratelimit/CarrierRateLimiter.java`; they’re keyed by normalized carrier code and configured through `kestrel.booking.ratelimit.*` in `BookingProperties.java`. When a bucket is empty, `acquire()` throws `CarrierCapacityExhaustedException`. `web/ApiExceptionHandler.java` maps that exception to HTTP 429.
```

judge: 2  ·  human: ___

---

## svc-002  (ref: svc-002__serena__r3)

**Question**

In the booking service, where does an incoming create or reserve request actually get
rate limited per carrier, and where does a rejection turn into the HTTP 429 response?

**Reference**

Enforcement is in the service layer, not a filter or controller:
booking/src/main/java/com/kestrel/booking/service/BookingService.java calls
rateLimiter.acquire(carrier.getCode()) in both create() and reserve(). CarrierRateLimiter.acquire
(ratelimit/CarrierRateLimiter.java) draws a token from that carrier's own TokenBucket
(ratelimit/TokenBucket.java) and throws CarrierCapacityExhaustedException when empty.
ApiExceptionHandler.capacityExhausted (web/ApiExceptionHandler.java) maps it to 429 with a
Retry-After header and the "carrier capacity exhausted" error string.

**Rubric**

2 = BookingService create/reserve call sites + CarrierRateLimiter/TokenBucket + the
    ApiExceptionHandler 429 mapping;
1 = finds CarrierRateLimiter but not the call sites or not the exception-to-429 mapping;
0 = points at the controller, a filter, or the wrong class.

**Answer**

```
The rate limit is enforced in `BookingService`, not in the controller:

- `POST /v2/shipments` delegates to `BookingService.create`; after idempotency, carrier lookup, and validation, it calls `rateLimiter.acquire(carrier.getCode())` at `src/main/java/com/kestrel/booking/service/BookingService.java:59`.
- `POST /v2/shipments/{id}/reserve` delegates to `BookingService.reserve`; after checking shipment status and carrier availability, it calls the same method at `BookingService.java:94`.

`CarrierRateLimiter.acquire` (`src/main/java/com/kestrel/booking/ratelimit/CarrierRateLimiter.java:39`) uses a separate in-memory token bucket per normalized carrier code. When the bucket is empty, it throws `CarrierCapacityExhaustedException`.

The HTTP 429 mapping is in `src/main/java/com/kestrel/booking/web/ApiExceptionHandler.java` in the `capacityExhausted` handler: it builds a `TOO_MANY_REQUESTS` problem response and sets the `Retry-After` header. The rate settings are under `kestrel.booking.ratelimit.*` in `BookingProperties` (default 20 requests/second per carrier, with a 2-second burst capacity).
```

judge: 2  ·  human: ___

---
