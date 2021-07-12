use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        mut data: [usize; n],
        // data: [[usize; m]; n]
    }

    data.sort_by(|a, b| a.cmp(b));
    println!("{}", data[n / 2] - data[n / 2 - 1]);
}
