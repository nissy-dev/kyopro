use proconio::{fastout, input};
// use proconio::marker::Chars;
use num::integer::lcm;

fn count(start: usize, end: usize, div: usize) -> usize {
    let mut cnt = end / div - start / div;
    if start % div == 0 {
        cnt += 1
    }
    return cnt;
}
#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        // (n, m): (usize, usize),
        (a, b, c, d): (usize, usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }
    let lcm = lcm(c, d);
    let ans = (b - a + 1) - count(a, b, c) - count(a, b, d) + count(a, b, lcm);
    println!("{}", ans);
}
