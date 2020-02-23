from sys import stdin


# Otoshidama
def get_result(data):
    N, Y = data
    # これも総当たり
    ans = '-1 -1 -1'
    for i in range(N+1):
        for j in range(N+1-i):
            k = N - i - j
            tmp = 10000 * i + 5000 * j + 1000 * k
            if tmp == Y:
                ans = '{} {} {}'.format(i, j, k)
                break
    return ans

if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)

