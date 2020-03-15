import math  # noqa
from sys import stdin


def get_result(data):
    cnt = 0
    quotient = data
    # cntはlog2で計算できる
    # cnt = math.ceil(math.log2(data))
    while quotient > 1:
        quotient = quotient // 2
        cnt += 1
    return 2**(cnt+1) - 1


# 以下のような再帰でも計算可能
# def get(x):
#     if x == 1:
#         return 1
#     return 1 + 2 * get(x//2)


if __name__ == '__main__':
    data = int(stdin.readline())
    result = get_result(data)
    print(result)
