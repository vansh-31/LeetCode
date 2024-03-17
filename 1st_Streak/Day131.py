# Problem : Uncrossed Lines
# Problem Statement : You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.
# We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:
# nums1[i] == nums2[j], and
# the line we draw does not intersect any other connecting (non-horizontal) line.
# Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).
# Return the maximum number of connecting lines we can draw in this way.
from functools import cache
class Solution:
    def maxUncrossedLines(self, nums1: list[int], nums2: list[int]) -> int:
        n,m = len(nums1),len(nums2)
        @cache
        def solve(i,j):
            if i == n or j == m:
                return 0
            if nums1[i] == nums2[j]:
                return 1 + solve(i+1,j+1)
            return max( solve(i+1,j), solve(i,j+1) )
        return solve(0,0)