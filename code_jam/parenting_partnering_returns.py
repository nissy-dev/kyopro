from sys import stdin


def show_result(data):
    T = data[0][0]  # test case num
    n_idx = 1
    for i in range(T):
        n = data[n_idx][0]
        origin_tasks = data[(n_idx+1):(n_idx+1+n)]
        tasks = [origin_tasks[j] + [j] for j in range(n)]
        tasks = sorted(tasks, key=lambda x: (x[0], x[1]))
        ans = []
        j_end = -1
        c_end = -1
        for k in range(n):
            if c_end <= tasks[k][0]:
                c_end = tasks[k][1]
                ans.append(['C', tasks[k][2]])
            elif j_end <= tasks[k][0]:
                j_end = tasks[k][1]
                ans.append(['J', tasks[k][2]])
            else:
                ans = 'IMPOSSIBLE'
                break
        if ans != 'IMPOSSIBLE':
            ans = sorted(ans, key=lambda x: x[1])
            ans = [ans[l][0] for l in range(n)]
        print('Case #{}: {}'.format(i+1, ''.join(ans)))
        n_idx = n_idx + 1 + n


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    show_result(data)
