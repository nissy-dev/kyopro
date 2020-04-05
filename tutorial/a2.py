from sys import stdin


def get_result(data):
    return sum([int(val) for val in data[0]])


if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)
