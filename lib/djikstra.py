from heapq import heappush, heappop


class Dijkstra:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.adj_list = [[] for _ in range(self.n)]

    # Edge数分回すことを想定
    def add_edge(self, start, end, weight=1, undirected=False):
        self.adj_list[start].append((end, weight))
        if undirected:
            self.adj_list[end].append((start, weight))

    def distance(self, start):
        # 始点から各頂点までの最短距離を格納する
        self.dist = [float('inf') for _ in range(self.n)]
        # 最短経路における, その頂点の前の頂点のIDを格納する
        self.prev = [-1 for _ in range(self.n)]
        self.dist[start] = 0
        # 各要素は，(頂点vのID, startからある頂点vまでの仮の距離)からなるタプル
        q = []
        heappush(q, (start, 0))
        while len(q) != 0:
            src, prov_cost  = heappop(q)
            # プライオリティキューに格納されている最短距離が, 現在計算できている最短距離より大きければ，distの更新をする必要はない
            if self.dist[src] < prov_cost:
                continue
            # 他の頂点の探索
            for val in self.adj_list[src]:
                dest, cost = val
                if self.dist[dest] > self.dist[src] + cost:
                    self.dist[dest] = self.dist[src] + cost # distの更新
                    heappush(q, (dest, self.dist[dest])) # キューに新たな仮の距離の情報をpush
                    self.prev[dest] = src
        return self.dist

    def shortest_path(self, goal):
        path = [goal]
        dest = goal
        # 終点から最短経路を逆順に辿る
        while self.prev[dest] != float('inf'):
            path.append(self.prev[dest])
            dest = self.prev[dest]
        return path[::-1]
