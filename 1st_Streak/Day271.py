# Problem : Sort Array By Parity
# Problem Statement : Given an integer array nums, move all the even integers at the beginning of the array followed by all the odd integers.
# Return any array that satisfies this condition.
class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sorted(nums,key=lambda x : x%2)