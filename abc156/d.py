from sys import stdin


def cmb_prepare(n, p=10**9+7):
    fact = [1, 1]
    factinv = [1, 1]
    inv = [0, 1]
    for i in range(2, n + 1):
        fact.append((fact[-1] * i) % p)
        inv.append((-inv[p % i] * (p // i)) % p)
        factinv.append((factinv[-1] * inv[-1]) % p)
    return fact, factinv


def cmb(n, r, fact, factinv, p=10**9+7):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n-r] % p


# not AC
def get_result(data):
    n, a, b = data[0]
    fact, factinv = cmb_prepare(n)
    mod = 10**9 + 7
    out = ((2 ** n - 1) % mod - cmb(n, a, fact, factinv) - cmb(n, b, fact, factinv)) % mod
    return out

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
