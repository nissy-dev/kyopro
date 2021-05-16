use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        data: [f64; n],
        // data: [[usize; m]; n]
    }

    // 解法
    // dp[i][j] = 最初の i 枚のコインを投げたときに、表が j 枚となる確率
    let mut dp = vec![vec![0.0; n + 1]; n + 1];
    dp[0][0] = 1.0;
    for i in 0..n {
        for j in 0..(i + 1) {
            // i+1枚目が表だった場合
            dp[i + 1][j + 1] += dp[i][j] * data[i];
            // i+1枚目が裏だった場合
            dp[i + 1][j] += dp[i][j] * (1.0 - data[i]);
        }
    }

    let mut ans = 0.0;
    for j in (n / 2 + 1)..(n + 1) {
        ans += dp[n][j];
    }
    println!("{}", ans);
}
