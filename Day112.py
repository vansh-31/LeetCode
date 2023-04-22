# Problem : Minimum Insertion Steps to Make a String Palindrome
# Problem Statement : Given a string s. In one step you can insert any character at any index of the string.
# Return the minimum number of steps to make s palindrome.
# A Palindrome String is one that reads the same backward as well as forward.
class Solution:
    def minInsertions(self, s: str) -> int:
        if s == s[::-1]:
            return 0
        dp = [ [ -1 for x in range(len(s)+1) ] for y in range(len(s)+1) ]
        def solve(i,j):
            if i == j:
                return 0
            if i + 1 == j:
                return 0 if s[i] == s[j] else 1

            if dp[i][j] != -1:
                return dp[i][j]

            op1 = op2 = op3 = 1000
            if s[i] == s[j]:
                op1 = solve(i+1,j-1)
            op2 = 1 + solve(i+1,j)
            op3 = 1 + solve(i,j-1)
            dp[i][j] = min([op1,op2,op3])
            return dp[i][j]
        return solve(0,len(s)-1)