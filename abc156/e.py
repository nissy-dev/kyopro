from sys import stdin



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


def get_result(data):
    n, k = data
    mod = 10**9+7
    fact, factinv = prepare(n, mod)
    ans = 0
    for m in range(n):
        # xHy = x+y−1Cx−1
        if m <= k:
            ans += (cmb(n, m, mod, fact, factinv) * cmb(n-1, n-m-1, mod, fact, factinv)) % mod
    ans %= mod
    return ans

if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)