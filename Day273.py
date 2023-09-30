# Problem : 132 Pattern
# Problem Statement : Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
# Return true if there is a 132 pattern in nums, otherwise, return false.
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        stack, minVal = [nums[-1]], float('-inf')
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < minVal:
                return True
            while stack and nums[i] > stack[-1]:
                minVal = stack[-1]
                stack.pop()
            stack.append(nums[i])
        return False