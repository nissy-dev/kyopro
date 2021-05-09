from sys import stdin


def get_result(data):
    T = data[0][0]
    S = data[1][0]
    return "Yes" if T == S[:-1] else "No"


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(str, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
