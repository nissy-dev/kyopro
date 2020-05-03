from sys import stdin


def get_result(data):
    N, M = data[0]
    H = data[1]
    adj_list = [set() for _ in range(N)]
    for val in data[2:]:
        adj_list[val[0]-1].add(val[1]-1)
        adj_list[val[1]-1].add(val[0]-1)

    ans = 0
    for i in range(N):
        base_h = H[i]
        flag = True
        edges = adj_list[i]
        for edge in edges:
            h = H[edge]
            if h >= base_h:
                flag = False
                break
        if flag:
            ans += 1
    return ans


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
