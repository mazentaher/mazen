#!/usr/bin/env python3
"""Educational permission checker for files explicitly supplied by the user."""

import argparse
from pathlib import Path
import stat


def describe(path: Path) -> str:
    mode = path.stat().st_mode
    return stat.filemode(mode)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Show permissions for authorized local files.")
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args()
    for path in args.paths:
        if path.exists():
            print(f"{path}: {describe(path)}")
        else:
            print(f"{path}: not found")
