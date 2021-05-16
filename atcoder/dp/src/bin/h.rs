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
    // 全てのセルを１回全走査していくので幅優先ではない...
    // そもそも更新元の値が定まっていることが一番重要
    // → 今回は普通にループすれば更新元は必ず定まっているようになっている
    //   上か左からの遷移しかありえないため
    //   幅優先だと以下の更新式では同じノードを何度も更新してしまうためおかしくなっている
    //   そもそも問題が最大・最小ではないので...純粋な数え上げをするしかない
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
