use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        data: [[usize; 2]; n]
    }

    // 二分探索で実装
    let mut left = 0usize;
    let mut right = std::usize::MAX;
    while right - left > 1 {
        let mid = (left + right) / 2;

        let mut flag = true;
        let mut limit_time = vec![0; n];
        for i in 0..n {
            if mid < data[i][0] {
                flag = false
            } else {
                limit_time[i] = (mid - data[i][0]) / data[i][1]
            }
        }

        // 時間が切迫している順にソート
        limit_time.sort();
        // 1つずつ割っていて間にあうのか確認
        for i in 0..n {
            if limit_time[i] < i {
                flag = false
            }
        }

        if flag {
            right = mid
        } else {
            left = mid
        }
    }

    println!("{}", right)
}
