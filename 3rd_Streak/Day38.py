# Problem : Largest Positive Integer That Exists With Its Negative
# Problem Statement : Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.
class Solution:
    def findMaxK(self, nums: list[int]) -> int:
        ans = -1
        seen = set()
        for num in nums:
            if -num in seen:
                ans = max(ans, abs(num))
            else:
                seen.add(num)
        return ans
