from sys import stdin


def get_result(data):
    A, B, C, K = data
    if (A + B) >= K:
        return K if A > K else A
    else:
        return A - (K - (A + B))


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
