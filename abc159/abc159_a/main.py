from sys import stdin


def get_result(data):
    N, M = data
    ans = N * (N-1) / 2 + M * (M-1) / 2 
    return int(ans)


if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)