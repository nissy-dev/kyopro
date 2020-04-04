import numpy as np
from sys import stdin


def show_result(data):
    T = data[0][0]  # test case num
    n_idx = 1
    for i in range(T):
        n = data[n_idx][0]
        origin_tasks = data[(n_idx+1):(n_idx+1+n)]
        tasks = sorted(origin_tasks, key=lambda x: x[0])
        sorted_idx = sorted([i for i in range(n)], key=lambda x: origin_tasks[x][0])
        ans = []
        j_flags = -1
        c_flags = -1
        for j in range(n):
            if j_flags <= tasks[j][0]:
                j_flags = tasks[j][1]
                ans += 'C'
            elif c_flags <= tasks[j][0]:
                c_flags = tasks[j][1]
                ans += 'J'
            else:
                ans = 'IMPOSSIBLE'
                break
        # check
        if len(ans) != n:
            ans = 'IMPOSSIBLE'
        if ans != 'IMPOSSIBLE':
            ans = np.array(ans)[sorted_idx]
        print('Case #{}: {}'.format(i+1, ''.join(ans)))
        n_idx = n_idx + 1 + n


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    show_result(data)
