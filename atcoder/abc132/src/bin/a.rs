use std::collections::HashSet;

use proconio::marker::Chars;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        s: Chars
        // n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    let mut set = HashSet::new();
    for c in s {
        set.insert(c);
    }

    if set.len() == 2 {
        println!("Yes")
    } else {
        println!("No")
    }
}
