import math
from sys import stdin


def get_result(data):
    N = data[0]
    cnt = math.ceil(math.log(N, 3)) - 1
    tmp = 3**cnt - 1
    return 0


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
