from sys import stdin


def get_result(data):
    return 'Yes' if len(list(set(data))) == 2 else 'No'

if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)
