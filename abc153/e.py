# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from sys import stdin


## This code doesn't pass the test
def get_result(data):
    H, N = data[0]
    A_and_B = np.array(data[1:])
    calc_efficient = np.array(list(map(lambda x: float(x[0] / x[1]), A_and_B)))
    sorted_index = np.argsort(-calc_efficient)

    cost = 0
    remainder_H = H
    for i in sorted_index:
        A, B = A_and_B[i]
        quotient = remainder_H // A
        if quotient > 0:
            cost += B * quotient
            remainder_H = remainder_H - A * quotient
        else:
            if remainder_H > 0:
                continue
            else:
                break

    return cost

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
