import tempfile
import unittest
from pathlib import Path

from projects.password_strength_checker.checker import assess


class SecurityToolsTests(unittest.TestCase):
    def test_common_password_is_weak(self):
        result, _ = assess("password")
        self.assertEqual(result, "Very weak")

    def test_stronger_password_scores_better(self):
        result, _ = assess("Example!Strong2026")
        self.assertEqual(result, "Strong")


if __name__ == "__main__":
    unittest.main()
