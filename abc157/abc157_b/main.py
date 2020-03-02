import numpy as np
from sys import stdin


def get_result(data):
    A = np.array([data[0], data[1], data[2]])
    N = data[3][0]
    B = [data[i+4][0] for i in range(N)]
    for i in range(3):
        for j in range(3):
            if A[i, j] in B:
                A[i, j] = 1
            else:
                A[i, j] = 0
    # judge bingo
    tmp = []
    for i in range(3):
        tmp.append(sum(A[:, i]))
        tmp.append(sum(A[i, :]))
    tmp.append(A[0,0] + A[1,1] + A[2,2])
    tmp.append(A[0,2] + A[1,1] + A[2,0])
    return 'Yes' if 3.0 in tmp else 'No'

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
