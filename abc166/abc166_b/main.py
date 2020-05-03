from sys import stdin


def get_result(data):
    N, K = data[0]
    A = data[1:]
    sunuke = set()
    for A_val in A[1::2]:
        for val in A_val:
            sunuke.add(val)

    return N - len(sunuke)


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
