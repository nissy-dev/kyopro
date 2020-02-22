from sys import stdin


def get_result(data):
    N, R = data
    if N < 10:
        return R + 100 * (10 - N)
    
    return R

if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)
