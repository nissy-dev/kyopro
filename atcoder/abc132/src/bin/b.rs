use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        data: [usize; n],
        // data: [[usize; m]; n]
    }

    let mut ans = 0;
    for i in 0..n - 2 {
        if (data[i] < data[i + 1] && data[i + 1] < data[i + 2])
            || (data[i] > data[i + 1] && data[i + 1] > data[i + 2])
        {
            ans += 1;
        }
    }

    println!("{}", ans);
}
