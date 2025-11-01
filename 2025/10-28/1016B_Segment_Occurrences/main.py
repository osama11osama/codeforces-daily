#!/usr/bin/env python3
import sys


def solve():
    # 1️⃣ Read and parse input
    data = sys.stdin.read().strip().split()
    n = int(data[0])  # length of string s
    m = int(data[1])  # length of string t
    q = int(data[2])  # number of queries
    s = data[3]  # main string
    t = data[4]  # substring we search for

    # 2️⃣ Step 1: Find where t occurs in s
    # occ[i] = 1 if t starts at position i (1-based), else 0
    occ = [0] * (n + 1)
    if m <= n:
        for i in range(n - m + 1):
            # check if substring of s starting at i equals t
            if s[i : i + m] == t:
                occ[i + 1] = 1  # mark position (1-based index)

    # 3️⃣ Step 2: Build prefix sums to count occurrences quickly
    # pref[i] = total number of t occurrences up to position i in s
    pref = [0] * (n + 1)
    for i in range(1, n + 1):
        pref[i] = pref[i - 1] + occ[i]

    # 4️⃣ Step 3: Answer each query efficiently
    # For each query [l, r], count how many t occur fully inside this range
    idx = 5
    results = []
    for _ in range(q):
        L = int(data[idx])
        r = int(data[idx + 1])
        idx += 2

        # the last possible start position where t fits in [l, r]
        last_start = r - m + 1

        if last_start < L or m > (r - L + 1):
            # substring too short → no matches
            results.append("0")
        else:
            # count = number of starts in [l, last_start]
            count = pref[last_start] - pref[L - 1]
            results.append(str(count))

    # 5️⃣ Print all results at once
    print("\n".join(results))


if __name__ == "__main__":
    solve()
