# Problem : K Inverse Pairs Array
# Problem Statement : For an integer array nums, an inverse pair is a pair of integers [i, j] where 0 <= i < j < nums.length and nums[i] > nums[j].
# Given two integers n and k, return the number of different arrays consist of numbers from 1 to n such that there are exactly k inverse pairs. Since the answer can be huge, return it modulo 109 + 7.
from functools import cache


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        @cache
        def dp(n: int, k: int) -> int:
            if k <= 0 or n == 1:
                return k == 0
            return dp(n, k - 1) + dp(n - 1, k) - dp(n - 1, k - n)

        return dp(n, k) % int(1e9 + 7)
