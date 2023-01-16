from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_price = prices[0]
        for price in prices:
            if min_price > price:
                min_price = price
            else:
                ans = max(ans, price - min_price)

        return ans
