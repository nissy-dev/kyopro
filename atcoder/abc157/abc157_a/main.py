import math
from sys import stdin


def get_result(data):
    N = data[0]
    return math.ceil(N / 2.0)


if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)
