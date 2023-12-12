# Problem :
# Problem Statement : Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
from heapq import nlargest
from math import prod
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return prod(x - 1 for x in nlargest(2, nums))
