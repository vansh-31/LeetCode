# Problem : Special Array With X Elements Greater Than or Equal X
# Problem Statement : You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that there are exactly x numbers in nums that are greater than or equal to x.
# Notice that x does not have to be an element in nums.
# Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is unique.
from bisect import bisect_left


class Solution:
    def specialArray(self, nums: list[int]) -> int:
        nums.sort()
        low, high = 0, len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            x = len(nums) - bisect_left(nums, mid)
            if mid == x:
                return mid
            if x > mid:
                low = mid + 1
            else:
                high = mid - 1
        return -1
