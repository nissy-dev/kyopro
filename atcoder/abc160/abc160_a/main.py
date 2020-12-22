from sys import stdin


def get_result(data):
    S = data[0]
    if S[2] == S[3] and S[4] == S[5]:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)
