from sys import stdin


def get_result(data):
    N = data[0]
    if N[-1] in ["2", "4", "5", "7", "9"]:
        return "hon"
    elif N[-1] in ["0", "1", "6", "8"]:
        return "pon"
    else:
        return "bon"


if __name__ == "__main__":
    data = list(map(str, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
