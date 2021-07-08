use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        (n, m): (usize, usize),
        mut data: [[usize; 2]; n]
    }

    data.sort_by(|a, b| a[0].cmp(&b[0]));
    let mut ans = 0;
    let mut cnt = 0;
    for val in data {
        if m > cnt + val[1] {
            ans += val[0] * val[1]
        } else {
            ans += val[0] * (m - cnt);
            break;
        }
        cnt += val[1];
    }

    println!("{}", ans)
}
