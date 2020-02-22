from sys import stdin

# Coins
def get_result(data):
    # ただの全探索
    A, B, C, X = data[0][0], data[1][0], data[2][0], data[3][0]
    count = 0
    for a in range(0, A+1):
        for b in range(0, B+1):
            for c in range(0, C+1):
                money = 500 * a + 100 * b + 50 * c
                if money == X:
                    count += 1
    return count

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
