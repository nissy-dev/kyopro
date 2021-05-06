use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (h, w): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[char; w]; h]
    }
    let mut data = vec![vec![]; h];
    for i in 0..h {
        input! {
            s: String
        }
        data[i] = s.chars().collect()
    }

    // dp[i][j] = (i,j)までの経路の数
    let mut dp = vec![vec![0; w]; h];
    dp[0][0] = 1;
    let ans_mod = 10i32.pow(9) + 7;
    for i in 0..h {
        for j in 0..w {
            if i + 1 < h && data[i + 1][j] == '.' {
                dp[i + 1][j] = (dp[i + 1][j] + dp[i][j]) % ans_mod;
            }

            if j + 1 < w && data[i][j + 1] == '.' {
                dp[i][j + 1] = (dp[i][j + 1] + dp[i][j]) % ans_mod;
            }
        }
    }

    println!("{}", dp[h - 1][w - 1]);
}
