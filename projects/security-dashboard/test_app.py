import unittest
from app import analyze


class DashboardTests(unittest.TestCase):
    def test_failed_authentication_counts(self):
        data = [
            "Failed password for invalid user demo from 192.0.2.10 port 22 ssh2",
            "Failed password for invalid user demo from 192.0.2.10 port 23 ssh2",
            "Accepted password for demo from 192.0.2.20 port 24 ssh2",
        ]
        counts = analyze(data)
        self.assertEqual(counts["192.0.2.10"], 2)
        self.assertNotIn("192.0.2.20", counts)


if __name__ == "__main__":
    unittest.main()
