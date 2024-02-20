# Problem : Missing Number
# Problem Statement : Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        for num in nums:
            ans ^= num
        for x in range(len(nums) + 1):
            ans ^= x
        return ans
