import math
from sys import stdin


def get_result(data):
    A, B, N = data
    if B == 1:
        return 0
    length = N // B + 1
    x = [B * (i + 1) - 1 for i in range(length)]
    ans = []
    for val in x:
        if val > N:
            val = N
        ans.append(math.floor(A * val / B) - A * math.floor(val / B))
    return max(ans)


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
