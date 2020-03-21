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

### 深さ優先探索 (Depth First Search)

### 幅優先探索 (Breadth First Search)

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

- データを互いに素な集合(素集合系)にして管理するためのデータ構造
- 木(集合)同士の併合や、同じ集合に含まれているかの判定は高速にできる
- 一度まとめた集合を分割したり、ノードを削除したりするのにはあまり向いていない
