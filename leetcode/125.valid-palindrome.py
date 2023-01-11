import re


# メモリ効率は悪い
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_re = re.sub(r"[^a-zA-Z0-9]+", "", s)
        str_list = list(s_re.lower())
        return str_list == str_list[::-1]
