"""Educational job research prototype. No network access or application submission."""
import argparse
import csv
import json
import re
from pathlib import Path


def tokens(text):
    return set(re.findall(r"[a-z0-9+#]+", str(text).lower()))


def assess(job, profile):
    """Simple transparent overlap; NOT a validated hiring suitability score."""
    skills = [str(s).strip() for s in profile.get("skills", []) if str(s).strip()]
    haystack = tokens(job.get("title", "") + " " + job.get("description", ""))
    matched = [s for s in skills if tokens(s) and tokens(s).issubset(haystack)]
    score = round(100 * len(matched) / len(skills), 1) if skills else 0.0
    return {**job, "overlap_percent": score, "matched_skills": "; ".join(matched),
            "note": "Keyword overlap only; verify eligibility and requirements manually"}


def main():
    p = argparse.ArgumentParser(description="Transparent local job research prototype")
    p.add_argument("--jobs", type=Path, required=True)
    p.add_argument("--profile", type=Path, required=True)
    p.add_argument("--output", type=Path, default=Path("results.csv"))
    args = p.parse_args()
    profile = json.loads(args.profile.read_text(encoding="utf-8"))
    with args.jobs.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        jobs = list(reader)
    if not jobs:
        raise SystemExit("Input jobs CSV contains no rows")
    ranked = sorted((assess(j, profile) for j in jobs), key=lambda j: j["overlap_percent"], reverse=True)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=ranked[0].keys())
        writer.writeheader()
        writer.writerows(ranked)
    print(f"Wrote {len(ranked)} example results to {args.output}")


if __name__ == "__main__":
    main()
