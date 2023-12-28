# Problem : String Compression II
# Problem Statement : Run-length encoding is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string becomes "a2bc3".
# Notice that in this problem, we are not adding '1' after single characters.
# Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.
# Find the minimum length of the run-length encoded version of s after deleting at most k characters.
from functools import cache
from math import log10, inf


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        rle = lambda x: x if x <= 1 else int(log10(x)) + 2

        @cache
        def fn(i, k, prev, cnt):
            if k < 0:
                return inf
            if i == len(s):
                return 0
            ans = fn(i + 1, k - 1, prev, cnt)  # delete current character
            if prev == s[i]:
                ans = min(ans, fn(i + 1, k, s[i], cnt + 1) + rle(cnt + 1) - rle(cnt))
            else:
                ans = min(ans, fn(i + 1, k, s[i], 1) + 1)
            return ans

        return fn(0, k, "", 0) # type: ignore
