# アルゴリズムのメモ

https://algo-logic.info/beginner/

## ソート

大きな分類

- 安定ソート vs 不安定ソート
- 内部ソート vs 外部ソート

**安定ソートと不安定ソートの違い**

> 順序的に同じ値を持つ要素が複数存在した時に、ソート後もその順序が保たれると「安定(stable)」といい、そうでない場合を「不安定(unstable)」といいます。

**内部ソートと外部ソートの違い**

> 配列の内部を使って処理を進めるか、配列の外部のメモリを使うかで分類されます。

**ソートまとめ**

|                | 最悪時間 | 安定 | 内部 |
| :------------- | :------: | :--: | :--: |
| 選択ソート     |  O(n^2)  |  △   |  ○   |
| バブルソート   |  O(n^2)  |  ○   |  ○   |
| 挿入ソート     |  O(n^2)  |  ○   |  ○   |
| マージソート   | O(nlogn) |  ○   |  ×   |
| クイックソート | O(nlogn) |  ×   |  ○   |

### 選択ソート

- 最小の要素を見つけて、配列の先頭と入れ替えることを続けるソート
- 一番思いつきやすいソート

```
def selection_sort(arr):
  for i in range(len(arr)):
    min_value = arr[i]
    min_index = i
    # ループで最小の要素を確認する
    for j in range(i, len(arr)):
      if arr[j] < min_value:
        min_value = arr[j]
        min_index = j
    # 要素の入れ替え
    tmp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = tmp
```

### バブルソート

- 隣接する要素の小さい方が前へ、大きい方が後ろに来るように入れ替えながらソート

```
def bubble_sort(arr):
  n = len(arr)
  for i in range(n-1):
    for j in range(n-i-1):
      # 右隣が小さければ入れ替える
      if arr[j] > arr[j+1]:
        arr[j], arr[j+1] = arr[j+1], arr[j]
```

### 挿入ソート

- 小さい要素を前に「挿入」するために、他の要素を前に 1 つずつ前にずらしてソート

```
def insertion_sort(arr):
  n = len(arr)
  for i in range(1, n):
    tmp = arr[i]
    j = i-1
    while j >= 0 and arr[j]>tmp:
      arr[j+1] = arr[j]
      j = j-1
    arr[j+1] = tmp
```

### マージソート

- 配列を 2 分割することを繰り返し、小さい配列を一つ一つソートしながら「マージ」(併合)するソート
- 分割統治法を用いたソートアルゴリズム
- 実装は少し長いので省略 (メモリも余分に必要なので、あまり使われない...)

### クイックソート

- 基準値(ピボット)を取り出して、小さい要素を左側・大きい要素を右側に移すことを繰り返すソート
- イメージが掴みやすかった資料 : https://wa3.i-3-i.info/word16752.html

```
import random

# 左右から探索して配列を分割
def partition(arr, l, r):
  # 配列からランダムにピボットを選ぶ
  pivot = random.choice(arr)
  left = l
  right = r
  while left < right:
    # left<=r が無いとleftがrを超えて配列外の領域を参照する可能性があります
    while(left<=r and arr[left] < pivot):
      left+=1
    # l<=right が無いとrightがlを超えて配列外の領域を参照する可能性があります
    while(l<=right and arr[right] >= pivot):
      right-=1
    if(left<right):
      arr[left],arr[right] = arr[right],arr[left]
  # 右側(ピボット以上の領域)の先頭のindexを出力
  return left

def quick_sort(arr, l, r):
  if l<r:
    mid = partition(arr, l, r)
    quick_sort(arr, l, mid-1)
    quick_sort(arr, mid, r)
```

## 探索

### 二分探索 (Binary Search)

- ソート済みである配列の中から、目的の値が存在するかを調べる探索アルゴリズム
- 計算量 : log(N) ・・・線形よりだいぶ高速
- Python だと `bisect` を使うと便利
  - https://qiita.com/ta7uw/items/d6d8f0ddb215c3677cd3
