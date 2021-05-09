from sys import stdin


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]  # 親
        self.rank = [1] * n  # 木の高さ
        self.size = [1] * n  # size[i] は i を根とするグループのサイズ

    def find(self, x):  # x の根を返す
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])  # 経路圧縮
            return self.parent[x]

    def unite(self, x, y):  # x, y の属する集合を併合する
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.size[y] += self.size[x]
            else:
                self.parent[y] = x
                self.size[x] += self.size[y]
                if self.rank[x] == self.rank[y]:
                    self.rank[x] += 1

    def is_same(self, x, y):  # x, y が同じ集合に属するか判定する
        return self.find(x) == self.find(y)

    def group_size(self, x):  # x が属する集合の大きさを返す
        return self.size[self.find(x)]

    def group_members(self, x):  # x が属する集合の要素を返す
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):  # すべての根をリストで返す
        return [i for i, x in enumerate(self.parent) if i == x]

    def group_count(self):  # 木の数を返す
        return len(self.roots())

    def all_group_members(self):  # すべての木の要素を辞書で返す
        return {r: self.group_members(r) for r in self.roots()}

    def __str__(self):  # print 表示用
        return "\n".join(
            "{}: {}".format(r, self.group_members(r)) for r in self.roots()
        )


def get_result(data):
    N, M, K = data[0]
    A, B = [0] * M, [0] * M
    C, D = [0] * K, [0] * K
    direct = [[] for _ in range(N)]  # 同じ集合の友達もしくはブロック関係の人
    uf = UnionFind(N)

    for i in range(M):
        A[i], B[i] = data[1 + i]
        # 入力時に 0-index に合わせる
        A[i] -= 1
        B[i] -= 1
        direct[A[i]].append(B[i])
        direct[B[i]].append(A[i])
        uf.unite(A[i], B[i])

    for i in range(K):
        C[i], D[i] = data[1 + M + i]
        # 入力時に 0-index に合わせる
        C[i] -= 1
        D[i] -= 1
        if uf.is_same(C[i], D[i]):
            direct[C[i]].append(D[i])
            direct[D[i]].append(C[i])

    ans = [0] * N
    for i in range(N):
        ans[i] = uf.group_size(i) - len(direct[i]) - 1
    return " ".join(list(map(str, ans)))


if __name__ == "__main__":
    raw_data = [val.rstrip("\n") for val in stdin.readlines()]
    data = [list(map(int, val.split(" "))) for val in raw_data]
    result = get_result(data)
    print(result)
