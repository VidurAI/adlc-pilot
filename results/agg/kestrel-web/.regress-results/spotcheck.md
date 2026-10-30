# Spot-check sheet (arm hidden)

1 of 6 judged answers. Fill `human:` with 0/1/2.
`adlc scorecard --spotcheck results/spotcheck.md` computes agreement.

## web-003  (ref: web-003__graphify__r3)

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
dry-run answer
```

judge: 2  ·  human: ___

---
