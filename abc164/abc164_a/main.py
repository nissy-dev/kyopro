from sys import stdin


def get_result(data):
    S, W = data
    return 'unsafe' if W >= S else 'safe'


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
