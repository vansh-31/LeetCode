# Problem : Number of Ways to Form a Target String Given a Dictionary
# Problem Statement :  You are given a list of strings of the same length words and a string target.

# Your task is to form target using the given words under the following rules:

# target should be formed from left to right.
# To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
# Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
# Repeat the process until you form the string target.
# Notice that you can use multiple characters from the same string in words provided the conditions above are met.

# Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.
class Solution:
    def numWays(self, words: list[str], target: str) -> int:
        n = len(words[0])
        m = len(target)
        mod = 10**9 + 7
        dp = [0] * (m+1)
        dp[0] = 1
        
        count = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for word in words:
                count[i][ord(word[i]) - ord('a')] += 1
        
        for i in range(n):
            for j in range(m-1, -1, -1):
                dp[j+1] += dp[j] * count[i][ord(target[j]) - ord('a')]
                dp[j+1] %= mod
        
        return dp[m]