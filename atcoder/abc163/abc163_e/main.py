from sys import stdin


# pypyでAC
def get_result(data):
    N = data[0][0]
    A = data[1]
    dp = [[0]*(N+1) for _ in range(N+1)]
    B = [[A[i], i] for i in range(N)]
    B = sorted(B, reverse=True)
    for i in range(N):
        for j in range(N-i):
            dp[i+1][j] = max(dp[i+1][j], dp[i][j] + B[i+j][0] * (B[i+j][1] - i))
            dp[i][j+1] = max(dp[i][j+1], dp[i][j] + B[i+j][0] * ((N-1-j) - B[i+j][1]))

    res = 0
    for i in range(N):
        res = max(res, dp[i][N-i])
    return res


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
