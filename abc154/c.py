from sys import stdin


def get_result(data):
    N, A = data[0], data[1]
    return 'YES' if len(set(A)) == N[0] else 'NO'

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
