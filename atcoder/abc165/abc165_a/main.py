from sys import stdin


def get_result(data):
    K = data[0][0]
    A, B = data[1]
    if A % K == 0 or B % K == 0:
        return "OK"
    else:
        if (A // K) == (B // K):
            return "NG"
        else:
            return "OK"


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
