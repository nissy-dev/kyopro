import itertools
from sys import stdin


def get_result(data):
    N, M, X = data[0]
    C_A = data[1:]
    min_const = float('inf')
    for bit in itertools.product([0, 1], repeat=N):
        cost = 0
        comp = [0] * M
        for i, val in enumerate(bit):
            if val == 1:
                cost += C_A[i][0]
                for j in range(M):
                    comp[j] += C_A[i][j+1]

        if min(comp) >= X and cost < min_const:
            min_const = cost

    return -1 if min_const == float('inf') else min_const


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
