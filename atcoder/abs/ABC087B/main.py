#!/usr/bin/env python3
from sys import stdin


def solve(data):
    ans = 0
    for a in range(data[0][0] + 1):
        for b in range(data[1][0] + 1):
            for c in range(data[2][0] + 1):
                if (a * 500 + b * 100 + c * 50) == data[3][0]:
                    ans += 1
    print(ans)


if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
