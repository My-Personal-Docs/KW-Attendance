# KW-Attendance

Employee Attendance Search System for COD Filter Plant

## 🌐 Live URL
**https://my-personal-docs.github.io/KW-Attendance/login.html**

## 🔐 Login Credentials
- **Username:** admin
- **Password:** admin

## Features
- 🔍 Live search by Employee ID or Name
- 📊 Monthly attendance tracking
- 📱 Responsive design (Mobile, Tablet, Desktop)
- ⚡ Fast and easy to use
- 🔒 Password-protected access
- ⏰ Auto session timeout (8 hours)

## Security Features
- ✅ SHA-256 password hashing
- ✅ Session token validation
- ✅ 8-hour auto logout
- ✅ Robots.txt to discourage search engines
- ✅ HTTPS encryption via GitHub Pages

## How to Add New Monthly Data

There are two easy options now.

### Option A) Paste-ready TXT/CSV (no Python)
1) Export or copy the monthly sheet data to a text file (tab-separated) named like:
   - `att-sum-oct-2025.txt` (preferred) or a CSV `att-sum-oct-2025.csv`.
2) Commit and push the file to the repo root.
3) Update `months.json` (optional). If you skip this, the site will still load `att-sum.txt` and any files found via the generator once you run Option B.

### Option B) Use helper scripts (recommended)
1) Convert Excel -> CSV
   - Install once: `pip install pandas xlrd openpyxl`
   - Run: `python3 scripts/convert_excel_to_csv.py --input "COD Filter Plant.xls" --sheet "Sheet1" --output "att-sum-oct-2025.csv"`
2) Generate/refresh months.json
   - Run: `python3 scripts/generate_manifest.py`
   - This scans for `*.txt` and `*.csv` and writes `months.json` automatically.
3) Commit and push the new files.

The site reads `months.json` and populates the month dropdown automatically, no code edits needed.

## File Format
Both TSV (`.txt`) and CSV (`.csv`) are supported.
- Headers can be like the current `att-sum.txt` (first 4 lines) — parser will auto-skip header.
- Required columns (first 3): Employee ID, Name, Department (remaining columns are parsed if present).

## Usage
1. Open `index.html` in a web browser
2. Select the month from dropdown
3. Type Employee ID or Name in the search box
4. Click on a suggestion or press Search

## Support
For any issues or questions, contact the system administrator.
