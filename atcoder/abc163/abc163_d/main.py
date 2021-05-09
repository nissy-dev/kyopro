from sys import stdin


def get_result(data):
    N, K = data
    mod = 10 ** 9 + 7
    e_val = [i for i in range(N + 1)]
    # 累積和を使ってsumを計算
    e_cumsum = [0]
    for i in range(N + 1):
        e_cumsum.append(e_cumsum[i] + e_val[i])
    ans = 0
    for r in range(K, N + 2):
        min_val = e_cumsum[r]
        max_val = e_cumsum[N + 1] - e_cumsum[N + 1 - r]
        ans += (max_val - min_val + 1) % mod
    return ans % mod


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
