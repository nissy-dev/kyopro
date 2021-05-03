use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        (n, q): (usize, usize),
        data: [[usize; 3]; q]
    }

    let mut ans = vec![0; n];
    for i in 0..q {
        for j in (data[i][0] - 1)..data[i][1] {
            ans[j] = data[i][2];
        }
    }

    for val in ans {
        println!("{}", val)
    }
}
