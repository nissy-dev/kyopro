use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (H, W): (usize, usize),
        (h, w): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    println!("{}", (H - h) * (W - w));
}
