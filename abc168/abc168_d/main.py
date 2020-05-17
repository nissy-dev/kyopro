from sys import stdin
from collections import deque
from heapq import heappush, heappop


class BreadthFirstSearch:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.adj_list = [[] for _ in range(self.n)]

    # Edge数分回すことを想定
    def add_edge(self, start, end, undirected=True):
        self.adj_list[start].append(end)
        if undirected:
            self.adj_list[end].append(start)

    # depth = distance
    def search(self, start_node):
        order = [-1] * self.n  # a bfs ordering of each vertex
        parent = [-1] * self.n  # parent of each vertex in the bfs search tree
        depth = [-1] * self.n  # the depth of each vertex
        q = deque([(start_node, -1, 0)])  # (vertex, parent, depth)
        num = 0  # current ordering
        while len(q) > 0:
            v, p, d = q.popleft()
            if order[v] < 0:  # visited v for the first time
                order[v] = num
                parent[v] = p
                depth[v] = d
                num += 1
                for u in self.adj_list[v]:
                    if order[u] >= 0:
                        continue
                    q.append((u, v, d+1))
        return order, parent, depth


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
            src, prov_cost = heappop(q)
            # プライオリティキューに格納されている最短距離が, 現在計算できている最短距離より大きければ，distの更新をする必要はない
            if self.dist[src] < prov_cost:
                continue
            # 他の頂点の探索
            for val in self.adj_list[src]:
                dest, cost = val
                if self.dist[dest] > self.dist[src] + cost:
                    self.dist[dest] = self.dist[src] + cost  # distの更新
                    heappush(q, (dest, self.dist[dest]))  # キューに新たな仮の距離の情報をpush
                    self.prev[dest] = src
        return self.dist, self.prev

    def shortest_path(self, goal):
        path = [goal]
        dest = goal
        # 終点から最短経路を逆順に辿る
        while self.prev[dest] != float('inf'):
            if self.prev[dest] == -1:
                break
            path.append(self.prev[dest])
            dest = self.prev[dest]
        return path[::-1]


def get_result(data):
    N, M = data[0]
    A = data[1:]
    solver = Dijkstra(N)
    for val in A:
        solver.add_edge(val[0]-1, val[1]-1, undirected=True)
    _, prev = solver.distance(0)
    print('Yes')
    for p in prev[1:]:
        print(p + 1)
    return None


# def get_result(data):
#     N, M = data[0]
#     A = data[1:]
#     solver = BreadthFirstSearch(N)
#     for val in A:
#         solver.add_edge(val[0]-1, val[1]-1)
#     _, parent, _ = solver.search(0)
#     print('Yes')
#     for p in parent[1:]:
#         print(p+1)
#     return None


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    get_result(data)
    # print(result)
