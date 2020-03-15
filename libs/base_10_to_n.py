"""雑多な関数の置き場"""


def base_10_to_n(origin_number, n):
    tmp = origin_number
    out = ''
    while tmp > 0:
        out = str(tmp % n) + out
        tmp = int(tmp / n)
    return out
