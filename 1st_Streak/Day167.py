# Problem : Number of Ways to Reorder Array to Get Same BST
# Problem Statement : Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.
# For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
# Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.
# Since the answer may be very large, return it modulo 109 + 7.
from math import comb
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        def f(nums):
            if len(nums) <= 2:
                return 1
            left = [v for v in nums if v < nums[0]]
            right = [v for v in nums if v > nums[0]]
            return comb(len(left) + len(right), len(right)) * f(left) * f(right)
        return (f(nums) - 1) % (10**9 + 7)