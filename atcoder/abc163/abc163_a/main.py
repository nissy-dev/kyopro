import math
from sys import stdin


def get_result(data):
    N = int(data[0])
    return math.pi * 2 * N


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
