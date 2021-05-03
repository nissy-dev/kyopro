use proconio::{fastout, input};
use std::cmp;

#[fastout]
fn main() {
    input! {
        (a, b, c): (usize, usize, usize)
    }

    let min = cmp::min(a, b);
    println!("{}", c / min);
}
