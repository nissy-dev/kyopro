from sys import stdin


def get_result(data):
    H, N = data[0]
    A = sorted(data[1])
    return 'No' if sum(A[:N]) < H else 'Yes'


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
