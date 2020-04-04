import numpy as np
from sys import stdin


def show_result(data):
    T = data[0][0]  # test case num
    n_idx = 1
    for i in range(T):
        n = data[n_idx][0]
        matrix = np.array(data[(n_idx+1):(n_idx+1+n)])
        trace = sum([matrix[i][i] for i in range(n)])
        cnt_row = 0
        for j in range(n):
            if len(set(matrix[j, :])) != n:
                cnt_row += 1
        cnt_col = 0
        for k in range(n):
            if len(set(matrix[:, k])) != n:
                cnt_col += 1
        print('Case #{}: {} {} {}'.format(i+1, trace, cnt_row, cnt_col))
        n_idx = n_idx + 1 + n


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    show_result(data)
