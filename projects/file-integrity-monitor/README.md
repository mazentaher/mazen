# File Integrity Monitor 🔐

A defensive Python tool that calculates SHA-256 hashes for files and compares them with a saved baseline.

## Features

- Create a baseline of authorized files.
- Detect modified, added, or removed files.
- Uses SHA-256 for integrity verification.
- Designed for local defensive monitoring.

## Usage

```bash
python3 monitor.py create ./sample-data baseline.json
python3 monitor.py check ./sample-data baseline.json
```

Use only on files and directories you are authorized to monitor.
