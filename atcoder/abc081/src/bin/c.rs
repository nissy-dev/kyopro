use std::collections::HashMap;

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (n, k): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        data: [usize; n],
        // data: [[usize; m]; n]
    }

    let mut counter: HashMap<usize, usize> = HashMap::new();
    for i in 0..n {
        let val = counter.entry(data[i]).or_insert(0);
        *val += 1;
    }

    // カウント数でソート
    let mut counter_vec: Vec<_> = counter.into_iter().collect();
    counter_vec.sort_by(|x, y| x.1.cmp(&y.1));

    let mut ans = 0;
    let unique_num_cnt = counter_vec.len();
    for (i, (_, val)) in counter_vec.iter().enumerate() {
        if k + i < unique_num_cnt {
            ans += val
        }
    }
    println!("{}", ans);
}
