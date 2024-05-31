# Problem : Single Number III
# Problem Statement : Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.
class Solution:
    def singleNumber(self, nums):
        xor = 0
        for num in nums:
            xor ^= num
        set_bit = xor & -xor
        a, b = 0, 0
        for num in nums:
            if num & set_bit:
                a ^= num
            else:
                b ^= num
        return [a, b]
