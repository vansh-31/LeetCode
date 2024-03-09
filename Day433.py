# Problem : Minimum Common Value
# Problem Statement : 2540. Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.
# Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.
class Solution:
    def getCommon(self, nums1: list[int], nums2: list[int]) -> int:
        n, m = len(nums1), len(nums2)
        i = j = 0
        while i < n and j < m:
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return -1
