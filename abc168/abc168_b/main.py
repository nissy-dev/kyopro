
from sys import stdin


def get_result(data):
    K = int(data[0][0])
    S = data[1][0]
    return S if len(S) <= K else S[:K] + "..."


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(str, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
