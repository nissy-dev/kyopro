#!/usr/bin/env python3
from sys import stdin
import collections

def solve(data):
    S = data[0]
    counter = collections.Counter(S)
    if counter['o'] > 4:
        print(0)
        return

    ans = 0
    for i in range(10000):
        password = str(i)
        if len(password) < 4:
            password = '0' * (4 - len(password)) + password

        flag = True
        for i, cond in enumerate(S):
            if cond == 'o' and str(i) not in password:
                flag = False
                break
            if cond == 'x' and str(i) in password:
                flag = False
                break
        if flag:
            ans += 1
    print(ans)






if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    # raw_data = [val.rstrip() for val in stdin.readlines()]
    # data = [list(map(int, val.split(' '))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
