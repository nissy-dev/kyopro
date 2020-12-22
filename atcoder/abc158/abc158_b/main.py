from sys import stdin


def get_result(data):
    N, A, B = data
    if A == 0:
        return 0

    remainder = N % (A+B)
    tmp = remainder if remainder < A else A
    quotient = N // (A+B)
    ans = A * quotient + tmp
    return ans


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)
