# Problem : Count Subarrays With Fixed Bounds
# Problem Statement : You are given an integer array nums and two integers minK and maxK.
# A fixed-bound subarray of nums is a subarray that satisfies the following conditions:
# The minimum value in the subarray is equal to minK.
# The maximum value in the subarray is equal to maxK.
# Return the number of fixed-bound subarrays.
# A subarray is a contiguous part of an array.
class Solution:
    def countSubarrays(self, nums, minK, maxK):
        n = len(nums)
        left_bound = -1
        last_min = -1
        last_max = -1
        count = 0
        for i in range(n):
            if minK <= nums[i] <= maxK:
                last_min = i if nums[i] == minK else last_min
                last_max = i if nums[i] == maxK else last_max
                count += max(0, min(last_min, last_max) - left_bound)
            else:
                left_bound = i
                last_min = -1
                last_max = -1
        return count
