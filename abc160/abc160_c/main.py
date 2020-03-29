from sys import stdin

def get_result(data):
    K, N = data[0]
    A = data[1]
    tmp = A[0]
    inter_dist = []
    for i in range(1, len(A)):
        inter_dist.append(A[i]-tmp)
        tmp = A[i]
    inter_dist += [K-A[-1]+A[0]]
    ans = sum(inter_dist) - max(inter_dist)
    return ans


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)