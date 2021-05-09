from sys import stdin


def get_result(data):
    N = data[0][0]
    A = data[1:]
    tmp = set()
    for i in range(int(N)):
        tmp.add(A[i][0])
    return len(tmp)


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(str, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
