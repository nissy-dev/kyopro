#!/usr/bin/env python3
from sys import stdin


def solve(data):
    H, W = int(data[0][0]), int(data[0][1])
    cell = [[1 if char == "+" else -1 for char in val[0]] for val in data[1:]]

    # dp[i][j] = (i, j) からスタートした時の自分ー相手の最大値
    dp = [[-float("inf") for _ in range(W)] for _ in range(H)]

    # ミニマックス法に関連する問題
    # https://qiita.com/drken/items/4e1bcf8413af16cb62da
    # 降順で回す
    for i in range(H)[::-1]:
        for j in range(W)[::-1]:
            # 初期条件
            if i == H - 1 and j == W - 1:
                dp[i][j] = 0

            if j + 1 < W:
                dp[i][j] = max(dp[i][j], cell[i][j + 1] - dp[i][j + 1])
            if i + 1 < H:
                dp[i][j] = max(dp[i][j], cell[i + 1][j] - dp[i + 1][j])

    if dp[0][0] == 0:
        print("Draw")
    elif dp[0][0] > 0:
        print("Takahashi")
    else:
        print("Aoki")


if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    raw_data = [val.rstrip() for val in stdin.readlines()]
    # data = [list(map(int, val.split(' '))) for val in raw_data]
    data = [list(map(str, val.split(" "))) for val in raw_data]
    solve(data)
