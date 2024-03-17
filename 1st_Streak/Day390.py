# Problem : Longest Common Subsequence
# Problem Statement : Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.
# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(2)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                take = 0
                if text1[i] == text2[j]:
                    take = 1 + dp[1][j + 1]
                not_take = max(dp[1][j], dp[0][j + 1])
                dp[0][j] = max(take, not_take)
            dp[1] = dp[0].copy()
        return dp[0][0]
