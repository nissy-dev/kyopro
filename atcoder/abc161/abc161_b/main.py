import numpy as np
from sys import stdin


def get_result(data):
    N, M = data[0]
    A = np.array(data[1])
    total = sum(A)
    pop_goods = A[A >= total / (4 * M)]
    if len(pop_goods) >= M:
        return "Yes"
    return "No"


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
