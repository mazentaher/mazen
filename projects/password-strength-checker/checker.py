#!/usr/bin/env python3
"""Educational password-strength checker. Passwords are never stored."""

import getpass
import re

COMMON = {"password", "123456", "qwerty", "admin", "letmein"}


def assess(password: str) -> tuple[str, list[str]]:
    score = 0
    tips = []
    if len(password) >= 12: score += 2
    elif len(password) >= 8: score += 1
    else: tips.append("Use at least 8 characters; longer is better.")
    if re.search(r"[a-z]", password): score += 1
    else: tips.append("Add lowercase letters.")
    if re.search(r"[A-Z]", password): score += 1
    else: tips.append("Add uppercase letters.")
    if re.search(r"\d", password): score += 1
    else: tips.append("Add numbers.")
    if re.search(r"[^A-Za-z0-9]", password): score += 1
    else: tips.append("Consider adding symbols.")
    if password.lower() in COMMON:
        return "Very weak", ["Avoid common passwords."]
    return ("Strong" if score >= 5 else "Moderate" if score >= 3 else "Weak"), tips


if __name__ == "__main__":
    result, tips = assess(getpass.getpass("Password: "))
    print(f"Assessment: {result}")
    for tip in tips:
        print(f"- {tip}")
