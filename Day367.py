# Problem : Convert an Array Into a 2D Array With Conditions
# Problem Statement : You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:
# The 2D array should contain only the elements of the array nums.
# Each row in the 2D array contains distinct integers.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.
from typing import List
from collections import defaultdict


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        ans = [[] for i in range(max(freq.values()))]
        for num in nums:
            while freq[num]:
                ans[freq[num] - 1].append(num)
                freq[num] -= 1
        return ans
