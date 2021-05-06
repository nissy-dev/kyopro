use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        s: String,
        // n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    println!(
        "{:?}",
        s.chars()
            .fold(0, |acc, x| acc + x.to_string().parse::<u32>().unwrap())
    )
}
