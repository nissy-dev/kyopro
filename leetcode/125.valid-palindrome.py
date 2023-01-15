import re


# メモリ効率は悪い O(n)
class _Solution:
    def isPalindrome(self, s: str) -> bool:
        s_re = re.sub(r"[^a-zA-Z0-9]+", "", s)
        str_list = list(s_re.lower())
        return str_list == str_list[::-1]


# O(1) の解法
class Solution:
    def isPalindrome(self, s: str) -> bool:
        beg, end = 0, len(s) - 1
        while beg <= end:
            while not s[beg].isalnum() and beg < end:
                beg += 1
            while not s[end].isalnum() and beg < end:
                end -= 1
            if s[beg].lower() == s[end].lower():
                beg, end = beg + 1, end - 1
            else:
                return False
        return True
