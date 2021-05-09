import math
from decimal import Decimal
from sys import stdin


def get_result(data):
    A, B = data
    return math.floor(A * B)


if __name__ == "__main__":
    data = stdin.readline().rstrip().split(" ")
    data = [int(data[0]), Decimal(data[1])]
    result = get_result(data)
    print(result)
