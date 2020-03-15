from sys import stdin


def get_result(data):
    return 'x' * len(data[0])


if __name__ == '__main__':
    # https://qiita.com/GHKEN/items/d179805f33abf51016d8
    data = list(map(str, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)
