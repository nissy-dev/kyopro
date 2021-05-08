#!/usr/bin/env python3
from sys import stdin


def solve(data):
    N = data[0][0]
    A = data[1]

    # 鳩の巣原理
    # 余りは200通りしかないので、実は全部数えあげる必要はない
    # 適当に少なくとも201個を数えれば、解は必ず1つは見つかる

    # 数列のうち先頭の min(N, 8)要素を取り出して、その中で数列の候補をbit全探索する
    n = min([N, 8])
    remainder_all = [None for _ in range(200)]
    # 1 << a : a桁の２進数、a=4なら1000(2進数)を表す
    for bit in range(1 << n):
        id_seq = []
        remainder = 0
        for i in range(n):
            # 2進数表記で共通部分だけを取り出す
            if bit & (1 << i):
                id_seq.append(i + 1)
                remainder = (remainder + A[i]) % 200

        if remainder_all[remainder] is not None:
            print("Yes")
            prev_id_seq = remainder_all[remainder]
            for idx in [prev_id_seq, id_seq]:
                line = str(len(idx))
                for val in sorted(idx):
                    line += " " + str(val)
                print(line)
            return
        else:
            remainder_all[remainder] = id_seq

    print("No")


if __name__ == "__main__":
    # 1行
    # data = list(map(int, stdin.readline().rstrip().split(" ")))
    # data = list(map(str, stdin.readline().rstrip().split(" ")))
    # 複数行
    raw_data = [val.rstrip() for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    # data = [list(map(str, val.split(' '))) for val in raw_data]
    solve(data)
