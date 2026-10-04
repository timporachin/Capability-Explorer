"""Behavioral tests for bounded catalog retrieval and non-destructive upserts."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("catalog", ROOT / "skills/capability-explorer/scripts/catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)

class CatalogTests(unittest.TestCase):
    def fixture(self, count=120):
        return {"schema_version": 1, "settings": {"auto_save_explorations": True},
                "entries": [{"url": f"https://github.com/demo/tool-{i}",
                             "name": f"tool-{i}", "tags": ["video"],
                             "inferred_ideas": ["Keep this proposal"]} for i in range(count)]}

    def test_large_catalog_returns_five_and_offers_expansion(self):
        result = catalog.query(self.fixture(), "video")
        self.assertEqual(result["returned_entries"], 5)
        self.assertEqual(result["matching_entries"], 120)
        self.assertTrue(result["more_available"])
        self.assertTrue(result["offer_broader_pass"])

    def test_expansion_is_bounded_and_explicit(self):
        with self.assertRaises(ValueError):
            catalog.query(self.fixture(), "video", limit=15)
        result = catalog.query(self.fixture(), "video", limit=15, expanded=True)
        self.assertEqual(result["returned_entries"], 15)
        with self.assertRaises(ValueError):
            catalog.query(self.fixture(), "video", limit=16, expanded=True)

    def test_oversized_record_does_not_overflow_context(self):
        data = self.fixture(1)
        data["entries"][0]["inferred_ideas"] = ["video " * 5000]
        result = catalog.query(data, "video")
        self.assertLessEqual(result["record_characters"], 12000)
        self.assertEqual(result["returned_entries"], 0)
        self.assertTrue(result["more_available"])

    def test_upsert_deduplicates_and_preserves_unrelated_data(self):
        data = self.fixture(2)
        catalog.upsert(data, {"url": "https://github.com/DEMO/TOOL-0.git",
                             "name": "New name", "evidence_status": "documentation_inspected"})
        self.assertEqual(len(data["entries"]), 2)
        self.assertEqual(data["entries"][0]["inferred_ideas"], ["Keep this proposal"])
        self.assertEqual(data["entries"][1]["name"], "tool-1")
        self.assertTrue(data["settings"]["auto_save_explorations"])

    def test_roundtrip_and_duplicate_detection(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "catalog.json"
            data = self.fixture(2)
            catalog.save(path, data)
            self.assertEqual(catalog.load(path), data)
            data["entries"].append(dict(data["entries"][0]))
            catalog.save(path, data)
            with self.assertRaises(ValueError):
                catalog.load(path)

    def test_no_match_does_not_invent_history(self):
        result = catalog.query(self.fixture(4), "unrelated")
        self.assertEqual(result["records"], [])
        self.assertEqual(result["matching_entries"], 0)

if __name__ == "__main__":
    unittest.main()
