from sys import stdin
from collections import Counter


def get_result(data):
    N = data[0][0]
    A = data[1]
    L = [0 for _ in range(N)]
    R = [0 for _ in range(N)]
    for i in range(N):
        L[i] = i + A[i] + 1
        R[i] = i + 1 - A[i]

    L_cnt = Counter(L)
    R_cnt = Counter(R)
    ans = 0
    all_key = list(set(R_cnt.keys() & L_cnt.keys()))
    for key in all_key:
        ans += L_cnt[key] * R_cnt[key]
    return ans


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
