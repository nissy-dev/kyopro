from sys import stdin


def get_result(data):
    N, A = data
    for a_i in A:
        if a_i % 2 == 0 and a_i % 3 != 0 and a_i % 5 != 0:
            return 'DENIED'

    return 'APPROVED'


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
