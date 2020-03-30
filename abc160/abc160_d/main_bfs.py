from sys import stdin
from collections import deque


def get_adj_list(num_nodes, data, undirected=True):
    # adj_list ex) {1:[2,3,4], 2:[1,4,5], 3:[1,4], 4:[1,2,3,5], 5:[2,4]}
    graph = {}
    for i in range(num_nodes):
        graph[i+1] = []
    for val in data:
        x, y = val
        graph[x] = graph[x] + [y]
        if undirected:
            graph[y] = graph[y] + [x]
    return graph


def breadth_first_search(adj_list, start_node):
    dist = {}
    queue = deque([(start_node, 0)])
    while len(queue) > 0:
        v, d = queue.popleft()
        if v in dist: continue
        dist[v] = d
        for u in adj_list[v]:
            if u not in dist:
                queue.append((u, d+1))
    return dist


# BFS pypyでAC
def get_result(data):
    N, X, Y = data
    _data = [[i, i+1] for i in range(1, N)]
    _data += [[X, Y]]
    adj_list = get_adj_list(N, _data)
    dist_cnt = [0 for i in range(N)]
    for i in range(N):
        dist = breadth_first_search(adj_list, i+1)
        for j in range(i, N):
            dist_cnt[dist[j+1]] += 1
    for i in range(1, N):
        print(dist_cnt[i])


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip('\n').split(' ')))
    get_result(data)