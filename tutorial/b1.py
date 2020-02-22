import math
import fractions
from functools import reduce
from sys import stdin

def gcd(*numbers):
    # gcd はバージョンの関係上, fractionsからimport
    return reduce(fractions.gcd, numbers)


# Shift only
def get_result(data):
    # 最大公約数が２で何回割れるか算出
    N, A = data[0], data[1]
    out = gcd(*A)
    ans = math.ceil(math.log2(out))
    return ans

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
