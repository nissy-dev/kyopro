from sys import stdin


def validate_num(num, n, sc):
    num = str(num)
    if not len(num) == n:
        return False

    for s, c in sc:
        if not num[s - 1] == str(c):
            return False

    return True


def get_result(data):
    N, M = data[0]
    sc = data[1:]
    # 全探索する
    for i in range(1000):
        if validate_num(i, N, sc):
            return i

    return "-1"


if __name__ == "__main__":
    raw_data = [val.rstrip("\n") for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
