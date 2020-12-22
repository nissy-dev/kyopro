from sys import stdin


def get_result(data):
    N = data[0]
    if '7' in list(str(N)):
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
