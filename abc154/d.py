from sys import stdin


def get_result(data):
    N, K = data[0]
    A = data[1]
    e_val = [(1 + val) / 2 for val in A]

    # 累積和を算出 (最初は0)
    e_cumsum = [0]
    for i in range(N):
        e_cumsum.append(e_cumsum[i] + e_val[i])

    # 隣接するK個の部分和を取得
    e_sum_k = []
    for i in range(N+1-K):
        e_sum_k.append(e_cumsum[i+K] - e_cumsum[i])

    return max(e_sum_k)


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
