# Spot-check sheet (arm hidden)

1 of 2 judged answers. Fill `human:` with 0/1/2.
`adlc scorecard --spotcheck results/spotcheck.md` computes agreement.

## nfy-001  (ref: nfy-001__graphify__r1)

**Question**

The notification queue retries a failed delivery a fixed number of times before dead-lettering.
How many times, and why that number? Point me at the rationale.

**Reference**

MAX_RETRIES = 3 in notify/queue.py (1 initial attempt + 3 retries, jittered exponential backoff,
base 0.5 s doubled per retry, jitter 0.5–1.5, capped at 30 s). The only rationale is a comment
"see OPS-61", and no OPS-61 document exists in the repo — the agent should say the rationale is
not recoverable from this repo and name the ticket id to look up elsewhere.

**Rubric**

2 = says 3 retries, names OPS-61, and states the rationale is not in the repo;
1 = says 3 retries but invents or omits the rationale question;
0 = wrong count.

**Answer**

```
It allows **3 retries after the initial delivery attempt**, so a persistently failing job gets up to **4 total attempts**. The limit is `MAX_RETRIES = 3` in [`notify/queue.py:11`](notify/queue.py#L11); the dead-letter check is at [line 83](notify/queue.py#L83), and [`tests/test_queue.py:59-60`](tests/test_queue.py#L59) confirms four attempts and three retry delays.

For the rationale, the code points to **OPS-61** in the constant’s comment. The checkout contains no explanation beyond that reference, and its Git remote isn’t a GitHub remote, so I can’t retrieve the issue details here.
```

judge: 2  ·  human: ___

---
