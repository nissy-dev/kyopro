import numpy as np
from sys import stdin

# not AC
def get_result(data):
    N, K = data[0]
    A = data[1]
    output_lens = int(N * (N-1) / 2)
    output = np.zeros(output_lens)
    idx = 0
    for i in range(N):
        for j in range(i+1, N):
            output[idx] = A[i] * A[j]
            idx += 1
    output = sorted(output)
    return output[K-1]

if __name__ == '__main__':
    raw_data = [val.rstrip('\n') for val in stdin.readlines()]
    data = [list(map(int, val.split(' '))) for val in raw_data]
    result = get_result(data)
    print(result)
