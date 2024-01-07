# Problem : Arithmetic Slices II - Subsequence
# Problem Statement : Given an integer array nums, return the number of all the arithmetic subsequences of nums.
# A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.
# For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
# For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
# A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.
# For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
# The test cases are generated so that the answer fits in 32-bit integer.
from typing import List
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        d = [defaultdict(int) for _ in range(len(nums))]
        ans = 0
        for i in range(1, len(nums)):
            for j in range(i):
                cd = nums[i] - nums[j]
                jj = d[j][cd]
                ii = d[i][cd]
                ans += jj
                d[i][cd] = jj + ii + 1
        return ans
