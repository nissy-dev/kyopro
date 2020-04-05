from sys import stdin
from collections import deque


def get_result(data):
    K = data[0]
    lunlun_num_q = deque([str(i+1) for i in range(9)])
    cnt = 9
    while cnt < K:
        tmp_num = lunlun_num_q.popleft()
        if tmp_num[-1] == '0':
            lunlun_num_q.extend([tmp_num + '0', tmp_num + '1'])
            cnt += 2
        elif tmp_num[-1] == '9':
            lunlun_num_q.extend([tmp_num + '8', tmp_num + '9'])
            cnt += 2
        else:
            last_digit = int(tmp_num[-1])
            lunlun_num_q.extend(
                [tmp_num + str(last_digit-1), tmp_num + str(last_digit),
                 tmp_num + str(last_digit+1)])
            cnt += 3

    return lunlun_num_q[-1+K-cnt]


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
