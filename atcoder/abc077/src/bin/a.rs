use proconio::marker::Chars;
use proconio::{fastout, input};
#[fastout]
fn main() {
    input! {
        c1: Chars,
        c2: Chars,
        // n: usize,
        // (n, m): (usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    if c1[0] == c2[2] && c1[1] == c2[1] && c1[2] == c2[0] {
        println!("YES")
    } else {
        println!("NO")
    }
}
