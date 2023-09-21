# Problem : Median of Two Sorted Arrays
# Problem Statement : Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i = j = 0
        nums = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
        if i < len(nums1):
            nums.extend(nums1[i:])
        if j < len(nums2):
            nums.extend(nums2[j:])
        n = len(nums)
        ans = 0
        if n & 1:
            ans = nums[n // 2]
        else:
            ans = (nums[(n - 1) // 2] + nums[n // 2]) / 2
        return ans
