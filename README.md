# 🧠 Codeforces Daily — Automated Challenge Framework

A lightweight, automated structure for solving and testing **Codeforces** problems — professionally organized and CI-ready.

---

## 🚀 What Is This Project?

This is not just a collection of solutions — it’s a **mini development & testing framework** for competitive programming.  
It helps you solve problems efficiently, stay organized, and prove consistent progress.

### 💡 Features

✅ Automatically create a structured folder for each new Codeforces problem  
✅ Include ready-to-use templates for solution (`main.py`) and tests (`test_ID.py`)  
✅ Auto-discover all sample input/output files under `samples/`  
✅ Run and verify **all samples** using `pytest` — one test per sample  
✅ Enforce clean code style with `black` and `ruff`  
✅ Optional CI validation with GitHub Actions  
✅ Easy version control via Git and GitHub  
✅ Daily problem folders organized by date for clear progress tracking  

---

## 🧩 Project Structure

codeforces-daily/
│
├── .github/workflows/ci.yml # GitHub CI automation (optional)
│
├── scripts/ # Automation utilities
│ └── new_challenge.py # Scaffolds new problem folders automatically
│
├── templates/ # Boilerplate templates for new problems
│ ├── main.py # Starter code for problem solutions
│ └── template_test_samples.py # Universal test template for all problems
│
├── 2025/ # Yearly folders (auto-created)
│ └── 10-26/
│ ├── 4A_Watermelon/ # Example problem folder
│ │ ├── main.py # Your solution code
│ │ ├── test_4A.py # Auto-generated test file
│ │ └── samples/ # Input/output samples for testing
│ │ ├── 1.in
│ │ ├── 1.out
│ │ ├── 2.in
│ │ └── 2.out
│ │
│ └── 508A_Pasha_and_Pixels/ # Another example problem
│ ├── main.py
│ ├── test_508A.py
│ └── samples/
│ ├── 1.in / 1.out
│ ├── 2.in / 2.out
│ └── ...
│
├── .gitignore # Ignore local-only files (.venv, cache, notes, etc.)
├── pyproject.toml # Project configuration (pytest, ruff, black)
├── requirements.txt # Python dependencies
└── README.md # You are here

---

## 🧠 How It Works

### 1️⃣ Create a new challenge

From your project root:
python scripts/new_challenge.py --id 508A --title "Pasha and Pixels" 

✅ A new folder is automatically created: the 2025 is the Year of ceration and 10-26 is the day and month- the first part of the name is the id of that chalenge and the other part is the name.
2025/10-26/508A_Pasha_and_Pixels/
  ├── main.py
  ├── test_508A.py
  └── samples/

---

### 2️⃣ Add sample test cases

Put the official Codeforces samples into the `samples/` folder:
samples/
  1.in
  1.out
  2.in
  2.out

---

### 3️⃣ Implement your solution

Edit the generated `main.py`:
#!/usr/bin/env python3
import sys

def solve():
    data = sys.stdin.read().strip().split()
    # TODO: implement the solution here
    print(data)

if __name__ == "__main__":
    solve()

---

### 4️⃣ Test automatically

# 🧪 Automated Testing & Code Quality (CI + DevOps)

Your project is designed with **continuous integration (CI)** principles in mind — meaning that every commit is automatically tested and checked on GitHub.

Here’s how it works locally and in CI 👇  

---

## ✅ Run Local Tests

To test your current problem only:
```bash
pytest 2025/10-26/508A_Pasha_and_Pixels -q
```

Each sample input (`.in`) is tested independently, with a clear pass/fail summary:
```
test_508A.py::test_sample[1.in] PASSED
test_508A.py::test_sample[2.in] FAILED
```

To run **all** problems and verify your entire progress:
```bash
pytest -q
```

---

## 🎨 Enforce Consistent Code Style

Before pushing your work, make sure your code is clean and consistent.

### 1. Format with [Black](https://black.readthedocs.io/):
```bash
black .
```
Automatically reformats all Python files according to a unified standard.  
(*In CI, this is checked using `black --check .` — so formatting must be correct.*)

### 2. Lint with [Ruff](https://docs.astral.sh/ruff/):
```bash
ruff check .
```
Detects common issues, unused imports, and deviations from PEP8.  
Fix them using:
```bash
ruff check . --fix
```

---

## 🧩 Combine Everything in CI (Continuous Integration)

Your `.github/workflows/ci.yml` runs the same steps automatically on every push:

1. ✅ Install dependencies  
2. ✅ Check linting with `ruff`  
3. ✅ Verify formatting with `black --check .`  
4. ✅ Run all tests with `pytest`  

If any of these fail, the GitHub Action marks the commit as ❌ failed —  
just like a real **DevOps-style code pipeline**.

---

## 💡 Tip for Developers

You can automate these checks **before every commit** using `pre-commit` hooks:

```bash
pip install pre-commit
pre-commit install
```

This ensures:
- Code is formatted by `black`
- Style checked by `ruff`
- Tests pass locally before committing

---


---

## 🧰 Local Development Notes

If you’re working locally:

### Create and activate a virtual environment
python -m venv .venv
.\.venv\Scripts ctivate   # Windows
source .venv/bin/activate  # Linux / macOS

### Run a script manually
python main.py < samples/1.in

### Deactivate
deactivate

---

## 🧪 How Automated Testing Works

- Every problem has its own test file (`test_<id>.py`) generated from `template_test_samples.py`
- `pytest` automatically finds all `samples/*.in` and runs them against your `main.py`
- Expected output comes from matching `.out` files
- Each sample is shown separately in test results
- Failures show clear diffs between **expected** and **got**

---

## ⚙️ Pytest Configuration (pyproject.toml)

[tool.pytest.ini_options]
pythonpath = ["."]
addopts = "-q --import-mode=importlib"
testpaths = ["2025"]

This ensures:
- Only problem folders are tested
- Import conflicts are avoided
- Output is clean and readable

---

## 🔒 Git Ignore Rules

`.gitignore` excludes:
.venv/
__pycache__/
*.pyc
.cache/
.idea/
.vscode/
*.local.txt
*.private.txt
local_*
dev_notes.txt
1-notes/

This prevents local environment and personal files from being pushed to GitHub.

---

## 🧱 Why This Setup Matters

- Keeps every day’s problem **isolated**, clean, and reproducible  
- Makes progress **visible** and testable via CI  
- Builds a verifiable public record of consistent problem-solving  
- Improves code quality with enforced testing and style checks  
- Scales perfectly for hundreds of problems  

---

## 🏁 Summary Workflow

| Step | Command | Description |
|------|----------|-------------|
| 🆕 Scaffold | `python scripts/new_challenge.py --id 123A --title "New Problem"` | Create new problem folder |
| 🧩 Add Samples | place `.in` / `.out` files in `/samples` | Set test data |
| 🧠 Solve | edit `main.py` | Write your solution |
| ✅ Test | `pytest 2025/MM-DD/123A_New_Problem -q` | Run sample tests |
| 🚀 Push | `git add . && git commit -m "solve: 123A New Problem" && git push` | Publish progress |

---

### 🧑‍💻 Author
Built and maintained by **Osama**  
GitHub: [osama11osama](https://github.com/osama11osama)

---

### ⭐ Goal
> Automate daily problem-solving, build discipline, and demonstrate continuous algorithmic progress through code and tests.
