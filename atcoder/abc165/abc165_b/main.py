import math
from sys import stdin


def get_result(data):
    N = data[0]
    cnt = 0
    val = 100
    while N > val:
        val = math.floor(val * 1.01)
        cnt += 1
    return cnt


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
