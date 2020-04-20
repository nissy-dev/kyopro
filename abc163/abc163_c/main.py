from sys import stdin


def get_result(data):
    N = data[0][0]
    A = data[1]
    ans = [0 for _ in range(N)]
    for val in A:
        ans[val-1] += 1
    for val in ans:
        print(val)


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    get_result(data)
