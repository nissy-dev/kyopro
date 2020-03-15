from sys import stdin


def get_result(data):
    S, T = data[0]
    A, B = data[1]
    U = data[2][0]
    if S == U:
        A = A - 1
    elif T == U:
        B = B - 1
    return ' '.join([str(A), str(B)])


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(str, val.split(' '))) for val in raw_data]
    data[1] = [int(val) for val in data[1]]
    result = get_result(data)
    print(result)
