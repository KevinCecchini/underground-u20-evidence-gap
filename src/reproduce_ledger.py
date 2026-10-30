"""Recompute the documented Nicolaisen 2026/27 partial-sample ledger.
No scraping, no hidden data, no invented extrapolation.
"""
import csv, json
from pathlib import Path

def analyze(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows=list(csv.DictReader(f))
    assert len({(r["match_date"], r["opponent"]) for r in rows})==len(rows), "Duplicate fixtures"
    for r in rows:
        entry=int(r["entry_minute"]); exit_=int(r["exit_minute_regulation"])
        assert 0<=entry<=exit_<=90, "Invalid regulation-minute interval"
        assert exit_-entry==int(r["minutes_regulation_estimate"]), "Inconsistent minutes"
        assert r["official_match_report_url"].startswith("https://"), "Missing source URL"
    return {
        "matched_reports": len(rows),
        "documented_regulation_minutes_estimate":sum(int(r["minutes_regulation_estimate"]) for r in rows),
        "starts":sum(r["starter"].lower()=="true" for r in rows),
        "bench_entries":sum(r["starter"].lower()=="false" for r in rows),
        "season_complete":False,
        "video_observations_completed":0,
    }

if __name__=="__main__":
    here=Path(__file__).resolve().parents[1]
    print(json.dumps(analyze(here/"data"/"verified_match_ledger.csv"),indent=2))
