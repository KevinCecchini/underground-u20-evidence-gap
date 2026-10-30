import unittest, tempfile, csv
from pathlib import Path
from src.reproduce_ledger import analyze
class LedgerTests(unittest.TestCase):
    def test_real_sample(self):
        result=analyze(Path(__file__).resolve().parents[1]/"data"/"verified_match_ledger.csv")
        self.assertEqual(result["documented_regulation_minutes_estimate"],235)
        self.assertEqual(result["matched_reports"],5)
        self.assertFalse(result["season_complete"])
    def test_reject_bad_minutes(self):
        with tempfile.TemporaryDirectory() as tmp:
            f=Path(tmp)/"bad.csv"
            f.write_text("match_date,opponent,entry_minute,exit_minute_regulation,minutes_regulation_estimate,starter,official_match_report_url\n2026-01-01,X,60,90,50,False,https://example.org\n",encoding="utf-8")
            with self.assertRaises(AssertionError):analyze(f)
if __name__=='__main__': unittest.main()
