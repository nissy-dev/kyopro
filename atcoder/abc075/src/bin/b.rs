use std::iter::FromIterator;

use proconio::marker::Chars;
use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        // n: usize,
        (h, w): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        data: [Chars; h]
    }

    let neighbors: Vec<(isize, isize)> = vec![
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
    ];

    let mut ans = vec![vec![String::from(""); w]; h];
    for i in 0..h {
        for j in 0..w {
            if data[i][j] == '#' {
                ans[i][j] = String::from("#");
                continue;
            }

            let mut cnt = 0;
            for (dx, dy) in neighbors.clone() {
                let ti = i as isize + dy;
                let tj = j as isize + dx;
                if 0 <= ti && ti <= (h - 1) as isize && 0 <= tj && tj <= (w - 1) as isize {
                    if data[ti as usize][tj as usize] == '#' {
                        cnt += 1;
                    }
                }
            }
            ans[i][j] = cnt.to_string();
        }
    }

    for row in ans {
        println!("{}", String::from_iter(row))
    }
}
