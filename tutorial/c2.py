import re
from sys import stdin


# 白昼夢
def get_result(data):
    S = data[0]
    pattern = r'^(dream|dreamer|erase|eraser)+$'
    result = re.match(pattern, S)
    return 'YES' if result else 'NO'


# 白昼夢
def get_result(data):  # noqa
    S = data[0]
    # 順番が大事
    words = ['eraser', 'erase', 'dreamer', 'dream']
    for val in words:
        S = S.replace(val, '')
    return 'YES' if len(S) == 0 else 'NO'


if __name__ == '__main__':
    data = list(map(str, stdin.readline().rstrip('\n').split(' ')))
    result = get_result(data)
    print(result)
