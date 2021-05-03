#!/usr/bin/env python3
from sys import stdin


def solve(data):
    ans = 0
    N, A, B = data
    for i in range(1, N + 1):
        keta_sum = sum([int(val) for val in str(i)])
        if A <= keta_sum <= B:
            ans += i
    print(ans)


if __name__ == "__main__":
    # 1行
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    # raw_data = [val.rstrip() for val in stdin.readlines()]
    # data = [list(map(int, val.split(' '))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
