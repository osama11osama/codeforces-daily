#!/usr/bin/env python3
import sys


def ints():
    # stream tokens without reading whole file into memory
    for line in sys.stdin.buffer:
        for tok in line.split():
            yield int(tok)

def solve():
    it = ints()
    n = next(it, None)  # not used, but read to advance
    m = next(it, None)
    if m is None:
        print(0)
        return

    pref = 0  # running sum of a's
    k = 0     # running sum of printed t's
    out = []  # tiny buffer to reduce write calls

    for x in it:              # stream remaining a's
        pref += x
        t = pref // m - k
        k += t
        out.append(str(t))
        if len(out) >= 1024:  # flush occasionally (keeps memory tiny)
            sys.stdout.write(" ".join(out) + " ")
            out.clear()

    if out:
        sys.stdout.write(" ".join(out))
    sys.stdout.write("\n")

if __name__ == "__main__":
    solve()
