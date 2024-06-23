# Problem : Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
# Problem Statement : Given an array of integers nums and an integer limit, return the size of the longest non-empty subarray such that the absolute difference between any two elements of this subarray is less than or equal to limit.
import bisect


class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        n = len(nums)
        i = 0
        ans = []
        for j in range(n):
            bisect.insort(ans, nums[j])
            if ans[-1] - ans[0] > limit:
                ans.pop(bisect.bisect(ans, nums[i]) - 1)
                i += 1
        return j - i + 1
