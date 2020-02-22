import numpy as np
from sys import stdin


def get_result(data):
    N, X = data[0][0], data[1:][0]
    X = np.array(X)
    max_X = max(X)
    tmp = np.zeros(max_X + 1)
    for i in range(max_X + 1):
        tmp[i] = np.sum((X - i) ** 2)
    return int(min(tmp))

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
