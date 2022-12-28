import collections
from typing import List


# 一応解けたが、メモリ効率が悪い、hash のキーが良くなさそう
class _Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # group = {}
        group = collections.defaultdict(list)  # default dict 使うともっと綺麗に書ける
        for val in strs:
            counter = collections.Counter(val)
            hash_key = frozenset(counter.items())
            # if hash_key in group:
            #     group[hash_key].append(val)
            # else:
            #     group[hash_key] = [val]
            group[hash_key].append(val)

        return group.values()


# 計算量は、O(NKlogK) になる (N: strs の長さ, K: strs の最大長)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            # キーをソートした文字列や、ソート済みの各文字の tuple にするとメモリ効率が格段に良くなる
            # 文字列より tuple の方が若干早い -> Iterable な object から 文字列に変換する処理にコストがかかるからとか？
            ans[tuple(sorted(s))].append(s)
        return ans.values()
