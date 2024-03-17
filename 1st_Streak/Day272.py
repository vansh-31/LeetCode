# Problem : Monotonic Array
# Problem Statement : An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# Given an integer array nums, return true if the given array is monotonic, or false otherwise.
class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        i,j,n = 0,1,len(nums)
        while j < n and nums[i] == nums[j]:
            i += 1
            j += 1
        if j == n:
            return True
        asc = (nums[i] < nums[j])
        while j < n:
            if (asc and nums[i] > nums[j]) or (not asc and nums[i] < nums[j]) :
                return False
            i += 1
            j += 1
        return True