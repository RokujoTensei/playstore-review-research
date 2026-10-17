# Findings: Play Store reviews, bill-splitting apps (run of 2026-10-17)

**Dataset:** newest 1,000 reviews each for Splitwise, Tricount, Settle Up and Splid,
fetched from the Indian Play Store listing (`data/reviews_in_2026-10-17.csv`).

**Important caveat:** the Indian-store filter does not restrict reviews to Indian users.
Only a handful of reviews show Indian signals (₹, UPI, GPay, Hindi words), and several
mention pounds or international trips. Treat this as a **global** picture of the category.

## Ratings in this sample

| App | Review window | Avg ★ | 1–3★ reviews |
|---|---|---|---|
| Splitwise | Jan–Oct 2026 | 2.90 | 554 |
| Tricount | Sep 2024–Oct 2026 | 3.22 | 491 |
| Settle Up | Apr 2019–Oct 2026 | 4.03 | 263 |
| Splid | Dec 2025–Oct 2026 | 4.84 | 23 |

## Themes in 1–3★ reviews (keyword tagging; one review can hit several themes)

| Theme | Splitwise | Tricount | Settle Up | Splid |
|---|---|---|---|---|
| Daily cap / limits | 136 | 5 | 3 | 0 |
| Paywall / Pro / price | 219 | 28 | 26 | 1 |
| Ads | 49 | 15 | 29 | 0 |
| Sync / bugs / crashes | 19 | 157 | 40 | 0 |
| Recurring / rent / flatmates | 20 | 38 | 14 | 2 |
| UI / complicated | 30 | 34 | 16 | 1 |
| Export / data loss | 8 | 41 | 7 | 2 |
| UPI / payment apps / settling | 16 | 9 | 16 | 1 |
| Regional language | 1 | 1 | 3 | 0 |

## What it says

1. **Splitwise's free-tier cap is driving users away.** Most of its 2026 negative reviews
   are about the cap (reported as roughly 3–5 expenses a day plus wait screens) and the
   paywall. Several reviewers say they switched to Splid, a notes app or GPay's split feature.
2. **Tricount's problem is reliability, not pricing.** Sync failures, crashes and lost
   data dominate after a major update and a business-model change.
3. **"Simple, free, no ads" is already served by Splid** (4.84★), so it isn't a
   differentiator on its own.
4. **Recurring bills appear as an unmet request** across apps (e.g. "no recurring bills"
   on Splid; "predicted monthly" spend on Splitwise).
5. **UPI integration is requested, but rarely in this global sample** (e.g. "It would have
   been easier if the UPI apps were redirected directly through this app"). This data
   neither proves nor rules out Indian demand for it.

## Next steps

- Indian-specific evidence: Reddit/Quora search, then 10–15 interviews with flatmates and
  trip groups in India.
- Optionally fetch Hindi-language reviews (`lang="hi"`) as a closer proxy for Indian users.
