use proconio::{fastout, input};
// use proconio::marker::Chars;

pub struct BellmanFord {
    num_nodes: usize,
    adj_list: Vec<Vec<(usize, isize)>>,
    dist: Vec<isize>,
}

impl BellmanFord {
    fn new(n: usize) -> Self {
        Self {
            num_nodes: n,
            adj_list: vec![vec![]; n],
            dist: vec![std::isize::MAX; n],
        }
    }

    // fn add_edge(&mut self, start: usize, end: usize, weight: isize) {
    //     self.adj_list[start].push((end, weight));
    // }

    // fn search(&mut self, start: usize, data: Vec<(usize, usize, isize)>) {
    //     let mut cnt = 0;
    //     self.dist[start] = 0;
    //     while cnt < self.num_nodes {
    //         let mut end_flag = true;
    //         for src in 0..self.num_nodes {
    //             let curr = self.dist[src];
    //             for &(dest, cost) in self.adj_list[src].iter() {
    //                 if curr != std::isize::MAX && self.dist[dest] > curr + cost {
    //                     self.dist[dest] = curr + cost;
    //                     end_flag = false;
    //                 }
    //             }
    //         }

    //         if end_flag {
    //             break;
    //         }

    //         cnt += 1;
    //     }
    // }

    fn ans(&mut self, start: usize, data: Vec<(usize, usize, isize)>) {
        self.dist[start] = 0;
        for _ in 0..self.num_nodes {
            for &(a, b, c) in data.iter() {
                if self.dist[a - 1] == std::isize::MAX {
                    continue;
                }

                if self.dist[b - 1] > self.dist[a - 1] - c {
                    self.dist[b - 1] = self.dist[a - 1] - c;
                }
            }
        }

        let ans = self.dist[self.num_nodes - 1];

        // コーナーケース用の処理
        // 頂点 1 から到達できる負閉路であっても、その閉路から頂点 N へと至ることができない場合
        // → 検出されるけど無視しなければならない
        let mut neg_flag = vec![false; self.num_nodes];
        for i in 0..self.num_nodes {
            for &(a, b, c) in data.iter() {
                if self.dist[a - 1] == std::isize::MAX {
                    continue;
                }

                if self.dist[b - 1] > self.dist[a - 1] - c {
                    self.dist[b - 1] = self.dist[a - 1] - c;
                    neg_flag[b - 1] = true;
                }

                if neg_flag[a - 1] {
                    neg_flag[b - 1] = true
                }
            }
        }

        if neg_flag[self.num_nodes - 1] {
            println!("inf");
        } else {
            println!("{}", -ans);
        }
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
        data: [(usize, usize, isize); m]
    }

    let mut bellman_ford = BellmanFord::new(n);
    bellman_ford.ans(0, data);
}
