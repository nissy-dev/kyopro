use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        (a, b, c): (isize, isize, isize),
    }

    if a == b {
        print!("{}", c);
        return;
    }

    if b == c {
        print!("{}", a);
        return;
    }

    if c == a {
        print!("{}", b);
        return;
    }
}
