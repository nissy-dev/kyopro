#!/usr/bin/env python3
from sys import stdin


def solve(data):
    N = data[0][0]
    A = data[1]
    ans = 0
    while True:
        for i in range(N):
            if (A[i] % 2) == 0:
                A[i] = A[i] / 2
            else:
                print(ans)
                return
        ans += 1


if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
