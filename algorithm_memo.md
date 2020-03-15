# アルゴリズムのメモ

https://algo-logic.info/

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
def partition(arr, l, r): # 左右から探索して配列を分割
  pivot = random.choice(arr) # 配列からランダムにピボットを選ぶ
  left = l
  right = r
  while left < right:
    while(left<=r and arr[left] < pivot): # left<=r が無いとleftがrを超えて配列外の領域を参照する可能性があります
      left+=1
    while(l<=right and arr[right] >= pivot):　# l<=right が無いとrightがlを超えて配列外の領域を参照する可能性があります
      right-=1
    if(left<right):
      arr[left],arr[right] = arr[right],arr[left]
  return left # 右側(ピボット以上の領域)の先頭のindexを出力

def quick_sort(arr, l, r):
  if l<r:
    mid = partition(arr, l, r)
    quick_sort(arr, l, mid-1)
    quick_sort(arr, mid, r)
```

## 探索

## データ構造

### Union Find

- データを互いに素な集合(素集合系)にして管理するためのデータ構造
- 木(集合)同士の併合や、同じ集合に含まれているかの判定は高速にできる
- 一度まとめた集合を分割したり、ノードを削除したりするのにはあまり向いていない
