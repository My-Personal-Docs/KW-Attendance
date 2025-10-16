#!/usr/bin/env python3
"""
Convert a specific sheet from an Excel file into CSV (UTF-8)
Usage:
  python3 scripts/convert_excel_to_csv.py --input "COD Filter Plant.xls" --sheet "Sheet1" --output "att-sum-oct-2025.csv"
Notes:
- Requires pandas and a compatible Excel engine (xlrd for .xls, openpyxl for .xlsx)
- Install: pip install pandas xlrd openpyxl
"""
import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Path to Excel file (.xls or .xlsx)')
    parser.add_argument('--sheet', required=True, help='Sheet name or index (0-based)')
    parser.add_argument('--output', required=True, help='Output CSV path')
    args = parser.parse_args()

    # Auto engine selection
    excel_path = args.input
    if excel_path.lower().endswith('.xls'):
        engine = 'xlrd'
    else:
        engine = 'openpyxl'

    # Read sheet
    sheet_arg = args.sheet
    if sheet_arg.isdigit():
        sheet_arg = int(sheet_arg)

    df = pd.read_excel(excel_path, sheet_name=sheet_arg, engine=engine)
    # Write CSV without index, keep all columns
    df.to_csv(args.output, index=False)
    print(f"Wrote CSV: {args.output} (rows={len(df)})")


if __name__ == '__main__':
    main()
