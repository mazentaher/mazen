import importlib.util
import tempfile
import unittest
from pathlib import Path

MONITOR = Path(__file__).parents[1] / "projects" / "file-integrity-monitor" / "monitor.py"
spec = importlib.util.spec_from_file_location("file_integrity_monitor", MONITOR)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class FileIntegrityMonitorTests(unittest.TestCase):
    def test_digest_changes_when_file_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sample.txt"
            path.write_text("before", encoding="utf-8")
            first = module.digest(path)
            path.write_text("after", encoding="utf-8")
            second = module.digest(path)
            self.assertNotEqual(first, second)

    def test_snapshot_contains_relative_file(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "sample.txt").write_text("hello", encoding="utf-8")
            self.assertIn("sample.txt", module.snapshot(root))


if __name__ == "__main__":
    unittest.main()
