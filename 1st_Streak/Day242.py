# Problem : Minimum Replacements to Sort the Array
# Problem Statement : You are given a 0-indexed integer array nums. In one operation you can replace any element of the array with any two elements that sum to it.
# For example, consider nums = [5,6,7]. In one operation, we can replace nums[1] with 2 and 4 and convert nums to [5,2,4,7].
# Return the minimum number of operations to make an array that is sorted in non-decreasing order.
from typing import List
class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        operations = 0
        prev_bound = nums[-1]

        for num in reversed(nums[:-1]):
            no_of_times = (num + prev_bound - 1) // prev_bound
            operations += no_of_times - 1
            prev_bound = num // no_of_times
                        
        return operations