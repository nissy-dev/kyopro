use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        // (n, m): (usize, usize),
        (sx, sy, tx, ty): (isize, isize, isize, isize),
        // data: [usize; n],
        // data: [[usize; m]; n]
    }

    // ただの考察問題
    let mut ans = String::from("");
    let dx = (tx - sx) as usize;
    let dy = (ty - sy) as usize;
    // path 1
    ans += "U".repeat(dy).as_str();
    ans += "R".repeat(dx).as_str();
    // path 2
    ans += "D".repeat(dy).as_str();
    ans += "L".repeat(dx).as_str();
    // path 3
    ans += "L";
    ans += "U".repeat(dy + 1).as_str();
    ans += "R".repeat(dx + 1).as_str();
    ans += "D";
    // path 4
    ans += "R";
    ans += "D".repeat(dy + 1).as_str();
    ans += "L".repeat(dx + 1).as_str();
    ans += "U";
    println!("{}", ans);
}
