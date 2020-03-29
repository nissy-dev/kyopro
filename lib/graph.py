# 重み付きグラフの初期化
def init_adj_mat(n, data):
    # d[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [[float("inf")]*n for i in range(n)]
    # 各辺のコストを更新
    for val in data:
        x, y, w = val
        d[x-1][y-1] = w
        d[y-1][x-1] = w
    # 自分自身のコストを0にする
    for i in range(n):
        d[i][i] = 0
    return d

# n <= 300 くらいだと通る
def warshall_floyd(d, n):
    #d[i][j]: iからjへの最短距離
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # dp の要領で更新
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d


