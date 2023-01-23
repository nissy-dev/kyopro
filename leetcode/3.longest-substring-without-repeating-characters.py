from collections import Counter


# Sliding Window を使う考え方はちょっと近かったけど詳細の解法に落とし込めなかった
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = Counter()

        left = right = 0

        res = 0
        while right < len(s):
            rv = s[right]
            chars[rv] += 1

            while chars[rv] > 1:
                lv = s[left]
                chars[lv] -= 1
                left += 1

            res = max(res, right - left + 1)
            right += 1

        return res
