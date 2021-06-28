use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        mut s: String,
        // n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    let mut prev_len = 0;
    while prev_len != s.len() {
        prev_len = s.len();
        for suffix in ["dream", "dreamer", "erase", "eraser"].iter() {
            if s.ends_with(suffix) {
                s = String::from(&s[0..s.len() - suffix.len()]);
                break;
            }
        }
    }

    if s.len() == 0 {
        println!("YES")
    } else {
        println!("NO")
    }
}
