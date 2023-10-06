# Problem : Integer Break
# Problem Statement : Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.
# Return the maximum product you can get.
class Solution:
    def integerBreak(self, n: int) -> int:
        memo = [-1] * (n + 1)
        def maxProduct(k):
            if memo[k] != -1:
                return memo[k]
            if k == 1:
                return 1
            result = -float('inf')
            for i in range(1, k):
                result = max(result, i * maxProduct(k - i), i * (k - i))
            memo[k] = result # type: ignore
            return result
        return maxProduct(n) # type: ignore