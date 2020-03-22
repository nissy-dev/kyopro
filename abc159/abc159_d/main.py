import collections
from sys import stdin


def counter(num_arr):
    uniq_dict = {}
    for val in num_arr:
        uniq_dict[val] = uniq_dict.get(val, 0) + 1
    return uniq_dict


def get_result(data):
    N = data[0][0]
    A = data[1]
    uniq_cnt = counter(A)
    item_dict = uniq_cnt.items()
    for i in range(N):
        ans = 0
        for key, value in item_dict:
            if key == A[i]:
                value -= 1
            if value == 1:
                continue
            ans += int(value * (value - 1) / 2)
        print(ans)


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    get_result(data)
