#!/usr/bin/env python3
"""Defensive SSH authentication log analyzer."""

import argparse
import re
from collections import Counter
from pathlib import Path

FAILED_LOGIN = re.compile(r"Failed password .* from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})")


def analyze_log(path: Path, threshold: int) -> Counter:
    failures = Counter()
    with path.open("r", encoding="utf-8", errors="replace") as log_file:
        for line in log_file:
            match = FAILED_LOGIN.search(line)
            if match:
                failures[match.group("ip")] += 1
    return failures


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze failed SSH authentication attempts.")
    parser.add_argument("logfile", type=Path, help="Path to an authorized SSH authentication log")
    parser.add_argument("--threshold", type=int, default=5, help="Failure count that triggers an alert")
    args = parser.parse_args()

    if args.threshold < 1:
        parser.error("--threshold must be at least 1")

    if not args.logfile.is_file():
        parser.error(f"log file not found: {args.logfile}")

    failures = analyze_log(args.logfile, args.threshold)

    print("SSH Authentication Summary")
    print("--------------------------")
    if not failures:
        print("No failed SSH authentication attempts found.")
        return

    for ip, count in failures.most_common():
        status = " [ALERT]" if count >= args.threshold else ""
        print(f"{ip} -> {count} failed attempts{status}")


if __name__ == "__main__":
    main()
