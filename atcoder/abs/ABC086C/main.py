#!/usr/bin/env python3
from sys import stdin


def solve(data):
    prev_pos = (0, 0)
    prev_time = 0
    for time, x, y in data[1:]:
        dist = abs(x - prev_pos[0]) + abs(y - prev_pos[1])
        time_diff = time - prev_time
        if dist > time_diff or (dist % 2 != time_diff % 2):
            print("No")
            return
        prev_pos = (x, y)
        prev_time = time
    print("Yes")


if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
