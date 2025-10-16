#!/usr/bin/env python3
"""
Scan the repo for monthly attendance files and generate months.json manifest.
- Supports .txt (tab-separated) and .csv (comma-separated)
- Tries to parse meta from header lines; falls back to filename-based name
Usage:
  python3 scripts/generate_manifest.py
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def infer_meta_from_txt(path: Path):
    period = None
    created = None
    try:
        with path.open('r', encoding='utf-8', errors='ignore') as f:
            lines = [next(f) for _ in range(5)]
        # Try to read lines like:
        # Create Time:2025/10/01 17:29:58
        # Made Date:2025/09/01-2025/09/30
        for line in lines:
            if 'Made Date' in line:
                m = re.search(r'(\d{4}/\d{2}/\d{2})-(\d{4}/\d{2}/\d{2})', line)
                if m:
                    start, end = m.groups()
                    # Format to friendly period
                    try:
                        y1, m1, d1 = start.split('/')
                        y2, m2, d2 = end.split('/')
                        period = f"{int(m1):02}/{int(d1)} - {int(m2):02}/{int(d2)}, {y2}"
                    except Exception:
                        period = f"{start} - {end}"
            if 'Create Time' in line:
                m = re.search(r'(\d{4}/\d{2}/\d{2})', line)
                if m:
                    created = m.group(1)
    except Exception:
        pass
    return period, created


def pretty_name_from_filename(path: Path):
    # Example: att-sum-oct-2025.csv -> October 2025
    name = path.stem.replace('att-sum-', '').replace('att-sum', '').replace('-', ' ').strip()
    # Basic map for months
    months = {
        'jan': 'January', 'feb': 'February', 'mar': 'March', 'apr': 'April',
        'may': 'May', 'jun': 'June', 'jul': 'July', 'aug': 'August',
        'sep': 'September', 'sept': 'September', 'oct': 'October', 'nov': 'November', 'dec': 'December'
    }
    parts = name.split()
    friendly = None
    for p in parts:
        key = p[:3].lower()
        if key in months:
            # Try to find year next to it
            year = next((q for q in parts if q.isdigit() and len(q) == 4), '')
            friendly = f"{months[key]} {year}".strip()
            break
    return friendly or path.name


def main():
    files = []
    for ext in ('*.txt', '*.csv'):
        files.extend(ROOT.glob(ext))
    # Prefer files sorted by modified time descending
    files = sorted(files, key=lambda p: p.stat().st_mtime, reverse=True)

    items = []
    for p in files:
        if p.name.lower() == 'months.json':
            continue
        period, created = (None, None)
        if p.suffix.lower() == '.txt':
            period, created = infer_meta_from_txt(p)
        name = pretty_name_from_filename(p)
        # Fallbacks
        period = period or 'Period not specified'
        created = created or 'Date not specified'
        items.append({
            'file': p.name,
            'name': name,
            'period': period,
            'created': created
        })

    manifest = items or [{
        'file': 'att-sum.txt',
        'name': 'September 2025',
        'period': 'September 1-30, 2025',
        'created': 'October 1, 2025'
    }]

    (ROOT / 'months.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f"Wrote months.json with {len(manifest)} items")


if __name__ == '__main__':
    main()
