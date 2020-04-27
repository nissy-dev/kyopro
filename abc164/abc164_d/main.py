from sys import stdin


def get_result(data):
    S = data[0]
    mod_all_bit = [0] * 2019
    mod_all_bit[0] = 1
    # 10**i の mod を漸化式的に事前計算
    # こうすることで計算が効率化できる
    ten_i_mod = [0] * len(S)
    ten_i_mod[0] = 1
    for i in range(len(S)-1):
        ten_i_mod[i+1] = (ten_i_mod[i] * 10) % 2019
    mod = 0
    for i in range(len(S)):
        # ここも漸化式的に計算
        mod = (mod + ten_i_mod[i] * int(S[-(i+1)])) % 2019
        mod_all_bit[mod] += 1
    ans = 0
    for val in mod_all_bit:
        if val >= 2:
            ans += val * (val-1) * 0.5
    return int(ans)


if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
