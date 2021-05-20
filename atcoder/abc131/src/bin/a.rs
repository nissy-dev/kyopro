use proconio::marker::Chars;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: Chars,
        // n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    for i in 0..3 {
        if s[i] == s[i + 1] {
            println!("Bad");
            return;
        }
    }

    println!("Good");
}
