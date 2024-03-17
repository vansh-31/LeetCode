# Problem : Minimum Number of Operations to Make Array Continuous
# Problem Statement : You are given an integer array nums. In one operation, you can replace any element in nums with any integer.
# nums is considered continuous if both of the following conditions are fulfilled:
# All elements in nums are unique.
# The difference between the maximum element and the minimum element in nums equals nums.length - 1.
# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.
# Return the minimum number of operations to make nums continuous.
from typing import List
from bisect import bisect_right
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(set(nums))
        ans = float("inf")

        for i, s in enumerate(nums):
            e = s + n - 1
            idx = bisect_right(nums, e)

            ans = min(ans, n - (idx - i))
        return int(ans)