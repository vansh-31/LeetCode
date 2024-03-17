# Problem : Minimum ASCII Delete Sum for Two Strings
# Problem Statement : Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n,m = len(s1),len(s2)
        dp = [ [-1 for _ in range(m) ] for _ in range(n) ]
        cumilative_sum_s1 = [ 0 ] * n
        cumilative_sum_s2 = [ 0 ] * m
        cumilative_sum_s1[-1],cumilative_sum_s2[-1] = ord( s1[-1] ),ord( s2[-1] )
        for i in range(n-2,-1,-1):
            cumilative_sum_s1[i] = ord( s1[i] ) + cumilative_sum_s1[i+1]
        for i in range(m-2,-1,-1):
            cumilative_sum_s2[i] = ord( s2[i] ) + cumilative_sum_s2[i+1]
        def solve(i,j):
            if i == n and j == m:
                return 0
            if i == n:
                return cumilative_sum_s2[j]
            if j == m:
                return cumilative_sum_s1[i]
            if dp[i][j] != -1:
                return dp[i][j]
            op1 = float("inf")
            if s1[i] == s2[j]:
                op1 = solve(i+1,j+1)
            op2 = ord(s1[i]) + solve(i+1,j)
            op3 = ord(s2[j]) + solve(i,j+1)
            dp[i][j] = min( op1,op2,op3 )
            return dp[i][j]
        return solve(0,0)