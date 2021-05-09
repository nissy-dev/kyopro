from sys import stdin


def get_result(data):
    # N = int(data[0][0])
    S = data[1][0]
    r_index = [i for i in range(len(S)) if S[i] == "R"]
    g_index = [i for i in range(len(S)) if S[i] == "G"]
    b_index = set([i for i in range(len(S)) if S[i] == "B"])
    all_case = len(r_index) * len(g_index) * len(b_index)
    invalid_case = 0
    for i in r_index:
        for j in g_index:
            s_i, s_j = sorted([i, j])
            tmp_max_b = s_j + (s_j - s_i)
            if tmp_max_b in b_index:
                invalid_case += 1
            tmp_min_b = s_i - (s_j - s_i)
            if tmp_min_b in b_index:
                invalid_case += 1
            tmp_mid_b = (s_i + s_j) / 2
            if tmp_mid_b in b_index:
                invalid_case += 1
    return all_case - invalid_case


if __name__ == "__main__":
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(str, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
