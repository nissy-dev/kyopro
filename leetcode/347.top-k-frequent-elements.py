import collections
import heapq
from typing import List


class __Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        # most_common 関数は便利
        return [element[0] for element in counter.most_common(k)]


# Counter を使わずに書いてみる
class _Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.defaultdict(lambda: 0)
        for num in nums:
            counter[num] += 1

        # ソートする O(NlogN) かかる
        sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        # most_common 関数は便利
        return [element[0] for element in sorted_counter][:k]


# 取り出しにヒープを使ってみる
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.defaultdict(lambda: 0)
        for num in nums:
            counter[num] += 1

        heap = []
        for key, value in counter.items():
            # heap は tuple を push できる。最初の要素が優先度が決まる
            heapq.heappush(heap, (-value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        return [element[1] for element in heap]
