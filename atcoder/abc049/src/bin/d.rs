use std::collections::HashMap;

use proconio::{fastout, input};
// use proconio::marker::Chars;

pub struct UnionFind {
    par: Vec<usize>,
    siz: Vec<usize>,
}

impl UnionFind {
    fn new(n: usize) -> Self {
        Self {
            par: (0..n).collect(),
            siz: vec![1; n],
        }
    }

    fn root(&mut self, x: usize) -> usize {
        if self.par[x] == x {
            return x;
        }

        self.par[x] = self.root(self.par[x]);
        return self.par[x];
    }

    fn issame(&mut self, x: usize, y: usize) -> bool {
        return self.root(x) == self.root(y);
    }

    fn unite(&mut self, x: usize, y: usize) -> bool {
        let mut x = self.root(x);
        let mut y = self.root(y);

        if x == y {
            return false;
        }

        if self.siz[x] < self.siz[y] {
            std::mem::swap(&mut x, &mut y);
        }

        self.par[y] = x;
        self.siz[x] += self.siz[y];
        return true;
    }

    fn size(&mut self, x: usize) -> usize {
        let root = self.root(x);
        return self.siz[root];
    }
}

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (n, k, l): (usize, usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        road_edges: [[usize; 2]; k],
        train_edges: [[usize; 2]; l]
    }

    let mut road_uf = UnionFind::new(n);
    for i in 0..k {
        road_uf.unite(road_edges[i][0] - 1, road_edges[i][1] - 1);
    }
    let mut train_uf = UnionFind::new(n);
    for i in 0..l {
        train_uf.unite(train_edges[i][0] - 1, train_edges[i][1] - 1);
    }

    // 普通に数えると O(N^2) で間に合わないので工夫する
    // 各頂点の根を求めて、根のペアが同じ頂点をカウントする
    let mut counter = HashMap::new();
    for i in 0..n {
        let value = counter
            .entry((road_uf.root(i), train_uf.root(i)))
            .or_insert(0);
        *value += 1;
    }

    for i in 0..n {
        let value = counter
            .entry((road_uf.root(i), train_uf.root(i)))
            .or_insert(0);
        println!("{}", value);
    }
}
