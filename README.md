# Play Store review research

Collects recent reviews from the Indian Google Play Store for bill-splitting
apps (Splitwise, Tricount, Settle Up, Splid) to research demand and gaps for
an India-first expense-splitting app.

- **Run it:** Actions tab → "Fetch Play Store reviews" → Run workflow.
- **Schedule:** runs automatically on the 1st of every month.
- **Output:** a dated CSV in `data/`.
- **Add an app:** edit `APPS` in `fetch_reviews.py`.

For personal research only; the raw review data is not for republication.
