from sys import stdin


def get_result(data):
    S = data[0]
    return 'ARC' if S == 'ABC' else 'ABC'


if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
