# Problem : Subarray Sums Divisible by K
# Problem Statement : Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.
from typing import List
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainderFrq = defaultdict(int)
        remainderFrq[0] = 1
        res = prefixSum = 0
        for n in nums:
            prefixSum += n
            remainder = prefixSum % k
            res += remainderFrq[remainder]
            remainderFrq[remainder] += 1
        return res
