from sys import stdin
from collections import deque

# not AC
# def get_result(data):
#     S, Q = data[0][0], int(data[1][0])
#     for i in range(Q):
#         if data[i+2][0] == '1':
#             S = S[::-1]
#         else:
#             F, C = data[i+2][1], data[i+2][2]
#             if F == '1':
#                 S = C + S
#             else:
#                 S = S + C
#     return S


def get_result(data):
    S, Q = data[0][0], int(data[1][0])
    # 文字列と反転状況を別で判断する
    ans = deque(S)
    cnt = 0
    for i in range(Q):
        if data[i+2][0] == '1':
            cnt += 1
        else:
            F, C = data[i+2][1], data[i+2][2]
            if F == '1':
                if cnt % 2 == 0:
                    # 前に追加
                    ans.appendleft(C)
                else:
                    ans.append(C)
            else:
                if cnt % 2 == 0:
                    ans.append(C)
                else:
                    ans.appendleft(C)

    ans = ''.join(ans)
    if cnt % 2 == 1:
        ans = ans[::-1]

    return ans


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(str, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
