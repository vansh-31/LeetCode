# Problem : Check if There is a Valid Partition For The Array
# Problem Statement : You are given a 0-indexed integer array nums. You have to partition the array into one or more contiguous subarrays.
# We call a partition of the array valid if each of the obtained subarrays satisfies one of the following conditions:
# The subarray consists of exactly 2 equal elements. For example, the subarray [2,2] is good.
# The subarray consists of exactly 3 equal elements. For example, the subarray [4,4,4] is good.
# The subarray consists of exactly 3 consecutive increasing elements, that is, the difference between adjacent elements is 1. For example, the subarray [3,4,5] is good, but the subarray [1,3,5] is not.
# Return true if the array has at least one valid partition. Otherwise, return false.
from functools import cache
from typing import List
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        @cache
        def solve(index):
            if index == n:
                return True
            if index + 1 == n:
                return False
            if index + 2 == n:
                return nums[index] == nums[index+1]
            if index + 3 == n:
                return ((nums[index] == nums[index+1] and nums[index+1] == nums[index+2]) or (nums[index] + 1 == nums[index+1] and nums[index+1] + 1 == nums[index+2] ) )
            ans = False
            if nums[index] == nums[index+1]:
                ans = ans or solve(index+2)
            if nums[index] == nums[index+1]:
                ans = ans or solve(index+2)
            if ((nums[index] == nums[index+1] and nums[index+1] == nums[index+2]) or (nums[index] + 1 == nums[index+1] and nums[index+1] + 1 == nums[index+2] ) ):
                ans = ans or solve(index+3)
            return ans
        return solve(0)