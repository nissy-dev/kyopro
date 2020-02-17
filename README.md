# kyopro

D, Eがある程度解けるまで精進する...

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

## ABC 155