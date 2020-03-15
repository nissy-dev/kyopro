from sys import stdin


def get_result(data):
    N, R = data
    return R if N >= 10 else R + 100 * (10 - N)


if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)
