from sys import stdin


def get_result(data):
    N, K = data[0]
    A = data[1]
    trans_num = [0] * N
    curr_pos = 1
    arrival_pos = set()
    for i in range(N):
        trans_num[curr_pos - 1] = i
        arrival_pos.add(curr_pos)

        # see next
        next_pos = A[curr_pos - 1]
        if next_pos in arrival_pos:
            loop_start = trans_num[next_pos - 1]
            loop_trans_num = i + 1 - loop_start
            break

        # update
        curr_pos = next_pos

    # K が loop 開始より小さい可能性を忘れていた
    loop = K if (K - loop_start) < 0 else loop_start + (K - loop_start) % loop_trans_num
    curr_pos = 1
    for _ in range(loop):
        next_pos = A[curr_pos - 1]
        curr_pos = next_pos
    return next_pos


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
