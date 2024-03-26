# Problem : First Missing Positive
# Problem Statement : Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.
class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            correct_index = nums[i] - 1
            while 0 < nums[i] <= n and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
                correct_index = nums[i] - 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1
