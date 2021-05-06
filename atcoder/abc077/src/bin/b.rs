use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        n: u64, // usizeでもダメな時がある...
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    // 累乗やルートは浮動小数点の問題が起きるからなるべく整数で処理すべき
    // println!("{}", n.powf(0.5).round().powi(2))

    let mut ans = 0;
    // ..=n は .. (n+1) と同じ
    for i in 0..(n + 1) {
        if i * i > n {
            break;
        }
        ans = i * i;
    }
    println!("{}", ans);
}
