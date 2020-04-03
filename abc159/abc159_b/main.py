from sys import stdin


def check_palindrome(str_):
    if str_ == str_[::-1]:
        return True

    return False


def get_result(data):
    S = data[0]
    right_idx = int((len(S) - 1) / 2)
    left_idx = int((len(S) + 3) / 2) - 1
    right_S = S[0:right_idx]
    left_S = S[left_idx:]
    if check_palindrome(S) and check_palindrome(right_S) and check_palindrome(left_S):
        return 'Yes'

    return 'No'


if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)
