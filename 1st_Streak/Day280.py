# Problem : Build Array Where You Can Find The Maximum Exactly K Comparisons
# Problem Statement : You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:
# You should build the array arr which has the following properties:
# arr has exactly n integers.
# 1 <= arr[i] <= m where (0 <= i < n).
# After applying the mentioned algorithm to arr, the value search_cost is equal to k.
# Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10**9 + 7
        
        dp = [[0] * (k+1) for _ in range(m+1)]
        prefix = [[0] * (k+1) for _ in range(m+1)]
        prevDp = [[0] * (k+1) for _ in range(m+1)]
        prevPrefix = [[0] * (k+1) for _ in range(m+1)]
        
        for j in range(1, m+1):
            prevDp[j][1] = 1
            prevPrefix[j][1] = j
        
        for _ in range(2, n+1):
            dp = [[0] * (k+1) for _ in range(m+1)]
            prefix = [[0] * (k+1) for _ in range(m+1)]
            
            for maxNum in range(1, m+1):
                for cost in range(1, k+1):
                    dp[maxNum][cost] = (maxNum * prevDp[maxNum][cost]) % mod
                    
                    if maxNum > 1 and cost > 1:
                        dp[maxNum][cost] += prevPrefix[maxNum - 1][cost - 1]
                        dp[maxNum][cost] %= mod
                    
                    prefix[maxNum][cost] = (prefix[maxNum - 1][cost] + dp[maxNum][cost]) % mod
            
            prevDp, prevPrefix = [row[:] for row in dp], [row[:] for row in prefix]
        
        return prefix[m][k]