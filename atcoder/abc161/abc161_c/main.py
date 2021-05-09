from sys import stdin


def get_result(data):
    N, K = data
    _, mod = divmod(N, K)
    ans = min([mod, abs(mod - K)])
    return ans


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
