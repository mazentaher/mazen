# SSH Log Analyzer 🔎

A small defensive cybersecurity project that analyzes Linux SSH authentication logs and highlights repeated failed login attempts.

## What it does

- Reads a local SSH authentication log file.
- Extracts failed login attempts.
- Counts failures by source IP address.
- Reports IPs that exceed a configurable threshold.

## Why it matters

Repeated authentication failures can be an indicator of password guessing or other suspicious activity. This project is intentionally designed for **defensive log analysis** using logs you are authorized to inspect.

## Run

```bash
python3 analyzer.py sample_auth.log --threshold 3
```

## Example output

```text
SSH Authentication Summary
--------------------------
203.0.113.10 -> 4 failed attempts [ALERT]
198.51.100.7 -> 1 failed attempts
```

> The IP addresses in the sample log use documentation-only ranges and are not real targets.
