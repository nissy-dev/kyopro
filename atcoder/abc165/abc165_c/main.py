from sys import stdin
from itertools import combinations_with_replacement


def get_result(data):
    N, M, Q = data[0]
    cond = data[1:]
    seq = [i + 1 for i in range(M)]
    all_seq = combinations_with_replacement(seq, N)
    scores = []
    for seq in all_seq:
        score = 0
        for c in cond:
            if (seq[c[1] - 1] - seq[c[0] - 1]) == c[2]:
                score += c[3]
        scores.append(score)
    return max(scores)


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
