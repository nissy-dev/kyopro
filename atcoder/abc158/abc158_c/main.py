import math
from sys import stdin


def get_result(data):
    A, B = data
    min_A, max_A = math.ceil(A / 0.08), math.floor((A + 1) / 0.08)
    min_B, max_B = math.ceil(B / 0.10), math.floor((B + 1) / 0.10)

    tmp_A = [i for i in range(min_A, max_A)]
    tmp_B = [i for i in range(min_B, max_B)]
    ans = list(set(tmp_A) & set(tmp_B))
    if len(ans) == 0:
        return -1

    return min(ans)


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip("\n").split(" ")))
    result = get_result(data)
    print(result)
