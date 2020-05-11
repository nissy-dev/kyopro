from sys import stdin


def get_result(data):
    N, M, X = data[0]
    data = [[val[0], val[1:]] for val in data[1:]]
    data = sorted(data, key=lambda x: (x[0], x[1]))
    print(data)
    sum_val = [0] * M
    cost = 0
    for val in data:
        cost += val[0]
        for i in range(M):
            sum_val[i] += val[1][i]
        if min(sum_val) >= X:
            return cost
    return -1


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
