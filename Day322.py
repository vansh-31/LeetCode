# Problem : Frequency of the Most Frequent Element
# Problem Statement : The frequency of an element is the number of times it occurs in an array.
# You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.
# Return the maximum possible frequency of an element after performing at most k operations.
class Solution:
    def maxFrequency(self, nums: list[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        left = 0
        right = 0
        dist = 0
        ans = 0
        while right < n:
            if right > 0 and nums[right] != nums[right - 1]:
                dist += (right - left) * (nums[right] - nums[right - 1])
            right += 1
            while dist > k:
                dist -= nums[right - 1] - nums[left]
                left += 1
            if right - left > ans:
                ans = right - left
        return ans
