# Problem : Longest Palindromic Subsequence
# Problem Statement : Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rev = s[::-1]
        n = len(s)
        m = len(s)

        curr = [0 for x in range(m+1)]
        next = [0 for x in range(m+1)]

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if s[i] == rev[j]:
                    curr[j] = 1 + next[j+1]
                else:
                    curr[j] = max( next[j], curr[j+1] )
            next = curr.copy()
        return curr[0]