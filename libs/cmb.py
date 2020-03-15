from functools import reduce


def comb_mod(n, a, mod=10**9+7):
    # https://img.atcoder.jp/abc156/editorial.pdf
    # nCk は, k回の積で計算できる
    num = reduce(lambda x, y: x * y % mod, range(n, n - a, -1))
    den = reduce(lambda x, y: x * y % mod, range(1, a + 1))
    # nCk mod = X/Y mod = X * Y^(10**9+7-2) mod
    return num * pow(den, mod - 2, mod) % mod


def prepare(n, p):
    fact = [1, 1]  # fact[n] = (n! mod p)
    factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
    inv = [0, 1]  # factinv 計算用
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)
    return fact, factinv


def cmb(n, r, p, fact, factinv):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p
