from typing import List


class _Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        front = [val for val in nums]
        for i in range(1, N):
            front[i] = front[i - 1] * nums[i]

        back = [val for val in nums]
        for i in range(N - 2, -1, -1):
            back[i] = back[i + 1] * nums[i]

        ans = [0 for _ in nums]
        ans[0] = back[1]
        ans[N - 1] = front[N - 2]
        for i in range(1, N - 1):
            ans[i] = front[i - 1] * back[i + 1]

        return ans


# 考え方は合っているけど、front と back を一度のループで計算できる
# 空間計算量を O(1) にできる
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length
        pre_product = 1
        post_product = 1

        # 賢いけど、自分で思いつける気はしない...
        for i in range(length):
            ans[i] *= pre_product
            pre_product = pre_product * nums[i]
            ans[length - i - 1] *= post_product
            post_product = post_product * nums[length - i - 1]

        return ans
