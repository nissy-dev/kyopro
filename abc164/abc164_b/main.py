
import math
from sys import stdin


def get_result(data):
    A, B, C, D = data
    takahasi_q = math.ceil(float(A/D))
    aoiki_q = math.ceil(float(C/B))
    if takahasi_q == aoiki_q:
        return 'Yes'
    return 'Yes' if takahasi_q > aoiki_q else 'No'


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
