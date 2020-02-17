import collections
from sys import stdin


def get_result(data):
    N, S = data[0], data[1:]
    c = collections.Counter(S)
    max_count = max(c.values())
    output_s = [key for key, val in c.items() if val == max_count]
    output_s = sorted(output_s)
    return '\n'.join(output_s)

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [val for val in raw_data]
    result = get_result(data)
    print(result)
