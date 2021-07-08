use proconio::{fastout, input};
// use proconio::marker::Chars;

#[fastout]
fn main() {
    input! {
        (n, m, c): (usize, usize, isize),
        B: [isize; m],
        A: [[isize; m]; n]
    }

    let mut ans = 0;
    for i in 0..n {
        let mut sum = c;
        for j in 0..m {
            sum += A[i][j] * B[j]
        }

        if sum > 0 {
            ans += 1
        }
    }
    println!("{}", ans);
}
