from sys import stdin


def get_result(data):
    S = data[0]
    return "Yes" if S != "AAA" and S != "BBB" else "No"


if __name__ == "__main__":
    data = list(map(str, stdin.readline().rstrip("\n").split(" ")))
    result = get_result(data)
    print(result)
