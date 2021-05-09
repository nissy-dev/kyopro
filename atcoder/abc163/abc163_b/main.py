from sys import stdin


def get_result(data):
    N, M = data[0]
    A = data[1]
    ans = N - sum(A)
    return ans if ans >= 0 else -1


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
