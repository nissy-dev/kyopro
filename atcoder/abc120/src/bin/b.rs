use std::cmp::min;

use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        // (n, m): (usize, usize),
        (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    let mut divisor: Vec<usize> = vec![];
    for i in 0..min(a, b) {
        if (a % (i + 1) == 0) & (b % (i + 1) == 0) {
            divisor.push(i + 1);
        }
    }

    divisor.sort_by(|a, b| b.cmp(a));
    println!("{}", divisor[c - 1]);
}
