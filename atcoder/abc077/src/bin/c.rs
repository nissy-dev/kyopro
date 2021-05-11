use proconio::{fastout, input};

// x 以上の値を持つ最小の index を返す
fn lower_bound(arr: &Vec<usize>, x: usize) -> usize {
    let mut left: isize = -1;
    let mut right = arr.len() as isize;
    while right - left > 1 {
        let mid = (right + left) / 2;
        if arr[mid as usize] < x {
            left = mid
        } else {
            right = mid
        }
    }
    return right as usize;
}

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        mut a: [usize; n],
        b: [usize; n],
        mut c: [usize; n],
    }

    // ソート
    a.sort();
    c.sort();

    let mut ans = 0;
    for middle in b {
        let bottom = lower_bound(&a, middle);
        let top = lower_bound(&c, middle + 1);
        ans += bottom * (n - top);
    }
    println!("{}", ans);
}
