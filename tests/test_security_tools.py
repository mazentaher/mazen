import importlib.util
import unittest
from pathlib import Path


CHECKER = Path(__file__).parents[1] / "projects" / "password-strength-checker" / "checker.py"
spec = importlib.util.spec_from_file_location("password_checker", CHECKER)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
assess = module.assess


class SecurityToolsTests(unittest.TestCase):
    def test_common_password_is_weak(self):
        result, _ = assess("password")
        self.assertEqual(result, "Very weak")

    def test_stronger_password_scores_better(self):
        result, _ = assess("Example!Strong2026")
        self.assertEqual(result, "Strong")


if __name__ == "__main__":
    unittest.main()
