from sys import stdin


# Kagami Mochi
def get_result(data):
    _, d = data[0][0], data[1:]
    # flatten
    d = sum(d, [])
    return len(set(d))


if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
