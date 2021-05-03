#!/usr/bin/env python3
from sys import stdin


def solve(data):
    N, Y = data
    for i in range(N + 1):
        for j in range(N + 1 - i):
            k = N - i - j
            tmp = 10000 * i + 5000 * j + 1000 * k
            if tmp == Y:
                print("{} {} {}".format(i, j, k))
                return
    print("-1 -1 -1")


if __name__ == "__main__":
    # 1行
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    # raw_data = [val.rstrip() for val in stdin.readlines()]
    # data = [list(map(int, val.split(' '))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
