use proconio::{fastout, input};
use std::cmp;

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        data: [isize; n],
        // data: [[usize; m]; n]
    }

    // dp[i][j] = 数列の一部 {a_i, a_i+1, ...., a_j-1 } が始まった時の 自分 - 相手 の最大値
    // 部分問題に帰着させることを忘れない
    // 数列が 短い → 長い で埋めていく
    let mut dp = vec![vec![0; n + 1]; n + 1];
    for len in 1..(n + 1) {
        for start in 0..(n - len + 1) {
            let end = start + len;
            dp[start][end] = cmp::max(
                data[start] - dp[start + 1][end],
                data[end - 1] - dp[start][end - 1],
            );
        }
    }
    println!("{}", dp[0][n]);
}
