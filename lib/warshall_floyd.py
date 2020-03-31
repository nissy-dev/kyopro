# n <= 300 くらいだと通る
class WarshallFloyd:
    def __init__(self):
        self.n = None
        # 経路保存用 dist_matrix[i][j]: iからjへの最短距離
        self.dist_matrix = None
        # 経路復元用 prev_matrix[i][j]: i から j への最短経路における j の1つ前の点
        self.prev_matrix = None

    # no_weight: 重みあり or 重みなし
    # undirected: 有向グラフ or 無向グラフ
    # data : [[start_node, end_node, weight]], 0-indexed nodes
    def create_adj_mat(self, num_nodes, data, no_weight=True, undirected=True):
        self.n = num_nodes
        self.prev_matrix = [[i]*self.n for i in range(self.n)]
        # 隣接行列 adj_mat[u][v] : 辺uvのコスト(存在しないときはinf)
        adj_mat = [[float("inf")]*self.n for i in range(self.n)]
        # 各辺のコストを更新
        for val in data:
            x, y = val[0:2]
            w = 1 if no_weight else val[2]
            adj_mat[x][y] = w
            if undirected:
                adj_mat[y][x] = w
        # 自分自身のコストを0にする
        for i in range(self.n):
            adj_mat[i][i] = 0
        self.dist_matrix = adj_mat
        return adj_mat

    def distance(self):
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    # dp の要領で更新
                    # min(d[i][k]+d[k][j], d[i][j])
                    if self.dist_matrix[i][k] + self.dist_matrix[k][j] < self.dist_matrix[i][j]:
                        self.dist_matrix[i][j] = self.dist_matrix[i][k] + self.dist_matrix[k][j]
                        self.prev_matrix[i][j] = self.prev_matrix[k][j]
        return self.dist_matrix

    def get_shortest_path(self, start, target):
        cur = target
        path = []
        while cur != start:
            path.append(cur)
            cur = self.prev_matrix[start][cur]
        path.append(start)
        return path[::-1]