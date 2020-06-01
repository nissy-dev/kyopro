# 10進数からn進数への変換
def base_10_to_n(origin_number, n):
    tmp = origin_number
    out = ''
    while tmp > 0:
        out = str(tmp % n) + out
        tmp = int(tmp / n)
    return out


# a, bの最大公約数
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# a, bの最小公倍数
def lcm(a, b):
    return a * b // gcd(a, b)


# 素数判定
# O(n**0.5)
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # nの平方根まで計算する
    for p in range(3, int(n**0.5)+1, 2):
        if n % p == 0:
            return False
    return True


# エラトステネスの篩による素数リストの作成
# O(nloglogn), Nが大きいと動かない
def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = False
    is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]


# 素因数分解 -> list で返す
def prime_factorization(n):
    b = 2
    fct = []
    while b * b <= n:
        while n % b == 0:
            n //= b
            fct.append(b)
        b = b + 1
    if n > 1:
        fct.append(n)
    return fct


def prime_factorization_with_prime_list(n, prime_list):
    fct = []
    for b in prime_list:
        while n % b == 0:
            n //= b
            fct.append(b)
    return fct


# 素因数分解 -> tuple で返す
def prime_factorization_tuple(n):
    fct = []  # prime factor
    b, e = 2, 0  # base, exponent
    while b * b <= n:
        while n % b == 0:
            n = n // b
            e = e + 1
        if e > 0:
            fct.append((b, e))
        b, e = b + 1, 0
    if n > 1:
        fct.append((n, 1))
    return fct


# nの約数列挙
def divisor(n):
    ass = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            ass.append(i)
            if i**2 == n:
                continue
            ass.append(n//i)
    return ass  # sortされていない
