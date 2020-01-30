from sys import stdin


def get_result(data):
    N, K = data[0]
    H = sorted(data[1])
    return 0 if N <= K else sum(H[0:(N-K)])

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
