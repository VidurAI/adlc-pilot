# Spot-check sheet (arm hidden)

1 of 3 judged answers. Fill `human:` with 0/1/2.
`adlc scorecard --spotcheck results/spotcheck.md` computes agreement.

## svc-002  (ref: svc-002__serena__r2)

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
The rate limit is enforced in **`BookingService`**, not in the controller:

- `create()` calls `rateLimiter.acquire(carrier.getCode())` after checking for an idempotent replay and validating the carrier/request, but before saving the shipment.
- `reserve()` calls it after loading and locking the shipment, checking its status and carrier availability, but before changing the status. Both operations therefore consume a token from the carrier’s bucket; an idempotent create replay does not.

**`CarrierRateLimiter.acquire()`** in `ratelimit/CarrierRateLimiter.java` normalizes the carrier code and uses a separate token bucket per carrier. Rates come from `kestrel.booking.ratelimit.per-carrier-rps` with optional carrier overrides; a non-positive rate disables limiting.

If the bucket is empty, the limiter throws `CarrierCapacityExhaustedException`. **`ApiExceptionHandler.capacityExhausted()`** in `web/ApiExceptionHandler.java` catches it and returns HTTP 429 with a `Retry-After` header and problem details. The controller simply delegates to the service.
```

judge: 2  ·  human: ___

---
