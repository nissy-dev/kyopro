import numpy as np
from sys import stdin


def get_result(data):
    N = data[0]
    ans = []
    for i in range(N):
        val = i + 1
        _, mod_3 = divmod(val, 3)
        _, mod_5 = divmod(val, 5)
        if mod_3 != 0 and mod_5 != 0:
            ans.append(val)
    ans = np.array(ans)
    return sum(ans[ans <= N])


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
