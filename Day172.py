# Problem : Minimum Cost to Make Array Equal
# Problem Statement : You are given two 0-indexed arrays nums and cost consisting each of n positive integers.
# You can do the following operation any number of times:
# Increase or decrease any element of the array nums by 1.
# The cost of doing one operation on the ith element is cost[i].
# Return the minimum total cost such that all the elements of the array nums become equal.
from typing import List
class Solution:
    def minCost(self, nums: List[int], cost: List[int]):
        arr = sorted(zip(nums, cost))
        mid = sum(cost) / 2
        count = 0
        for target, co in arr:
            count += co
            if count >= mid:
                return sum(abs(target - n) * c for n, c in arr)