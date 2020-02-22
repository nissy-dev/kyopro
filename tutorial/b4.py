from sys import stdin


# Card Game for Two
def get_result(data):
    N, A = data[0][0], data[1]
    A = sorted(A, reverse=True)
    ans = sum(A[0::2]) - sum(A[1::2])
    return ans

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)

