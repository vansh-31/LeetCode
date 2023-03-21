# Problem : Number of Zero-Filled Subarrays
# Problem Statement : Given an integer array nums, return the number of subarrays filled with 0.
# A subarray is a contiguous non-empty sequence of elements within an array.
class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        ans = 0
        zeroes=0
        for i in range(len(nums)):
            if nums[i]==0:
                zeroes+=1
            else:
                ans += zeroes*(zeroes+1)//2
                zeroes = 0
        ans += zeroes*(zeroes+1)//2
        return ans