# n <= 300 くらいだと通る
class WarshallFloyd:
    def __init__(self, num_nodes):
        self.n = num_nodes
        # 経路保存用 dist_matrix[i][j]: iからjへの最短距離
        self.dist_matrix = [[float("inf")]*self.n for i in range(self.n)]
        # 経路復元用 prev_matrix[i][j]: i から j への最短経路における j の1つ前の点
        self.prev_matrix = [[i]*self.n for i in range(self.n)]
        # 自身の距離は0にする
        for i in range(self.n):
            self.dist_matrix[i][i] = 0

    # undirected: 有向グラフ or 無向グラフ
    # Edge数分回すことを想定
    def add_edge(self, start, end, weight=1, undirected=False):
        self.dist_matrix[start][end] = weight
        if undirected:
            self.dist_matrix[end][start] = weight

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