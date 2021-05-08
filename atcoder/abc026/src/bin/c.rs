use proconio::{fastout, input};

#[fastout]
fn main() {
    input! {
        // s: String,
        n: usize,
        // (n, m): (usize, usize),
        // (a, b, c): (usize, usize, usize),
        // data: [usize; n],
        data: [[usize; 1]; n-1]
    }

    // 部下リスト
    let mut subordinates: Vec<Vec<usize>> = vec![vec![]; n];
    for i in 0..n {
        for j in 0..(n - 1) {
            if (i + 1) == data[j][0] {
                subordinates[i].push(j + 1);
            }
        }
    }

    let mut salary = vec![1; n];
    for i in (0..n).rev() {
        if subordinates[i].len() == 1 {
            salary[i] = 2 * salary[subordinates[i][0]] + 1;
        }

        if subordinates[i].len() > 1 {
            let subordinates_salary = subordinates[i]
                .iter()
                .map(|&sub_num| salary[sub_num])
                .collect::<Vec<usize>>();
            salary[i] = subordinates_salary.iter().max().unwrap()
                + subordinates_salary.iter().min().unwrap()
                + 1;
        }
    }

    println!("{}", salary[0]);
}
