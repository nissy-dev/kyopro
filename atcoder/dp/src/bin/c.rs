use proconio::{fastout, input};
use std::cmp;
#[fastout]
fn main() {
    input! {
        n: usize,
        h: [[usize; 3]; n]
    }

    let mut dp = vec![vec![0; 3]; n];
    dp[0] = h.get(0).unwrap().clone();

    for i in 1..n {
        dp[i][0] = cmp::max(dp[i - 1][1] + h[i][0], dp[i - 1][2] + h[i][0]);
        dp[i][1] = cmp::max(dp[i - 1][0] + h[i][1], dp[i - 1][2] + h[i][1]);
        dp[i][2] = cmp::max(dp[i - 1][0] + h[i][2], dp[i - 1][1] + h[i][2]);
    }

    println!("{}", dp[n - 1].iter().max().unwrap());
}
