# Problem : Majority Element
# Problem Statement : Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        element = -1
        freq = 0
        for num in nums:
            if freq == 0:
                element = num
                freq = 1
                continue
            if element == num:
                freq += 1
            else:
                freq -= 1
        return element
