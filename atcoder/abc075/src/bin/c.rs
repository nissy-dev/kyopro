use std::usize;

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
        (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        edges: [[usize; 2]; m]
    }

    let mut ans = 0;
    for i in 0..m {
        let mut uf = UnionFind::new(n);
        for (j, edge) in edges.iter().enumerate() {
            if i != j {
                uf.unite(edge[0] - 1, edge[1] - 1);
            }
        }

        let mut cnt = 0;
        for k in 0..n {
            if uf.root(k) == k {
                cnt += 1
            }
        }

        if cnt > 1 {
            ans += 1
        }
    }

    println!("{}", ans);
}
