use proconio::marker::Chars;
use std::iter::FromIterator;

use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        (h, w): (usize, usize),
        data: [Chars; h]
    }

    let mut new_data = vec![vec!['0'; w]; 2 * h];
    for i in 0..(2 * h) {
        for j in 0..w {
            new_data[i][j] = data[i / 2][j];
        }
    }

    for h_row in new_data {
        println!("{}", String::from_iter(h_row))
    }
}
