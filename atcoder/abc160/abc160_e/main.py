from sys import stdin


def get_result(data):
    X, Y, A, B, C = data[0]
    p = sorted(data[1], reverse=True)
    q = sorted(data[2], reverse=True)
    r = sorted(data[3], reverse=True)
    tmp = p[0:X] + q[0:Y] + r
    ans = sum(sorted(tmp, reverse=True)[0 : (X + Y)])
    return ans


if __name__ == "__main__":
    raw_data = [val.rstrip("\n") for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
