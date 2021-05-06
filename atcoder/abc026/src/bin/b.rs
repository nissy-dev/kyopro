use std::f32::consts::PI;

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        mut data: [[usize; 1]; n]
    }

    // 大きい順にソート
    data.sort_by(|a, b| b[0].cmp(&a[0]));

    let mut ans = 0isize;
    for (i, val) in data.iter().enumerate() {
        if i % 2 == 0 {
            ans += val[0].pow(2) as isize
        } else {
            ans -= val[0].pow(2) as isize
        }
    }

    println!("{}", ans as f32 * PI)
}
