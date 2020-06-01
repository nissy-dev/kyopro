from sys import stdin


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


def get_result(data):
    N = data[0]
    fct = prime_factorization_tuple(N)
    ans = 0
    for (_, exp) in fct:
        cnt = 0
        for i in range(1, 11):
            exp -= i
            if exp >= 0:
                cnt += 1
        ans += cnt
    return ans


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
