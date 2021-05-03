use proconio::{fastout, input};
use std::cmp;
use std::collections::VecDeque;

#[fastout]
fn main() {
    input! {
        (n, m): (usize, usize),
        edges: [[usize; 2]; m]
    }

    // トポロジカルソートをする (BFS)
    // https://algo-logic.info/topological-sort/#toc_id_2_1

    // グラフデータの取得 (隣接リスト形式でもっておく)
    let mut graphs: Vec<Vec<usize>> = vec![vec![]; n];
    // ノードの入次数を計算する
    let mut deg: Vec<usize> = vec![0; n];
    for edge in edges {
        // 頂点の番号を0始まりにする
        graphs[edge[0] - 1].push(edge[1] - 1);
        deg[edge[1] - 1] += 1;
    }

    // 入次数が0の点をキューに入れる
    let mut queue: VecDeque<usize> = VecDeque::new();
    for i in 0..n {
        if deg[i] == 0 {
            queue.push_back(i)
        }
    }

    // dp[i] = 最初に入力辺を持たなかった点からノードiまでの最長パス
    let mut dp = vec![0; n];
    // BFSでノードの並び替え
    // 最長経路を調べるので、入次数が少ないノードから調べる必要がある
    while queue.len() > 0 {
        let src = queue.pop_front().unwrap();
        for dest in graphs[src].clone() {
            deg[dest] -= 1;
            if deg[dest] == 0 {
                queue.push_back(dest);
                // 入次数が0になる = src→destへの経路が確定
                dp[dest] = cmp::max(dp[dest], dp[src] + 1);
            }
        }
    }

    println!("{}", dp.iter().max().unwrap());
}
