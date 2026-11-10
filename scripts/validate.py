#!/usr/bin/env python3
from __future__ import annotations
import argparse, sys
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser(); ap.add_argument("--root", default=".")
    root = Path(ap.parse_args().root)
    files = sorted(
        f for base in ("schemas", "migrations", "queries", "tests")
        for f in (root / base).rglob("*.sql")
    )
    if not files:
        print("no sql files", file=sys.stderr); return 1
    for p in files:
        text = p.read_text(encoding="utf-8")
        if "DROP DATABASE" in text.upper():
            print(f"{p}: DROP DATABASE is forbidden", file=sys.stderr); return 1
        if ";" not in text:
            print(f"{p}: no statement terminator", file=sys.stderr); return 1
    print(f"sql validation ok ({len(files)} files)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
