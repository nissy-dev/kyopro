from sys import stdin


def get_result(data):
    remainder = data[0] % data[1]
    quotient = data[0] // data[1]
    return quotient if remainder == 0 else quotient + 1

if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)
