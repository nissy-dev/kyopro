from sys import stdin


def get_result(data):
    a, b = data
    return 'Even' if (a*b) % 2 == 0 else 'Odd'

if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)