- 解けるタスク
  - ソート済み配列内で x 以上の値を持つもののうち、左端にあるものは何か(最小の index は何か？)
    - lowerbound : bisect_left
  - ソート済み配列内で x 以降の値を持つもののうち、左端にあるものは何か(最小の index は何か？)
    - upperbound : bisect_right
    - upperbound - 1 すると、「ソート済み配列内で x 以上の値を持つもののうち、右端にあるもの」になる
  - 以上を応用して、平均値の最大化や、最小値の最大化を求めることは多い
  - https://qiita.com/drken/items/2f56925972c1d34e05d8

アルゴリ (lower bound)

> 1. L=-1, R=配列の index の最大値 として以下を繰り返す
>    1. R-L>1 なら以下を実行する
>    2. L と R の中間にある M が指す要素について、x との大小関係を調べる
>       1. x 未満ならば、右側半分にある部分配列に対して 1 と 2 の探索を行う（L を M があった場所に移す）
>       2. 上ならば、左側半分にある部分配列に対して 1 と 2 の探索を行う（R を M があった場所に移す）

### 重みなしグラフの経路探索

記事 (実装がわかりやすいもの, C++):  
http://yamagensakam.hatenablog.com/entry/2018/09/15/094504

問題例 (DFS, BFS は基本どちらも同じタスクに適応できる)

- A から B への経路の存在確認
- A から B への最短経路の算出
- 二部グラフ判定
  - 二部グラフ : https://ja.wikipedia.org/wiki/2%E9%83%A8%E3%82%B0%E3%83%A9%E3%83%95
- トポロジカルソート
  - タスク間に依存関係がある場合、どんな順番でタスクをこなせば良いかを決めるのに役立つ
  - https://ikatakos.com/pot/programming_algorithm/graph_theory/topological_sort
- サイクル検出

#### 深さ優先探索 (Depth First Search)

