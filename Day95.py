# Problem : Minimize Maximum of Array
# Problem Statement : You are given a 0-indexed array nums comprising of n non-negative integers.
# In one operation, you must:
# Choose an integer i such that 1 <= i < n and nums[i] > 0.
# Decrease nums[i] by 1.
# Increase nums[i - 1] by 1.
# Return the minimum possible value of the maximum integer of nums after performing any number of operations.
from itertools import accumulate
class Solution:
    def minimizeArrayValue(self, A: list[int]) -> int:
        return max((a + i) // (i + 1) for i,a in enumerate(accumulate(A)))