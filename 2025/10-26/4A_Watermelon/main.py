#!/usr/bin/env python3
import sys

def solve():
    n = int(sys.stdin.read().strip())
    print("YES" if n % 2 == 0 and n > 2 else "NO")

if __name__ == "__main__":
    solve()
