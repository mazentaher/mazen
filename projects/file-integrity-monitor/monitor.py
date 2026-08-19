#!/usr/bin/env python3
"""Defensive file integrity monitor using SHA-256."""

import argparse
import hashlib
import json
from pathlib import Path


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def snapshot(root: Path) -> dict[str, str]:
    return {
        str(p.relative_to(root)): digest(p)
        for p in sorted(root.rglob("*"))
        if p.is_file() and p.name != "baseline.json"
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Monitor file integrity with SHA-256.")
    sub = parser.add_subparsers(dest="command", required=True)
    create = sub.add_parser("create")
    create.add_argument("directory", type=Path)
    create.add_argument("baseline", type=Path)
    check = sub.add_parser("check")
    check.add_argument("directory", type=Path)
    check.add_argument("baseline", type=Path)
    args = parser.parse_args()

    if not args.directory.is_dir():
        parser.error(f"directory not found: {args.directory}")

    current = snapshot(args.directory)
    if args.command == "create":
        args.baseline.write_text(json.dumps(current, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"Baseline created: {args.baseline}")
        return

    baseline = json.loads(args.baseline.read_text(encoding="utf-8"))
    added = sorted(set(current) - set(baseline))
    removed = sorted(set(baseline) - set(current))
    modified = sorted(k for k in set(current) & set(baseline) if current[k] != baseline[k])

    for label, items in (("ADDED", added), ("REMOVED", removed), ("MODIFIED", modified)):
        for item in items:
            print(f"{label}: {item}")

    if not (added or removed or modified):
        print("OK: no integrity changes detected.")


if __name__ == "__main__":
    main()
