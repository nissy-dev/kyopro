from sys import stdin


def get_result(data):
    A = sorted(data[1])
    ans = 1
    for val in A:
        ans = ans * val
        if ans > 10 ** 18:
            ans = -1
            break
        elif ans == 0:
            ans = 0
            break
    return ans


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
