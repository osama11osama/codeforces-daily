import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parent
PY = sys.executable

def run_case(fin: Path):
    expected = fin.with_suffix(".out").read_text().strip()

    proc = subprocess.run(
        [PY, str(HERE / "main.py")],
        input=fin.read_text(),
        text=True,
        capture_output=True,
        check=False,
    )

    got = proc.stdout.strip()

    # If program crashed or wrote to stderr, show a short reason
    assert proc.returncode == 0, f"{fin.name}: exited {proc.returncode}\nstderr: {proc.stderr.strip()}"
    # Clear one-line diff: shows the sample name + expected vs got
    assert got == expected, f"{fin.name}: expected {expected!r}, got {got!r}"

# one test per sample, readable IDs "1.in", "2.in", ...
samples = sorted((HERE / "samples").glob("*.in"), key=lambda p: p.name)
@pytest.mark.parametrize("fin", samples, ids=[p.name for p in samples])
def test_sample(fin):
    run_case(fin)
