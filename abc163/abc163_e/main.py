from sys import stdin


# def get_result(data):
#     N, K = data[0]
#     A = data[1]
#     dp = [[-1]*(N+1) for _ in range(N+1)]
#     B = [[A[i], i] for i in range(N)]
#     B = sorted(B, reverse=True)
#     ans = 0
#     for r in range(K, N+2):
#         min_val = e_cumsum[r]
#         max_val = e_cumsum[N+1] - e_cumsum[N+1-r]
#         ans += (max_val - min_val + 1) % mod
#     return ans % mod


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
