# Problem : Max Dot Product of Two Subsequences
# Problem Statement : Given two arrays nums1 and nums2.
# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.
# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).
from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)

        @cache
        def solve(i, j):
            if i == n or j == m:
                return 0
            x = nums1[i] * nums2[j]
            take = not_take = 0
            if x > 0:
                take = x + solve(i + 1, j + 1)
            not_take = max(solve(i + 1, j), solve(i, j + 1))
            return max(take, not_take)

        mx1, mx2 = max(nums1), max(nums2)
        if mx1 < 0 and mx2 > 0:
            return mx1 * min(nums2)
        if mx2 < 0 and mx1 > 0:
            return min(nums1) * mx2
        return solve(0, 0)
