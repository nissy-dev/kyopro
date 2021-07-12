use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        data: [[usize; 2]; m]
    }

    let mut adj_list = vec![0; n];
    for edge in data {
        adj_list[edge[0] - 1] += 1;
        adj_list[edge[1] - 1] += 1;
    }

    for val in adj_list {
        println!("{}", val)
    }
}
