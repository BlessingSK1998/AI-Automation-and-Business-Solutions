import importlib.util
import pathlib
import unittest

MODULE_PATH = pathlib.Path(__file__).with_name("score_jobs.py")
spec = importlib.util.spec_from_file_location("score_jobs", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class TestJobScoring(unittest.TestCase):
    def test_simple_overlap(self):
        result = module.assess({"title": "Data analyst", "description": "Python and SQL"},
                               {"skills": ["Python", "SQL", "project coordination"]})
        self.assertEqual(result["overlap_percent"], 66.7)
        self.assertIn("Python", result["matched_skills"])

    def test_no_skills(self):
        self.assertEqual(module.assess({"title": "Analyst"}, {"skills": []})["overlap_percent"], 0)

    def test_missing_fields(self):
        self.assertEqual(module.assess({}, {"skills": ["Python"]})["overlap_percent"], 0)


if __name__ == "__main__":
    unittest.main()
