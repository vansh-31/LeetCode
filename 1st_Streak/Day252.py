# Problem : Combination Sum IV
# Problem Statement : Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.
# The test cases are generated so that the answer can fit in a 32-bit integer.
from functools import cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def solve(x):
            if x == 0:
                return 1
            if x < 0:
                return 0
            ans = 0
            for i in range(n):
                ans += solve(x - nums[i])
            return ans

        return solve(target)
