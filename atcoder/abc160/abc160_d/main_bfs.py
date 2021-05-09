from sys import stdin
from collections import deque


class BreadthFirstSearch:
    def __init__(self, num_nodes):
        self.n = num_nodes
        self.graph = [[] for _ in range(self.n)]

    # Edge数分回すことを想定
    def add_edge(self, start, end, undirected=True):
        self.graph[start].append(end)
        if undirected:
            self.graph[end].append(start)

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
                for u in self.graph[v]:
                    if order[u] >= 0:
                        continue
                    q.append((u, v, d + 1))
        return order, parent, depth


# BFS pypyでAC
def get_result(data):
    N, X, Y = data
    _data = [[i, i + 1] for i in range(1, N)]
    _data += [[X, Y]]
    bfs = BreadthFirstSearch(N)
    for val in _data:
        bfs.add_edge(val[0] - 1, val[1] - 1)
    dist_cnt = [0 for i in range(N)]
    for i in range(N):
        _, _, depth = bfs.search(i)
        for j in range(i, N):
            dist_cnt[depth[j]] += 1
    for i in range(1, N):
        print(dist_cnt[i])


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip("\n").split(" ")))
    get_result(data)
