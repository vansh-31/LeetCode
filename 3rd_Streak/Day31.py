# Problem : Longest Ideal Subsequence
# Problem Statement : You are given a string s consisting of lowercase letters and an integer k. We call a string t ideal if the following conditions are satisfied:
# t is a subsequence of the string s.
# The absolute difference in the alphabet order of every two adjacent letters in t is less than or equal to k.
# Return the length of the longest ideal string.
# A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
# Note that the alphabet order is not cyclic. For example, the absolute difference in the alphabet order of 'a' and 'z' is 25, not 1.
class Solution(object):
    def longestIdealString(self, s: str, k: int) -> int:
        dp = [0] * 26
        for ch in s:
            i = ord(ch) - ord("a")
            minInd, maxInd = max(0, i - k), min(25, i + k)
            sub = dp[minInd : maxInd + 1]
            longest = max(sub)
            dp[i] = longest + 1
        return max(dp)
