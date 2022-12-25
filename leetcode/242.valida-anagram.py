import collections


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # sorted は、文字列を一文字ずつソートしたリストを返す
        # 例: sorted('abc') -> ['a', 'b', 'c']
        # ただこれだと文字列全てを保持するので、メモリ効率が悪い
        # Counter を使った方がメモリ効率がいい
        # return sorted(s) == sorted(t)
        return collections.Counter(s) == collections.Counter(t)
