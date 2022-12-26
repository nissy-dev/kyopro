import itertools


# ナイーブな解法、計算量もメモリ効率も良くない
class _Solution:
    def twoSum(self, nums, target):
        for pair in itertools.combinations(range(len(nums)), 2):
            if nums[pair[0]] + nums[pair[1]] == target:
                return list(pair)


# 残りの数を hash に入れることで、一回のループで解を出せるようにできる
# 計算量は O(n)、メモリ効率は O(n)
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for i, v in enumerate(nums):
            remaining = target - v
            if remaining in seen:
                return [seen[remaining], i]
            seen[v] = i
