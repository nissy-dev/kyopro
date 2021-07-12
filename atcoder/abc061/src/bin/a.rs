use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        // (n, m): (usize, usize),
        (a, b, c): (isize, isize, isize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    if c >= a && c <= b {
        println!("Yes")
    } else {
        println!("No")
    }
}
