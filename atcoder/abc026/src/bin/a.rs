use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    println!("{}", (n / 2).pow(2));
}
