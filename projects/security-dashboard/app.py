#!/usr/bin/env python3
"""Small local defensive security dashboard using only Python's stdlib."""

from collections import Counter
from html import escape
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import re

SAMPLE_LOG = Path(__file__).with_name("sample_auth.log")
FAILED = re.compile(r"Failed password .* from (\d+\.\d+\.\d+\.\d+)")


def analyze(lines: list[str]) -> Counter:
    ips = Counter()
    for line in lines:
        match = FAILED.search(line)
        if match:
            ips[match.group(1)] += 1
    return ips


class Dashboard(BaseHTTPRequestHandler):
    def do_GET(self):
        lines = SAMPLE_LOG.read_text(encoding="utf-8").splitlines()
        ips = analyze(lines)
        rows = "".join(f"<tr><td>{escape(ip)}</td><td>{count}</td></tr>" for ip, count in ips.most_common())
        page = f"""<!doctype html><html><head><meta charset='utf-8'><title>Security Lab Dashboard</title></head>
<body><h1>🛡️ Security Lab Dashboard</h1><p>Local sample data only.</p>
<h2>Failed SSH Authentication</h2><table border='1' cellpadding='8'><tr><th>Source IP</th><th>Failures</th></tr>{rows}</table></body></html>"""
        data = page.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)


if __name__ == "__main__":
    print("Dashboard: http://127.0.0.1:8000")
    HTTPServer(("127.0.0.1", 8000), Dashboard).serve_forever()
