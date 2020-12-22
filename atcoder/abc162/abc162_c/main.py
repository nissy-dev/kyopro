import math
from sys import stdin


def get_result(data):
    K = data[0]
    ans_list = []
    for i in range(K):
        for j in range(K):
            for k in range(K):
                ans = math.gcd(i+1, j+1)
                ans = math.gcd(ans, k+1)
                ans_list.append(ans)
    return sum(ans_list)


if __name__ == '__main__':
    data = list(map(int, stdin.readline().rstrip().split(' ')))
    result = get_result(data)
    print(result)
