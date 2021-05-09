import collections
from sys import stdin

# # not AC
# def counter(num_arr):
#     uniq_dict = {}
#     for val in num_arr:
#         uniq_dict[val] = uniq_dict.get(val, 0) + 1
#     return uniq_dict


# def get_result(data):
#     N = data[0][0]
#     A = data[1]
#     uniq_cnt = counter(A)
#     ans = {}
#     for key in uniq_cnt.keys():
#         tmp = uniq_cnt.copy()
#         tmp[key] -= 1
#         ans[key] = int(sum([val * (val-1) / 2 for val in tmp.values()]))

#     for i in range(N):
#         print(ans[A[i]])


def get_result(data):
    N = data[0][0]
    A = data[1]
    uniq_cnt = collections.Counter(A)
    all_selection = 0
    for val in uniq_cnt.values():
        all_selection += int(val * (val - 1) / 2)

    for i in range(N):
        print(all_selection - uniq_cnt[A[i]] + 1)


if __name__ == "__main__":
    raw_data = [val.rstrip("\n") for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    get_result(data)
