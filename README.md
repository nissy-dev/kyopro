# kyopro

D, Eがどっちか解けるまで精進する...

## ABC 156
急いで出したら、WAだらけだった...  
CLI出た!! : https://qiita.com/sachaos/items/37bb4a32ff49ab4a3ac0

- B問題
  - 10進数 -> n進数の変換
  - nで割っていき、その余りをつなげる
- D問題
  - n_C_kの計算の高速化まではわかった
    - 2**n - n_C_a - n_C_b - 1 まではいけた
  - コンペ中の理解は諦めた...
    - pypyで出したけど、TLE...appendが遅すぎる...?
    - https://drken1215.hatenablog.com/entry/2018/06/08/210000

## ABC 155

- D問題
  - Eより難しいらしい...
  - 類題がある : https://atcoder.jp/contests/abc149/tasks/abc149_e
    - https://tt-conpetitive.hatenablog.com/entry/2020/01/03/221433
    - 類題をみると 二分探索 + 累積和 の知識が必要という感じ
  - 解説読んでもピント来ないので今回はパス
- 前回に引き続き桁dpとかいうやつ (E問題)
  - 今回は制約がかなり大きいので再帰は通らない
    - メモ化してもきついものはきつい...
  - 解説の通りにすれば良い
    - https://qiita.com/c-yan/items/cb843ad3ba9a5009ad51#abc155e---payment
    - ちゃんと考察すればわかりそう

## ABC 154

- 入出力でハマった (B問題)
  - 問題は改行コードだった
  - 標準入力のenterは改行になる
  - int 関数は改行文字を処理する
- 区間和は累積和で前処理すると早い (D問題)
  - https://qiita.com/drken/items/56a6b68edef8fc605821
  - これは実務でも役立ちそう
- 桁dpとかいうやつ (E問題)
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
- ソートの計算量 (B問題)
  - https://qiita.com/drken/items/44c60118ab3703f7727f
  - ソートの最悪計算量の最小が O(nlogn)
  - マージソートとクイックソートが有名...?
- DPの計算 (D問題)
  - https://qiita.com/drken/items/a5e6fe22863b7992efdb
  - 自分は典型的なハマり方をしたっぽい
  - http://wakabame.hatenablog.com/entry/2017/09/10/211428
  - DPはテーブルを埋めていくイメージ
  - 難しい...完全に慣れな予感がする
