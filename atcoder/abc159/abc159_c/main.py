from sys import stdin


def get_result(data):
    L = data[0]
    return pow((L / 3.0), 3.0)


if __name__ == "__main__":
    data = list(map(int, stdin.readline().split(" ")))
    result = get_result(data)
    print(result)
