from sys import stdin


def get_result(data):
    X, Y, Z = data
    return ' '.join([Z, X, Y])


if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
