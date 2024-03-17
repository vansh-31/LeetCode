# Problem : Maximize Score After N Operations
# Problem Statement : You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.
# In the ith operation (1-indexed), you will:
# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# Return the maximum score you can receive after performing n operations.
# The function gcd(x, y) is the greatest common divisor of x and y.
from math import gcd
class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums)
        
       
        gcd_matrix = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                gcd_matrix[i][j] = gcd_matrix[j][i] = gcd(nums[i], nums[j])
        
      
        dp = [0] * (1 << n)
        
        
        for state in range(1, 1 << n):
          
            cnt = bin(state).count('1')
            
           
            if cnt % 2 == 1:
                continue
            
            
            for i in range(n):
                if not (state & (1 << i)):
                    continue
                for j in range(i+1, n):
                    if not (state & (1 << j)):
                        continue
                    nextState = state ^ (1 << i) ^ (1 << j)
                    dp[state] = max(dp[state], dp[nextState] + cnt // 2 * gcd_matrix[i][j])
        
        return dp[(1 << n) - 1]