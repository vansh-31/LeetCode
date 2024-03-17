# Problem : Palindromic Substrings
# Problem Statement : Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.
class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)

        def solve(l, r):
            if l == -1 or r == n:
                return 0
            if s[l] == s[r]:
                return 1 + solve(l - 1, r + 1)
            return 0

        res = n
        for i in range(1, n):
            res += solve(i - 1, i) + solve(i - 1, i + 1)
        return res
