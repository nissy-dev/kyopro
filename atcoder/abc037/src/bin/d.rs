use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        (h, w): (usize, usize),
        data: [[usize; w]; h]
    }

    // セルの保存
    let mut cell: Vec<(usize, usize, usize)> = Vec::new();
    for i in 0..h {
        for j in 0..w {
            cell.push((data[i][j], i, j));
        }
    }
    // 値が大きい順にソート
    cell.sort_by(|a, b| a.0.cmp(&b.0));

    // DPでやるときは更新の順序が大事、更新が終わってないといけない
    // dp[i][j] = i 行 j 列からスタートする経路の総数
    // 値が大きいセルほど、進める経路は少ないから更新は早く終了する
    let mut dp = vec![vec![1; w]; h];
    let dxy: Vec<(isize, isize)> = vec![(0, 1), (1, 0), (0, -1), (-1, 0)];
    let ans_mod = 10i32.pow(9) + 7;
    while cell.len() > 0 {
        let (_, i, j) = cell.pop().unwrap();
        for (k, l) in dxy.iter().cloned() {
            let nxt_i = (i as isize) + k;
            let nxt_j = (j as isize) + l;
            if 0 <= nxt_i && nxt_i < (h as isize) && 0 <= nxt_j && nxt_j < (w as isize) {
                if data[i][j] < data[nxt_i as usize][nxt_j as usize] {
                    dp[i][j] = (dp[i][j] + dp[nxt_i as usize][nxt_j as usize]) % ans_mod;
                }
            }
        }
    }

    let mut ans = 0;
    for i in 0..h {
        for j in 0..w {
            ans = (ans + dp[i][j]) % ans_mod
        }
    }
    println!("{}", ans)
}
