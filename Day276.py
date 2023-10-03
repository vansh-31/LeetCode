# Problem : Number of Good Pairs
# Problem Statement : Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.
from collections import defaultdict
from functools import cache
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        vals = defaultdict(int)
        for x in nums:
            vals[x] += 1
        ans = 0
        for x in vals.values():
            if x >= 2:
                ans += comb(x,2)
        return ans