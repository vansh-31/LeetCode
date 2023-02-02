# Problem : Subarray Sums Divisible by K
# Problem Statement : Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.
from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        remainderFrq = defaultdict(int)
        remainderFrq[0] = 1
        
        res = prefixSum = 0
        for n in nums:
            # Adding n to the prefixSum, so we have the prefixSum up to the ith position.
            prefixSum += n
            # Get the remainder of the current prefixSum.
            remainder = prefixSum % k
            # We need to increase the result before update the frequency table.
            # Because we are counting how many previous prefixSum have the same remainder.
            res += remainderFrq[remainder]
            # Update the frequency table.
            remainderFrq[remainder] += 1
        return res