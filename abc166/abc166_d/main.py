from sys import stdin


def get_result(data):
    N = data[0]
    for a in range(-1000, 1000):
        for b in range(-1000, 1000):
            if (a**5 - b**5) == N:
                return '{} {}'.format(a, b)


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
