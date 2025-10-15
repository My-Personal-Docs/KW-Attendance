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

### Step 1: Add your monthly text file
Save your new attendance report as a text file, for example:
- `att-sum-oct-2025.txt` for October 2025
- `att-sum-nov-2025.txt` for November 2025
- etc.

### Step 2: Update the month selector
Open `index.html` and find this section (around line 270):

```javascript
const monthFiles = {
    'att-sum.txt': {
        name: 'September 2025',
        period: 'September 1-30, 2025',
        created: 'October 1, 2025'
    }
    // Add new months below:
};
```

Add your new month like this:

```javascript
const monthFiles = {
    'att-sum.txt': {
        name: 'September 2025',
        period: 'September 1-30, 2025',
        created: 'October 1, 2025'
    },
    'att-sum-oct-2025.txt': {
        name: 'October 2025',
        period: 'October 1-31, 2025',
        created: 'November 1, 2025'
    }
};
```

### Step 3: Add the dropdown option
Find the `<select id="monthSelect">` section (around line 227) and add a new option:

```html
<select id="monthSelect" onchange="loadSelectedMonth()">
    <option value="att-sum.txt">September 2025 (Sep 1-30)</option>
    <option value="att-sum-oct-2025.txt">October 2025 (Oct 1-31)</option>
</select>
```

### Step 4: Done!
That's it! The page will now show a dropdown to select different months.

## File Format
The text file should have the same format as the current `att-sum.txt`:
- First 4 lines are headers
- Tab-separated values
- Columns: Employee ID, Name, Department, Work Duration, Late, Leave Early, etc.

## Usage
1. Open `index.html` in a web browser
2. Select the month from dropdown
3. Type Employee ID or Name in the search box
4. Click on a suggestion or press Search

## Support
For any issues or questions, contact the system administrator.
