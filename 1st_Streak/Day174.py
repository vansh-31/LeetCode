# Problem : Longest Arithmetic Subsequence
# Problem Statement : Given an array nums of integers, return the length of the longest arithmetic subsequence in nums.
# Note that:
# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.
# A sequence seq is arithmetic if seq[i + 1] - seq[i] are all the same value (for 0 <= i < seq.length - 1).
from typing import List
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n
        longest = 2
        dp = [{} for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                longest = max(longest, dp[i][diff])
        return longest