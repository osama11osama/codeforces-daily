# 🧠 Codeforces Daily Automation Framework

This repository contains my **daily Codeforces problem-solving practice**, built using a custom **Python automation framework**.

The goal is to **maintain consistency**, **track progress**, and **automate repetitive setup tasks** while ensuring **clean, tested, and high-quality solutions**.

---

## 🚀 What Is This Project?

This is not just a folder of solutions — it’s a **mini development framework** designed to:

✅ Automatically create a structured folder for each new Codeforces problem  
✅ Provide ready-to-use templates for solutions and tests  
✅ Run automated sample tests locally with `pytest`  
✅ Enforce clean code style using `black` and `ruff`  
✅ Verify everything with GitHub Actions (CI) on every push  
✅ Document daily progress in a professional, reproducible way  

---

## 🌿 Project Structure

```
codeforces-daily/
├─ .github/workflows/ci.yml      # GitHub CI automation
├─ scripts/                      # Automation utilities
│  └─ new_challenge.py           # Scaffolds new problem folders
├─ templates/                    # Boilerplate templates for new problems
│  ├─ main.py                    # Starter code for problem solutions
│  └─ test_samples.py            # Template for automated sample tests
├─ 2025/                         # Yearly solved problems (auto-created)
│  └─ 10-26/4A_Watermelon/       # Example challenge folder
│     ├─ main.py                 # Solution file
│     ├─ test_samples.py         # Test file for sample cases
│     └─ samples/                # Input/output examples
├─ pyproject.toml                # Formatter, linter, and pytest config
├─ requirements.txt              # Dependencies (black, ruff, pytest)
├─ .gitignore                    # Ignored files/folders
└─ README.md                     # Project documentation (this file)
```

---

## ⚙️ How It Works

1. **scripts/new_challenge.py**  
   Creates a new folder with today’s date, copies templates, and prepares sample files.

   Example:
   ```
   python scripts/new_challenge.py --id 4A --title "Watermelon"
   ```

   Generates:
   ```
   2025/10-26/4A_Watermelon/
   ├─ main.py
   ├─ test_samples.py
   └─ samples/
       ├─ 1.in
       └─ 1.out
   ```

2. **templates/main.py** — Starter code for every new problem  
3. **templates/test_samples.py** — Auto-tests your solution using sample I/O  
4. **pytest** — Runs all tests and checks your output matches expected results  
5. **GitHub Actions** — Automatically lints, formats, and tests every commit  

---

## 📘 Example: Solve and Test a Challenge

1️⃣ Scaffold today’s problem:
```
python scripts/new_challenge.py --id 4A --title "Watermelon"
```

2️⃣ Add sample I/O:  
`samples/1.in`
```
8
```
`samples/1.out`
```
YES
```

3️⃣ Write the solution (`main.py`)
```
import sys

def solve():
    n = int(sys.stdin.read().strip())
    print("YES" if n % 2 == 0 and n > 2 else "NO")

if __name__ == "__main__":
    solve()
```

4️⃣ Test it:
```
pytest
```

✅ Output:
```
collected 1 item
.
1 passed in 0.03s
```

5️⃣ Push to GitHub:
```
git add .
git commit -m "feat(4A): Watermelon — solved"
git push
```

---

## 🧪 Continuous Integration (CI)

Every commit triggers this workflow automatically:

![CI](https://github.com/osama11osama/codeforces-daily/actions/workflows/ci.yml/badge.svg)

Checks performed:
- `black` — Formatting  
- `ruff` — Linting  
- `pytest` — Sample tests  

---

## 🧰 Tools and Technologies

| Purpose | Tool |
|----------|------|
| Language | Python 3.12 |
| Testing | Pytest |
| Linting | Ruff |
| Formatting | Black |
| Automation | GitHub Actions |
| Version Control | Git |
| IDE | Visual Studio Code |

---

## 🎯 Purpose and Goals

This framework helps me:

- Stay consistent with daily problem solving  
- Build habits of testing and clean code  
- Demonstrate real-world engineering practices  
- Showcase progress publicly on GitHub  

Over time, this becomes a **portfolio of disciplined problem-solving and automation skills**.

---

## 📅 Daily Workflow Summary

```
python scripts/new_challenge.py --id <ProblemID> --title "<Title>"
# edit main.py, add samples, run pytest
git add .
git commit -m "feat(<ID>): <Title> — solved"
git push
```

Everything else (linting, testing, CI) runs automatically.

---

## 👤 Author

**Osama Altamar**  
Cybersecurity & Software Developer  
[GitHub Profile](https://github.com/osama11osama)

⭐ *If you like this project, feel free to fork or adapt it for your own problem-solving journey!*
