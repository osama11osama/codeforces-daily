#!/usr/bin/env python3
import sys


def solve():
    data = sys.stdin.read().strip().split()  # noqa: F841
    a1 = int(data[0])
    a2 = int(data[1])
    a3 = int(data[2])
    a4 = int(data[3])
    s = data[4]
    answer = 0
    for ch in s:
        if ch == "1":
            answer += a1
        elif ch == "2":
            answer += a2
        elif ch == "3":
            answer += a3
        elif ch == "4":
            answer += a4

    print(answer)

    # print(answer)


if __name__ == "__main__":
    solve()
