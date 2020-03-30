# 隣接行列の初期化
# no_weight: 重みあり or 重みなし
# undirected: 有向グラフ or 無向グラフ
def get_adj_mat(num_nodes, data, no_weight=True, undirected=True):
    # d[u][v] : 辺uvのコスト(存在しないときはinf)
    adj_mat = [[float("inf")]*num_nodes for i in range(num_nodes)]
    # 各辺のコストを更新
    for val in data:
        x, y = val[0:2]
        w = 1 if no_weight else val[2]
        adj_mat[x-1][y-1] = w
        if undirected:
            adj_mat[y-1][x-1] = w
    # 自分自身のコストを0にする
    for i in range(num_nodes):
        adj_mat[i][i] = 0
    return adj_mat


# n <= 300 くらいだと通る
def warshall_floyd(adj_mat, num_nodes):
    #d[i][j]: iからjへの最短距離
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                # dp の要領で更新
                adj_mat[i][j] = min(adj_mat[i][j], adj_mat[i][k] + adj_mat[k][j])
    return adj_mat


# 重みなしグラフの隣接リスト
def get_adj_list(num_nodes, data, undirected=True):
    # adj_list ex) {1:[2,3,4], 2:[1,4,5], 3:[1,4], 4:[1,2,3,5], 5:[2,4]}
    graph = {}
    # 初期化 
    for i in range(num_nodes):
        graph[i+1] = []
    # 辺の追加
    for val in data:
        x, y = val
        graph[x] = graph[x] + [y]
        if undirected:
            graph[y] = graph[y] + [x]
    return graph


from collections import deque


# BFSで各ノードへの距離を取得
def breadth_first_search(adj_list, start_node):
    dist = {} #ノードへの距離
    queue = deque([(start_node, 0)])
    while len(queue) > 0:
        v, d = queue.popleft()
        if v in dist: continue
        dist[v] = d
        for u in adj_list[v]:
            if u not in dist:
                queue.append((u, d+1))
    return dist


# 行きがけ順...?要確認
def depth_first_search(adj_list, start_node):
    arr_time = {} # 探索順が返る
    time = 0
    stack = [start_node]
    while len(stack) > 0:
        v = stack.pop()
        if v in arr_time:
            continue
        arr_time[v] = time
        time += 1
        for u in adj_list[v]:
            if u not in arr_time:
                stack.append(u)
    return arr_time
