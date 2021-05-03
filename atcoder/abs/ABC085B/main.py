#!/usr/bin/env python3
from sys import stdin


def solve(data):
    N = data[0][0]
    uniq_rad = set()
    for i in range(N):
        uniq_rad.add(data[i + 1][0])
    print(len(uniq_rad))


if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
