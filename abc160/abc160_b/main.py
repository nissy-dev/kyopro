from sys import stdin


def get_result(data):
    N = data[0]
    q, mod = divmod(N, 500)
    q_5, _ = divmod(mod, 5)
    return q * 1000 + q_5 * 5


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)