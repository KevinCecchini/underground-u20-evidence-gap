# UNDERGROUND U20 — The Evidence Gap

**Independent youth-football scouting research | Portugal · Italy · Denmark | Research release 1.0 (28 October 2026)**

> Finding an underexposed player is not the same as proving he is a good signing. We study the distance between evidence of development and market visibility, and explicitly preserve uncertainty.

## Executive finding
This release demonstrates a reproducible approach to recovering partial U19 playing-time evidence from dated **official match reports**. Across **five selected** Vejle U19 reports, Benjamin Nicolaisen is documented in **5 appearances (3 starts and 2 substitute entries), approximately 235 capped regulation minutes and 1 goal**. This is **not a season total**. The club confirmed a contract extension through 2028, which means he should **not** be marketed as an overlooked, cheap acquisition.

## What you get
- `docs/DECISION_BRIEF.md`: four-player triage, with action and rejection criteria.
- `docs/METHOD.md`: the original Evidence-to-Opportunity Gap decision framework and validation conditions.
- `docs/SOURCES.md`: first-party links and the historic Wyscout reference.
- `data/verified_match_ledger.csv`: five traceable official reports; **partial sample**.
- `data/candidate_decision_register.csv`: transparent investigative statuses.
- `src/reproduce_ledger.py` and `tests/`: executable integrity checks.
- `FINAL_EVIDENCE_REPORT.pdf`: designed narrative report.
- `publication/LINKEDIN_POST_IT.md`: ready-to-paste launch post with placeholders for your real GitHub URL.

## Run locally
```bash
python -m src.reproduce_ledger
python -m unittest discover -s tests -v
```
Only Python standard library is required. These checks validate the calculation consistency, **not talent potential**.

## Novel contribution / what is not claimed
The original element is the *documented evidence gap* and decision protocol, not the fact that these athletes are previously unknown. **No video scouting completed, no accurate full-season U19 datasets, no transfer market quotes, no model validation or predictive ML.** The output is an **investigative product**, ready to publish as research, **not a finished club-grade acquisition shortlist**.

## Research integrity
We do not redistribute copyrighted club photos, video, or bulk scraped match data. External sites retain their rights. The software is MIT; source material follows each publisher's terms. Wyscout 2017/18 is an independent historical methodology lab and is not used as proof about current academy players.

## Citation
Underground U20 Talent Radar (2026). *The Evidence Gap: audit-based youth winger investigation*. Research release 1.0. Source register in `docs/SOURCES.md`.
