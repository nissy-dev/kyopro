use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        mut data: [[usize; 2]; n]
    }
    // 締め切りでソート
    data.sort_by(|a, b| a[1].cmp(&b[1]));

    let mut now = 0;
    for val in data.iter() {
        now += val[0];
        if now > val[1] {
            println!("No");
            return;
        }
    }

    println!("Yes");
}
