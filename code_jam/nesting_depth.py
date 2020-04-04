from sys import stdin


def show_result(data):
    T = int(data[0][0])  # test case num
    for i in range(T):
        S = data[i+1][0]
        prev_num = 0
        ans = ''
        for j in range(len(S)):
            diff = int(S[j]) - prev_num
            if diff > 0:
                ans += '(' * diff + S[j]
            elif diff == 0:
                ans += S[j]
            else:
                ans += ')' * abs(diff) + S[j]
            prev_num = int(S[j])

        if ans[-1] != '0':
            ans += ')' * int(ans[-1])
        print('Case #{}: {}'.format(i+1, ans))


if __name__ == '__main__':
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(str, val.split(' '))) for val in raw_data]
    show_result(data)
