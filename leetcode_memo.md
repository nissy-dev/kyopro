# Leetcode をやったときのメモ

## Hashmap のキーは immutable である必要がある

Python で Hashmap のキーには、List, dict, set などの mutable なオブジェクトは指定できない。
一方で、frozenset, tuple などの immutable なオブジェクトは指定できる。これはなぜなのか？

参考: [Python における hashable の定義](https://docs.python.org/3/glossary.html#term-hashable)

Hashmap は、key を hash 関数に通して生成された index に値を格納する。
key が immutable だと index が変わる可能性があるため、index と 値の 1 対 1 対応が崩れて検索が O(1) でできなくなる。

ちなみに、python の set の検索の計算量が O(1) なのは、key に set の要素、value にダミー値を設定した hashmap を内部実装に使っているからである。
