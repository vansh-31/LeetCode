# Problem : Squares of a Sorted Array
# Problem Statement : Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        return sorted(x**2 for x in nums)
