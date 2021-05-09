from sys import stdin


# 解説のコード
def get_result(data):
    N, X, Y = data
    dist_cnt = [0 for i in range(N)]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            min_dist = min(
                [j - i, abs(X - i) + 1 + abs(Y - j), abs(Y - i) + 1 + abs(X - j)]
            )
            dist_cnt[min_dist] += 1
    for i in range(1, N):
        print(dist_cnt[i])


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip("\n").split(" ")))
    get_result(data)
