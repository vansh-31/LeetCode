# Problem : Extra Characters in a String
# Problem Statement : You are given a 0-indexed string s and a dictionary of words dictionary. You have to break s into one or more non-overlapping substrings such that each substring is present in dictionary. There may be some extra characters in s which are not present in any of the substrings.
# Return the minimum number of extra characters left over if you break up s optimally.
class Solution(object):
    def minExtraChar(self, s, dictionary):
        dp = {}
        def solve(i):
            if i >= l:
                return 0
            if i in dp:
                return dp[i]
            res = 1 + solve(i + 1)
            for word in dictionary:
                tmp = len(word)
                if tmp + i <= l and word == s[i: i + tmp]:
                    res = min(res, solve(i + tmp))
            dp[i] = res
            return dp[i]
        l = len(s)
        return solve(0)