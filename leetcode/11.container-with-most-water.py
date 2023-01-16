from typing import List


# これだとTLEになる
class _Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                ans = max(ans, min(height[i], height[j]) * (j - i))

        return ans


# これも Two Pointer でとける
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left, right = 0, len(height) - 1

        while left < right:
            max_area = max(max_area, min(height[left], height[right]) * (right - left))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
