import unittest
from csv_diff import csv_diff


class TestCSVDiff(unittest.TestCase):
    """tests various cases for the csv differ"""

    def failure(self, info, expected_added=0, expected_removed=0):
        """checks that the info dict has a failure"""
        self.assertIsInstance(info, dict)
        self.assertTrue(info["error"])
        self.assertEqual(len(info["added"]), expected_added)
        self.assertEqual(len(info["removed"]), expected_removed)
        return True

    def success(self, info):
        """checks that the info dict is a complete success"""
        self.assertIsInstance(info, dict)
        self.assertFalse(info["error"])
        self.assertEqual(len(info["added"]), 0)
        self.assertEqual(len(info["removed"]), 0)
        return True

    def test_small_same(self):
        """tests that diffing against the same file doesn't fail"""
        info = csv_diff("./data/small.csv", "./data/small.csv")
        assert self.success(info)

    def test_small_row_insensitive(self):
        """tests the small csvs with row order insensitive"""
        info = csv_diff("./data/small.csv", "./data/small_row_unordered.csv")
        assert self.success(info)

    def test_small_dupe(self):
        """tests the small csvs, with some duplicated rows"""
        info = csv_diff("./data/small.csv", "./data/small_dupe.csv")
        assert self.failure(info, expected_added=5)

    def test_small_incorrect(self):
        """tests the small csvs, with some issues"""
        info = csv_diff("./data/small.csv", "./data/small_incorrect.csv")
        assert self.failure(info, expected_added=3, expected_removed=3)

    def test_small_col_insensitive(self):
        """tests the small csvs, requiring column insensitive"""
        info = csv_diff("./data/small.csv", "./data/small_col_unordered.csv")
        assert self.success(info)

    def test_large_col_insensitive(self):
        """tests the large csvs, requiring column insensitive"""
        info = csv_diff("./data/large.csv", "./data/large_col_ordered.csv")
        assert self.success(info)

    def test_large_incorrect(self):
        """tests the large csvs, with some missing and added rows"""
        info = csv_diff("./data/large.csv", "./data/large_incorrect.csv")
        assert self.failure(info, expected_added=31, expected_removed=15)

    def test_large_added(self):
        """tests the large csvs, with some added rows"""
        info = csv_diff("./data/large.csv", "./data/large_added.csv")
        assert self.failure(info, expected_added=31, expected_removed=0)

    def test_large_added_dupe(self):
        """tests the large csvs, with some added rows and duplicates"""
        info = csv_diff("./data/large.csv", "./data/large_added_dupe.csv")
        assert self.failure(info, expected_added=33, expected_removed=0)

    def test_large_modified(self):
        """tests the large csvs, with some modified rows"""
        info = csv_diff("./data/large.csv", "./data/large_modified.csv")
        assert self.failure(info, expected_added=3, expected_removed=3)

    def test_incompatible_csv(self):
        """tests checking incompatible csvs against each other"""
        info = csv_diff("./data/small.csv", "./data/large.csv")
        self.assertTrue(info["error"])

    def test_small_tsv_row_insensitive(self):
        """tests the small tsvs with row order insensitive"""
        info = csv_diff("./data/small.tsv", "./data/small_row_unordered.tsv", sep="\t")
        assert self.success(info)


if __name__ == "__main__":
    unittest.main()
