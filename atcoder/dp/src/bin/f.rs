use proconio::{fastout, input};
use std::cmp;

#[fastout]
fn main() {
    input! {
        s: String,
        t: String,
    }

    let s_length = s.chars().count();
    let t_length = t.chars().count();

    // dp[i][j] = Sの最初のi文字と、Tの最初のj文字における最長共通部分列の長さ
    let mut dp = vec![vec![0; t_length + 1]; s_length + 1];
    for i in 0..s_length {
        for j in 0..t_length {
            if &s[i..i + 1] == &t[j..j + 1] {
                dp[i + 1][j + 1] = dp[i][j] + 1;
            } else {
                dp[i + 1][j + 1] = cmp::max(dp[i + 1][j], dp[i][j + 1])
            }
        }
    }

    let mut ans_length = dp[s_length][t_length];
    let mut s_index = s_length;
    let mut t_index = t_length;
    let mut ans = String::from("");
    // 逆から取り出す
    while ans_length > 0 {
        if &s[s_index - 1..s_index] == &t[t_index - 1..t_index] {
            ans += &s[s_index - 1..s_index];
            s_index -= 1;
            t_index -= 1;
            ans_length -= 1;
        } else if dp[s_index][t_index] == dp[s_index - 1][t_index] {
            s_index -= 1;
        } else {
            t_index -= 1
        }
    }

    // 逆からつなげたので反転させる
    println!("{}", ans.chars().rev().collect::<String>());
}
