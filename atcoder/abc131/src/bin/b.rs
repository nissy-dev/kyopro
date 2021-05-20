use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (n, l): (isize, isize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    let taste = (1..(n + 1)).map(|x| l + x - 1);
    let remove_value = taste.clone().map(|x| x.abs()).min().unwrap();
    let mut ans = 0;
    for val in taste {
        if val.abs() == remove_value {
            continue;
        }
        ans += val
    }
    println!("{}", ans);
}
