# Problem : Word Break
# Problem Statement : Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        n = len(s)
        dp = [-1] * n
        def solve(index):
            if index >= n:
                return True
            if dp[index] != -1:
                return dp[index]
            for word in wordDict:
                m = len(word)
                if word == s[ index: index+ m ] :
                    if solve( index+m ):
                        dp[index] = True
                        return True
            dp[index] = False
            return False
        return solve(0)