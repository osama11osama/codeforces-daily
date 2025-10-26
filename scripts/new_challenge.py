#!/usr/bin/env python3
import argparse
import datetime
import shutil
from pathlib import Path


def slugify(s: str) -> str:
    return "".join(c if c.isalnum() or c in ("-", "_") else "_" for c in s).strip("_")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--id", required=True, help="Codeforces ID (e.g., 4A)")
    p.add_argument("--title", required=True, help="Problem title (e.g., Watermelon)")
    args = p.parse_args()

    today = datetime.date.today()
    month_dir = Path(f"{today:%Y}/{today:%m-%d}")
    prob_dir = month_dir / f"{args.id}_{slugify(args.title)}"
    prob_dir.mkdir(parents=True, exist_ok=True)

    root = Path(__file__).resolve().parents[1]
    tmpl = root / "templates"

    shutil.copy(tmpl / "main.py", prob_dir / "main.py")
    shutil.copy(tmpl / "template_test_samples.py", prob_dir / f"test_{args.id}.py")

    samples = prob_dir / "samples"
    samples.mkdir(exist_ok=True)
    (samples / "1.in").write_text("", encoding="utf-8")
    (samples / "1.out").write_text("", encoding="utf-8")

    print(f"✅ Created {prob_dir}")
    print("   Add sample I/O in samples/ and run: pytest")


if __name__ == "__main__":
    main()
