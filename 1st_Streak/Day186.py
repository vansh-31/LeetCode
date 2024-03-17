# Problem : Longest Subarray of 1's After Deleting One Element
# Problem Statement : Given a binary array nums, you should delete one element from it.
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
from typing import List
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        best_sub = cur_sub = cur_start = 0
        zero = None
        elem_deleted = False
        for cur_end, n in enumerate(nums):
            if n == 0:
                if zero is not None:
                    cur_start = zero + 1
                    elem_deleted = True
                zero = cur_end

            cur_sub = cur_end - cur_start + 1
            if cur_sub > best_sub:
                best_sub = cur_sub

        if zero is not None or not elem_deleted:
            return max(best_sub - 1, 0)
        return best_sub