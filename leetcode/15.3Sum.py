import itertools
from typing import List


# これは TLE になる
class __Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        for item in itertools.combinations(nums, 3):
            if sum(item) == 0:
                ans.add(tuple(sorted(item)))

        return ans


# 空間計算量は良くないけど、O(n^2) で解ける
class _Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3 or nums[0] > 0:
            return []

        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i

        ans = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                required = -(nums[i] + nums[j])
                if required in hashmap and hashmap[required] > j:
                    ans.add((nums[i], nums[j], required))

        return ans


# two pointer (日本語だと尺取法と呼ばれている) を使う方法
# https://qiita.com/drken/items/ecd1a472d3a0e7db8dce
# 次のような問題で使えることが多いらしい
# 「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求めよ
# 「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求めよ
# 「条件」を満たす区間 (連続する部分列) を数え上げよ
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        if len(nums) < 3 or nums[0] > 0:
            return []

        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # 二つのポインタを用意し、向き合うように探索する
            low, high = i + 1, len(nums) - 1
            sum = 0
            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum > 0:
                    high -= 1
                elif sum < 0:
                    low += 1
                else:
                    ans.append([nums[i], nums[low], nums[high]])
                    last_low, last_high = nums[low], nums[high]
                    # 重複をスキップする
                    while low < high and nums[low] == last_low:
                        low += 1
                    while low < high and nums[high] == last_high:
                        high -= 1

        return ans
