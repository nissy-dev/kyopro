use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (n, k): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        mut data: [[usize; 2]; n]
    }

    data.sort_by(|a, b| a[0].cmp(&b[0]));
    let mut tmp = 0;
    for val in data {
        if tmp + val[1] >= k {
            println!("{}", val[0]);
            break;
        }
        tmp += val[1]
    }
}
