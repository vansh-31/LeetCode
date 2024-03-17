# Problem : Contiguous Array
# Problem Statement : Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        n = len(nums)
        n1 = 0
        n0 = 0
        maxLen = 0
        mp = {}
        mp[0] = -1
        for i in range(n):
            n1 += nums[i]
            n0 = (i + 1) - n1
            if (n1 - n0) in mp:
                maxLen = max(maxLen, i - mp[n1 - n0])
            else:
                mp[n1 - n0] = i
        return maxLen
