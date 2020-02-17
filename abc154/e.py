from sys import stdin
from functools import lru_cache

@lru_cache(None)
def solver(N, K):
    """N以下で0でないものがちょうどK個。0を含める"""
    if N < 10:
        if K == 0:
            return 1
        if K == 1:
            return N
        return 0
    # divmod : 商と余りを両方取れる
    m, r = divmod(N,10)
    ans = 0
    if K >= 1:
        # 1の位が not 0
        ans += solver(m, K-1) * r
        ans += solver(m-1, K-1) * (9-r)
    # 1の位が 0
    ans += solver(m, K)
    return ans


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = solver(data[0][0], data[1][0])
    print(result)