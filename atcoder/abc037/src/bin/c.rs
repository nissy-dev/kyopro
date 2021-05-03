use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        (n, k): (usize, usize),
        a: [usize; n],
    }

    // 累積和の計算
    let mut cumsum = vec![0; n + 1];
    for i in 0..n {
        cumsum[i + 1] = cumsum[i] + a[i];
    }

    let mut ans = 0;
    for i in 0..(n - k + 1) {
        ans += cumsum[i + k] - cumsum[i];
    }
    println!("{}", ans)
}
