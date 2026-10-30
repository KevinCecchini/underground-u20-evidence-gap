# Data dictionary & provenance

## verified_match_ledger.csv
One row per **selected and documented** Vejle U19 match. `entry_minute` and `exit_minute_regulation` define an **approximate, 90-minute capped interval**; `minutes_regulation_estimate` is the difference. No stoppage time or unobserved matches. `official_match_report_url` points to the first-party source. Five selected reports only; **NOT a complete season**.

## candidate_decision_register.csv
Investigative status of a small selection. `evidence` and `critical_gap` are qualitative summaries, not independent scout video analysis. Club/role/contract should be rechecked on the date of use.

## candidate_registry_audited.csv
Historical exploratory research from earlier project stages. **Not a vetted 2026/27 comprehensive candidate census**. Not used to generate market rankings or numerical claims in the final report.

## Licensing
The MIT license applies to original code only, not third-party sports data or publisher images. First-party source URLs are credited. Wyscout 2017/18 source dataset is CC BY 4.0, but raw Wyscout files are deliberately NOT redistributed in this repository. No match footage or copyrighted photography is redistributed.
