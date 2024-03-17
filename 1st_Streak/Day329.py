# Problem : Sum of Absolute Differences in a Sorted Array
# Problem Statement : You are given an integer array nums sorted in non-decreasing order.
# Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.
# In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        prefix_sum = [0] * n
        suffix_sum = [0] * n

        prefix_sum[0] = nums[0]
        suffix_sum[n - 1] = nums[n - 1]

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i]
            suffix_sum[n - i - 1] = suffix_sum[n - i] + nums[n - i - 1]

        for i in range(n):
            current_absolute_diff = ((nums[i] * i) - prefix_sum[i]) + (
                suffix_sum[i] - (nums[i] * (n - i - 1))
            )
            result[i] = current_absolute_diff

        return result
