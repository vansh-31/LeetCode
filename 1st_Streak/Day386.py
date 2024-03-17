# Problem : House Robber
# Problem Statement : You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @cache
        def solve(n):
            if n < 0:
                return 0
            inc = nums[n] + solve(n - 2)
            exc = solve(n - 1)
            return max(inc, exc)

        return solve(n - 1)
