use proconio::{fastout, input};
use std::cmp;
#[fastout]
fn main() {
    input! {
        (n, k): (usize, usize),
        h: [isize; n]
    }

    let mut dp = vec![std::isize::MAX; n];
    dp[0] = 0;

    for i in 1..n {
        for j in 1..(k + 1) {
            if i >= j {
                dp[i] = cmp::min(dp[i], dp[i - j] + (h[i] - h[i - j]).abs());
            }
        }
    }

    println!("{}", dp[n - 1]);
}
