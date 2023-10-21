# Problem : Constrained Subsequence Sum
# Problem Statement : Given an integer array nums and an integer k, return the maximum sum of a non-empty subsequence of that array such that for every two consecutive integers in the subsequence, nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.
# A subsequence of an array is obtained by deleting some number of elements (can be zero) from the array, leaving the remaining elements in their original order.
from collections import deque
from typing import List


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = nums[:]
        q = deque()
        q.append(0)
        for i in range(1, len(nums)):
            while q[-1] < i - k:
                q.pop()
            dp[i] = max(dp[i], dp[q[-1]] + nums[i])
            while len(q) > 0 and dp[q[0]] <= dp[i]:
                q.popleft()
            q.appendleft(i)
        return max(dp)
