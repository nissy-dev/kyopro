import math
from sys import stdin


def get_result(data):
    A, B, H, M = data
    h_deg = (H + M / 60.0) * 30.0
    m_deg = M * 6.0
    theta = math.radians(abs(m_deg - h_deg))
    ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta))
    return ans


if __name__ == "__main__":
    data = list(map(int, stdin.readline().rstrip().split(" ")))
    result = get_result(data)
    print(result)
