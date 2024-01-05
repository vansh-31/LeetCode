# Problem : Longest Increasing Subsequence
# Problem Statement : Given an integer array nums, return the length of the longest strictly increasing subsequence.
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [nums[0]]
        for num in nums:
            if num > ans[-1]:
                ans.append(num)
            else:
                ind = bisect_left(ans, num)
                ans[ind] = num
        return len(ans)
