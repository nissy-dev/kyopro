use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        // (n, m): (usize, usize),
        (r, c, k): (usize, usize, usize),
        n: usize,
        // data: [usize; n],
        data: [[usize; 2]; n]
    }

    let mut row_sum = vec![0; r];
    let mut col_sum = vec![0; c];
    for pos in data.iter() {
        row_sum[pos[0] - 1] += 1;
        col_sum[pos[1] - 1] += 1;
    }

    let mut cnt_row_sum = vec![0; k + 1];
    let mut cnt_col_sum = vec![0; k + 1];
    for &row_cnt in row_sum.iter() {
        if row_cnt <= k {
            cnt_row_sum[row_cnt] += 1;
        }
    }
    for &col_cnt in col_sum.iter() {
        if col_cnt <= k {
            cnt_col_sum[col_cnt] += 1;
        }
    }
    let mut cnt = 0i64; // i32だとオーバーフローもあるので注意...
    for i in 0..k + 1 {
        cnt += cnt_row_sum[i] * cnt_col_sum[k - i];
    }

    // 以下がTLEの原因
    // for i in 0..r {
    //     for j in 0..c {
    //         if row_sum[i] + col_sum[j] == k {
    //             cnt += 1;
    //         }
    //     }
    // }

    // あめが置かれているところは別条件で探索
    for pos in data.iter() {
        if row_sum[pos[0] - 1] + col_sum[pos[1] - 1] == (k + 1) {
            cnt += 1;
        }
        if row_sum[pos[0] - 1] + col_sum[pos[1] - 1] == k {
            cnt -= 1;
        }
    }
    println!("{}", cnt)
}
