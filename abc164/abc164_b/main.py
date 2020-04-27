
import math
from sys import stdin


def get_result(data):
    A, B, C, D = data
    takahasi_q = math.ceil(A/D)
    aoiki_q = math.ceil(C/B)
    return 'Yes' if takahasi_q >= aoiki_q else 'No'


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
