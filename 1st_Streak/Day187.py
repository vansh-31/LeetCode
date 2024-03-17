# Problem : Minimum Size Subarray Sum
# Problem Statement : Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
#  whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]):
        left = 0
        sum_of_subarray = 0
        min_length = float('inf')
        for right in range(len(nums)):
            sum_of_subarray += nums[right]
            while sum_of_subarray >= target:
                min_length = min(min_length, right - left + 1)
                sum_of_subarray -= nums[left]
                left += 1
        if min_length == float('inf'):
            return 0
        return min_length