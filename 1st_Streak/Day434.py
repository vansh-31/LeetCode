# Problem : Intersection of Two Arrays
# Problem Statement : Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums1.sort()
        nums2.sort()
        n, m = len(nums1), len(nums2)
        ans = []
        i = j = 0
        while i < n and j < m:
            x, y = nums1[i], nums2[j]
            if x == y:
                ans.append(x)
                while i < n and nums1[i] == x:
                    i += 1
                while j < m and nums2[j] == y:
                    j += 1
            if x < y:
                i += 1
            if y < x:
                j += 1
        return ans
