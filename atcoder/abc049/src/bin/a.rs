use proconio::{fastout, input};
// use proconio::marker::Chars;

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

    let vowels = vec![
        String::from("a"),
        String::from("e"),
        String::from("i"),
        String::from("u"),
        String::from("o"),
    ];

    if vowels.contains(&s) == true {
        println!("vowel")
    } else {
        println!("consonant")
    }
}
