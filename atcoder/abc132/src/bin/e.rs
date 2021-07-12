use proconio::{fastout, input};
use std::collections::VecDeque;
// use proconio::marker::Chars;

pub struct BFS {
    num_nodes: usize,
    adj_list: Vec<Vec<usize>>,
    dist: Vec<Vec<isize>>,
}

impl BFS {
    fn new(n: usize) -> Self {
        Self {
            num_nodes: n,
            adj_list: vec![vec![]; n],
            dist: vec![vec![-1; 3]; n],
        }
    }

    fn add_edge(&mut self, start: usize, end: usize) {
        self.adj_list[start].push(end);
    }

    fn search(&mut self, start: usize, end: usize) {
        self.dist[start][0] = 0;
        let mut queue: VecDeque<(usize, usize)> = VecDeque::new();
        queue.push_back((start, 0));
        while queue.len() > 0 {
            let (curr, path_cnt) = queue.pop_front().unwrap();
            for &dest in self.adj_list[curr].iter() {
                let next_path_cnt = (path_cnt + 1) % 3;
                if self.dist[dest][next_path_cnt] == -1 {
                    self.dist[dest][next_path_cnt] = self.dist[curr][path_cnt] + 1;
                    queue.push_back((dest, next_path_cnt))
                }
            }
        }

        if self.dist[end][0] == -1 {
            println!("-1");
        } else {
            println!("{}", self.dist[end][0] / 3);
        }
    }
}

#[fastout]
fn main() {
    input! {
        (n, m): (usize, usize),
        data: [[usize; 2]; m],
        (s, t): (usize, usize),
    }

    let mut bfs = BFS::new(n);
    for val in data {
        bfs.add_edge(val[0] - 1, val[1] - 1);
    }

    bfs.search(s - 1, t - 1);
}
