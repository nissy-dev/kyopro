#!/usr/bin/env python3
from sys import stdin


def solve(data):
    ans = int(data[0][0]) + int(data[1][0]) + int(data[1][1])
    print(str(ans) + " " + data[2][0])


if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(str, val.split(" "))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
