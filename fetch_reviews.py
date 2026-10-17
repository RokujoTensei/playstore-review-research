"""Fetch Indian Play Store reviews for bill-splitting apps and save a dated CSV.

Apps listed by name only are looked up with a Play Store search, and the
package ID that was picked is printed in the run log and saved in the CSV.
"""
import csv
import datetime
import os
import sys
import time

from google_play_scraper import Sort, reviews, search

COUNTRY = "in"
LANG = "en"
REVIEWS_PER_APP = int(os.environ.get("REVIEWS_PER_APP", "1000"))

# name -> package id (None = look it up by searching the name)
APPS = {
    "Splitwise": "com.Splitwise.SplitwiseMobile",
    "Tricount": "com.tribab.tricount.android",
    "Settle Up": "cz.destil.settleup",
    "Splid": "splid.teamturtle.com.splid",
}


def resolve(name):
    results = search(name, lang=LANG, country=COUNTRY, n_hits=5)
    for r in results:
        if name.lower().split()[0] in (r.get("title") or "").lower():
            return r["appId"], r["title"]
    if results:
        return results[0]["appId"], results[0]["title"]
    return None, None


def fetch(app_id):
    out, token = [], None
    while len(out) < REVIEWS_PER_APP:
        for attempt in range(3):
            try:
                batch, token = reviews(
                    app_id, lang=LANG, country=COUNTRY, sort=Sort.NEWEST,
                    count=min(200, REVIEWS_PER_APP - len(out)),
                    continuation_token=token,
                )
                break
            except Exception as e:  # rate limits or transient errors
                print(f"  retry {attempt + 1} for {app_id}: {e}")
                time.sleep(10 * (attempt + 1))
        else:
            return out
        if not batch:
            break
        out.extend(batch)
        if token is None:
            break
        time.sleep(2)
    return out


LOG = []


def log(msg):
    print(msg)
    LOG.append(msg)


def main():
    rows = []
    for name, app_id in APPS.items():
        title = name
        if app_id is None:
            app_id, title = resolve(name)
            if app_id is None:
                log(f"{name}: not found, skipped")
                continue
        got = fetch(app_id)
        log(f"{name} -> {app_id}: {len(got)} reviews")
        for r in got:
            rows.append({
                "app": name,
                "package_id": app_id,
                "stars": r["score"],
                "date": r["at"].strftime("%Y-%m-%d") if r.get("at") else "",
                "app_version": r.get("reviewCreatedVersion") or "",
                "thumbs_up": r.get("thumbsUpCount", 0),
                "review": (r.get("content") or "").replace("\n", " "),
            })
    if not rows:
        print("No reviews fetched.")
        sys.exit(1)
    path = f"data/reviews_in_{datetime.date.today():%Y-%m-%d}.csv"
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    log(f"Saved {len(rows)} reviews to {path}")
    with open("data/run_log.txt", "a", encoding="utf-8") as f:
        f.write(f"--- {datetime.datetime.utcnow():%Y-%m-%d %H:%M} UTC ---\n")
        f.write("\n".join(LOG) + "\n")


if __name__ == "__main__":
    main()
