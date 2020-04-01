class BellmanFord:
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
        cnt = 0
        while cnt < self.n:
            end_flag = True
            for src in range(self.n):
                curr = self.dist[src]
                for dest, cost in self.adj_list[src]:
                    if curr != float('inf') and self.dist[dest] > curr + cost:
                        self.dist[dest] = curr + cost
                        self.prev[dest] = src
                        end_flag = False
            if end_flag:
                break
            cnt += 1

        if cnt == self.n:
            # 負の閉路の検出
            return None

        return self.dist

    def shortest_path(self, goal):
        path = [goal]
        dest = goal
        # 終点から最短経路を逆順に辿る
        while self.prev[dest] != float('inf'):
            path.append(self.prev[dest])
            dest = self.prev[dest]
        return path[::-1]