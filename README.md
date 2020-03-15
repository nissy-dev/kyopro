# kyopro

D, E がどっちか解けるまで精進する...

## ABC 158

- D 問題
  - 文字列の先頭追加は遅い
  - Queue で管理しよう

> Deque はどちらの側からも append と pop が可能で、スレッドセーフでメモリ効率がよく、どちらの方向からもおよそ O(1) のパフォーマンスで実行できます。list オブジェクトでも同様の操作を実現できますが、これは高速な固定長の操作に特化されており、内部のデータ表現形式のサイズと位置を両方変えるような pop(0) や insert(0, v) などの操作ではメモリ移動のために O(n) のコストを必要とします

## ABC 157

酷すぎた...

- D 問題
  - Union Find を使う問題
  - Union Find を使うのを思いつくのが思いつくのがキツそう
  - グラフ問題面白い

## ABC 156

急いで出したら、WA だらけだった...  
CLI 出た!! : https://qiita.com/sachaos/items/37bb4a32ff49ab4a3ac0

- B 問題
  - 10 進数 -> n 進数の変換
  - n で割っていき、その余りをつなげる
- D 問題
  - n_C_k の計算の高速化まではわかった
    - 2\*\*n - n_C_a - n_C_b - 1 まではいけた
    - そのまま使える
      - http://wakabame.hatenablog.com/entry/2017/09/21/211357
  - コンペ中の理解は諦めた...
- E 問題
  - 普通に考察問題だった
    - 数え上げの条件を正確に掴むのがポイント
    - xHy = x+y−1Cx−1 (忘れていた)
  - 数え上げさえ分かれば、あとは nCk や nHk を計算するだけ
  - https://img.atcoder.jp/abc156/editorial.pdf
  - https://drken1215.hatenablog.com/entry/2018/06/08/210000

## ABC 155

- D 問題
  - E より難しいらしい...
  - 類題がある : https://atcoder.jp/contests/abc149/tasks/abc149_e
    - https://tt-conpetitive.hatenablog.com/entry/2020/01/03/221433
    - 類題をみると 二分探索 + 累積和 の知識が必要という感じ
  - 解説読んでもピント来ないので今回はパス
- 前回に引き続き桁 dp とかいうやつ (E 問題)
  - 今回は制約がかなり大きいので再帰は通らない
    - メモ化してもきついものはきつい...
  - 解説の通りにすれば良い
    - https://qiita.com/c-yan/items/cb843ad3ba9a5009ad51#abc155e---payment
    - ちゃんと考察すればわかりそう

## ABC 154

- 入出力でハマった (B 問題)
  - 問題は改行コードだった
  - 標準入力の enter は改行になる
  - int 関数は改行文字を処理する
- 区間和は累積和で前処理すると早い (D 問題)
  - https://qiita.com/drken/items/56a6b68edef8fc605821
  - これは実務でも役立ちそう
- 桁 dp とかいうやつ (E 問題)
  - 制約がバカみたいにでかい (それ気になった...)
  - メモ化再帰で書いた方がわかりやすかった
    - 計算量はかかるし、メモリ効率も悪いからいつも使えるとは限らない
  - DP : 要は適切に場合分けできるか
  - https://maspypy.com/atcoder-%E5%8F%82%E5%8A%A0%E6%84%9F%E6%83%B3-2019-02-09abc-154#toc3
  - divmod 積極的に使っていきたい

## ABC153

- 計算量の感覚
  - https://qiita.com/drken/items/872ebc3a2b5caaa4a0d0
  - 実用上の多くの場面では、n=10^5 ~ 10^7 付近のデータを扱うケースが多い
  - O(n^2) なアルゴリズムを O(nlogn) に改善できるかどうかが鍵
- ソートの計算量 (B 問題)
  - https://qiita.com/drken/items/44c60118ab3703f7727f
  - ソートの最悪計算量の最小が O(nlogn)
  - マージソートとクイックソートが有名...?
- DP の計算 (D 問題)
  - https://qiita.com/drken/items/a5e6fe22863b7992efdb
  - 自分は典型的なハマり方をしたっぽい
  - http://wakabame.hatenablog.com/entry/2017/09/10/211428
  - DP はテーブルを埋めていくイメージ
  - 難しい...完全に慣れな予感がする
