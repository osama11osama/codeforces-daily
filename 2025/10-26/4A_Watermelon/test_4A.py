import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
PY = sys.executable


def run_case(folder: Path, case: Path):
    proc = subprocess.run(
        [PY, str(folder / "main.py")],
        input=case.read_bytes(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    expected = (case.with_suffix(".out")).read_text().strip()
    got = proc.stdout.decode().strip()
    assert got == expected, f"\nExpected:\n{expected}\nGot:\n{got}\n"


def test_samples():
    samples = sorted((HERE / "samples").glob("*.in"))
    for s in samples:
        run_case(HERE, s)
