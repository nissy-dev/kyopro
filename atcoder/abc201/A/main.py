#!/usr/bin/env python3
from sys import stdin


def solve(data):
    data = sorted(data)
    if (data[2] - data[1]) == (data[1] - data[0]):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    # 1行
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    # raw_data = [val.rstrip() for val in stdin.readlines()]
    # data = [list(map(int, val.split(' '))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
