use proconio::{fastout, input};
use std::cmp;

#[fastout]
fn main() {
    input! {
        (n, w): (usize, usize),
        data: [[usize; 2]; n]
    }

    // dp[i][j]= 最初のi個の品物{0,1,...,i－1}までの中から重さがjになるように選んだときの，価値の総和の最大値
    let mut dp = vec![vec![0; w + 1]; n + 1];

    for i in 0..n {
        for j in 0..(w + 1) {
            if j >= data[i][0] {
                // i番目の品物を選べる時
                // 選ばない場合と比較して、大きい方で更新
                dp[i + 1][j] = cmp::max(dp[i][j], dp[i][j - data[i][0]] + data[i][1])
            } else {
                // i番目の品物を選べない時
                dp[i + 1][j] = dp[i][j]
            }
        }
    }

    println!("{}", dp[n][w])
}
