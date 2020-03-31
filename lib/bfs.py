# 重みなしグラフの隣接リスト
# 0-indexed nodes
def get_adj_list(num_nodes, data, undirected=True):
    graph = [[] for _ in range(num_nodes)]
    for val in data:
        x, y = val
        graph[x].append(y)
        if undirected:
            graph[y].append(x)
    return graph


from collections import deque


# BFS depth = distance
def breadth_first_search(adj_list, start_node):
    N = len(adj_list)
    order = [-1] * N # a bfs ordering of each vertex
    parent = [-1] * N # parent of each vertex in the bfs search tree
    depth = [-1] * N # the depth of each vertex
    q = deque([(start_node, -1, 0)]) # (vertex, parent, depth)
    num = 0 # current ordering
    while len(q) > 0:
        v, p, d = q.popleft()
        if order[v] < 0: # visited v for the first time
            order[v] = num; parent[v] = p; depth[v] = d
            num += 1
            for u in adj_list[v]:
                if order[u] >= 0: continue
                q.append((u, v, d+1))
    return order, parent, depth