[アルゴリズムロジック 深さ優先探索(Depth First Search)の基本](https://algo-logic.info/dfs/?customize_changeset_uuid=d5d704d5-3408-4126-9339-847efd308030&customize_autosaved=on)  
[DFS (深さ優先探索) 超入門！ 〜 グラフ・アルゴリズムの世界への入口 〜【前編】](https://qiita.com/drken/items/4a7869c5e304883f539b)  
[DFS (深さ優先探索) 超入門！ 〜 グラフ・アルゴリズムの世界への入口 〜【後編】](https://qiita.com/drken/items/a803d4fc4a727e02f7ba)

- 計算量 O(V+E)
- Stack を使って実装されている
- 探索イメージ :
- 得意なタスク
  - 与えられたコスト以内でたどり着ける頂点の列挙

#### 幅優先探索 (Breadth First Search)

[アルゴリズムロジック 幅優先探索(Breadth First Search)の基本](https://algo-logic.info/bfs/?customize_changeset_uuid=d5d704d5-3408-4126-9339-847efd308030&customize_autosaved=on)  
[BFS (幅優先探索) 超入門！ 〜 キューを鮮やかに使いこなす 〜](https://qiita.com/drken/items/996d80bcae64649a6580)

- 計算量 O(V+E)
- Queue を使って実装されている
- メモリを比較的多く使う
- 探索イメージ : https://qiita.com/drken/items/996d80bcae64649a6580#1-1-bfs-%E3%81%AE%E5%8B%95%E4%BD%9C
- 得意なタスク
  - 迷路などの最短経路探索

### 重みありグラフの経路探索

#### ワーシャルフロイド法

- グラフの各ノード間の最短経路の算出
- 計算量 O(N^3), N<=300 くらいで問題ない
- DP で効率良く全探索している
  - d[i][j][k] = (頂点 0 から頂点 k までだけを通ってよいときの、頂点 i と頂点 j の最短距離)
  - 更新式 : min(d[i][j][k-1], d[i][k][k-1] + d[k][j][k-1])
    - ある中間点 k を通るものと通らないものを比較して、最小のものを採択

#### ダイクストラ法

[アルゴリズムロジック ダイクストラ法による単一始点最短経路を求めるアルゴリズム](https://algo-logic.info/dijkstra/)

- 単一始点最短経路問題を解く時に使う
  - 始点を固定した時に、他のすべての頂点への最短経路を求める問題
- 計算量 O(|E|log|V|)
  - ベルマン–フォード法より高速
  - 普通にやると O(V^2) だけど、ヒープを使って計算量を減らしている
- 負の辺があると使えない

アルゴリ

> 1. 始点 s を「既に最短距離が確定した頂点」、他の頂点を「まだ最短距離が確定していない頂点」とする
> 2. 以下をすべての頂点の最短距離が確定するまで繰り返す
>    1. 全ての「既に最短距離が確定した頂点 u 」から「まだ最短距離が確定していない頂点 v 」へ伸びる全ての辺 e=(u,v) について、「v と d[v] の候補」をまとめておく
>    2. 候補の中から、d[v] が最小のものを選択し、v を「既に最短距離が確定した頂点」に加える

最短距離を 1 つずつ確定させていくイメージ

#### ベルマン–フォード法

[アルゴリズムロジック ベルマンフォード法による単一始点最短経路を求めるアルゴリズム](https://algo-logic.info/bellman-ford/)

- 単一始点最短経路問題を解く時に使う
  - 始点を固定した時に、他のすべての頂点への最短経路を求める問題
- 計算量 O(|E|\*|V|)
- 負の辺があっても使える
  - 負の閉路がの検出にも使える

アルゴリ

1. 最短距離が更新されなくなるか、|V| 回目の更新が終わるまで以下を繰り返す
   - 全ての辺に対して、d[v] = min{ d[u] + ( u から v への距離 ) } という更新式を利用して最短距離を更新する
2. |V-1| 回以内の更新で終了すれば負の閉路は存在しない。|V| 回まで更新が続けば負の閉路が存在する

## データ構造

### 基本的なデータ構造

- Stack
  - 最後に格納したデータが最初に出てくるようなデータ構造
  - Last In First Out
- Queue
  - 最初に格納したデータが最初に出てくるようなデータ構造
  - First In First Out
  - collections モジュールにある deque というクラス が高速なアクセスに対応
- Set
  - **要素の挿入・削除・検索を高速に行うことができる特徴を持つ**
  - 順序依存しない・重複も許さない
- 配列/連想配列/Set の違い
  - 配列はデータの位置を使ってデータを取得するが、連想配列は key を利用して取得 (key は set の形で保持する)
  - Set と連想配列の違いは、連想配列のケースは key に値が紐付いている点

**Python における Queue と List の違い**

> Deque はどちらの側からも append と pop が可能で、スレッドセーフでメモリ効率がよく、どちらの方向からもおよそ O(1) のパフォーマンスで実行できます。list オブジェクトでも同様の操作を実現できますが、これは高速な固定長の操作に特化されており、内部のデータ表現形式のサイズと位置を両方変えるような pop(0) や insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします

### 優先度付きキュー (Priority Queue)

- リスト内の最大値・最小値の検索がかなり高速にできる (O(logN), 普通は O(N))
- ヒープという木構造を使って実装されている
  - ヒープの解説 : https://yottagin.com/?p=8706
  - max heap であれば「親が子より常に大きい」、min heap であれば「親が子より常に小さい」 という制約を満たす木構造のこと

### Union Find

[アルゴリズムロジック Union-Find Tree を理解する！素集合系を扱うデータ構造](https://algo-logic.info/union-find-tree/)

- データを互いに素な集合(素集合系)にして管理するためのデータ構造
- 木(集合)同士の併合や、同じ集合に含まれているかの判定は高速にできる
- 一度まとめた集合を分割したり、ノードを削除したりするのにはあまり向いていない
