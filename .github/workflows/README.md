@"
# Codeforces Daily

Solve one Codeforces problem every day. Each folder contains `main.py`, `samples/*.in/.out`, and tests.

![CI](https://github.com/<your-username>/codeforces-daily/actions/workflows/ci.yml/badge.svg)

## Usage
```bash
python -m venv .venv
.\.venv\Scripts\activate
pip install -U -r requirements.txt

# scaffold today's problem
python scripts/new_challenge.py --id 4A --title "Watermelon"

# add sample I/O to 2025/MM-DD/4A_Watermelon/samples/1.in and 1.out
pytest
