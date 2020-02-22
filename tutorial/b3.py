from sys import stdin

# Some Sums
def get_result(data):
    N, A, B = data
    tmp = [sum(list(map(int, str(i)))) for i in range(1, N+1)]
    tmp = [i + 1 for i in range(len(tmp)) if tmp[i] >= A and tmp [i] <= B]
    return sum(tmp)

if __name__ == '__main__':
    data = list(map(int, stdin.readline().split(' ')))
    result = get_result(data)
    print(result)
