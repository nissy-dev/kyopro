from sys import stdin
from functools import reduce


def comb_mod(n, a, mod=10**9+7):
    # https://img.atcoder.jp/abc156/editorial.pdf
    # nCk は, k回の積で計算できる
    num = reduce(lambda x, y: x * y % mod, range(n, n - a, -1))
    den = reduce(lambda x, y: x * y % mod, range(1, a + 1))
    # nCk mod = X/Y mod = X * Y^(10**9+7-2) mod
    return num * pow(den, mod - 2, mod) % mod


def get_result(data):
    n, a, b = data[0]
    mod = 10**9+7
    out = pow(2, n, mod) - comb_mod(n, a, mod) - comb_mod(n, b, mod) - 1 
    out %= mod
    return out

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
