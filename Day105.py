# Problem : Maximum Value of K Coins From Piles
# Problem Statement : There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.
# In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.
# Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.s
import functools
class Solution:
    def maxValueOfCoins(self, piles: list[list[int]], k: int) -> int:
        @functools.lru_cache(None)
        def func(i, k):
            if k == 0 or i == len(piles):
                return 0
            res, cur = func(i + 1, k), 0
            for j in range(min(len(piles[i]), k)):
                cur += piles[i][j]
                res = max(res, cur + func(i+1, k-j-1))
            return res
        
        return func(0, k)