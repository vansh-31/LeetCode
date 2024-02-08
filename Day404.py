# Problem : Perfect Squares
# Problem Statement : Given an integer n, return the least number of perfect square numbers that sum to n.
# A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
class Solution:
    def numSquares(self, n: int):
        # @cache
        # def solve(x):
        #     if x == 0:
        #         return 0
        #     num = 1
        #     ans = x
        #     while x >= (num*num):
        #         ans = min(ans, 1 + solve(x - (num*num) ) )
        #         num += 1
        #     return ans
        dp = [float("Inf")] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for x in range(2, n + 1):
            num = 1
            ans = x
            while x >= (num * num):
                if (x - num * num) >= 0:
                    ans = min(ans, 1 + dp[(x - num * num)])
                num += 1
            dp[x] = ans
        return dp[n]
