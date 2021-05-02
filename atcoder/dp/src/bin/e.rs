use proconio::{fastout, input};
use std::cmp;

// この問題はwが非常に大きくなるので、dとは同じ感じで解けない
//「～となる〇〇の最大値」を値に持つDPは、適当な添字と入れ替えて「～となる××の最小値」というDPにできることが多い
#[fastout]
fn main() {
    input! {
        (n, w): (usize, usize),
        data: [[usize; 2]; n]
    }

    let max_value = 100000;
    let max_weight = ((10 as i32).pow(9) + 1) as usize;
    // dp[i][j]= 最初のi個の品物{0,1,...,i－1}までの中から価値がjになるように選んだときの，価値の総和の最大値
    let mut dp = vec![vec![max_weight; max_value + 1]; n + 1];
    dp[0][0] = 0;

    for i in 0..n {
        for j in 0..(max_value + 1) {
            if j >= data[i][1] {
                // i番目の品物を選べる時
                dp[i + 1][j] = cmp::min(dp[i][j], dp[i][j - data[i][1]] + data[i][0])
            } else {
                // i番目の品物を選べない時
                dp[i + 1][j] = dp[i][j]
            }
        }
    }

    let mut ans = max_value;
    while dp[n][ans] > w {
        ans -= 1;
    }
    println!("{}", ans);
}
