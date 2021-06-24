use proconio::marker::Chars;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: Chars,
        // n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    let mut stack: Vec<char> = Vec::new();
    let mut cnt = 0;
    for curr_char in s {
        let prev_char_option = stack.pop();
        if let Some(prev_char) = prev_char_option {
            if prev_char == curr_char {
                stack.push(prev_char);
                stack.push(curr_char);
            } else {
                cnt += 2;
            }
        } else {
            stack.push(curr_char);
        }
    }

    println!("{}", cnt)
}
