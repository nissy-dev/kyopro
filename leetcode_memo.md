# Leetcode をやったときのメモ

## Hashmap のキーは immutable である必要がある

Python で Hashmap のキーには、List, dict, set などの mutable なオブジェクトは指定できない。
一方で、frozenset, tuple などの immutable なオブジェクトは指定できる。これはなぜなのか？

参考: [Python における hashable の定義](https://docs.python.org/3/glossary.html#term-hashable)

この理由としては、immutable なオブジェクトだと

## Hashmap のキーを検索する際の計算量が O(1) になる原理

ちなみに、python の set の検索の計算量が O(1) なのは、key に set の要素、value にダミー値を設定した hashmap を内部実装に使っているからである。
