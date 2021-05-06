use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        s: String,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    let mut accessories = String::from("b");
    let mut cnt = 0;
    while accessories.len() <= n {
        for (start, end) in [("a", "c"), ("c", "a"), ("b", "b")].iter().cloned() {
            if accessories == s {
                println!("{}", cnt);
                return;
            }
            accessories.insert_str(0, start);
            accessories.insert_str(accessories.len(), end);
            cnt += 1;
        }
    }

    println!("{}", -1)
}
