#!/usr/bin/env python3
import sys


def solve():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        print(0)
        return
    else:
        m = data[1]
        a = data[2:]

        pref = 0        # running sum of a
        k = 0  # running sum of t
        t_list = []

        for x in a:
            pref += x
            # t = int(sum(a_lsit[:i+1])/m) - k
            t = pref // m - k
            t_list.append(t)
            k+=t
            
        # print("n =", n, " m =", m)
        print(*t_list)
        


if __name__ == "__main__":
    solve()
