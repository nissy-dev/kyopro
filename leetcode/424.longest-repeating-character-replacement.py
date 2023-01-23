# 答えは単調増加するので、二分探索を利用する
class _Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # binary search over the length of substring
        # lo contains the valid value, and hi contains the
        # invalid value
        lo = 1
        hi = len(s) + 1
        while lo + 1 < hi:
            mid = lo + (hi - lo) // 2

            # can we make a valid substring of length `mid`?
            if self.__can_make_valid_substring(s, mid, k):
                # explore the right half
                lo = mid
            else:
                # explore the left half
                hi = mid

        # length of the longest substring that satisfies
        # the given condition
        return lo

    # ある長さが ans になるかどうか、window をスライドさせてチェックする
    def __can_make_valid_substring(self, s: str, substring_length: int, k: int):
        # take a window of length `substring_length` on the given
        # string, and move it from left to right. If this window
        # satisfies the condition of a valid string, then we return
        # true
        freq_map = {}
        max_frequency = 0
        start = 0
        for end in range(len(s)):
            freq_map[s[end]] = freq_map.get(s[end], 0) + 1

            # if the window [start, end] exceeds substring_length
            # then move the start pointer one step toward right
            if end + 1 - start > substring_length:
                # before moving the pointer toward right, decrease
                # the frequency of the corresponding character
                freq_map[s[start]] -= 1
                start += 1

            # record the maximum frequency seen so far
            max_frequency = max(max_frequency, freq_map[s[end]])
            if substring_length - max_frequency <= k:
                return True

        # we didn't a valid substring of the given size
        return False


# こっちの解法の方が自分の考えていたものに近かった
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start = 0
        frequency_map = {}
        max_frequency = 0
        longest_substring_length = 0
        for end in range(len(s)):
            frequency_map[s[end]] = frequency_map.get(s[end], 0) + 1

            # the maximum frequency we have seen in any window yet
            max_frequency = max(max_frequency, frequency_map[s[end]])

            # move the start pointer towards right if the current
            # window is invalid
            is_valid = end + 1 - start - max_frequency <= k
            if not is_valid:
                frequency_map[s[start]] -= 1
                start += 1

            # the window is valid at this point, store length
            # size of the window never decreases
            longest_substring_length = end + 1 - start

        return longest_substring_length
