from sys import stdin


# Traveling
def get_result(data):
    N, T = data[0][0], data[1:]
    # init
    t, x, y = 0, 0, 0
    for i in range(N):
        ti, tx, ty = T[i]
        interval = ti - t
        distance = abs(tx - x) + abs(ty - y)
        if interval < distance or (interval % 2) != (distance % 2):
            return 'No'
        # update
        t, x, y = ti, tx, ty
    return 'Yes'

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)

