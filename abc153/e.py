from sys import stdin


## This code doesn't pass the test
# def get_result(data):
#     H, N = data[0]
#     A_and_B = np.array(data[1:])
#     calc_efficient = np.array(list(map(lambda x: float(x[0] / x[1]), A_and_B)))
#     sorted_index = np.argsort(-calc_efficient)

#     cost = 0
#     remainder_H = H
#     for i in sorted_index:
#         A, B = A_and_B[i]
#         quotient = remainder_H // A
#         if quotient > 0:
#             cost += B * quotient
#             remainder_H = remainder_H - A * quotient
#         else:
#             if remainder_H > 0:
#                 continue
#             else:
#                 break

#     return cost

## 答え (DP, ナップザック問題の典型らしい)
# pythonだとTLEになる, pypyでAC (pypyはnumpy使えない)
# 自分の解法は典型的なハマり方をしたっぽい

def get_result(data):
    # データ取得
    H, N = data[0]
    A_and_B = data[1:]
    A = [0 for _ in range(N)]
    B = [0 for _ in range(N)]
    for i in range(N):
        Ai, Bi = A_and_B[i]
        A[i] = Ai
        B[i] = Bi

    # 最小化問題だから無限で初期化
    # DP[j] = Aの和が j の時の最小コスト (魔力)
    # 個数制限がないから通常のDP[i][j]のiがないってこと...?
    # 普通は、dp[i][j] = i番目までを使って Aの和が j の時の最小コスト
    inf = float("inf")
    # 長さ H (制約条件) のテーブルを作成
    dp =[inf for _ in range(H+1)]
    # 初期値
    dp[0] = 0

    # DP (コードはなんとなく理解できた)
    for i in range(H):
        for j in range(N):
            # 魔力1つずつについてloopさせる
            # 個数制限なしのナップザックの漸化式
            if (i+1) - A[j] < 0:
                dp[i+1] = min(dp[i+1], dp[0] + B[j])
            else:
                dp[i+1] = min(dp[i+1], dp[i+1-A[j]] + B[j])

    return dp[H]

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
